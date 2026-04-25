from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.pdfgen import canvas as canvas_module

# ── Colour Palette ──────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0F2D5A")
AZURE_BLUE = colors.HexColor("#0078D4")   # Microsoft Azure brand blue
ACCENT     = colors.HexColor("#50E6FF")   # Azure light
GOLD       = colors.HexColor("#FFB900")   # highlight
DARK_GRAY  = colors.HexColor("#2D2D2D")
MID_GRAY   = colors.HexColor("#555555")
LIGHT_GRAY = colors.HexColor("#F3F3F3")
SUCCESS    = colors.HexColor("#107C10")   # green
WARNING    = colors.HexColor("#D83B01")   # red-orange
WHITE      = colors.white

PAGE_W, PAGE_H = A4

# ── Header / Footer ─────────────────────────────────────────────────────────
def make_header_footer(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 28*mm, PAGE_W, 28*mm, fill=1, stroke=0)
    canvas.setFillColor(AZURE_BLUE)
    canvas.rect(0, PAGE_H - 30*mm, PAGE_W, 2*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.setFillColor(WHITE)
    canvas.drawString(18*mm, PAGE_H - 16*mm, "ROHIT RANVIR  |  Junior Software Developer + AI  |  Interview Prep Guide")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(ACCENT)
    canvas.drawRightString(PAGE_W - 18*mm, PAGE_H - 16*mm, "Azure Focus Edition")
    # Footer bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 12*mm, fill=1, stroke=0)
    canvas.setFillColor(AZURE_BLUE)
    canvas.rect(0, 12*mm, PAGE_W, 1*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(WHITE)
    canvas.drawString(18*mm, 4.5*mm, "Confidential Interview Prep  •  Rohit Ranvir  •  2025")
    canvas.drawRightString(PAGE_W - 18*mm, 4.5*mm, f"Page {doc.page}")
    canvas.restoreState()

# ── Style Sheet ─────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

sTitle = S("sTitle", fontSize=28, textColor=WHITE, fontName="Helvetica-Bold",
           leading=34, alignment=TA_CENTER)
sSubtitle = S("sSubtitle", fontSize=13, textColor=ACCENT, fontName="Helvetica",
              leading=18, alignment=TA_CENTER)
sSectionHead = S("sSectionHead", fontSize=15, textColor=WHITE, fontName="Helvetica-Bold",
                 leading=20, spaceBefore=2, spaceAfter=2, backColor=NAVY,
                 leftIndent=-6, rightIndent=-6, borderPad=6)
sSubHead = S("sSubHead", fontSize=12, textColor=AZURE_BLUE, fontName="Helvetica-Bold",
             leading=16, spaceBefore=8, spaceAfter=3)
sMiniHead = S("sMiniHead", fontSize=10, textColor=NAVY, fontName="Helvetica-Bold",
              leading=14, spaceBefore=4, spaceAfter=2)
sBody = S("sBody", fontSize=9.5, textColor=DARK_GRAY, fontName="Helvetica",
          leading=14, spaceBefore=2, spaceAfter=2, alignment=TA_JUSTIFY)
sBullet = S("sBullet", fontSize=9.5, textColor=DARK_GRAY, fontName="Helvetica",
            leading=13, leftIndent=14, firstLineIndent=-10, spaceBefore=1)
sCode = S("sCode", fontSize=8.5, textColor=colors.HexColor("#1A1A2E"),
          fontName="Courier", leading=12, backColor=colors.HexColor("#EFF6FF"),
          leftIndent=8, rightIndent=8, spaceBefore=2, spaceAfter=2, borderPad=4)
sQ = S("sQ", fontSize=10, textColor=NAVY, fontName="Helvetica-Bold",
       leading=14, spaceBefore=5, spaceAfter=1, leftIndent=14,
       firstLineIndent=-14)
sA = S("sA", fontSize=9.5, textColor=DARK_GRAY, fontName="Helvetica",
       leading=14, spaceBefore=1, spaceAfter=4, leftIndent=14)
sTip = S("sTip", fontSize=9, textColor=SUCCESS, fontName="Helvetica-BoldOblique",
         leading=13, leftIndent=10)
sWarn = S("sWarn", fontSize=9, textColor=WARNING, fontName="Helvetica-BoldOblique",
          leading=13, leftIndent=10)
sTOC = S("sTOC", fontSize=10, textColor=DARK_GRAY, fontName="Helvetica",
         leading=16, leftIndent=6)
sTOCHead = S("sTOCHead", fontSize=12, textColor=NAVY, fontName="Helvetica-Bold",
             leading=18, leftIndent=6)

# ── Helpers ─────────────────────────────────────────────────────────────────
def section(title):
    return [
        Spacer(1, 8*mm),
        Table([[Paragraph(title, sSectionHead)]],
              colWidths=[PAGE_W - 36*mm],
              style=TableStyle([
                  ("BACKGROUND", (0,0), (-1,-1), NAVY),
                  ("TOPPADDING",   (0,0), (-1,-1), 6),
                  ("BOTTOMPADDING",(0,0), (-1,-1), 6),
                  ("LEFTPADDING",  (0,0), (-1,-1), 10),
              ])),
        Spacer(1, 4*mm),
    ]

def sub(title):
    return Paragraph(title, sSubHead)

def mini(title):
    return Paragraph(title, sMiniHead)

def body(text):
    return Paragraph(text, sBody)

def bullet(text):
    return Paragraph(f"&#8226;  {text}", sBullet)

def qa(q, a):
    return [
        Paragraph(f"Q: {q}", sQ),
        Paragraph(f"A: {a}", sA),
    ]

def tip(text):
    return Paragraph(f"✅  {text}", sTip)

def warn(text):
    return Paragraph(f"⚠️  {text}", sWarn)

def info_table(rows, col_widths=None):
    if col_widths is None:
        col_widths = [(PAGE_W - 36*mm)/2, (PAGE_W - 36*mm)/2]
    tbl = Table(rows, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,0), AZURE_BLUE),
        ("TEXTCOLOR",    (0,0), (-1,0), WHITE),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 9),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_GRAY, WHITE]),
        ("GRID",         (0,0), (-1,-1), 0.4, colors.HexColor("#CCCCCC")),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
    ]))
    return tbl

def ref_card(title, rows):
    header = [Paragraph(title, S("th", fontSize=9, textColor=WHITE,
                                  fontName="Helvetica-Bold", leading=12))]
    data = [header] + [[Paragraph(r, S("td", fontSize=8.5, textColor=DARK_GRAY,
                                        fontName="Helvetica", leading=12))] for r in rows]
    tbl = Table(data, colWidths=[PAGE_W/2 - 22*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,0), GOLD),
        ("TEXTCOLOR",    (0,0), (-1,0), NAVY),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.HexColor("#FFFDE7"), WHITE]),
        ("GRID",         (0,0), (-1,-1), 0.3, colors.HexColor("#E0E0E0")),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING",   (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
    ]))
    return tbl

# ── DOCUMENT BUILD ──────────────────────────────────────────────────────────
out = "Rohit_Ranvir_Interview_Prep.pdf"

