programa {
  funcao inicio() {
    real ano,poder
    escreva("Qual o ano do seu nascimento?")
    leia(ano)

    poder = 2025-ano

    se (poder>= 16){
      escreva("Voce pode votar")
    }
    
    senao {
      escreva("Voce nao pode votar")

    }
  }
}
