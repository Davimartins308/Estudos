programa {
  funcao inicio() {
    const real porcentagem = 0.15
    cadeia item
    real preco,desconto,final
    
     
    escreva("Nome do produto:")
    leia(item)
    escreva("preço do produto:")
    leia(preco)
    escreva("--- preço promocional ---\n")
    escreva("preço original: ",preco,"\n")

   desconto = preco *porcentagem
   final= preco - desconto
  
    escreva("Desconto:",desconto,"\n")
    escreva("preço final:",final)
    
  }
}
