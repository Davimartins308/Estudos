programa {
  funcao inicio() {
const cadeia monstro = "cabana de glololobins"
const real xp_p_m = 100
const real gp_m_m = 25
const real p_lootmedio = 3.2
cadeia nome
real quantidade,tempo,custo
escreva("--- relatorio detalhado de caçada dos globlins ---\n")
escreva("monstro caçado: ",monstro,"\n")

escreva("nome do seu personagem: ")
leia(nome)
escreva("quantos ",monstro," voce derrotou?")
leia(quantidade)
escreva("tempo total gasto na caçada:")
leia(tempo)
escreva("custo total dos suprimentos em GPs:")
leia(custo)

escreva(" --- relatorio da caçada de Paladino Aventureiro --- \n")
escreva("monstro focado:",monstro,"\n")
escreva("quantidade derrotada:",quantidade,"\n")
escreva("tempo da caçada:",tempo," horas \n")
escreva("-------------------------------------------\n")
escreva("Xp total ganhada: ",quantidade*xp_p_m,"\n")
escreva("GP total estimulado coletado: ",quantidade*gp_m_m,"\n")
escreva("peso estimado do Loot: ",quantidade*p_lootmedio,"\n")
escreva("-------------------------------------------\n")
escreva("custo dos suprimentos:",custo," GPs \n")
escreva("Lucro/Prejuizo estimado : ", (quantidade * gp_m_m) - custo,"\n" )
escreva("----------------------------------------------\n")
escreva("Media de XP por Hora:",(quantidade*xp_p_m)/tempo,"XP/h \n")
escreva("media de Gp por hora:",(quantidade*gp_m_m)/tempo,"GP/h\n")
escreva("--------------------------------------------------------\n")
escreva("Bom jogo, ",nome,"!")








  }
}