def cover_page(canvas, doc):
    canvas.saveState()
    # Full navy background
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Azure blue accent strip top
    canvas.setFillColor(AZURE_BLUE)
    canvas.rect(0, PAGE_H - 6*mm, PAGE_W, 6*mm, fill=1, stroke=0)
    # Gold accent strip bottom
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, PAGE_W, 6*mm, fill=1, stroke=0)
    canvas.setFillColor(AZURE_BLUE)
    canvas.rect(0, 6*mm, PAGE_W, 2*mm, fill=1, stroke=0)
    # Side accent stripe
    canvas.setFillColor(AZURE_BLUE)
    canvas.rect(0, 0, 6*mm, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(6*mm, 0, 2*mm, PAGE_H, fill=1, stroke=0)

    # Main Title
    canvas.setFont("Helvetica-Bold", 34)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.72, "INTERVIEW PREP GUIDE")
    canvas.setFont("Helvetica-Bold", 18)
    canvas.setFillColor(ACCENT)
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.65, "Junior Software Developer + AI Role")
    canvas.setFont("Helvetica", 13)
    canvas.setFillColor(GOLD)
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.60, "Azure Focus  |  Product-Based Company")

    # Divider
    canvas.setStrokeColor(AZURE_BLUE)
    canvas.setLineWidth(1.5)
    canvas.line(50*mm, PAGE_H*0.56, PAGE_W - 50*mm, PAGE_H*0.56)

    # Name block
    canvas.setFont("Helvetica-Bold", 22)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.50, "Rohit Ranvir")
    canvas.setFont("Helvetica", 11)
    canvas.setFillColor(colors.HexColor("#BBDEFB"))
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.455, "B.E. Computer Science  |  Maharashtra")
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.425, "Python Full Stack  |  Django  |  React  |  FastAPI  |  LLM Integration")

    # Tech pills
    pills = ["Django", "FastAPI", "React", "PostgreSQL", "Celery", "Azure", "LLM", "Groq"]
    pill_w = 26*mm
    total = len(pills) * pill_w + (len(pills)-1) * 4*mm
    x = (PAGE_W - total) / 2 + 4*mm
    y = PAGE_H * 0.35
    for p in pills:
        canvas.setFillColor(AZURE_BLUE)
        canvas.roundRect(x, y, pill_w, 7*mm, 2*mm, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawCentredString(x + pill_w/2, y + 2*mm, p)
        x += pill_w + 4*mm

    # Sections preview
    canvas.setFont("Helvetica-Bold", 10)
    canvas.setFillColor(ACCENT)
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.25, "COVERS:")
    sections_text = "Projects  •  Azure Fundamentals  •  AI/LLM Concepts  •  Behavioural Questions"
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.215, sections_text)
    sections_text2 = "Mock Interview Scenarios  •  Pitfall Guide  •  Quick Reference Cards"
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.185, sections_text2)

    canvas.setFont("Helvetica-Oblique", 8.5)
    canvas.setFillColor(colors.HexColor("#90CAF9"))
    canvas.drawCentredString(PAGE_W/2 + 4*mm, PAGE_H*0.10, "Prepared for tomorrow's interview  |  Study, practise, own it.")
    canvas.restoreState()

# Use two-template approach
cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, bottomPadding=0,
                    rightPadding=0, topPadding=0)
content_frame = Frame(18*mm, 20*mm, PAGE_W - 36*mm, PAGE_H - 56*mm,
                      leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)

doc = BaseDocTemplate(
    out, pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=36*mm, bottomMargin=20*mm,
    title="Interview Prep Guide – Rohit Ranvir",
)
doc.addPageTemplates([
    PageTemplate(id="Cover", frames=[cover_frame], onPage=cover_page),
    PageTemplate(id="Content", frames=[content_frame], onPage=make_header_footer),
])

story = []

# ── Cover spacer (fills the cover frame with nothing — cover drawn by onPage)
from reportlab.platypus import NextPageTemplate
story.append(NextPageTemplate("Content"))
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("TABLE OF CONTENTS", sSectionHead))
story.append(Spacer(1, 4*mm))

toc_items = [
    ("1", "Your Elevator Pitch & Professional Summary", "Pg 3"),
    ("2", "Project Deep-Dives", "Pg 3"),
    ("  2.1", "Multi-Tenant SaaS Expense Manager", ""),
    ("  2.2", "Vendor Connect India", ""),
    ("  2.3", "Smart Review AI (LLM Project)", ""),
    ("  2.4", "Autonomous Insurance Claims Agent (PDF Assignment)", ""),
    ("3", "Azure Fundamentals", "Pg 7"),
    ("4", "AI / LLM Concepts", "Pg 9"),
    ("5", "Behavioural Questions (STAR Method)", "Pg 11"),
    ("6", "Common Interview Pitfalls", "Pg 12"),
    ("7", "Practice Delivery Tips", "Pg 13"),
    ("8", "Mock Interview Scenarios with Sample Answers", "Pg 13"),
    ("9", "Quick Reference Card — Azure Services", "Pg 16"),
    ("10", "Quick Reference Card — LLM & AI Terms", "Pg 17"),
]

# FIXED: Changed the font name generation to use "Helvetica" instead of "Helvetica-Normal"
for num, title, page in toc_items:
    if num.startswith("  "):  # Indented items (subsections)
        story.append(Paragraph(
            f'<font name="Helvetica" color="#{MID_GRAY.hexval()[2:]}">{num}. {title}</font>',
            sTOC
        ))
    else:  # Main sections
        story.append(Paragraph(
            f'<font name="Helvetica-Bold" color="#{NAVY.hexval()[2:]}">{num}. {title}</font>',
            sTOC
        ))
story.append(Spacer(1, 4*mm))
story.append(HRFlowable(width="100%", thickness=1, color=AZURE_BLUE))

# ════════════════════════════════════════════════════════════════════════════
# 1. ELEVATOR PITCH
# ════════════════════════════════════════════════════════════════════════════
story += section("1. YOUR ELEVATOR PITCH & PROFESSIONAL SUMMARY")
story.append(sub("60-Second Polished Intro (Memorise This)"))
story.append(body(
    "Good morning! My name is <b>Rohit Ranvir</b>, and I'm from Maharashtra. "
    "I completed my <b>Bachelor of Engineering in Computer Science in 2025</b> with a CGPA of 7.5. "
    "During college I built strong skills in <b>Python full-stack development</b> — primarily with "
    "Django, Django REST Framework, FastAPI, and React — and got hands-on with production concerns "
    "like multi-tenancy, CI/CD, JWT security, and Celery-based background processing."
))
story.append(body(
    "In my final year I got deeply interested in <b>AI and LLMs</b>, enrolled at Naresh IT to formalise "
    "those skills, and published a peer-reviewed NLP paper on sentiment analysis via deep learning. "
    "My flagship projects include a <b>multi-tenant SaaS expense manager</b>, a <b>street-vendor discovery "
    "platform</b> with real-time geospatial filtering, and an <b>AI-powered insurance claims agent</b> that "
    "reads PDFs, extracts structured data via an LLM, and routes claims automatically."
))
story.append(body(
    "I also completed an <b>internship at Zidio Development</b> where I resolved 15+ frontend/backend "
    "issues and built reusable React components using Agile/Git workflows. "
    "I'm a fast learner who loves building systems that actually work in production — and I'm excited "
    "to bring that energy to this role."
))
story.append(Spacer(1, 3*mm))
story.append(tip("End with: 'I'm particularly excited about the Azure focus here — I'd love to talk about how my backend and AI experience maps to Azure services.'"))

