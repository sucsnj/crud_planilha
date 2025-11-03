import pandas as pd

def get_planilha(caminho):
    df = pd.read_excel(caminho, engine='openpyxl') if caminho.endswith(('.xls', '.xlsm')) else pd.read_csv(caminho)
    print(df)

def delete_linha(caminho, indice):
    df = pd.read_excel(caminho, engine='openpyxl') if caminho.endswith(('.xls', '.xlsm')) else pd.read_csv(caminho)
    df = df.drop(indice)
    if caminho.endswith('.csv'):
        df.to_csv(caminho, index=False)
    else:
        df.to_excel(caminho, index=False)

def post_linha(caminho, dados):
    df = pd.read_excel(caminho, engine='openpyxl') if caminho.endswith(('.xls', '.xlsm')) else pd.read_csv(caminho)
    df.loc[len(df)] = dados
    if caminho.endswith('.csv'):
        df.to_csv(caminho, index=False)
    else:
        df.to_excel(caminho, index=False)

def put_linha(caminho, indice, novos_dados):
    df = pd.read_excel(caminho, engine='openpyxl') if caminho.endswith(('.xls', '.xlsm')) else pd.read_csv(caminho)
    df.loc[indice] = novos_dados
    if caminho.endswith('.csv'):
        df.to_csv(caminho, index=False)
    else:
        df.to_excel(caminho, index=False)
