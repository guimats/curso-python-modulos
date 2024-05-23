# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


# Denifindo caminhos
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

# Criando pasta nova
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# for page in reader.pages:
#     print(page)
#     print()

page_0 = reader.pages[0]
imagem_0 = page_0.images[0]

# writer = PdfWriter()

# print(page0.extract_text())

# Pegando imagem do pdf e separando em outro local
# with open(PASTA_NOVA / imagem_0.name, 'wb') as fp:
#     fp.write(imagem_0.data)

# Separa cada pag. do pdf em um novo arquivo
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'NOVO_PDF_{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)


# Juntar pdfs em um só
merger = PdfMerger()
files = [
    PASTA_NOVA / 'NOVO_PDF_1.pdf',
    PASTA_NOVA / 'NOVO_PDF_0.pdf',
]

for file in files:
    merger.append(file)

with open(PASTA_NOVA / 'MERGED.pdf', 'wb') as fp:
    merger.write(fp)
