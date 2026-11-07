"""
Vector-Shield Stage 1: Symbolic Topographic Anomaly Detector (LOF Interceptor)
Lead Architect: Vignesh V S (cb.ai.u4aid23057)
Mathematical Optimization & Dynamic Centroid Tracking: Team 14

Implements real-time density-based outlier filtering on high-dimensional embedding tensors
using Local Outlier Factor (LOF) combined with Cosine Domain-Centroid Density Scaling
and Adaptive Streaming Centroid Evolution with Adversarial Drift Gating.
Sub-2ms execution latency.
"""

import time
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
from sklearn.decomposition import PCA


class VectorShieldLOFInterceptor:
    """
    Stage 1 Symbolic Interceptor for high-dimensional vector spaces.

    Mathematical Formulation:
    1. Reachability Distance: rd_k(p, o) = max(k_distance(o), d(p, o))
    2. Local Reachability Density: lrd_k(p) = |N_k(p)| / sum_{o in N_k(p)} rd_k(p, o)
    3. Local Outlier Factor: LOF_k(p) = (1 / |N_k(p)|) * sum_{o in N_k(p)} (lrd_k(o) / lrd_k(p))
    4. Cosine Density Scaling: LOF_scaled(p) = LOF_k(p) * (cos_dist(p, c_clean) / mean_clean_dist)^density_exponent
    5. Adaptive Centroid Evolution (EMA): c_{t+1} = normalize((1 - alpha)*c_t + alpha*v_inlier)
       subject to the Adversarial Drift Gate: LOF_scaled(v) <= tau_safe (1.30).

    Soft-Margin Decision Rules:
      - LOF <= safe_threshold (1.30)          -> 'SAFE' (Pass Direct to Context Window)
      - safe_threshold < LOF < anom_threshold -> 'BORDERLINE' (Route to Stage 2 ModernBERT)
      - LOF >= anom_threshold (2.50)         -> 'QUARANTINE_ANOMALY' (Drop Vector & Self-Heal)
    """

    def __init__(
        self,
        n_neighbors: int = 5,
        safe_threshold: float = 1.30,
        anomaly_threshold: float = 2.50,
        pca_dimensions: int = 16,
        density_exponent: float = 1.2,
        metric: str = "minkowski",
        adaptive_alpha: float = 0.05
    ):
        self.n_neighbors = n_neighbors
        self.safe_threshold = safe_threshold
        self.anomaly_threshold = anomaly_threshold
        self.pca_dimensions = pca_dimensions
        self.density_exponent = density_exponent
        self.metric = metric
        self.adaptive_alpha = adaptive_alpha

        self.pca = None
        self.lof_model = None
        self.clean_centroid = None
        self.initial_centroid = None
        self.baseline_cosine_dist = 0.5
        self.initial_baseline_dist = 0.5
        self.is_fitted = False

        # Adaptive Centroid Telemetry for MDPI Mathematics
        self.update_count = 0
        self.cumulative_drift = 0.0
        self.update_history = []

    def fit(self, reference_vectors: np.ndarray):
        """
        Fits the clean baseline density manifold.
        reference_vectors: shape (N, D) where D is high-dimensional (e.g., 384 or 1536).
        """
        ref = np.asarray(reference_vectors, dtype=np.float32)
        n_samples, n_features = ref.shape

        # Compute clean baseline centroid for Cosine Density Scaling
        ref_norms = ref / (np.linalg.norm(ref, axis=1, keepdims=True) + 1e-8)
        self.clean_centroid = np.mean(ref_norms, axis=0)
        self.clean_centroid /= (np.linalg.norm(self.clean_centroid) + 1e-8)
        self.initial_centroid = np.copy(self.clean_centroid)

        # Baseline mean cosine distance
        clean_dists = [1.0 - np.dot(v, self.clean_centroid) for v in ref_norms]
        self.baseline_cosine_dist = max(0.1, float(np.mean(clean_dists)))
        self.initial_baseline_dist = self.baseline_cosine_dist

        # Adaptive PCA dimensionality reduction to mitigate curse of dimensionality
        n_components = min(self.pca_dimensions, n_samples - 1, n_features)
        if n_components < n_features:
            self.pca = PCA(n_components=n_components, random_state=42)
            ref_reduced = self.pca.fit_transform(ref)
        else:
            self.pca = None
            ref_reduced = ref

        actual_k = min(self.n_neighbors, n_samples - 1)
        self.actual_k = max(2, actual_k)

        self.lof_model = LocalOutlierFactor(
            n_neighbors=self.actual_k,
            novelty=True,
            metric=self.metric
        )
        self.lof_model.fit(ref_reduced)
        self.is_fitted = True

    def score_vector(self, query_vector: np.ndarray) -> dict:
        """
        Scores a single query vector tensor in real-time (< 2ms).
        Returns diagnostic dictionary with scaled LOF score, classification, and latency.
        """
        if not self.is_fitted:
            raise RuntimeError("Interceptor must be fitted on reference vectors before scoring.")

        vec = np.asarray(query_vector, dtype=np.float32).reshape(1, -1)
        v_flat = query_vector.flatten()

        start_t = time.perf_counter()
        if self.pca is not None:
            vec_reduced = self.pca.transform(vec)
        else:
            vec_reduced = vec

        # Raw LOF score from k-NN density
        raw_lof = -float(self.lof_model.score_samples(vec_reduced)[0])

        # Cosine distance scaling relative to clean domain centroid
        v_norm = v_flat / (np.linalg.norm(v_flat) + 1e-8)
        cos_dist = 1.0 - float(np.dot(v_norm, self.clean_centroid))
        density_multiplier = (cos_dist / self.baseline_cosine_dist) ** self.density_exponent
        scaled_lof = float(raw_lof * density_multiplier)

        elapsed_ms = (time.perf_counter() - start_t) * 1000.0

        # Soft-margin decision boundary
        if scaled_lof <= self.safe_threshold:
            status = "SAFE"
            action = "PASS_TO_LLM"
            recommendation = "Vector coordinates conform to verified knowledge cluster."
        elif scaled_lof < self.anomaly_threshold:
            status = "BORDERLINE"
            action = "ROUTE_TO_STAGE2"
            recommendation = "Topographic density is ambiguous. Hand off to ModernBERT for semantic inspection."
        else:
            status = "QUARANTINE_ANOMALY"
            action = "DROP_AND_SELF_HEAL"
            recommendation = "Adversarial geometric outlier detected. Intercepted before context exposure."

        return {
            "lof_score": round(scaled_lof, 4),
            "raw_lof": round(raw_lof, 4),
            "cosine_dist": round(cos_dist, 4),
            "status": status,
            "action": action,
            "recommendation": recommendation,
            "latency_ms": round(elapsed_ms, 3),
            "is_outlier": bool(scaled_lof >= self.anomaly_threshold)
        }

    def update_centroid_adaptive(
        self,
        new_vector: np.ndarray,
        alpha: float = None,
        max_allowable_lof: float = None
    ) -> dict:
        """
        Dynamically adapts the knowledge centroid c_t in streaming time.

        Mathematical Guardrail (Adversarial Drift Gate):
        To prevent 'centroid creep' or poisoning attacks, only vectors that pass
        the strict inlier condition (LOF_scaled <= tau_safe) are permitted to update c_t.
        """
        if not self.is_fitted:
            raise RuntimeError("Interceptor must be fitted before updating centroid.")

        if alpha is None:
            alpha = self.adaptive_alpha
        if max_allowable_lof is None:
            max_allowable_lof = self.safe_threshold

        # Step 1: Pre-screen vector with existing manifold
        score_res = self.score_vector(new_vector)

        # Gate Check: Reject non-inliers immediately
        if score_res["lof_score"] > max_allowable_lof:
            return {
                "updated": False,
                "reason": "ADVERSARIAL_DRIFT_GATE_REJECTED",
                "lof_score": score_res["lof_score"],
                "threshold": max_allowable_lof,
                "status": score_res["status"],
                "centroid_update_count": self.update_count,
                "cumulative_drift": round(self.cumulative_drift, 6)
            }

        # Step 2: Exponential Moving Average (EMA) update on normalized unit sphere
        v_flat = new_vector.flatten()
        v_norm = v_flat / (np.linalg.norm(v_flat) + 1e-8)

        old_centroid = np.copy(self.clean_centroid)
        updated_raw = (1.0 - alpha) * self.clean_centroid + alpha * v_norm
        self.clean_centroid = updated_raw / (np.linalg.norm(updated_raw) + 1e-8)

        # Step 3: Update running baseline dispersion radius tau_t
        step_cos_dist = 1.0 - float(np.dot(v_norm, old_centroid))
        self.baseline_cosine_dist = (1.0 - alpha) * self.baseline_cosine_dist + alpha * step_cos_dist
        self.baseline_cosine_dist = max(0.08, float(self.baseline_cosine_dist))

        # Step 4: Compute Step Drift and Cumulative Metrics
        step_drift = float(np.linalg.norm(self.clean_centroid - old_centroid))
        self.cumulative_drift += step_drift
        self.update_count += 1

        drift_from_initial = 1.0 - float(np.dot(self.clean_centroid, self.initial_centroid))

        event = {
            "update_id": self.update_count,
            "step_drift": round(step_drift, 6),
            "cumulative_drift": round(self.cumulative_drift, 6),
            "drift_from_initial": round(drift_from_initial, 6),
            "new_baseline_dist": round(self.baseline_cosine_dist, 5),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
        self.update_history.append(event)
        if len(self.update_history) > 100:
            self.update_history.pop(0)

        return {
            "updated": True,
            "reason": "INLIER_ADAPTIVE_CENTROID_UPDATED",
            "step_drift": round(step_drift, 6),
            "cumulative_drift": round(self.cumulative_drift, 6),
            "drift_from_initial": round(drift_from_initial, 6),
            "new_baseline_dist": round(self.baseline_cosine_dist, 5),
            "centroid_update_count": self.update_count,
            "alpha_used": alpha
        }

    def get_mathematical_diagnostics(self) -> dict:
        """
        Returns theoretical and statistical properties for the MDPI Mathematics paper:
        - PCA explained variance ratio & cumulative coverage
        - Centroid drift metrics from initial state
        - Condition number and dispersion radius
        """
        if not self.is_fitted:
            return {"status": "UNFITTED"}

        drift_from_initial = 1.0 - float(np.dot(self.clean_centroid, self.initial_centroid))

        pca_coverage = 1.0
        explained_variance = []
        if self.pca is not None:
            explained_variance = [round(float(v), 4) for v in self.pca.explained_variance_ratio_]
            pca_coverage = round(float(np.sum(self.pca.explained_variance_ratio_)), 4)

        return {
            "is_fitted": self.is_fitted,
            "dimensions_original": len(self.clean_centroid),
            "dimensions_pca": self.pca.n_components if self.pca is not None else len(self.clean_centroid),
            "pca_variance_coverage": pca_coverage,
            "pca_explained_variance_ratio": explained_variance[:8],
            "initial_dispersion_radius": round(self.initial_baseline_dist, 5),
            "current_dispersion_radius": round(self.baseline_cosine_dist, 5),
            "total_adaptive_updates": self.update_count,
            "cumulative_l2_drift": round(self.cumulative_drift, 6),
            "cosine_drift_from_initial": round(drift_from_initial, 6),
            "density_scaling_exponent": self.density_exponent,
            "safe_threshold": self.safe_threshold,
            "anomaly_threshold": self.anomaly_threshold
        }

    def batch_evaluate(self, vectors: np.ndarray) -> list:
        """Evaluates a batch of vectors."""
        return [self.score_vector(v) for v in vectors]