story.append(sub("Key Stats to Drop Naturally"))
stats = [
    ["Metric", "Detail"],
    ["CGPA", "7.5 / 10 — B.E. Computer Science, BNCOE Pusad"],
    ["Publication", "IJISRT 2025 — NLP/Deep Learning Sentiment Analysis"],
    ["Internship", "Zidio Development (Jan–Apr 2025) — Frontend + Backend"],
    ["REST APIs shipped", "15+ (Expense Manager) + 12+ (Vendor Connect) + LLM pipeline"],
    ["Languages / Core", "Python, JavaScript, SQL"],
    ["AI/ML exposure", "Scikit-learn, LLM Integration, Prompt Engineering, Groq, LLaMA 3.3-70B"],
    ["Cloud / Deploy", "AWS (EC2, S3, IAM), Vercel, Render, GitHub Actions CI/CD"],
]
story.append(info_table(stats, col_widths=[70*mm, PAGE_W - 36*mm - 70*mm]))

# ═══════════════════════════════════════════════════════════════
# 2. PROJECT DEEP-DIVES
# ════════════════════════════════════════════════════════════════════════════
story += section("2. PROJECT DEEP-DIVES")

# ── 2.1 Multi-Tenant SaaS ──────────────────────────────────────────────────
story.append(sub("2.1  Multi-Tenant SaaS Expense Manager"))
story.append(body("<b>Stack:</b> Django · DRF · PostgreSQL · Celery · Redis · React · GitHub Actions · Vercel"))
story.append(body(
    "A full SaaS platform where multiple organisations share one deployment but enjoy <b>complete "
    "data isolation</b> via PostgreSQL schema-based multi-tenancy. Incoming requests are dynamically "
    "routed to the correct tenant schema, eliminating any risk of cross-tenant data leakage."
))

story.append(mini("Architecture Snapshot"))
for b_text in [
    "<b>Multi-tenancy:</b> Each tenant gets a separate PostgreSQL schema. A middleware reads the subdomain/header, switches the DB search_path dynamically.",
    "<b>15+ REST APIs:</b> Built with DRF; JWT authentication + RBAC controls which roles (admin, manager, employee) can access which endpoints.",
    "<b>Celery + Redis:</b> Heavy async jobs (report generation, CSV/PDF exports, email reminders) offloaded so the main API stays fast.",
    "<b>Frontend:</b> React + Tailwind CSS on Vercel; GitHub Actions pipeline runs pytest on every PR before deploy.",
    "<b>Testing:</b> 40+ pytest tests verifying tenant isolation, auth, and background task completion.",
]:
    story.append(bullet(b_text))

story.append(mini("Likely Interview Questions"))
for q, a in [
    ("What is multi-tenancy and why did you choose schema-based?",
     "Multi-tenancy = multiple customers share one app. Schema-based means each tenant has separate DB tables — strongest isolation short of separate databases. Simpler than separate DBs to manage, better isolation than row-level. Chosen because the project needed auditability and zero leakage guarantees."),
    ("How did you prevent data leakage between tenants?",
     "Three layers: (1) Middleware sets the PostgreSQL search_path to the correct tenant schema on every request. (2) Every ORM query runs inside that schema — no cross-schema joins are possible. (3) JWT tokens include the tenant ID claim and are verified server-side on every call."),
    ("Why Celery instead of threading?",
     "Celery with Redis is production-grade and persistent — tasks survive server restarts. Python threading is not suitable for long-running IO or CPU tasks due to the GIL. Celery also provides task retries, rate-limiting, monitoring via Flower, and horizontal scaling by adding workers."),
    ("How does your CI/CD work?",
     "GitHub Actions triggers on every push to main. It runs the pytest suite, and if tests pass, deploys the frontend to Vercel. Backend can be deployed to Render/EC2. This ensures broken code never reaches production."),
]:
    story += qa(q, a)

# ── 2.2 Vendor Connect India ───────────────────────────────────────────────
story.append(PageBreak())
story.append(sub("2.2  Vendor Connect India — Street Vendor Digital Shop Builder"))
story.append(body("<b>Stack:</b> Django · MongoDB Atlas · PyMongo · JWT · Razorpay · React 19 · Leaflet · Tailwind CSS"))
story.append(body(
    "A platform that lets street vendors create digital shop profiles discoverable by nearby buyers. "
    "Key features: <b>5 km geospatial radius search</b> on an interactive Leaflet map, "
    "Razorpay payment integration with webhook verification, and JWT + bcrypt security."
))

story.append(mini("Architecture Snapshot"))
for b_text in [
    "<b>12+ REST APIs:</b> Vendor onboarding, product management, shop profiles, location-tagged data.",
    "<b>MongoDB Atlas + Geospatial:</b> Vendor documents store GeoJSON coordinates. 2dsphere index enables fast $nearSphere queries for 5 km radius filtering.",
    "<b>Leaflet map:</b> Frontend fetches nearby vendors from API and plots markers on an interactive map with shop details on click.",
    "<b>Razorpay webhooks:</b> Payments verified server-side using HMAC signature check on every webhook event — prevents fake payment signals.",
    "<b>Security:</b> JWT access tokens, bcrypt password hashing (cost factor 12), rate limiting at 100 req/min per IP to prevent brute force.",
]:
    story.append(bullet(b_text))

story.append(mini("Likely Interview Questions"))
for q, a in [
    ("Why MongoDB over PostgreSQL for this project?",
     "Vendor data is document-centric (shop profile, product list, images, location all in one document). MongoDB's native GeoJSON support and 2dsphere index made geospatial queries trivial. For a relational use case like the expense manager, PostgreSQL is better — I chose based on the data model."),
    ("Explain the 5 km geospatial query.",
     "Each vendor document stores a location field as GeoJSON Point. I created a 2dsphere index on that field. The query uses $nearSphere with $maxDistance in meters (5000). MongoDB returns documents sorted by proximity, which I return to the frontend to render on the Leaflet map."),
    ("How do you verify Razorpay webhooks?",
     "Razorpay sends a HMAC-SHA256 signature in the X-Razorpay-Signature header. On the server I recompute the HMAC using the raw request body and my webhook secret key. If they match, the event is authentic. If not, I return 400 and ignore it — prevents attackers faking payment success events."),
    ("What is rate limiting and how did you implement it?",
     "Rate limiting caps requests per IP per time window. I used Django's django-ratelimit decorator or DRF throttle classes set to 100 req/min. Requests over the limit get 429 Too Many Requests. This prevents brute-force login attacks and API abuse."),
]:
    story += qa(q, a)

# ── 2.3 Smart Review AI ───────────────────────────────────────────────────
story.append(sub("2.3  Smart Review AI — LLM-Powered Code Review Tool"))
story.append(body("<b>Stack:</b> Django REST · React · Groq API · LLaMA · Prompt Engineering"))
story.append(body(
    "An AI tool where developers paste code and receive structured, actionable feedback "
    "generated by an LLM. The key challenge was <b>prompt engineering</b> to produce consistent, "
    "structured output rather than noisy or hallucinated responses."
))

story.append(mini("Key Talking Points"))
for b_text in [
    "<b>Prompt Engineering:</b> Designed system prompts that instruct the LLM to return feedback in a fixed JSON schema (issues, severity, suggestions). Prevents free-form rambling.",
    "<b>Output Handling:</b> LLM responses are parsed and validated. If the JSON is malformed, the system retries once with a corrective prompt before returning an error.",
    "<b>Backend:</b> Django REST endpoint accepts code + language, calls Groq API, parses response, returns structured feedback.",
    "<b>Frontend:</b> React UI with syntax-highlighted code editor, displays feedback by category (bugs, style, performance).",
]:
    story.append(bullet(b_text))

