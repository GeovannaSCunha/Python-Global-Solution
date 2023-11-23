import json
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

        # Verifica se já existem resultados de exames para essa data
        if data in infoCliente["resultados_exames"]:
            raise ValueError(f"Já existe um exame cadastrado para a data {data}.")
        
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

        # Carrega os dados existentes do arquivo
        with open(f'usuarios/{infoCliente["email"]}.json', 'r', encoding='utf-8') as arquivo:
            dados_existentes = json.load(arquivo)

        # Adiciona os novos resultados aos dados existentes
        dados_existentes["resultados_exames"].update(infoCliente["resultados_exames"])

        # Salva os resultados no arquivo
        with open(f'usuarios/{infoCliente["email"]}.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados_existentes, arquivo)

    except ValueError as ve:
        print(f"\nErro: {ve}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")


def verificar_resultados(infoCliente):
    print("\n--- Resultados dos Exames ---")

    # Verifica se existem resultados de exames no dicionário
    resultados_exames = infoCliente.get("resultados_exames")

    if resultados_exames:
        for data, resultados in resultados_exames.items():
            print(f"\nData do Exame: {data}")
            for chave, valor in resultados.items():
                print(f"{chave}: {valor}")

            # Realize a avaliação com base nos resultados dos exames
            mensagem_avaliacao = avalia_resultados(resultados)

            print("\nAvaliação do seu estado de saúde:")
            print(mensagem_avaliacao)

            # Adicione a mensagem de retorno ao médico se necessário
            if "fora da faixa normal" in mensagem_avaliacao.lower():
                print("Recomendação: Retorne ao médico para uma avaliação mais detalhada.")
    else:
        print("Nenhum resultado de exame cadastrado.")

def avalia_resultados(resultados):
    hemacias = resultados.get("hemacias", 0)
    hemoglobina = resultados.get("hemoglobina", 0)
    hematocrito = resultados.get("hematocrito", 0)
    vcm = resultados.get("vcm", 0)
    hcm = resultados.get("hcm", 0)
    chcm = resultados.get("chcm", 0)
    plaquetas = resultados.get("plaquetas", 0)

    mensagem = "Seus resultados estão dentro da faixa normal. Continue cuidando da sua saúde."

    mensagens_fora_do_normal = []

    if hemacias < 4.5 or hemacias > 6.5:
        mensagens_fora_do_normal.append("hemácias")

    if hemoglobina < 13 or hemoglobina > 16:
        mensagens_fora_do_normal.append("hemoglobina")

    if hematocrito < 38 or hematocrito > 54:
        mensagens_fora_do_normal.append("hematócrito")

    if vcm < 80 or vcm > 100:
        mensagens_fora_do_normal.append("VCM")

    if hcm < 27 or hcm > 33:
        mensagens_fora_do_normal.append("HCM")

    if chcm < 32 or chcm > 36:
        mensagens_fora_do_normal.append("CHCM")

    if plaquetas < 150 or plaquetas > 450:
        mensagens_fora_do_normal.append("plaquetas")

    if mensagens_fora_do_normal:
        mensagem = f"Seus resultados indicam condições fora da faixa normal: {', '.join(mensagens_fora_do_normal)}. Recomendamos consultar um médico."

    return mensagem


def validaNome(nome):
    erro=""
    if re.search("\d",nome) or nome == '':
        erro = "Campo obrigatório. Por favor, insira um nome válido, sem números."
    return erro

def validaEmail(email):
    erro=""
    if not re.search("\w+@\w+\.\w+", email) or email == '':
        erro = "Campo obrigatório. Por favor, insira um e-mail válido."
    return erro

def validaSenha(senha):
    erro=""
    if not re.search("\d{6}",senha) or len(senha) > 6 or senha == '':
        erro = "Campo obrigatório. Por favor, insira uma senha válida de 6 dígitos."
    return erro
