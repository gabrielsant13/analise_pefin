import pandas as pd

# Define o caminho do arquivo .pefin
caminho_arquivo = 'caminho_do_arquivo_a_ser_tratado'

# Lê o arquivo .pefin, pulando a primeira e a última linha, e armazena cada linha em uma lista
with open(caminho_arquivo, "r") as f:
    linhas = f.readlines()[1:-1]

# Cria uma lista de dicionários, onde cada dicionário representa uma linha da planilha com as colunas especificadas
dados = []
for linha in linhas:
    valor_titulo = linha[423:438].strip()
    valor_titulo = valor_titulo[:2] + valor_titulo[2:13] + ',' + valor_titulo[13:]

    # Formata a data de vencimento como "dd/mm/yyyy"
    data_vencimento = linha[8:16]
    data_vencimento_formatada = f"{data_vencimento[6:8]}/{data_vencimento[4:6]}/{data_vencimento[:4]}"

    # Adiciona os dados da linha atual ao dicionário
    dados.append({
        "CLIENTE": linha[105:175].strip(),
        "TIPO": linha[31],
        "CPF/CNPJ": linha[33:48].strip(),
        "TIPO_REMESSA": linha[1],
        "VALOR_TITULO": valor_titulo,
        "TITULO": linha[438:445].strip(),
        "PARCELA": linha[445:447].strip(),
        "DATA_VENCIMENTO": data_vencimento_formatada,
        "ANO_VENC": linha[8:12],
        "MES_VENC": linha[12:14],
        "DIA_VENC": linha[14:16],
	"RETORNO": linha[533:537]
    })

# Cria um DataFrame do pandas a partir da lista de dicionários
df = pd.DataFrame(dados)

# Salva o DataFrame em um arquivo Excel
df.to_excel("caminho_do_lugar_onde_a_planilha_sera_salva", index=False)
