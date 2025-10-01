try:
    a =  int(input("Digite um numero inteiro:"))
except ValueError:
    print("Entrada invalida, tente novamente")
else:
    print(f"Número valído : {a}")
finally:
    print("programa executado")
