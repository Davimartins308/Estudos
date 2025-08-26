pessoa = {
"nome" : "Davi",
"idade" : "17",
"peso" : "100 kg"

}

print(pessoa)   # atribui valores (nome = davi)
print(pessoa["nome"]) # mostra apenas o atributo desejado

print(pessoa.keys()) # mostra apenas as chaves

print(pessoa.values()) # mostra os valores

pessoa ["altura"] = 1.97 # acrescenta um titulo e valor ao dicionario

print(pessoa)


pessoa["peso"]=75
print(pessoa)

del pessoa ["idade"]
print(pessoa)
print("nome" in pessoa)
print("idade" in pessoa)

