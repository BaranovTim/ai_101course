"""PDF certificate generation with ReportLab."""
import io

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

INDIGO = HexColor("#4F46E5")
PURPLE = HexColor("#9333EA")
SLATE = HexColor("#131B2E")
GRAY = HexColor("#464555")
LIGHT = HexColor("#FAF8FF")


def build_certificate_pdf(cert):
    buf = io.BytesIO()
    page = landscape(letter)
    width, height = page
    c = canvas.Canvas(buf, pagesize=page)

    # Background
    c.setFillColor(LIGHT)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Border frame
    c.setStrokeColor(INDIGO)
    c.setLineWidth(3)
    c.rect(0.4 * inch, 0.4 * inch, width - 0.8 * inch, height - 0.8 * inch)
    c.setStrokeColor(PURPLE)
    c.setLineWidth(1)
    c.rect(0.5 * inch, 0.5 * inch, width - 1.0 * inch, height - 1.0 * inch)

    # Header
    c.setFillColor(INDIGO)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 1.3 * inch, "AI 101 ACADEMY  ·  CAYMAN ISLANDS")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 1.9 * inch, "Certificate of Completion")

    # Recipient
    user = cert.user
    full_name = (user.get_full_name() or user.username).title()
    c.setFillColor(SLATE)
    c.setFont("Helvetica-Bold", 38)
    c.drawCentredString(width / 2, height - 2.9 * inch, full_name)

    c.setStrokeColor(PURPLE)
    c.setLineWidth(2)
    c.line(width / 2 - 2.6 * inch, height - 3.1 * inch, width / 2 + 2.6 * inch, height - 3.1 * inch)

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 3.6 * inch, "has successfully completed the course")

    c.setFillColor(INDIGO)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 4.2 * inch, cert.course.title)

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 12)
    c.drawCentredString(
        width / 2,
        height - 4.7 * inch,
        "covering AI fundamentals, prompt engineering, practical applications,",
    )
    c.drawCentredString(
        width / 2,
        height - 4.95 * inch,
        "industry use cases, and modern AI tools.",
    )

    # Footer
    issued = cert.issued_at.strftime("%B %d, %Y")
    c.setFont("Helvetica", 11)
    c.drawString(1.0 * inch, 1.0 * inch, f"Issued: {issued}")
    c.drawRightString(width - 1.0 * inch, 1.0 * inch, f"Verification ID: {cert.uid}")

    c.setFillColor(PURPLE)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, 1.0 * inch, "ai101.ky")

    c.showPage()
    c.save()
    buf.seek(0)
    return buf
