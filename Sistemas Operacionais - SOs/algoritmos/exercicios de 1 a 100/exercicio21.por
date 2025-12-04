programa {
  funcao inicio() {
    inteiro ano

    escreva("Digite o ano aqui:")
    leia(ano)

    se (ano %4 == 0  e ano %100 != 0 ou ano %400 == 0) {
      escreva("O ano e bissexto")



    }

    senao {
    escreva("o ano nao e bissexto")

    }
    
  }
}
