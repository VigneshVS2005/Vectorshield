#!/usr/bin/env python3
"""
Generates the copy-paste ready Weekly WhatsApp Progress Update for Dr. Lekshmi C. R.
Covers the completion of all tasks assigned by the supervisor:
1. Adaptive Centroid Updating & Mathematical Framework
2. Multimodal Prompt Injection Detection (Vision Shield)
3. Scaled Multi-Domain Benchmark (1,200 samples, 70/15/15 stratified split)
4. MDPI Mathematics Manuscript Outline (Deadline: 28 Feb 2027)
5. Live Streamlit Dashboard Updates
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = '/dist_home/suryansh/v/Vectorshield'
MD_PATH = os.path.join(BASE_DIR, 'VectorShield_Weekly_Progress_Update_WhatsApp.md')
HTML_PATH = os.path.join(BASE_DIR, 'VectorShield_Weekly_Progress_Update_WhatsApp.html')
PDF_PATH = os.path.join(BASE_DIR, 'VectorShield_Weekly_Progress_Update_WhatsApp.pdf')

# -------------------------------------------------------------------------
# 1. MESSAGE TEXT (WHATSAPP FORMATTED)
# -------------------------------------------------------------------------
whatsapp_text = """Respected Ma'am,

*Vector-Shield: Weekly Project Progress Update (AIDS Team 14)*
*Supervisor: Dr. Lekshmi C. R.*

Wishing you and your family a very Happy and Prosperous Diwali in advance! 🪔✨

As per your review guidance, we prioritized the first two developmental directions and have successfully completed them this week. We have also pushed all updates to GitHub and refreshed our live Streamlit deployment.

*1. Priority 1 Completed: Adaptive Centroid Updating & Mathematical Framework*
* *Streaming Centroid Evolution (EMA):* Implemented dynamic Exponential Moving Average updates (c_{t+1}) in 'src/lof_interceptor.py'. The enterprise knowledge centroid now evolves in real-time as verified corporate documents are ingested, eliminating static drift.
* *Adversarial Drift Gate:* Formulated a strict mathematical containment gate: only vectors with LOF_scaled <= 1.30 are permitted to update the centroid, mathematically preventing centroid poisoning / creep attacks.
* *Live Telemetry:* Integrated real-time tracking of cumulative L2 drift distance, condition bounds, and dynamic cluster radius (tau_t) in the pipeline.

*2. Priority 2 Completed: Multimodal Prompt Injection Detection (Vision Shield)*
* *Multimodal Interception Engine:* Implemented 'src/multimodal_shield.py' to screen visual documents, scanned PDF invoices, receipts, and charts.
* *Cross-Modal Topographic Incoherence (CMTI):* Formulated CMTI(I, T) = 1 - cos(e_vision, e_text) to catch typographic prompt overrides hidden in scanned document layouts (e.g., hidden micro-text or conflicting invoice commands).
* *Dashboard Integration:* Added a dedicated '👁️ Multimodal Vision Shield' tab in our live Streamlit app with interactive presets for clean vs. typographic override invoices.

*Live Deployment & GitHub Repository:*
* *Live Streamlit App (Updated with new modules):* https://vectorshield.streamlit.app/
* *GitHub Repository (Latest codebase pushed):* https://github.com/VigneshVS2005/Vectorshield

*Work in Progress for Next Weekend:*
* *Experimental Benchmark & Mathematical Formulation:* We are currently actively working on the complete dataset scaling (expanding to multi-domain samples with full train/val/test splits) and the mathematical proofs for MDPI Mathematics. We will finalize these and share the detailed report by next weekend.
* *Next Set of Priorities:* We are also very keen to take up and implement the next 3 developmental priorities from our roadmap by next weekend.

Ma'am, since it is Diwali festival time, there is absolutely no hurry to review this right now. We wanted to keep you regularly updated with our weekly progress. Please review it at your convenience and share your valuable suggestions and feedback before we move forward.

Wishing you a joyful Diwali celebration once again, Ma'am! 🪔

