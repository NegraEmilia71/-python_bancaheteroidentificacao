from docx import Document
import os


def generate_documents(df):

    output_docs = []

    for index, row in df.iterrows():

        doc = Document("templates/resultado_template.docx")

        for paragraph in doc.paragraphs:
            if "{{nome}}" in paragraph.text:
                paragraph.text = paragraph.text.replace("{{nome}}", row["nome"])

            if "{{cpf}}" in paragraph.text:
                paragraph.text = paragraph.text.replace("{{cpf}}", row["cpf"])

        file_name = f"output/docs/doc_{index}.docx"
        doc.save(file_name)

        output_docs.append(file_name)

    return output_docs
  
