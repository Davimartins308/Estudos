import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")

# Qual é o produto mais caro e o Produto mais barato?

barato = dados_df.loc[dados_df["Preço"].idxmin()]
print(barato)
