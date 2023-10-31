import sys
import PyPDF2
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.psparser import PSLiteral

def check_pdf_x_4(filename):
    #try:
        with open(filename, "rb") as f:
            # PyPDF2を使ってPDFファイルを開く
            pdf_reader = PyPDF2.PdfReader(f)
            # PDFファイルのXMPメタデータを取得する
            xmp_metadata = pdf_reader.getXmpMetadata()
            if not xmp_metadata:
                print("The PDF does not have a metadata.")
            else:
                # PDFファイルのサブタイプを判定する
                for desc in xmp_metadata.descendants:
                    if isinstance(desc, PSLiteral) and desc.name == b'subtype' and desc not in ["PDF/A", "PDF/X-1a", "PDF/X-3"]:
                        print("The PDF conforms to PDF/X-4.")
                        return
                print("The PDF does not conform to PDF/X-4.")
    #except:
    #    print("An error occurred while checking the PDF.")
    #return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <PDF file>")
        sys.exit(1)
    check_pdf_x_4(sys.argv[1])