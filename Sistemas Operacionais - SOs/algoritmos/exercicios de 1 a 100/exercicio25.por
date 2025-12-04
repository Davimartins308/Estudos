programa {
  funcao inicio() {
    real a,b,c

  escreva("Digite o tamanho do primeiro segmento de reta do triangulo em cm : ")
  leia(a)

  escreva("Digite o tamanho do segundo segmento de reta do triangulo em cm : ")
  leia(b)

  escreva("Digite o tamanho do terceiro segmento de reta do triangulo em cm : ")
  leia(c)

  se ( (a < b+c) e (b < a+c) e (c < a+b)) {

    escreva("É possivel formar um triangulo")



  }

 senao {

 escreva("Nao e possivel formar um triangulo")

 }

    
  }
}
