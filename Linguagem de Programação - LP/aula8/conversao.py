import operaçoes

print("qual conversao voce deseja usar?")
print("1- metros para centimetros")
print("2- centimetros para metros")
print("3- kilometros para metros")

opçao = int(input("escolha uma opçao :  "))

a = float(input("digite o primeiro numero  "))




if opçao == 1 :
    print("resultado:  ",operaçoes.mcm(a))


elif opçao == 2 :
    print("resultado:  ",operaçoes.cmm(a))

elif opçao == 3 :
    print("resultado:  ",operaçoes.kmm(a))

else:
    print("opçao invalida")
