programa {
  funcao inicio() {
    const cadeia energy = "energybeam "
    const inteiro mana = 20
    inteiro vezes ,custo

    escreva(" ---  Calculadora de mana de magia Energy beam ---\n")
    escreva("quantas vezes voce pretende lançar a magia?")
    leia(vezes)
    custo = vezes*mana

    escreva("para lançar a magia ",energy,vezes," vezes, voce gastará: ",custo," de mana")

    
  }
}