story.append(mini("Key Question"))
for q, a in [
    ("How do you ensure consistent LLM output?",
     "Three techniques: (1) Detailed system prompt specifying exact JSON schema with field names and types. (2) Temperature set to 0 or 0.1 for deterministic output. (3) JSON parsing wrapped in try/except — on failure, a retry prompt explicitly says 'return ONLY valid JSON, no markdown'. If retry also fails, I surface a clear error rather than showing garbage output."),
]:
    story += qa(q, a)

# ── 2.4 Insurance Claims Agent (The PDF Assignment) ───────────────────────
story.append(PageBreak())
story.append(sub("2.4  Autonomous Insurance Claims Processing Agent (Your PDF Assignment)"))
story.append(body("<b>Stack:</b> FastAPI · Groq API · LLaMA 3.3-70B · pdfplumber · SQLAlchemy · React · Vercel · Render"))

story.append(mini("What It Does (One Breath)"))
story.append(body(
    "An end-to-end AI agent: upload an insurance claim PDF → pdfplumber extracts raw text → "
    "LLM extracts 7 structured fields as JSON → rules-based router assigns one of four queues "
    "(Fast-Track, Manual Review, Investigation Flag, Specialist Queue) → saved to SQLite with "
    "full audit trail → visible in React dashboard with analytics."
))

story.append(mini("Architecture — The Full Flow"))
arch_rows = [
    ["Step", "What Happens", "Technology"],
    ["1", "User uploads PDF via drag-drop", "React + Vite (port 5173)"],
    ["2", "POST /api/claims/process (multipart form-data)", "FastAPI (port 8000)"],
    ["3", "Text extraction page by page", "pdfplumber"],
    ["4", "Text + system prompt → LLM call", "Groq API / LLaMA 3.3-70B"],
    ["5", "LLM returns JSON with 7 fields (null if missing)", "Prompt Engineering"],
    ["6", "Mandatory field check → missing fields list", "Pydantic validation"],
    ["7", "Rules engine assigns route + reasoning", "Deterministic Python"],
    ["8", "Claim + route + fields saved", "SQLAlchemy / SQLite"],
    ["9", "JSON response to React frontend", "FastAPI response model"],
]
story.append(info_table(arch_rows, col_widths=[20*mm, 75*mm, 60*mm]))
story.append(Spacer(1, 3*mm))

story.append(mini("The 5-Tier Routing Logic (Priority Order)"))
for b_text in [
    "<b>1 — Fraud / Investigation Flag:</b> Fraud-related keywords detected in description (e.g., 'staged', 'suspicious', 'inconsistent').",
    "<b>2 — Manual Review:</b> ANY mandatory field is null (claim number, claimant name, policy number, incident date, description, claim type, damage amount).",
    "<b>3 — Specialist Queue:</b> Claim type is injury — requires medical expertise.",
    "<b>4 — Fast-Track:</b> All fields present + damage under ₹25,000 → approve quickly.",
    "<b>5 — Standard Review:</b> Default if no other rule matches.",
]:
    story.append(bullet(b_text))

story.append(mini("Deep-Dive Q&A — Expect These"))
for q, a in [
    ("Why deterministic routing and not AI-based routing?",
     "Insurance routing decisions must be auditable, consistent, and explainable for regulatory compliance. If an AI made routing decisions, the same document could theoretically get different routes on different days. A deterministic rules engine guarantees: same input → same output always. This is crucial for claim SLA agreements and fraud litigation."),
    ("Why FastAPI over Django for this project?",
     "FastAPI is async by default — critical when waiting on Groq API calls (IO-bound). It auto-generates Swagger docs via OpenAPI, has built-in Pydantic request/response validation, and has much lower boilerplate than Django for a pure-API service. Django would be overkill without the ORM, admin, or auth machinery being needed."),
    ("Why Groq instead of OpenAI?",
     "Groq offers a completely free tier with LLaMA 3.3-70B — comparable quality to GPT-4 for structured extraction. It also has best-in-class inference speed (tokens/sec) because it runs on custom LPU hardware. For a v1 project, free tier + speed + quality made it the obvious choice."),
    ("What if the PDF is scanned / image-based?",
     "pdfplumber returns empty or near-empty text for scanned PDFs. I handle this gracefully: a ValueError is raised with a clear user-facing message explaining OCR is not supported in v1. In v2 I would integrate pytesseract — convert PDF pages to images with pdf2image, then run tesseract OCR to extract text before the LLM step."),
    ("What if the LLM returns invalid JSON?",
     "I wrap JSON parsing in try/except. On failure: (1) Log the raw LLM response for debugging. (2) Return a 422 HTTP error with a descriptive message. I could also implement a retry with a corrective system prompt as v2 improvement."),
    ("How do you handle different document types?",
     "First a document-type detection LLM call identifies whether it's an insurance claim, medical claim, police report, legal complaint, or property damage report. Then I use a different extraction prompt and different mandatory field rules for each type. This makes the system generic rather than hardcoded to ACORD forms."),
    ("Walk me through what happens when I upload a PDF.",
     "1) Drag and drop PDF. 2) React sends POST /api/claims/process as multipart form-data. 3) pdfplumber extracts raw text page by page. 4) Text + system prompt sent to Groq LLaMA. 5) LLM returns JSON with 7 fields or null. 6) Validator builds missing-fields list. 7) Router applies 5 rules in priority order. 8) Claim + result saved to SQLite via SQLAlchemy. 9) Response shows extracted fields, missing fields, route, and reasoning."),
    ("What are the four routing outcomes?",
     "Fast-Track (all fields present, low damage — approve quickly), Manual Review (missing mandatory fields — human must complete), Investigation Flag (fraud keywords detected — escalate), Specialist Queue (injury claim — medical expertise needed)."),
    ("What would you improve in v2?",
     "OCR for scanned PDFs (pytesseract), real JWT authentication, PostgreSQL instead of SQLite for concurrency, batch PDF processing, email notifications on dispatch, and a trained fraud-detection ML model replacing keyword matching."),
]:
    story += qa(q, a)

# ════════════════════════════════════════════════════════════════════════════
# 3. AZURE FUNDAMENTALS
# ════════════════════════════════════════════════════════════════════════════
story += section("3. AZURE FUNDAMENTALS (Product-Based Company Focus)")
story.append(body(
    "Even if you haven't deployed production systems on Azure, demonstrating solid conceptual "
    "understanding and the ability to map your existing skills to Azure services is exactly what "
    "interviewers expect at the junior level. Study these core services and concepts."
))

