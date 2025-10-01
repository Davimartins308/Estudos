programa {
  funcao inicio() {
   real nota_prova, nota_trabalho,media_semestral
   logico atingiu
   const real media = 7

   escreva("digite a nota da prova:")
   leia(nota_prova)
   escreva("digite a nota do trabalho : ")
   leia(nota_trabalho)

   media_semestral = (nota_prova + nota_trabalho) / 2

  atingiu = (media_semestral>= media)

  escreva("nota da prova:",nota_prova,"\n")
  escreva("nota do trabalho:",nota_trabalho,"\n")
  escreva("media semestral:",media_semestral,"\n")
  escreva("atingiu a media de aprovaçao (",media,")?", atingiu,"\n")

    
  }
}
