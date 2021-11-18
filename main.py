# Sistemas Inteligentes Aplicados - 16/11/2021 - Professora tacyana C. Batista
# Aluna: Marta S. de Santana Lima - 6º Período de Sistemas de Informação


from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
from analise_palavras import AnalisePalavras
import os

# Função para ouvir e reconhecer a fala

analise = AnalisePalavras()

def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

        print('Pensando...')

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        array = microfone.recognize_google(audio, language='pt-BR').split()

        frase = ''
        for i in array:
            retorno = analise.avalia(str(i))
            if (retorno['score'] == 1):
                i = ''
            if(i != ''):
                frase = frase + ' ' + i


        if "navegador" in frase:
            os.system("start chrome.exe")

        if "Excel" in frase:
            os.system("start Excel.exe")

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

        #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase


ouvir_microfone()


# Funcao responsavel por falar

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    # Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    # Da play ao audio
    playsound('hello.mp3')


frase = ouvir_microfone()
if(frase):
    cria_audio(frase)
