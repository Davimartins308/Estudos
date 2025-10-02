programa {
  funcao inicio() {
    cadeia nome
    real nota1,nota2,media

    escreva("Digite o nome do aluno ")
    leia(nome)
    escreva("digite a primeira nota do aluno ",nome," ")
    leia(nota1)
    escreva("digite a segunda nota do aluno ",nome," ")
    leia(nota2)

  media = (nota1+nota2)/2

  se (media >= 7) {
  escreva("O/A aluno/a ",nome,"teve um bom aproveitamento")
  }
    
    senao {
  escreva("O/A aluno/a ",nome," teve um mal aproveitamento")


    }
    
  }
}
