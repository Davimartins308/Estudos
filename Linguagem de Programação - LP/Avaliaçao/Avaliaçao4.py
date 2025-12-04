nome1 = str(input("digite o nome"))
nome2 = str(input("digite o nome"))
nome3 = str(input("digite o nome"))





with open('alunos.txt', 'w') as arquivo: 
    arquivo.write(f"{nome1}.\n")
    arquivo.write(f"{nome2}.\n")
    arquivo.write(f"{nome3}.\n")




