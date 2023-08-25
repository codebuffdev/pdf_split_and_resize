import os
from pdf2image import convert_from_path

def convert_pdf_folder_to_images(pdf_folder, output_folder):
    # List all PDF files in the input folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the input folder.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        try:
            # Convert the PDF to images
            images = convert_from_path(pdf_path, dpi=300)
        except Exception as e:
            print(f"Error during conversion of {pdf_file}: {str(e)}")
            continue

        for i, image in enumerate(images):
            # Save each page as an image
            image_filename = f"{pdf_file}_page_{i + 1}.png"
            image.save(os.path.join(output_folder, image_filename), 'PNG')
            print(f"Page {i + 1} of {pdf_file} saved as {image_filename}")

if __name__ == '__main__':
    input_pdf_folder = '/workspaces/pdf_split_and_resize/NetworkingForDummiesSplits2'  # Replace with the path to your input PDF folder
    output_image_folder = '/workspaces/pdf_split_and_resize/NetworkingForDummiesSplits3'  # Replace with the path to your output image folder

    convert_pdf_folder_to_images(input_pdf_folder, output_image_folder)

 