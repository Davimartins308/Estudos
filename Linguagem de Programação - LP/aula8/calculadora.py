import operaçoes

print("==Calculadora==")
print("1-somar")
print("2-subtrair")
print("3-multiplicaçao")
print("4-divisao")



opçao=int(input("escola a operaçao"))
a=float(input("digite o primeiro numero:"))
b=float(input("digite o segundo numero:"))

if opçao == 1 :
    print("resultado:",operaçoes.soma(a,b))


elif opçao == 2 :
    print("resultado:",operaçoes.sub(a,b))

elif opçao == 3 :
    print("resultado:",operaçoes.mult(a,b))

elif opçao == 4 :
    print("resultado:",operaçoes.div(a,b)) 




