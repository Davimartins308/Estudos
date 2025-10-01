programa {
  funcao inicio() {
    inteiro n1,n2, n3
    logico multiplo

    escreva("digite o primeiro numero:")
    leia(n1)
    escreva("digite o segundo numero:")
    leia(n2)
    
    n3 = (n1 % n2)

    multiplo = (n3 == 0)
    escreva(multiplo)
    
  }
}
