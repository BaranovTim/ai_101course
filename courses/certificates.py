"""Professional PDF certificate generation with ReportLab."""
import io
import math

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

INDIGO = HexColor("#3525CD")
INDIGO_DARK = HexColor("#1E1580")
PURPLE = HexColor("#831ADA")
GOLD = HexColor("#C9A227")
GOLD_LIGHT = HexColor("#E7D9A8")
SLATE = HexColor("#131B2E")
GRAY = HexColor("#4A4A5A")
CREAM = HexColor("#FDFBF5")


def _draw_border(c, width, height):
    # Outer thick indigo frame
    c.setStrokeColor(INDIGO)
    c.setLineWidth(4)
    c.rect(0.35 * inch, 0.35 * inch, width - 0.7 * inch, height - 0.7 * inch)
    # Gold accent frame
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.rect(0.47 * inch, 0.47 * inch, width - 0.94 * inch, height - 0.94 * inch)
    # Inner hairline
    c.setStrokeColor(INDIGO)
    c.setLineWidth(0.5)
    c.rect(0.55 * inch, 0.55 * inch, width - 1.1 * inch, height - 1.1 * inch)

    # Corner ornaments
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    off = 0.55 * inch
    length = 0.45 * inch
    for cx, cy, dx, dy in [
        (off, off, 1, 1),
        (width - off, off, -1, 1),
        (off, height - off, 1, -1),
        (width - off, height - off, -1, -1),
    ]:
        c.line(cx, cy + dy * 0.12 * inch, cx, cy + dy * (0.12 * inch + length))
        c.line(cx + dx * 0.12 * inch, cy, cx + dx * (0.12 * inch + length), cy)


def _draw_seal(c, x, y, r):
    """Gold rosette seal with ribbon tails."""
    # Ribbon tails
    c.setFillColor(INDIGO)
    c.saveState()
    for angle in (-20, 20):
        c.saveState()
        c.translate(x, y - r * 0.35)
        c.rotate(angle)
        c.rect(-r * 0.16, -r * 1.9, r * 0.32, r * 1.6, stroke=0, fill=1)
        c.restoreState()
    c.restoreState()

    # Rosette (scalloped edge)
    c.setFillColor(GOLD)
    n = 24
    for i in range(n):
        ang = 2 * math.pi * i / n
        c.circle(x + r * 0.92 * math.cos(ang), y + r * 0.92 * math.sin(ang), r * 0.16, stroke=0, fill=1)
    c.circle(x, y, r * 0.95, stroke=0, fill=1)
    c.setFillColor(GOLD_LIGHT)
    c.circle(x, y, r * 0.78, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.circle(x, y, r * 0.66, stroke=0, fill=1)

    # Seal text
    c.setFillColor(INDIGO_DARK)
    c.setFont("Helvetica-Bold", r * 0.30)
    c.drawCentredString(x, y + r * 0.18, "AI 101")
    c.setFont("Helvetica-Bold", r * 0.16)
    c.drawCentredString(x, y - r * 0.10, "ACADEMY")
    c.setFont("Helvetica", r * 0.13)
    c.drawCentredString(x, y - r * 0.36, "CAYMAN ISLANDS")


def build_certificate_pdf(cert):
    buf = io.BytesIO()
    page = landscape(letter)
    width, height = page
    c = canvas.Canvas(buf, pagesize=page)
    c.setTitle(f"AI 101 Academy Certificate — {cert.uid}")

    # Background
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    _draw_border(c, width, height)

    # Header
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 1.15 * inch, "A I   1 0 1   A C A D E M Y   ·   C A Y M A N   I S L A N D S")

    c.setFillColor(INDIGO_DARK)
    c.setFont("Times-Bold", 40)
    c.drawCentredString(width / 2, height - 1.75 * inch, "Certificate of Completion")

    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(width / 2 - 2.1 * inch, height - 1.95 * inch, width / 2 + 2.1 * inch, height - 1.95 * inch)

    c.setFillColor(GRAY)
    c.setFont("Times-Italic", 15)
    c.drawCentredString(width / 2, height - 2.4 * inch, "This certifies that")

    # Recipient
    user = cert.user
    full_name = (user.get_full_name() or user.username).title()
    c.setFillColor(SLATE)
    c.setFont("Times-BoldItalic", 44)
    c.drawCentredString(width / 2, height - 3.15 * inch, full_name)

    name_width = c.stringWidth(full_name, "Times-BoldItalic", 44)
    c.setStrokeColor(INDIGO)
    c.setLineWidth(1.2)
    underline_half = max(name_width / 2 + 0.3 * inch, 2.2 * inch)
    c.line(width / 2 - underline_half, height - 3.38 * inch, width / 2 + underline_half, height - 3.38 * inch)

    c.setFillColor(GRAY)
    c.setFont("Times-Italic", 15)
    c.drawCentredString(width / 2, height - 3.85 * inch, "has successfully completed all lessons and assessments of")

    c.setFillColor(INDIGO)
    c.setFont("Times-Bold", 24)
    c.drawCentredString(width / 2, height - 4.4 * inch, cert.course.title)

    if cert.course.tagline:
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 10.5)
        tagline = cert.course.tagline
        if len(tagline) > 110:
            tagline = tagline[:107] + "…"
        c.drawCentredString(width / 2, height - 4.75 * inch, tagline)

    # Seal (right side)
    _draw_seal(c, width - 2.0 * inch, 1.85 * inch, 0.62 * inch)

    # Signature blocks (left + centre)
    sig_y = 1.55 * inch
    for sx, name, role in [
        (2.4 * inch, "Program Director", "AI 101 Academy"),
        (width / 2 + 0.4 * inch, "Date of Issue", cert.issued_at.strftime("%B %d, %Y")),
    ]:
        c.setStrokeColor(SLATE)
        c.setLineWidth(0.8)
        c.line(sx - 1.3 * inch, sig_y, sx + 1.3 * inch, sig_y)
        c.setFillColor(SLATE)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(sx, sig_y - 0.22 * inch, name)
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 9)
        c.drawCentredString(sx, sig_y - 0.38 * inch, role)

    # Verification footer
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(
        width / 2,
        0.62 * inch,
        f"Verification ID: {cert.uid}   ·   Verify at ai101.ky/certificates",
    )

    c.showPage()
    c.save()
    buf.seek(0)
    return buf
