# Criar um pequeno sistema automatizaçao que mostre uma mensagem de alerta e confirmaçao para o usuario,peça informaçoes basicas (nome e email)confirme se o suario quer continuar,caso sim tire um print da tela
import pyautogui
import time


pyautogui.alert(text='Bem vindo ao sistema automatizado!',
                title= 'inicio da automaçao',
                button='OK')

nome=pyautogui.prompt(text='Digite seu nome:',title='Informaçao obrigatoria')
email=pyautogui.prompt(text='Digite seu email:',title='informaçao obrigatoria')

resposta= pyautogui.confirm(
    text= f'Confirme seus dados:\n\n nome: {nome}\n\n Email : {email} \n\n Deseja continuar com a captura de tela?',
    title='confirmação de dados', 
    buttons= ['Sim','Nao','Cancelar']
)

if resposta=="Sim":
    pyautogui.alert('prepare-se! a captura de tela sera feita em 3 segundos',title='captura de tela')
    time.sleep(3)
    pyautogui.screenshot('captura_usuario.png')
    pyautogui.alert('captura realizada com sucesso',title='sucesso')
elif resposta=='Nao':
    pyautogui.alert('Processo cancelado pelo usuario',title='cancelado')
else : pyautogui.alert('automaçao foi interrompida',title='encerrado')

print(f"nome: {nome}")
print(f"email: {email}")
print(f"Resposta do usuario: {resposta}")




