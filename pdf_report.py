from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Sales_Report.pdf")

pdf.drawString(100, 750, "E-Commerce Sales Report")

pdf.drawString(100, 720, "Generated using Python")

pdf.save()

print("PDF Created")