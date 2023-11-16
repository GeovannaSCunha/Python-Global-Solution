import re

def validar_data(data):
    # Expressão regular para validar data no formato DD/MM/AAAA
    pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    return bool(pattern.match(data))

def cadastrar_novo_exame(infoCliente):
    print("\n--- Cadastro de Novo Exame ---")
    
    try:
        data = input("Digite a data deste novo exame (formato: DD/MM/AAAA): ")
        
        if not validar_data(data):
            raise ValueError("Data inválida. Por favor, insira no formato correto.")

        # Adiciona os resultados ao dicionário do cliente
        infoCliente["resultados_exames"][data] = {
            "hemacias": float(input("Digite a quantidade de hemácias (milhões/mm³): ")),
            "hemoglobina": float(input("Digite o valor da hemoglobina (g/dL): ")),
            "hematocrito": float(input("Digite o valor do hematócrito (%): ")),
            "vcm": float(input("Digite o valor do Volume Corpuscular Médio (VCM): ")),
            "hcm": float(input("Digite o valor da Hemoglobina Corpuscular Média (HCM): ")),
            "chcm": float(input("Digite o valor da Concentração de Hemoglobina Corpuscular Média (CHCM): ")),
            "plaquetas": float(input("Digite o valor de plaquetas (mil/mm³): "))
            # Adicione outros campos, se necessário
        }
        print("Exame cadastrado com sucesso!")

    except ValueError as ve:
        print(f"\nErro: {ve}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def verificar_resultados(infoCliente):
    print("\n--- Resultados dos Exames ---")

    # Verifica se existem resultados de exames no dicionário
    resultados_exames = infoCliente.get("resultados_exames")

    if resultados_exames:
        for data, valores in resultados_exames.items():
            print(f"\nData do Exame: {data}")
            for chave, valor in valores.items():
                print(f"{chave}: {valor}")

            # Realize a avaliação com base nos resultados dos exames
            mensagem_avaliacao = avalia_resultados(
                valores["hemacias"],
                valores["hematocrito"]
            )

            print("\nAvaliação do seu estado de saúde:")
            print(mensagem_avaliacao)
    else:
        print("Nenhum resultado de exame cadastrado.")

# função que verifica o resultado do exame
def avalia_resultados(hemacias, hematocrito):
    if hemacias < 4.5 or hemacias > 6.5 or hematocrito < 38 or hematocrito > 54:
        return "Seus resultados indicam uma condição fora da faixa normal. Recomendamos consultar um médico."
    else:
        return "Seus resultados estão dentro da faixa normal. Continue cuidando da sua saúde!"


# função que verifica se o nome tem números ou está vazio
def validaNome(nome):
    erro=""
    if re.search("\d",nome) or nome == '':
        erro = "Campo obrigatório.Por favor, insira um nome válido, sem números."
    return erro

# verifica se o email está na estrutura padrão aceita
def validaEmail(email):
    erro=""
    if not re.search("\w+@\w+\.\w+", email) or email == '':
        erro = "Campo obrigatório. Por favor, insira um e-mail válido."
    return erro

# verifica se a senha possui 6 números
def validaSenha(senha):
    erro=""
    if not re.search("\d{6}",senha) or len(senha) > 6 or senha == '':
        erro = "Campo obrigatório. Por favor, insira uma senha válida de 6 dígitos."
    return erro

