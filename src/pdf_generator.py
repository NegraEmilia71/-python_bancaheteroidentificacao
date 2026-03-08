import os

def convert_to_pdf(doc_files):

    pdf_files = []

    for file in doc_files:

        pdf_file = file.replace(".docx", ".pdf")

        os.rename(file, pdf_file)

        pdf_files.append(pdf_file)

    return pdf_files
  
