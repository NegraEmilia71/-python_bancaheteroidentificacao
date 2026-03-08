from data_loader import load_candidates
from data_validator import validate_data
from document_engine import generate_documents
from pdf_generator import convert_to_pdf
from storage_manager import organize_files


def run_pipeline():

    print("Carregando base de dados...")
    data = load_candidates("data/raw/candidatos.csv")

    print("Validando dados...")
    validated_data = validate_data(data)

    print("Gerando documentos...")
    docs = generate_documents(validated_data)

    print("Convertendo para PDF...")
    pdf_files = convert_to_pdf(docs)

    print("Organizando arquivos...")
    organize_files(pdf_files)

    print("Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()
