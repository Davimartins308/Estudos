programa {
  funcao inicio() {
    cadeia item
    real preco,total
    inteiro quantidade

  escreva("nome do item:")
  leia(item)
  escreva("preço unitario(oz):")
  leia(preco)
  escreva("quantidade em posse:")
  leia(quantidade)

  escreva("--- Detalhes do item ---\n")
  escreva("item:",item,"\n")
  escreva("preço unitario:",preco,"\n")
  escreva("quantidade em posse:",quantidade," oz\n")
  total= preco*quantidade
  escreva("peso total:",total," oz\n")
    
  }
}