story.append(sub("Core Azure Services You Must Know"))
azure_services = [
    ["Service", "What It Is", "Your Map"],
    ["Azure App Service", "Managed PaaS for web apps/APIs — no server management", "Like Render/Vercel but on Azure. Your Django/FastAPI backends would deploy here."],
    ["Azure Functions", "Serverless compute — runs code triggered by events", "Like Celery tasks but serverless. Perfect for your background jobs (report generation)."],
    ["Azure Container Apps", "Managed Kubernetes-based container hosting", "Run your Docker containers without managing K8s clusters."],
    ["Azure Blob Storage", "Scalable object storage for files, images, backups", "Like S3 (which you've used). Store PDFs, CSV exports, claim documents."],
    ["Azure SQL / Cosmos DB", "Managed SQL (PostgreSQL/MySQL) or NoSQL (like MongoDB Atlas)", "Azure DB for PostgreSQL = your SaaS expense manager's DB on Azure."],
    ["Azure Service Bus", "Managed message queue + pub/sub", "Like Redis + Celery for async messaging. Enterprise-grade."],
    ["Azure API Management", "API gateway — rate limiting, auth, monitoring, versioning", "Sits in front of your FastAPI/DRF APIs. Like a managed reverse proxy."],
    ["Azure Cognitive Services", "Pre-built AI APIs — Vision, Language, Speech, OpenAI", "Azure OpenAI Service = GPT-4 / embeddings via Azure instead of OpenAI directly."],
    ["Azure DevOps", "CI/CD pipelines, repos, boards, test plans", "Like GitHub Actions — you already know CI/CD concepts."],
    ["Azure Key Vault", "Secure storage for secrets, API keys, connection strings", "No more secrets in .env files. Apps fetch secrets from Key Vault at runtime."],
    ["Azure Active Directory (Entra)", "Identity and access management — SSO, MFA, RBAC", "Like your JWT + RBAC but enterprise-grade. B2C variant for external users."],
    ["Azure Monitor / App Insights", "Logging, metrics, alerts, distributed tracing", "Know when your app is down before users do."],
    ["Azure CDN", "Content delivery network — cache static assets globally", "Like your Vercel CDN but configurable. Speed up your React apps."],
    ["Azure Load Balancer", "Distributes traffic across multiple app instances", "Scale your API horizontally under load."],
]
story.append(info_table(azure_services, col_widths=[45*mm, 60*mm, PAGE_W-36*mm-45*mm-60*mm]))
story.append(Spacer(1, 3*mm))

story.append(sub("Azure Concept Q&A"))
for q, a in [
    ("What is the difference between IaaS, PaaS, and SaaS on Azure?",
     "IaaS (Infrastructure as a Service) = Azure gives you VMs, networking, storage — you manage the OS and runtime (Azure VMs, like AWS EC2). PaaS (Platform as a Service) = Azure manages OS and runtime — you just deploy code (Azure App Service, Azure Functions). SaaS = fully managed software (Microsoft 365, Dynamics). For a junior dev role you'll mostly work with PaaS."),
    ("How would you deploy your Django DRF API on Azure?",
     "Option 1: Azure App Service — push code or Docker container, Azure manages the runtime. Set env vars via Application Settings (mapped from Key Vault). Configure custom domain and SSL. Option 2: Azure Container Apps — package Django in Docker, push to Azure Container Registry, deploy to Container Apps. Connect to Azure DB for PostgreSQL. Set up managed identity so the app fetches DB credentials from Key Vault without hardcoded secrets."),
    ("How would you replace Celery+Redis with Azure services?",
     "Azure Service Bus handles the message queue (like Redis). Azure Functions or Azure Container Apps workers consume messages from the queue — like Celery workers. Azure Storage Queues is a simpler alternative for basic async tasks. Azure Durable Functions handle complex workflows with state, retries, and orchestration."),
    ("What is Azure Managed Identity and why does it matter?",
     "Managed Identity gives an Azure resource (like an App Service) an automatically-managed Azure AD identity. This identity can be granted RBAC permissions to access other Azure services (Key Vault, Blob Storage, SQL) without any passwords or connection strings in code. It eliminates secret sprawl — a major security improvement over storing credentials in environment variables."),
    ("How does Azure OpenAI Service differ from calling OpenAI directly?",
     "Same GPT-4/embeddings models but hosted within Azure's security boundary. Benefits: data never leaves Azure (compliance), can use Managed Identity for auth, subject to your Azure SLA, integrates with Azure Monitor for usage tracking. Important for regulated industries like insurance, finance, healthcare that cannot send data to external APIs."),
    ("What is Azure DevOps and how does it relate to GitHub Actions?",
     "Azure DevOps is a full ALM suite: Boards (project tracking like Jira), Repos (Git hosting), Pipelines (CI/CD like GitHub Actions), Test Plans, and Artifacts (package registry). GitHub Actions is simpler and developer-friendly. Azure DevOps is enterprise-focused with more governance controls. You can also use GitHub Actions to deploy to Azure — they are complementary."),
    ("Explain Azure RBAC.",
     "Role-Based Access Control in Azure lets you assign roles to users/groups/service principals at different scopes (management group, subscription, resource group, resource). Built-in roles: Owner (full access), Contributor (create/manage but no access grants), Reader (view only). Custom roles can be defined for fine-grained control. This is the same concept as the RBAC you built in your DRF APIs."),
]:
    story += qa(q, a)

# ════════════════════════════════════════════════════════════════════════════
# 4. AI / LLM CONCEPTS
# ════════════════════════════════════════════════════════════════════════════
story += section("4. AI / LLM CONCEPTS")

story.append(sub("Core Concepts to Know Cold"))
for q, a in [
    ("What is an LLM?",
     "A Large Language Model is a neural network trained on massive text corpora to predict the next token in a sequence. At inference time, given a prompt, it generates tokens probabilistically. Modern LLMs (GPT-4, LLaMA, Gemini) have billions of parameters and exhibit emergent capabilities like reasoning, code generation, and structured extraction."),
    ("What is prompt engineering?",
     "The practice of designing input prompts to elicit desired outputs from an LLM. Key techniques: (1) System prompt — sets the model's role and output format. (2) Few-shot examples — show 1–3 input/output pairs in the prompt. (3) Chain-of-thought — ask the model to reason step-by-step. (4) Output constraints — specify JSON schema, response length, tone. You used this in your insurance project to get reliable JSON extraction."),
    ("What is temperature in LLMs?",
     "Temperature controls output randomness. Temperature=0 → almost deterministic, always picks the highest-probability token. Temperature=1 → default, balanced creativity and coherence. Temperature>1 → more random/creative but less reliable. For structured extraction (like your JSON claims data), use temperature=0 or 0.1 for consistency."),
    ("What is RAG (Retrieval-Augmented Generation)?",
     "RAG combines a retrieval system (vector database search) with an LLM. When a question comes in: (1) Embed the question as a vector. (2) Retrieve the top-K most similar document chunks from a vector store (Pinecone, FAISS, Azure Cognitive Search). (3) Inject retrieved chunks into the LLM prompt as context. (4) LLM answers grounded in retrieved facts. Reduces hallucinations and lets you use private data without fine-tuning."),
    ("What is fine-tuning vs prompting?",
     "Prompting = you provide instructions in the prompt at inference time — no training required, fast iteration. Fine-tuning = you further train a pre-trained model on your domain-specific examples — requires labelled data, compute, and time. Fine-tuning creates a specialised model; prompting adapts a general model on-the-fly. For most production use cases, prompt engineering + RAG beats fine-tuning in cost-effectiveness."),
    ("What is a hallucination in LLMs?",
     "When the model generates plausible-sounding but factually incorrect information with high confidence. Common causes: question is outside training data, model fills gaps with statistical patterns. Mitigation: RAG (ground answers in retrieved facts), low temperature, output validation, asking the model to say 'I don't know' if uncertain, and deterministic rules for critical decisions (as you did with routing)."),
    ("What is Groq and why is it fast?",
     "Groq is an AI inference company that built custom LPU (Language Processing Unit) hardware specifically optimised for transformer inference. Unlike GPUs (general parallel compute), LPUs have deterministic execution and massive memory bandwidth, enabling 500+ tokens/second versus 30–80 tokens/second on typical GPU clouds. This is why Groq API responses feel near-instant."),
    ("What is pdfplumber and when would you use OCR instead?",
     "pdfplumber extracts text from PDF files that contain actual text objects (digitally-created PDFs). It works excellently for forms, reports, and most business documents. OCR (Optical Character Recognition) is needed when the PDF is a scanned image — there are no text objects, just pixel data. You'd use pytesseract + pdf2image to convert each page to an image then extract text with Tesseract. Your v2 plan correctly identifies this limitation."),
    ("Explain your prompt engineering approach for the insurance project.",
     "System prompt instructs the model to: (1) Act as an insurance document parser. (2) Extract exactly 7 named fields. (3) Return ONLY a valid JSON object with no markdown, no explanation. (4) Set missing fields to null (not empty string). (5) Be format-agnostic — find field values regardless of how they're labelled in the document. Temperature set to 0. Response parsed with json.loads() in a try/except with a clear 422 error on failure."),
    ("What are embeddings?",
     "Dense vector representations of text in high-dimensional space where semantically similar text has similar vectors. Generated by embedding models (OpenAI text-embedding-ada-002, sentence-transformers). Used in: semantic search, RAG retrieval, clustering, classification, recommendation systems. Foundation of modern NLP pipelines."),
    ("What is the difference between GPT-4 and LLaMA?",
     "GPT-4 is OpenAI's proprietary, closed-source model accessed via API. LLaMA (Meta) is an open-source model family with weights you can download and run locally or via providers like Groq. LLaMA 3.3-70B (which you used) is competitive with GPT-4 on many benchmarks. Open-source models can be self-hosted for data privacy, cost control, and no vendor lock-in."),
]:
    story += qa(q, a)

