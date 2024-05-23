# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv_ex.csv'

# leitura normal
# with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

# leitura em formato de dicionario
with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
