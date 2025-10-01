programa {
  funcao inicio() {
    real a,b
    logico igual,barato
    escreva("Preço do Produto A:")
    leia(a)
    escreva("Preço do Produto B:")
    leia(b)

    barato = (a < b)
    igual = (a == b)

    escreva("Produto A é mais barato que B? ", barato,"\n")
    escreva("os preços sao iguais? ",igual)
    
  }
}
