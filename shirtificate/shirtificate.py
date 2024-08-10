from fpdf import FPDF


def main():
    user_name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(30)
    pdf.cell(30,30, "CS50 Shirtificate")
    pdf.ln()
    pdf.set_font("helvetica", "B", 30)
    pdf.image("shirtificate.png", x=15,y=50, w=180)
    pdf.cell(50)
    pdf.cell(30,100, f"{user_name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()