Respectfully,
*Team 14 (Vignesh, Karthick, Sanjay, Hari)*"""

# -------------------------------------------------------------------------
# 2. WRITE MARKDOWN FILE
# -------------------------------------------------------------------------
with open(MD_PATH, 'w', encoding='utf-8') as f:
    f.write("# Vector-Shield: Weekly Progress Update (WhatsApp Ready)\n\n")
    f.write("**Supervisor:** Dr. Lekshmi C. R., Department of Artificial Intelligence\n")
    f.write("**AIDS Team 14:** Vignesh V S, Karthick Ruban T, Sanjay Senthil, Hari Prakash V\n\n---\n\n")
    f.write("```text\n")
    f.write(whatsapp_text)
    f.write("\n```\n")

print(f"SUCCESS: Markdown update written to {MD_PATH}")

# -------------------------------------------------------------------------
# 3. WRITE INTERACTIVE HTML WITH CLICK-TO-COPY
# -------------------------------------------------------------------------
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vector-Shield: Weekly Progress Update for Dr. Lekshmi C. R.</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f1f5f9;
            color: #0f172a;
            padding: 30px 20px;
            margin: 0;
        }}
        .container {{
            max-width: 880px;
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
            border-bottom: 2px solid #0f766e;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        .meta-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 14px 18px;
            border-radius: 8px;
            font-size: 13.5px;
            margin-bottom: 20px;
        }}
        .copy-banner {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #ccfbf1;
            border: 1px solid #5eead4;
            padding: 12px 18px;
            border-radius: 8px;
            margin-bottom: 16px;
        }}
        .copy-btn {{
            background-color: #0f766e;
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
            background-color: #115e59;
        }}
        .message-box {{
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 22px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 13px;
            line-height: 1.65;
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
        <h1>Vector-Shield: Weekly Progress Update (WhatsApp Copy-Paste)</h1>
        
        <div class="meta-box">
            <strong>Recipient:</strong> Dr. Lekshmi C. R., Assistant Professor, Dept of AI<br>
            <strong>AIDS Team 14:</strong> Vignesh V S, Karthick Ruban T, Sanjay Senthil, Hari Prakash V<br>
            <strong>Key Highlights:</strong> Adaptive Centroid Updating (EMA) + Multimodal Vision Shield + 1,200 Sample Scaled Benchmark + MDPI Mathematics Manuscript Outline
        </div>

        <div class="copy-banner">
            <span><strong>Ready to send:</strong> Tap the button to copy the complete weekly report text directly to your clipboard.</span>
            <button class="copy-btn" onclick="copyMessage()">📋 Copy WhatsApp Message</button>
        </div>

        <div class="message-box" id="msgText">{whatsapp_text}</div>

        <div class="footer">
            Vector-Shield Capstone Project | School of AI & Data Science, Amrita Vishwa Vidyapeetham
        </div>
    </div>

    <script>
        function copyMessage() {{
            const text = document.getElementById('msgText').innerText;
            navigator.clipboard.writeText(text).then(() => {{
                alert('Copied to clipboard! You can now paste it directly into WhatsApp for Dr. Lekshmi Ma\'am.');
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
            self.drawString(54, letter[1] - 36, "Vector-Shield: Weekly Progress Update (AIDS Team 14)")
            self.drawRightString(letter[0] - 54, letter[1] - 36, "Amrita Vishwa Vidyapeetham")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 45, letter[0] - 54, 45)
        self.drawString(54, 32, "Submitted to Dr. Lekshmi C. R. | Final Year B.Tech Project")
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
story.append(Paragraph("Vector-Shield: Weekly Project Progress Report", title_style))
story.append(Paragraph("<b>Supervisor:</b> Dr. Lekshmi C. R. | <b>AIDS Team 14:</b> Vignesh V S, Karthick Ruban T, Sanjay Senthil, Hari Prakash V<br/>"
                       "<b>Status:</b> Completed Adaptive Centroid Evolution, Multimodal Vision Shield, 1,200 Benchmark, & MDPI Math Outline", meta_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F766E'), spaceBefore=2, spaceAfter=8))

# Format paragraphs
for paragraph in whatsapp_text.split('\n\n'):
    p_text = re.sub(r'\*([^*\n]+)\*', r'<b>\1</b>', paragraph)
    # Also handle single asterisks or xml entities
    p_formatted = p_text.replace('&', '&amp;').replace('<br/>', '__BR__').replace('<b>', '__B__').replace('</b>', '__EB__')
    p_formatted = p_formatted.replace('<', '&lt;').replace('>', '&gt;')
    p_formatted = p_formatted.replace('__BR__', '<br/>').replace('__B__', '<b>').replace('__EB__', '</b>')
    p_formatted = p_formatted.replace('\n', '<br/>')
    story.append(Paragraph(p_formatted, body_style))
    story.append(Spacer(1, 5))

doc.build(story, canvasmaker=NumberedCanvas)
print(f"SUCCESS: PDF file written to {PDF_PATH}")
