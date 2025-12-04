programa {
real valor,valor2
cadeia produto,produto2
real preco,preco2
real subtotal,subtotal2
real total
  funcao inicio() {
    escreva("--supermercado preço bom --- \n")
    escreva("vamos registrar sua compra!\n")
    escreva("--- PRODUTO 1 ---\n")
    escreva("digite o nome do produto:")
    leia(produto)
    escreva("quantidade:")
    leia(valor)
    escreva("preço unitario do produto:")
    leia(preco)
    escreva("\n")

  escreva("--- PRODUTO 2 ---\n")
  escreva("digite o nome do produto:")
    leia(produto2)
    escreva("quantidade:")
    leia(valor2)
    escreva("preço unitario do produto:")
    leia(preco2)
subtotal= valor*preco
subtotal2= valor2*preco2
total= subtotal+subtotal2
  escreva("--- RECIBO DA COMPRA ---\n")
  escreva("item:",produto,",")
  escreva("quantidade:  ",valor,"    ,preço unitario: R$",preco,"    ,subtotal:",subtotal,"\n")

  
  escreva("item:  ",produto2)
  escreva(",quantidade:     ",valor2,",   preço unitario: R$",preco2,",   subtotal:",subtotal2,("\n"))



escreva("--------------------------------------\n")
escreva("Valor total da compra:R$",total,"\n")
escreva("--------------------------------------")


    

    
    
  }
}
