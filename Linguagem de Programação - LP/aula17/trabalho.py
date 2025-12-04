import pandas as pd
dados_df = pd.read_csv("titanic.csv")



# 1) Quantas linhas e colunas o dataset possui?
#print(dados_df.shape)



#2) Qual é a idade média dos passageiros?
#print(dados_df['Age'].mean())



#3) Trazer apenas as colunas 'Name' e 'Age'
#print(dados_df[['Name','Age']])



#4) Trazer apenas os passageiros do sexo feminino
#print(dados_df[dados_df['Sex'] == 'female'])


#5) Trazer apenas passageiros do sexo masculino com idade > 30
#print(dados_df[(dados_df['Sex'] == 'male') & (dados_df['Age'] > 30)])


#6) Mostrar apenas mulheres sobreviventes
#print(dados_df[(dados_df['Sex'] == 'female') & (dados_df ['Survived'] == 1)])


#7) Mostrar passageiros da 1ª classe com menos de 18 anos
#print(dados_df[(dados_df['Pclass'] == 1) & (dados_df ['Age'] < 18)])


#8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18
dados_df['Faixa'] =  dados_df['Faixa'] = 'N/a'
dados_df.loc[dados_df['Age'] < 18, 'Faixa'] = 'Criança'
dados_df.loc[dados_df['Age'] >= 18, 'Faixa'] = 'Adulto'



#9) Agrupar e mostrar taxa de sobrevivência por sexo
#print(dados_df.groupby('Sex')['Survived'].mean())


# 10) Mostrar a tarifa média por classe
#print(dados_df.groupby('Pclass')['Fare'].mean())


# 11) Qual é a idade da pessoa mais velha do Titanic?
#print(dados_df['Age'].max())


#12) Qual foi a tarifa mais alta paga no Titanic?
#print(dados_df['Fare'].max())


#13) Qual classe tinha mais passageiros?
#print(dados_df['Pclass'].value_counts())



#14) Exportar apenas os sobreviventes para um arquivo CSV
#     Nome sugerido: sobreviventes.csv
#sobreviventes = dados_df[dados_df['Survived'] == 1]
#sobreviventes.to_csv("sobreviventes.csv",index=False)













