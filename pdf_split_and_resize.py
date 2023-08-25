import fitz
import os

def split_and_resize_pdf(input_pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf_path)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]

        # Modify the media box to A4 size (595x842 points)
        page.set_mediabox(fitz.Rect(0, 0, 595, 842))

        # Create a new PDF with the modified page
        new_pdf = fitz.open()
        new_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        # Save the A4-sized PDF page
        output_pdf_path = os.path.join(output_folder, f'page_{page_num + 1}.pdf')
        new_pdf.save(output_pdf_path)
        new_pdf.close()

if __name__ == '__main__':
    input_pdf_path = '/workspaces/pdf_split_and_resize/Networking For Dummies.pdf'  # Replace with your input PDF file path
    output_folder = '/workspaces/pdf_split_and_resize/NetworkingForDummiesSplits2'      # Replace with your desired output folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    split_and_resize_pdf(input_pdf_path, output_folder)
 