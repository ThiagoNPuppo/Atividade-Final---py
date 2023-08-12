from datetime import datetime
import json

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome_profissional(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def get_nome_visitante(self):
        return self.__nome


class Visita:
    def __init__(self, visitante, profissional, data_entrada):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = data_entrada


def cadastrar_profissional():
    n = input("Nome: ").lower().title()
    e = input("Especialidade: ").upper()
    s = input("Sala: ")
    prof = Profissional(n, e, s)
    l_profissionais.append(prof)
    print("Cadastrado com sucesso!")


def cadastrar_visitante():
    n = input("Nome visitante: ").lower().title()
    d = input("Documento nº: ")
    vis = Visitante(n, d)
    l_visitantes.append(vis)
    print("Cadastrado com sucesso!")


def localizar_profissional():
    while True:
        try:
            opc = int(input('''Localizar Profissional por:
            [1] Nome
            [2] Profissão
            [3] Menu Principal
            opção => '''))

            if opc == 1:
                nome = input("Digite nome: ").lower().title()
                prof_encontrado = False
                for prof in l_profissionais:
                    if prof.get_nome_profissional() == nome:
                        print(
                            f"{prof.get_nome_profissional()}, {prof.get_especialidade()} está na sala {prof.get_sala()}")
                        prof_encontrado = True
                        break

                if not prof_encontrado:
                    print("Nome não encontrado!")

            elif opc == 2:
                profissao = input("Digite profissão: ").upper()
                prof_encontrado = False
                for prof in l_profissionais:
                    if prof.get_especialidade() == profissao:
                        print(
                            f"{prof.get_nome_profissional()}, {prof.get_especialidade()} está na sala {prof.get_sala()}")
                        prof_encontrado = True
                        break

                if not prof_encontrado:
                    print("Profissional não encontrado!")

            elif opc == 3:
                break
            else:
                print("Opção inválida!")

        except ValueError:
            print("Valor inválido!")


def registrar_visita():
    verifica_nome = input("Nome do Visitante: ").lower().title()
    encontrado = False
    while True:
        for vi in l_visitantes:
            if vi.get_nome_visitante() == verifica_nome:
                print("Cadastro Localizado!")
                encontrado = True
                visitante = verifica_nome
                verifica_profissional = input("Nome do Profissional: ").lower().title()
                encontrado_prof = False
                for pr in l_profissionais:
                    if pr.get_nome_profissional() == verifica_profissional:
                        print("Cadastro encontrado!")
                        profissional = verifica_profissional
                        entrada = datetime.now().strftime("%H:%M")
                        sala = input("sala: ")
                        dict_visitas[visitante] = {"profissional": profissional,
                                                   "entrada": entrada,
                                                   "sala": sala}
                        print("Visita Autorizada!")
                        encontrado_prof = True
                        break
                if encontrado_prof:
                    break
                if not encontrado_prof:
                    print("Profissional não localizado!")
        if encontrado:
            break
        else:
            print("Visitante não encontrado!")
            break


def relatorio_visitas():
    nome_prof = input("Nome do Profissional: ").lower().title()
    for visitante, visita in dict_visitas.items():
        if visita["profissional"] == nome_prof:
            print(f"Visitante: {visitante}")
            print(f"Hora entrada: {visita['entrada']}")
            print(f"Sala: {visita['sala']}")
            print(f"======================================")


def gerar_arquivo_registros():
    nome_arquivo = input("Digite o nome do arquivo: ")
    if nome_arquivo.endswith(".txt"):
        with open(nome_arquivo, "w") as arquivo:
            for visitante, dados in dict_visitas.items():
                profissional = dados["profissional"]
                entrada = dados["entrada"]
                sala = dados["sala"]
                linha = f"Visitante: {visitante}, Profissional: {profissional}, Entrada: {entrada}, Sala: {sala}\n"
                arquivo.write(linha)
        print("Arquivo de registros gerado com sucesso!")
    else:
        print("Nome de arquivo inválido. Certifique-se de fornecer um nome de arquivo com a extensão .txt")


def ler_arquivos():
    arquivo_profissionais = "profissionais.txt"
    arquivo_visitantes = "visitantes.txt"

    with open(arquivo_profissionais, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.strip():
                nome, especialidade, sala = linha.strip().split(':')
                profissional = Profissional(nome, especialidade, sala)
                l_profissionais.append(profissional)
    print("Arquivo de profissionais lido com sucesso!")

    with open(arquivo_visitantes, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.strip():
                nome, documento = linha.strip().split(':')
                visitante = Visitante(nome, documento)
                l_visitantes.append(visitante)
    print("Arquivo de visitantes lido com sucesso!")



l_profissionais = []
l_visitantes = []
dict_visitas = {}

while True:
    try:
        op = int(input('''
            MENU
    ======================
    1- Cadastrar Profissional
    2- Cadastrar Visitante
    3- Localizar Profissional
    4- Registrar Visita
    5- Relatório de Conferência
    6- Gerar arquivo de Registros do dia
    7- Ler arquivos profissionais / visitantes
    Escolha: '''))
        if op == 1:
            cadastrar_profissional()
        if op == 2:
            cadastrar_visitante()
        if op == 3:
            localizar_profissional()
        if op == 4:
            registrar_visita()
        if op == 5:
            relatorio_visitas()
        if op == 6:
            gerar_arquivo_registros()
        if op == 7:
            ler_arquivos()
        elif op > 7 or op < 1:
            print("Opção inválida!")
            print("Escoilha uma opção do menu")

    except:
        print("Valor inválido!")