# ════════════════════════════════════════════════════════════════════════════
# 5. BEHAVIOURAL QUESTIONS
# ════════════════════════════════════════════════════════════════════════════
story += section("5. BEHAVIOURAL QUESTIONS — STAR METHOD")
story.append(body(
    "For every behavioural question, use the <b>STAR framework</b>: "
    "<b>S</b>ituation → <b>T</b>ask → <b>A</b>ction → <b>R</b>esult. "
    "Keep answers to 90–120 seconds. Always end with a concrete result or learning."
))
story.append(Spacer(1, 3*mm))

bq_data = [
    ("Tell me about a time you solved a difficult technical problem.",
     "S: During the insurance claims project, the LLM kept returning null for all fields on some documents. T: I needed reliable extraction across varied document formats. A: I analysed 10 real ACORD forms, identified that rigid field-name matching failed on synonyms. Rewrote the system prompt to be format-agnostic — instructing the model to find semantic equivalents, not exact labels. Added few-shot examples. R: Extraction accuracy improved dramatically. The system now handles FNOL, ACORD, and generic claim letters without document-specific prompts."),
    ("Describe a time you had to learn something quickly.",
     "S: In my final year, I had no ML background but wanted to build the sentiment analysis project. T: Needed to learn deep learning fundamentals and publish a paper. A: Enrolled at Naresh IT, studied intensively, built the project iteratively — starting with scikit-learn baselines, progressing to LSTM models. R: Published a peer-reviewed paper in IJISRT 2025 and gained hands-on AI/ML skills I've since applied to LLM integration projects."),
    ("Tell me about a time you improved code quality.",
     "S: At Zidio Development internship, the onboarding flow had 15+ frontend/backend bugs and inconsistent UI. T: My responsibility was to resolve these issues within the sprint. A: Systematically triaged bugs by severity, fixed React component state issues, standardised API error handling, built 10+ reusable components with Axios integration. R: Application errors reduced, UI consistency improved, and the reusable components were adopted across other modules — I received positive feedback in my sprint review."),
    ("Describe a project you're most proud of and why.",
     "S: The multi-tenant SaaS expense manager. T: Build a production-grade platform supporting multiple real organisations with zero data leakage. A: Designed schema-based PostgreSQL multi-tenancy from scratch, built 15+ authenticated APIs, implemented Celery for async, set up CI/CD with GitHub Actions. R: 40+ tests pass, zero cross-tenant leakage demonstrated, deployed and running. Proud because it required integrating every layer — DB design, security, async processing, testing, deployment — into a coherent system."),
    ("Tell me about a time you worked in a team.",
     "S: At Zidio Development, working in an Agile team with daily standups and sprint cycles. T: Deliver features and bug fixes on time while maintaining code quality. A: Participated in peer code reviews, flagged issues constructively, used Git branching and PRs to collaborate, communicated blockers early. R: Sprint goals were consistently met and my PRs had minimal rework — the team lead praised my code review contributions."),
    ("Where do you see yourself in 3 years?",
     "In 3 years I want to be a solid backend engineer with deep Azure and cloud-native expertise. I'd like to be leading small technical initiatives — designing system architecture for AI-powered features, mentoring junior developers, and contributing to production systems that serve real users at scale. This role feels like the right foundation for that path."),
]
for q, a in bq_data:
    story += qa(q, a)
    story.append(Spacer(1, 2*mm))

# ════════════════════════════════════════════════════════════════════════════
# 6. COMMON INTERVIEW PITFALLS
# ════════════════════════════════════════════════════════════════════════════
story += section("6. COMMON INTERVIEW PITFALLS — AVOID THESE")
pitfalls = [
    ("Vague tech answers", "Never say 'I used JWT for security.' Always say WHY: 'JWT was chosen because it's stateless — the server doesn't need to store session data, which is critical for horizontal scaling across multiple instances.'"),
    ("Saying 'I just followed a tutorial'", "Never diminish your work. You built these systems and understand every layer. Talk about decisions you made, problems you debugged, trade-offs you evaluated."),
    ("Freezing on unknown Azure service names", "If they name a service you don't know: 'I haven't worked with [X] directly, but based on the name/context it sounds similar to [Y] which I have used. Could you tell me more about where it sits in the stack? I'm a fast learner and would ramp up quickly.'"),
    ("Forgetting numbers", "Always have 3–4 stats ready: 15+ APIs, 40+ tests, 5 km radius, 7 extracted fields. Specificity signals credibility."),
    ("Answering behavioural questions abstractly", "Don't say 'I'm a team player.' Tell a specific story with a real outcome. Abstract answers are forgettable."),
    ("Not asking questions at the end", "Always ask 2–3 smart questions. Shows genuine interest. See Section 7 for ideas."),
    ("Talking too fast when nervous", "Nervous = fast = unclear. Pause after each answer. Breathe. It's okay to say 'Let me think for a second.'"),
    ("Over-claiming Azure expertise", "Be honest about your level. 'I have solid conceptual knowledge of Azure services and I've worked with AWS (EC2, S3, IAM). I'm confident I can ramp up on Azure-specific tooling quickly — the core concepts transfer.'"),
    ("Saying your project has no weaknesses", "Every honest engineer knows their v1 has limitations. Name them proactively: 'In v2 I would add OCR support, replace SQLite with PostgreSQL, and add JWT auth.' This shows maturity and forward thinking."),
    ("Not connecting your projects to business value", "Always tie technical work to outcomes: 'This cuts manual claim processing from hours to seconds' or 'This eliminates cross-tenant data leakage which would be a compliance catastrophe.'"),
]
for title, detail in pitfalls:
    story.append(warn(f"<b>{title}:</b> {detail}"))
    story.append(Spacer(1, 1*mm))

