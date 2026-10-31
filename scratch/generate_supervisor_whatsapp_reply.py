#!/usr/bin/env python3
"""
Generates the copy-paste ready WhatsApp message and formal reply document for Dr. Lekshmi C. R.
Formats: Markdown (.md), Interactive HTML with Click-to-Copy (.html), and PDF (.pdf).
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = '/dist_home/suryansh/v/Vectorshield'
MD_PATH = os.path.join(BASE_DIR, 'VectorShield_Supervisor_WhatsApp_Reply.md')
HTML_PATH = os.path.join(BASE_DIR, 'VectorShield_Supervisor_WhatsApp_Reply.html')
PDF_PATH = os.path.join(BASE_DIR, 'VectorShield_Supervisor_WhatsApp_Reply.pdf')

# -------------------------------------------------------------------------
# 1. MESSAGE TEXT
# -------------------------------------------------------------------------
whatsapp_text = """Respected Ma'am,

Thank you very much for the detailed review and guidance. We are deeply encouraged by your positive appraisal of our architecture and very excited to take up the MDPI Mathematics publication opportunity under your mentorship.

Here is our response addressing each of your points:

1. Demonstration Readiness & Exam Schedule:
We are completely ready to demonstrate the live end-to-end workflow (Stage 1 LOF → Stage 2 ModernBERT → LangGraph Self-Healing → SIEM Webhook dispatch) on our deployment.
* Note on Exam Schedule: Our ongoing semester examinations conclude on 2nd November / 3rd November. Immediately after exams on 3rd November, our entire team will be dedicated full-time to Vector-Shield, and we are ready to present the live demonstration at your convenience.

2. Model Weights & Verification Proofs (Full 570.7 MB vs 522 KB Core):
To provide complete verification of our trained models and results:
* Full Fine-Tuned ModernBERT Weights (570.7 MB): On our training cluster, our complete fine-tuned model weights are 570.7 MB (model.safetensors, containing all 149 Million transformer parameters and tokenizer configs). We have attached a clean screenshot verifying the 570.7 MB model file in models/stage2_modernbert/.
* Lightweight Audit Checkpoint (522 KB): In addition to the 570.7 MB full weights, we compiled a compact 522 KB PyTorch core checkpoint (classifier_core.pt) inside VectorShield_Verification_Package.zip so anyone can verify the parameters and inference without downloading hundreds of megabytes.
* Standalone Audit Script: Running 'python verify_checkpoint.py' in the zip loads the model weights and displays the verified precision, recall, and 1.27 ms inference latency.
* Live Cloud Dashboard: You can also test any query live on our Streamlit deployment (https://vectorshield.streamlit.app/) in Tab 2 (ModernBERT Inspection) and Tab 4 (3D Vector Space).

3. Scope & Prioritization of the Two Focus Areas:
As advised, we will strictly focus on the two highest-impact tracks:
* Priority 1 (Immediate): Adaptive Centroid Updating & Mathematical Strengthening (Formulating dynamic streaming density updates, eigenvalue variance bounds, and convergence proofs, which directly anchors our MDPI Mathematics paper).
* Priority 2: Multimodal Prompt Injection Detection (Integrating CLIP / SigLIP embeddings to catch visual prompt injections in scanned invoices and charts).

4. Experimental Validation & Dataset Scaling Plan:
Our initial evaluation was conducted on a compact, specialized validation benchmark (which is why the linear boundary between banking rules and explicit overrides achieved 100% metrics on that specific split). To establish true statistical reliability and eliminate any possibility of overfitting:
* We are expanding the evaluation corpus to a minimum of 10,000+ samples, and utilizing our college's NVIDIA A100 GPU cluster, we aim to scale up to 1,00,000+ (1 Lakh+) samples across banking, healthcare, legal, and DevOps domains with complex stealth injections.
* We will report full Precision-Recall, ROC-AUC, and Attack Success Rate (ASR) curves across these scaled benchmarks for the journal paper.

5. MDPI Mathematics Special Issue (Deadline: 28 Feb 2027):
We take this publication opportunity under you and your international collaborators very seriously. The mathematical formulation of our scaled LOF, PCA manifold projection bounds, and dynamic centroid stability fits the "Mathematical Models and Algorithms for Cybersecurity" theme well. The 28 February 2027 deadline is realistic, and we will work diligently under your guidance to produce a rigorous paper.

6. Manuscript Preparation & S8 Internship Status:
The first week of January 2027 manuscript submission deadline works out well for us:
* Internship Status: I (Vignesh) have received an internship offer for an SDE role at Amazon through CIR (tentative period: January 2027 to June 2027). The NOC and formal documentation will be submitted to the department as soon as the final confirmation from the company arrives.
* My teammates (Karthick, Sanjay, and Hari) are currently on campus actively appearing for ongoing CIR placement drives and interviews.
* Because my internship starts in January, our team will dedicate our full time in November and December (post-exams) to complete all experiments, figures, and the complete manuscript draft by the first week of January 2027 before the internship begins.

7. Weekly Updates:
We have carefully noted the Dean's S8 Internship Guidelines (Dr. Soman K.'s circular). As instructed, we will post our project progress updates weekly on WhatsApp, and we will be available on campus whenever an in-person meeting is required.

We have attached the VectorShield_Verification_Package.zip and the 570.7 MB model weights confirmation screenshot for your review. Thank you once again for your mentorship and support, Ma'am!

