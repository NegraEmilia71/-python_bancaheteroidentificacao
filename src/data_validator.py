def validate_data(df):

    required_columns = [
        "nome",
        "cpf"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")

    df = df.dropna()

    return df
