"""
merge multiple pdfs
"""
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(input_pdfs, merged_pdf='merged.pdf'):
    merger = PdfWriter()

    for pdf in input_pdfs:
        with open(pdf, 'rb') as file:
            reader = PdfReader(file)
            print(f"[INFO] {pdf} loaded.")

            # Add all the pages from the current PDF
            for page in reader.pages:
                merger.add_page(page)

    # Write the merged output to a new file
    with open(merged_pdf, 'wb') as merged_file:
        merger.write(merged_file)

    return merged_pdf


def main(origin_pdf_list):
    print(f"[INFO] Mini PDF Utility")
    print(f"[INFO] Micro Edition Beta 1.0\n")

    print(f"[INFO] Start merging...")
    merged_doc = merge_pdfs(origin_pdf_list)
    print(f"[INFO] Merged as {merged_doc}.")


# start main app
input_pdf_files = ["input/quiz242.pdf", "input/quiz243.pdf", "input/quiz244.pdf"]
main(input_pdf_files)

