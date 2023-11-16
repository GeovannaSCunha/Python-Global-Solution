import os
import json
from funcoes import *

continua = "sim"
msgFinal = []

try:
    print("\n")
    cadastro = input("Você já possui cadastro? (Digite 'sim' ou 'não'): ").lower()

    if cadastro == "não":
        # Área de cadastro e validação
        print("--- CADASTRO ---")
        
        nome = input("Informe seu nome: ")
        erro = validaNome(nome)
        if erro:
            raise ValueError(erro)
        
        email = input("Informe seu e-mail: ")
        erro = validaEmail(email)
        if erro:
            raise ValueError(erro)
        
        senha = input("Crie uma senha de 6 dígitos: ")
        erro = validaSenha(senha)
        if erro:
            raise ValueError(erro)

        infoCliente = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "resultados_exames": {}  # Adiciona um campo para armazenar os resultados dos exames
        }

        if os.path.exists(f'usuarios/{email}.json'):
            raise FileExistsError("Email já cadastrado.")
        else:
            with open(f'usuarios/{email}.json', 'w', encoding='utf-8') as arquivo:
                json.dump(infoCliente, arquivo)

    elif cadastro == "sim":
        email = input("Informe seu e-mail: ")
        erro = validaEmail(email)
        if erro:
            raise ValueError(erro)

        if os.path.exists(f'usuarios/{email}.json'):
            with open(f'usuarios/{email}.json', 'r', encoding='utf-8') as arquivo:
                infoCliente = json.loads(arquivo.read())
                senha = input("Digite sua senha de 6 dígitos: ")
                erro = validaSenha(senha)
                if erro:
                    raise ValueError(erro)

                if email == infoCliente['email'] and senha == infoCliente['senha']:
                    print(f"Acesso permitido! Bem-vindo(a), {infoCliente['nome']}")
                else:
                    raise ValueError("Senha incorreta")
        else:
            raise FileNotFoundError("E-mail incorreto")
    else:
        raise ValueError("Por favor, digite sim ou não.")

    print("\n")
    while continua.lower() == "sim":
        print("\nDigite 1 para cadastrar um novo exame.\nDigite 2 para verificar seus resultados.\nDigite 3 para sair.")
        escolha = input()

        if escolha == "1":
            cadastrar_novo_exame(infoCliente)

        elif escolha == "2":
            verificar_resultados(infoCliente)

        elif escolha == "3":
            continua = "não"

        else:
            raise ValueError("Por favor, digite uma opção válida.")
        
        continua = input("\nVocê deseja fazer uma nova ação? (Digite 'sim' ou 'não') ")
        if continua.lower() != "sim" and continua.lower() != "não":
            raise ValueError("Por favor, digite sim ou não.")

    # Exibe as mensagens finais: informações do cliente, resumo da operação e agradecimento
    with open(f'usuarios/{email}.json', 'w', encoding='utf-8') as arquivo:
        json.dump(infoCliente, arquivo)

    print("*" * 70)
    print("INFORMAÇÕES DO CLIENTE:")
    print(f"Nome: {infoCliente['nome']}")
    print(f"E-mail: {infoCliente['email']}")
    
    # Exibe os resultados dos exames
    resultados_exames = infoCliente.get("resultados_exames")
    if resultados_exames:
        print("\n--- Resultados dos Exames ---")
        for chave, valor in resultados_exames.items():
            print(f"{chave}: {valor}")
    
    print("*" * 70)
    print("\nObrigada por utilizar nossos serviços.")

except ValueError as ve:
    print(f"\nErro: {ve}")
except FileNotFoundError:
    print("\nErro: Arquivo não encontrado.")
except FileExistsError as fee:
    print(f"\nErro: {fee}")
except Exception as e:
    print(f"\nErro inesperado: {e}")

finally:
    print("Fim da sessão")