# ════════════════════════════════════════════════════════════════════════════
# 7. PRACTICE DELIVERY TIPS
# ════════════════════════════════════════════════════════════════════════════
story += section("7. PRACTICE DELIVERY TIPS")
tips_list = [
    "Record yourself answering the top 5 project questions on your phone. Watch it back. Notice where you hesitate or say 'um'.",
    "Prepare a 30-second, 90-second, and 3-minute version of each project explanation. Match length to the question depth.",
    "Know your resume numbers cold: 15+ APIs, 40+ tests, 5 km radius, 7 fields, 4 routing outcomes, 12+ APIs, 5-tier priority.",
    "Draw your insurance claims architecture on paper from memory. If you can draw it, you can explain it.",
    "Practice the routing logic out loud: 'First I check for fraud keywords, then mandatory fields, then claim type, then damage amount, then default.' Smooth recall signals deep understanding.",
    "Prepare 3 smart questions to ask the interviewer: (1) 'What Azure services does the team use most today?' (2) 'What does the first 90 days look like for someone joining this team?' (3) 'What's the biggest technical challenge you're currently working on?'",
    "Night before: review the quick reference cards (Sections 9 & 10). Morning of: read your elevator pitch once, then put the guide down. Trust your preparation.",
    "If you blank on a technical question: 'That's a great question. Let me think through it...' then reason out loud. Interviewers value thinking process over instant recall.",
]
for t in tips_list:
    story.append(tip(t))
    story.append(Spacer(1, 1*mm))

# ════════════════════════════════════════════════════════════════════════════
# 8. MOCK INTERVIEW SCENARIOS
# ════════════════════════════════════════════════════════════════════════════
story += section("8. MOCK INTERVIEW SCENARIOS WITH SAMPLE ANSWERS")

story.append(sub("Scenario A — Technical Deep Dive (30 min)"))
story.append(body("<i>Interviewer plays a senior engineer. You have 90 seconds per answer max.</i>"))
story.append(Spacer(1, 2*mm))

for q, a in [
    ("Walk me through your most complex project architecture.",
     "I'll walk you through the insurance claims agent since it's the most technically layered. At the top is a React + Vite frontend running on Vercel. When a user uploads a PDF, it hits POST /api/claims/process on a FastAPI backend deployed on Render. The backend uses pdfplumber to extract raw text from the PDF — page by page, layout preserved. That text goes to the Groq API with LLaMA 3.3-70B. My system prompt instructs the model to return only a valid JSON object with exactly 7 fields — null for anything not found. FastAPI's Pydantic model validates the response. Then a pure Python routing engine checks 5 conditions in priority order — fraud keywords, missing fields, injury type, damage amount, and a default — and assigns one of four queue outcomes. Everything is persisted to SQLite via SQLAlchemy. The response comes back to React showing fields, missing fields, the route, and the reasoning. Total time from upload to result: under 10 seconds."),
    ("How would you scale this system to handle 10,000 claims per day?",
     "Several changes: First, swap SQLite for PostgreSQL on Azure DB for PostgreSQL — handles concurrent writes. Second, make the claim processing async: the POST endpoint immediately returns a claim_id and status 'processing', pushes the work to Azure Service Bus. Azure Functions workers pull from the queue and process claims — horizontally scalable. Third, replace direct Groq API calls with a connection pool and retry logic with exponential backoff. Fourth, add Azure Blob Storage for PDF storage instead of keeping files in memory. Fifth, add Azure Application Insights for monitoring queue depth, processing latency, and error rates. The deterministic routing engine is already stateless and scales linearly."),
    ("How would you add authentication to the claims system?",
     "JWT-based auth using Azure Active Directory B2C for external users. The FastAPI backend would validate the Azure AD JWT token on every request using the python-jose library and the Azure AD public keys endpoint. Role claims in the token would drive RBAC — claims processors can upload PDFs, managers can see analytics, admins can configure routing rules. Secrets like DB connection strings and Groq API key would be moved to Azure Key Vault, fetched at runtime via Managed Identity — no secrets in environment variables."),
    ("What would you do if the LLM's extracted data is wrong?",
     "Three layers of defence: First, validation — Pydantic checks field types and formats at parse time. Second, completeness check — if mandatory fields are null, it routes to Manual Review automatically — a human reviews and corrects. Third, audit trail — every claim is saved with the raw extracted JSON and the routing decision. If a mistake is caught later, you can trace back the exact LLM output for that claim. In v2 I'd add a human-in-the-loop review step for the first N claims from a new document format to catch systematic extraction errors before they compound."),
]:
    story += qa(q, a)
    story.append(Spacer(1, 1.5*mm))

story.append(sub("Scenario B — Azure-Focused Questions"))
for q, a in [
    ("If we asked you to migrate your expense manager to Azure from day one, what would your plan look like?",
     "Week 1 — understand the target Azure subscription, resource group structure, and naming conventions. Week 2 — containerise the Django app with Docker, push to Azure Container Registry. Deploy to Azure App Service or Container Apps. Connect to Azure DB for PostgreSQL — migrate schema with Django migrations. Move static/media files to Azure Blob Storage, set up CDN in front. Week 3 — replace Redis+Celery with Azure Service Bus + Azure Functions workers. Move secrets to Azure Key Vault with Managed Identity. Week 4 — set up Azure DevOps pipelines or GitHub Actions targeting Azure. Add Application Insights for monitoring. Throughout: maintain all existing tests passing."),
    ("We use Azure Cognitive Services for document processing. How does that compare to your pdfplumber + Groq approach?",
     "Azure Cognitive Services — specifically the Document Intelligence (formerly Form Recognizer) service — is a managed, pre-trained model specifically built for document extraction. It handles both text PDFs and scanned images natively with built-in OCR, and is SLA-backed by Microsoft with GDPR compliance. My pdfplumber + Groq approach is more flexible — I can customise the extraction schema and reasoning through prompt engineering, and it works well for variable formats. For an enterprise insurance product, Azure Document Intelligence would be a strong v2 consideration because of compliance, OCR support, and reduced maintenance. I'd evaluate based on the document variety and compliance requirements."),
]:
    story += qa(q, a)

story.append(sub("Scenario C — Behavioural Panel (15 min)"))
for q, a in [
    ("Why do you want to work at a product-based company vs a service company?",
     "In a product company I get to own a problem end-to-end and iterate on the same system over months and years — I see the real-world impact of my decisions. In service companies you often build for a brief engagement and move on. I want to build systems that scale, that I can improve based on production learnings, and that serve real users. The Azure focus here also means I'd be working with enterprise-grade infrastructure — that's the kind of depth I want to develop early in my career."),
    ("You're a fresher. Why should we pick you over someone with 2 years of experience?",
     "Fair question. I may have fewer years of employment, but I've shipped production-grade systems: a multi-tenant SaaS with 40+ tests and CI/CD, an AI claims agent with a deterministic routing engine, and a geospatial vendor platform with Razorpay webhooks. I've also published a research paper. I have no bad habits to unlearn, I learn fast, and I bring genuine excitement for the problem space. I'll need mentoring on your specific stack and processes — and I'll invest fully in that ramp-up. The question is whether the team has the appetite to grow someone who will deliver real value from month 2 or 3."),
]:
    story += qa(q, a)

