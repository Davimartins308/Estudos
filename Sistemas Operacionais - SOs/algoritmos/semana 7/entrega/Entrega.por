programa {
  funcao inicio() {
    cadeia nome,pagamento
    real preco,desconto,final
    logico brinde

    
    
    escreva(" --- Sistema de caixa da loja --- \n")
    escreva("Nome do cliente: ")
    leia(nome)
    escreva("Valor total dos produtos:")
    leia(preco)
    escreva("Forma de Pagamento (Pix ou cartão):")
    leia(pagamento)
    desconto = preco * 0.10
    final = preco - desconto
    brinde = (final>100)
    escreva("--- Recibo para ",nome,"--- \n")
    escreva("Valor dos produtos:",preco,"\n")
    escreva("Desconto (10%):", desconto,"\n")
    escreva("Valor final da compra : ",final,"\n")
    escreva("forma de pagamento: ",pagamento,"\n")
    escreva("Cliente ganhou brinde especial? ",brinde)




  

    
  }
}
