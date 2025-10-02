programa {
  funcao inicio() {
    real idade,alistamento,poder,npoder

    escreva("Digite o ano de nascimento  aqui: ")
    leia(idade)

  alistamento = 2025  - idade

  poder = alistamento - 18

  npoder = 18-alistamento
    se (alistamento>=18){

      escreva("Voce pode se alistar e se passou ",poder," anos\n")




    }
  senao {

escreva("voce nao pode se alistar e falta ", npoder," anos\n")


  }


    
    
  }
}