# ════════════════════════════════════════════════════════════════════════════
# 9. AZURE QUICK REFERENCE CARD
# ════════════════════════════════════════════════════════════════════════════
story += section("9. QUICK REFERENCE CARD — AZURE SERVICES")
story.append(body("Photocopy this page and study it on the morning of your interview."))
story.append(Spacer(1, 3*mm))

col1 = [
    "COMPUTE",
    "App Service — PaaS web/API hosting",
    "Azure Functions — Serverless compute",
    "Container Apps — Managed containers",
    "Virtual Machines — IaaS, full control",
    "AKS — Managed Kubernetes",
    "",
    "STORAGE",
    "Blob Storage — Object store (files, PDFs)",
    "Azure Files — Managed file share (NFS)",
    "Table Storage — NoSQL key-value",
    "Queue Storage — Simple async queue",
    "",
    "DATABASE",
    "Azure SQL Database — Managed SQL Server",
    "Azure DB for PostgreSQL — Managed Postgres",
    "Azure Cosmos DB — Global NoSQL",
    "Azure Cache for Redis — Managed Redis",
    "",
    "INTEGRATION",
    "Service Bus — Enterprise messaging",
    "Event Grid — Event routing",
    "Event Hubs — Big data streaming",
    "Logic Apps — Low-code workflows",
]

col2 = [
    "AI / COGNITIVE",
    "Azure OpenAI Service — GPT-4, embeddings",
    "Document Intelligence — Form extraction, OCR",
    "Cognitive Search — Vector + keyword search",
    "Language Service — NLP, sentiment",
    "Computer Vision — Image analysis",
    "",
    "SECURITY & IDENTITY",
    "Azure AD / Entra ID — Identity platform",
    "Key Vault — Secrets management",
    "Managed Identity — Passwordless auth",
    "Defender for Cloud — Security posture",
    "",
    "DEVOPS & MONITORING",
    "Azure DevOps — CI/CD, boards, repos",
    "Application Insights — APM tracing",
    "Azure Monitor — Metrics + alerts",
    "Container Registry — Docker image store",
    "",
    "NETWORKING",
    "API Management — API gateway",
    "Azure CDN — Content delivery",
    "VNet — Virtual networking",
    "Load Balancer — Traffic distribution",
    "Front Door — Global load balancer + CDN",
]

ref_tbl = Table(
    [[ref_card("AZURE SERVICES — LEFT", col1),
      Spacer(4*mm, 1),
      ref_card("AZURE SERVICES — RIGHT", col2)]],
    colWidths=[(PAGE_W - 36*mm)/2 - 2*mm, 4*mm, (PAGE_W - 36*mm)/2 - 2*mm]
)
story.append(ref_tbl)

# ════════════════════════════════════════════════════════════════════════════
# 10. LLM QUICK REFERENCE CARD
# ════════════════════════════════════════════════════════════════════════════
story += section("10. QUICK REFERENCE CARD — LLM & AI TERMS")
story.append(Spacer(1, 3*mm))

llm_terms_1 = [
    "LLM FUNDAMENTALS",
    "Token — smallest text unit the model processes",
    "Context window — max tokens in one call",
    "Temperature — 0=deterministic, 1=default, >1=creative",
    "Top-p (nucleus sampling) — token sampling strategy",
    "System prompt — model role/instruction prefix",
    "User prompt — the actual input message",
    "Few-shot — examples in prompt to guide format",
    "Zero-shot — no examples, model uses general knowledge",
    "Chain-of-thought — step-by-step reasoning in prompt",
    "",
    "RETRIEVAL & MEMORY",
    "RAG — Retrieval-Augmented Generation",
    "Embedding — vector representation of text",
    "Vector DB — Pinecone, FAISS, Azure Cognitive Search",
    "Semantic search — similarity by meaning, not keywords",
    "Chunking — splitting docs into LLM-sized pieces",
    "Hallucination — confident but false LLM output",
    "",
    "YOUR PROJECT TERMS",
    "FNOL — First Notice of Loss (insurance claim start)",
    "ACORD — Standard insurance form format",
    "pdfplumber — Python text-PDF extraction library",
    "Groq — LPU inference platform, very fast",
    "LLaMA 3.3-70B — Meta open-source LLM you used",
]

llm_terms_2 = [
    "MODEL TYPES",
    "Foundation model — large pre-trained base (GPT-4, LLaMA)",
    "Fine-tuned model — foundation + domain training",
    "Embedding model — converts text to vectors",
    "Instruction-tuned — trained to follow instructions",
    "RLHF — Reinforcement Learning from Human Feedback",
    "",
    "ARCHITECTURE",
    "Transformer — attention-based neural architecture",
    "Attention — mechanism that weights token relationships",
    "Parameters — model weights (70B = 70 billion)",
    "Inference — running the model to generate output",
    "Training — learning weights from data",
    "",
    "AI SERVICES ON AZURE",
    "Azure OpenAI — GPT-4, embeddings, within Azure boundary",
    "Document Intelligence — pre-trained form extraction",
    "Cognitive Search — RAG-ready search with AI enrichment",
    "AI Studio — Azure ML model hub and playground",
    "Responsible AI — fairness, reliability, safety principles",
    "",
    "PYTHON AI STACK",
    "Scikit-learn — classical ML (you used this)",
    "NumPy / Pandas — data handling (you used these)",
    "LangChain — LLM orchestration framework",
    "Hugging Face — open-source model hub",
    "FastAPI — async Python API (you used this)",
]

llm_tbl = Table(
    [[ref_card("LLM TERMS — LEFT", llm_terms_1),
      Spacer(4*mm, 1),
      ref_card("LLM TERMS — RIGHT", llm_terms_2)]],
    colWidths=[(PAGE_W - 36*mm)/2 - 2*mm, 4*mm, (PAGE_W - 36*mm)/2 - 2*mm]
)
story.append(llm_tbl)

# ── Final page ──────────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(Spacer(1, 30*mm))
story.append(Paragraph("YOU'VE GOT THIS, ROHIT.", S("final",
    fontSize=22, textColor=NAVY, fontName="Helvetica-Bold",
    alignment=TA_CENTER, leading=28)))
story.append(Spacer(1, 5*mm))
story.append(Paragraph(
    "You've shipped real production systems, published research, and built an AI agent "
    "from scratch. That's not fresher work — that's engineer work.",
    S("final2", fontSize=11, textColor=MID_GRAY, fontName="Helvetica",
      alignment=TA_CENTER, leading=16, spaceAfter=4)
))
story.append(Spacer(1, 3*mm))
story.append(Paragraph(
    "Sleep well. Review the quick reference cards in the morning. "
    "Walk in confident. Speak clearly. Own your projects.",
    S("final3", fontSize=10, textColor=AZURE_BLUE, fontName="Helvetica-BoldOblique",
      alignment=TA_CENTER, leading=15)
))
story.append(Spacer(1, 8*mm))
story.append(HRFlowable(width="60%", thickness=2, color=GOLD, hAlign="CENTER"))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("rohitranveer358@gmail.com  |  +91 9158000676",
    S("contact", fontSize=9, textColor=MID_GRAY, fontName="Helvetica",
      alignment=TA_CENTER)))

# ── Build ────────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF generated successfully:", out)