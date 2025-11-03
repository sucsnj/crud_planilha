import pandas as pd

df = pd.DataFrame(columns=['col1', 'col2'])
df.to_excel('planilha.xlsx', index=False)
