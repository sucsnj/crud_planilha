import pandas as pd

def get_planilha(caminho):
    df = pd.read_excel(caminho, engine='openpyxl') if caminho.endswith(('.xls', '.xlsm')) else pd.read_csv(caminho)
    print(df)
