import pandas

# utilização da pandas para leitura do arquivo csv, recebe o nome de 'data'
data = pandas.read_csv("br-capes-bolsistas-uab.csv", delimiter = ';', encoding = "ISO-8859-1")
# lista do alfabeto para utilização na codificação dos nomes
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# função simples que retorna o primeiro bolsista do ano desejado
def consulta_bolsa_zero_ano(data):
    ano = input("Informe o ano desejado: ")
    for lines in range(len(data)):
        if ano == str(data["AN_REFERENCIA"][lines]):
            return(print(data["NM_BOLSISTA"][lines]))
    return(print("ERRO - ano não encontrado!"))

# função que calcula a média do ano desejado
def consulta_media_anual(data):
    acumulador = 0 #variavel apenas para caso de erro
    divisor = 0
    soma = 0
    ano = input("Informe o ano desejado: ")
    for lines in range(len(data)):
        if ano == str(data["AN_REFERENCIA"][lines]):
            divisor += 1
            soma += int(data["VL_BOLSISTA_PAGAMENTO"][lines])
        elif ano != str(data["AN_REFERENCIA"][lines]):
            acumulador += 1
    if acumulador == len(data):
        return (print("ERRO - ano não encontrado!"))
    return(print(soma/divisor))

# função que encontra as 3 maiores e 3 menores bolsas
# acredito que o cósigo dessa função tenha ficado extremamente repetitivo, porém não encontrei maneira de contornar
def ranking_valores_de_bolsa(data):
    maior1 = 0
    maior2 = 0 #variaveis que vão guardando os valores de bolsa até encontrar o maior ou menor
    maior3 = 0
    menor1 = 10000
    menor2 = 10000
    menor3 = 10000
    for lines in range(len(data)):
        if int(data["VL_BOLSISTA_PAGAMENTO"][lines]) > maior1:
            maior1 = int(data["VL_BOLSISTA_PAGAMENTO"][lines])
            maior1_nome = (data["NM_BOLSISTA"][lines])
        elif int(data["VL_BOLSISTA_PAGAMENTO"][lines]) > maior2:
            maior2 = int(data["VL_BOLSISTA_PAGAMENTO"][lines])
            maior2_nome = (data["NM_BOLSISTA"][lines])
        elif int(data["VL_BOLSISTA_PAGAMENTO"][lines]) > maior3:
            maior3 = int(data["VL_BOLSISTA_PAGAMENTO"][lines])
            maior3_nome = (data["NM_BOLSISTA"][lines])
        elif int(data["VL_BOLSISTA_PAGAMENTO"][lines]) < menor1:
            menor1 = int(data["VL_BOLSISTA_PAGAMENTO"][lines])
            menor1_nome = (data["NM_BOLSISTA"][lines])
        elif int(data["VL_BOLSISTA_PAGAMENTO"][lines]) < menor2:
            menor2 = int(data["VL_BOLSISTA_PAGAMENTO"][lines])
            menor2_nome = (data["NM_BOLSISTA"][lines])
        elif int(data["VL_BOLSISTA_PAGAMENTO"][lines]) < menor3:
            menor3 = int(data["VL_BOLSISTA_PAGAMENTO"][lines])
            menor3_nome = (data["NM_BOLSISTA"][lines])
    return(print(f"Tres bolsas mais altas = {maior1_nome, maior2_nome, maior3_nome},"
                 f"\nTres bolsas mais baixas = {menor1_nome, menor2_nome, menor3_nome}"))

# função que encontra os nomes através de um input parcial ou completo
def encontra_nomes(data):
    acumulador2 = 0
    nome = (input("Insira o nome do bolsista: ")).upper()
    lista = []
    for lines in range(len(data)):
        acumulador = 0
        if nome == (data["NM_BOLSISTA"][lines]): # se o input for completo
            bolsista = (data["NM_BOLSISTA"][lines])
            lista.append(bolsista)
            lista.append(data["AN_REFERENCIA"][lines])
            lista.append(data["NM_ENTIDADE_ENSINO"][lines])
            lista.append(data["VL_BOLSISTA_PAGAMENTO"][lines])
            return(lista)
        elif nome != (data["NM_BOLSISTA"][lines]): # se o input for parcial ou errado
            bolsista = (data["NM_BOLSISTA"][lines])
            if len(bolsista) > len(nome): # compara o tamanho do input com o do nome, para eliminar os menores
                for letter in range(len(nome)):
                    if nome[letter] == bolsista[letter]: # compara letra por letra do input com o nome do bolsista
                        acumulador += 1 # e junta nessa variavel
                if acumulador == len(nome): # se o valor juntado for igual ao tamanho do input, então todas as letras são iguais
                    lista.append(bolsista)
                    lista.append(data["AN_REFERENCIA"][lines])
                    lista.append(data["NM_ENTIDADE_ENSINO"][lines])
                    lista.append(data["VL_BOLSISTA_PAGAMENTO"][lines])
                    return(lista)
                else:
                    acumulador2 += 1 # acumula caso o input não seja igual a nenhum nome
        if acumulador2 == len(data):
            return(1)

# função que codifica o nome encontrado na função anterior, através de 3 etapas
def codifica_nomes(data, alfabeto):
    nome_codificado = []
    lista = encontra_nomes(data)
    if lista == 1:
        return("ERRO - nome nao encontrado!")
    nome_separado = lista[0].split()
    for i in range(len(nome_separado)):
        aux = 0
        nome = list(nome_separado[i])
        primeira_letra = nome[0] # etapa 1
        nome[0] = nome[-1]
        nome[-1] = primeira_letra
        nome = nome[::-1] # etapa 2
        for letter in nome: # etapa 3, cifra de césar e utilização da lista alfabeto
            posicao = alfabeto.index(letter)
            nova_posicao = posicao + 1
            nome[aux] = alfabeto[nova_posicao]
            aux += 1
        nome_codificado.append(''.join(nome))
    lista[0] = ' '.join(nome_codificado)
    return(print(lista))

# função main do programa
def programa(data, alfabeto):
    end = False
    while end == False:
        print("\nDigite 1 para consultar bolsa zero/Ano;"
        "\n\t   2 para consultar um bolsista especifico;"
        "\n\t   3 para consultar media anual;"
        "\n\t   4 para consultar o ranking de valores de bolsa;"
        "\n\t   5 para terminar o programa.")
        option = input()

        if option == '1':
            consulta_bolsa_zero_ano(data)
        elif option == '2':
            codifica_nomes(data, alfabeto)
        elif option == '3':
            consulta_media_anual(data)
        elif option == '4':
            ranking_valores_de_bolsa(data)
        elif option == '5':
            end = True
        else:
            print("ERRO - opcao nao encontrada!")

programa(data,alfabeto)
