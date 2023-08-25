import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def split_and_resize_pdf(input_pdf_path, output_folder):
    # Open the PDF file
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)

    # Iterate through each page
    for page_num, pdf_page in enumerate(pdf_reader.pages):
        # Create a new PDF canvas with A4 size
        buffer = BytesIO()
        pdf_canvas = canvas.Canvas(buffer, pagesize=letter)

        # Add the page content from the original PDF
        pdf_canvas.showPage()
        pdf_canvas.save()

        # Save the A4-sized PDF page
        buffer.seek(0)
        output_pdf_path = f'{output_folder}/page_{page_num + 1}.pdf'
        with open(output_pdf_path, 'wb') as output_pdf:
            output_pdf.write(buffer.read())

        # Close the buffer
        buffer.close()

if __name__ == '__main__':
    input_pdf_path = '/workspaces/pdf_split_and_resize/Networking For Dummies.pdf'  # Replace with your input PDF file path
    output_folder = '/workspaces/pdf_split_and_resize/NetworkingForDummiesSplits'      # Replace with your desired output folder

    split_and_resize_pdf(input_pdf_path, output_folder)
