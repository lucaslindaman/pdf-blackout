from PyPDF2 import PdfFileWriter, PdfFileReader

def create_watermark(input_pdf, output_pdf, watermark_pdf):
    watermark_obj = PdfFileReader(watermark_pdf)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    create_watermark(input_pdf = 'INSERT INPUT FILE LOCATION HERE', output_pdf = 'INSERT OUTPUT LOCATION HERE', watermark_pdf = 'INSERT WATERMARK FILE LOCATION HERE')
