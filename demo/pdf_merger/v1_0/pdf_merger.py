from PyPDF2 import PdfReader, PdfWriter


def merge_pdf(input_pdf_1, input_pdf_2, merged_pdf='merged.pdf'):
    merger = PdfWriter()

    with open(input_pdf_1, 'rb') as file1, open(input_pdf_2, 'rb') as file2:
        reader1 = PdfReader(file1)
        print(f"[INFO] {input_pdf_1} loaded.")

        reader2 = PdfReader(file2)
        print(f"[INFO] {input_pdf_2} loaded.")

        # 添加第一页
        for page in reader1.pages:
            merger.add_page(page)

        # 添加第二页
        for page in reader2.pages:
            merger.add_page(page)

        # 输出合并的 PDF 文件
        with open(merged_pdf, 'wb') as merged_file:
            merger.write(merged_file)

        return merged_pdf


def main(origin_pdf_list):
    print(f"[INFO] Mini PDF Utility")
    print(f"[INFO] Micro Edition Beta 1.0\n")

    print(f"[INFO] Start merging...")
    merged_doc = merge_pdf(origin_pdf_list[0], origin_pdf_list[1])
    print(f"[INFO] Merged as {merged_doc}.")


# start main app
input_pdfs = ["p1.pdf", "p2.pdf"]
main(input_pdfs)

