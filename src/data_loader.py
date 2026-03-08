import pandas as pd


def load_candidates(path):
    df = pd.read_csv(path)

    print(f"{len(df)} candidatas(os) carregados.")

    return df
  
