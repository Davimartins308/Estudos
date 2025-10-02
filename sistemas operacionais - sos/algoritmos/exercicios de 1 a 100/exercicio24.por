programa {
  funcao inicio() {
    real km,pme,pma

    escreva("Quantos km voce deseja percorrer? ")
    leia(km)

pme = km * 0.50
pma = km * 0.45
se (km <= 200) {

  escreva("o preço da passagem será de : ",pme)


}
senao {

escreva("O preço da passagem será de : ",pma)


}
    
  }
}
