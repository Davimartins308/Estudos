try:
    a = int(input("Numerador:"))
    b = int(input("Denominador:"))

    d = a/b

    


except ZeroDivisionError:
    print("nao e possivel dividir por 0")

except ValueError:
    print("Voce digitou o valor da variavel errado")

else: 
    print(f"O resultado é : {d}")




finally:
    print("seu programa foi executado")



    #try tentar
    # except falhou
    # else bao
    # finally final de codigo