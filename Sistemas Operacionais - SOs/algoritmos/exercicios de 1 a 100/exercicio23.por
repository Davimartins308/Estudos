programa {
  funcao inicio() {
    real preco,desh,desm
    cadeia nome
    caracter sexo

    escreva("Digite seu nome aqui: ")
    leia(nome)

    escreva("Digite h se for homem e m se for mulher :")
    leia(sexo)

    escreva("qual foi o valor de compras?:")
    leia(preco)

desh =    preco - (preco * 0.05)
desm =    preco - (preco * 0.13)

se (sexo == "h" ) {

  escreva("o preço do produto descontado para homens foi: ",desh)
}

senao {

escreva("o preço do produto descontado para mulheres foi :",desm)

}
    
  }
}