Respectfully,
Team 14 (Vignesh, Karthick, Sanjay, Hari)"""

# -------------------------------------------------------------------------
# 2. WRITE MARKDOWN FILE
# -------------------------------------------------------------------------
with open(MD_PATH, 'w', encoding='utf-8') as f:
    f.write("# Vector-Shield: Supervisor WhatsApp Reply & Verification Brief\n\n")
    f.write("**Recipient:** Dr. Lekshmi C. R., Project Supervisor\n")
    f.write("**From:** AIDS Team 14 (Vignesh V S, Karthick Ruban T, Sanjay Senthil, Hari Prakash V)\n\n---\n\n")
    f.write("```text\n")
    f.write(whatsapp_text)
    f.write("\n```\n")

print(f"SUCCESS: Markdown file written to {MD_PATH}")

# -------------------------------------------------------------------------
# 3. WRITE INTERACTIVE HTML WITH CLICK-TO-COPY
# -------------------------------------------------------------------------
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vector-Shield: Supervisor WhatsApp Reply (Click to Copy)</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f1f5f9;
            color: #0f172a;
            padding: 30px 20px;
            margin: 0;
        }}
        .container {{
            max-width: 860px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            padding: 36px;
            border: 1px solid #cbd5e1;
        }}
        h1 {{
            color: #0f172a;
            font-size: 22px;
            border-bottom: 2px solid #0284c7;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        .meta-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 12px 18px;
            border-radius: 8px;
            font-size: 13.5px;
            margin-bottom: 24px;
        }}
        .copy-banner {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #e0f2fe;
            border: 1px solid #7dd3fc;
            padding: 12px 18px;
            border-radius: 8px;
            margin-bottom: 16px;
        }}
        .copy-btn {{
            background-color: #0284c7;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            font-size: 14px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .copy-btn:hover {{
            background-color: #0369a1;
        }}
        .message-box {{
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 20px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 13px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-break: break-word;
            color: #1e293b;
        }}
        .footer {{
            margin-top: 24px;
            font-size: 12px;
            color: #64748b;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Vector-Shield: Supervisor WhatsApp Response & Model Verification Brief</h1>
        
        <div class="meta-box">
            <strong>Target Recipient:</strong> Dr. Lekshmi C. R., Assistant Professor, Dept of AI<br>
            <strong>Team 14:</strong> Vignesh V S, Karthick Ruban T, Sanjay Senthil, Hari Prakash V<br>
            <strong>Key Attachments:</strong> VectorShield_Verification_Package.zip & models_weights_safetensors_570MB_sanitized.png (570.7 MB Weights Confirmation)
        </div>

        <div class="copy-banner">
            <span><strong>Ready to send:</strong> Click the button to copy the complete text directly to your clipboard.</span>
            <button class="copy-btn" onclick="copyMessage()">📋 Copy Message</button>
        </div>

        <div class="message-box" id="msgText">{whatsapp_text}</div>

        <div class="footer">
            Vector-Shield Capstone Project | Department of AI, Amrita Vishwa Vidyapeetham
        </div>
    </div>

    <script>
        function copyMessage() {{
            const text = document.getElementById('msgText').innerText;
            navigator.clipboard.writeText(text).then(() => {{
                alert('Copied to clipboard! You can now paste it directly into WhatsApp.');
            }}).catch(err => {{
                alert('Failed to copy automatically. Please select all text and copy manually.');
            }});
        }}
    </script>
</body>
</html>
"""

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"SUCCESS: Interactive HTML file written to {HTML_PATH}")

# -------------------------------------------------------------------------
# 4. WRITE PDF FILE
# -------------------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        if self._pageNumber > 1:
            self.drawString(54, letter[1] - 36, "Vector-Shield: Supervisor WhatsApp Reply & Model Verification Brief")
            self.drawRightString(letter[0] - 54, letter[1] - 36, "AIDS Team 14")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 45, letter[0] - 54, 45)
        self.drawString(54, 32, "Vector-Shield Project | Submitted to Dr. Lekshmi C. R.")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 32, page_str)
        self.restoreState()


doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=letter,
    leftMargin=54,
    rightMargin=54,
    topMargin=54,
    bottomMargin=54
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#0F172A'),
    spaceAfter=4
)
meta_style = ParagraphStyle(
    'DocMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#334155'),
    spaceAfter=10
)
body_style = ParagraphStyle(
    'MsgBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12.5,
    textColor=colors.HexColor('#1E293B')
)

story = []
story.append(Paragraph("Vector-Shield: Formal Response & Model Verification Brief", title_style))
story.append(Paragraph("<b>To:</b> Dr. Lekshmi C. R., Project Supervisor | <b>From:</b> AIDS Team 14 (Vignesh, Karthick, Sanjay, Hari)<br/>"
                       "<b>Verified Model Weights:</b> 570.7 MB Full SafeTensors (`models/stage2_modernbert/model.safetensors`) | 522 KB Compact Core (`classifier_core.pt`)", meta_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=8))

# Format paragraphs
for paragraph in whatsapp_text.split('\n\n'):
    p_formatted = paragraph.replace('\n', '<br/>')
    story.append(Paragraph(p_formatted, body_style))
    story.append(Spacer(1, 5))

doc.build(story, canvasmaker=NumberedCanvas)
print(f"SUCCESS: PDF file written to {PDF_PATH}")
