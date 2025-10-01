nome= str(input("digite o nome aqui "))
idade = int(input("digite a sua idade aqui "))


with open('dados.txt', 'w') as arquivo: 
    arquivo.write(f"{nome}.\n")
    arquivo.write(f"{idade}.\n")



 