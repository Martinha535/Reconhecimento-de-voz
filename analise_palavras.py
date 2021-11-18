class AnalisePalavras: 
    """ 
        Classe para analisar se o nome do objeto é masculino ou feminino, retorna 0 em masculino e 1 em feminino
    """ 
    def __init__(self):
        self.__dicionario = {}
        self.__criaDicionario()
    """ Ler linha por linha do yoloNames e adiciona no dicionario o valor e o gênero da palavra """
    def __criaDicionario(self):
        #Busca o yoloNames
        arquivo = open('.\dados.txt', 'r')
        linhas = arquivo.readlines()
        #Salva as palavras no dicionario
        for linha in linhas:
            dado = linha.split(',')
            self.__dicionario[dado[0]] = int(dado[1])
        #Encerra o arquivo
        arquivo.close()
    """ 
        Avalia se o que foi detectado é uma palavra masculina ou feminina
        @param texto - String a ser avaliada
        @return {score: number}
    """
    def avalia(self, texto): 
        retorno = {'score': 0}
        if (texto in self.__dicionario):
            retorno['score'] += self.__dicionario[texto] 
        return retorno