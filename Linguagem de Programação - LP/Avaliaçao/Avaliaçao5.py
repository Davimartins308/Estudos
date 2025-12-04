try :
    a = float(input("Numerador "))
    b = float(input("Denominador "))

    c = a/b

except ZeroDivisionError:
    print("nao e possivel dividir por 0")



else: 
    print(f"O resultado é : {c}")