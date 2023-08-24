import os
import pikepdf

# Write in the variable bellow the directory that contains the file(s)
root_dir = r''
os.chdir(root_dir)

for root, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.pdf'):

            # Merges the file path and file name into one
            pdf_path = os.path.join(root, file)

            try:

                # Opens a PDF using the pikepdf library, retrieves author and
                # title information from the document, constructs a new title
                # incorporating the author's name, and then closes the PDF.
                pdf = pikepdf.open(pdf_path)
                # print(f"Opened: {pdf_path}")
                author = pdf.docinfo['/Author']
                title = pdf.docinfo['/Title']
                new_title = (f"{title} - {author}.pdf")
                pdf.close()

                # Construct the new path inside the same subfolder
                new_pdf_path = os.path.join(root, new_title)

                # If there is already a file with the same name in the directory,
                # splits the variable into file name (with path) and extension,
                # adds a number to the end (starting in 1) and renames the fale
                i = 1
                while os.path.exists(new_pdf_path):
                    base_name, extension = os.path.splitext(new_title)
                    new_title = f"{base_name}({i}){extension}"
                    new_pdf_path = os.path.join(root, new_title)
                    i += 1

                os.rename(pdf_path, new_pdf_path)
                print(f"Renamed: {pdf_path} to {new_pdf_path}")

            except Exception as e:
                print(f"Error opening {pdf_path}: {e}")
