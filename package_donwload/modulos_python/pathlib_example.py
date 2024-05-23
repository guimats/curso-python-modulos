from pathlib import Path
# from shutil import rmtree

# ***puxa a pasta geral em que o arquivo está***
caminho_projeto = Path()
# print(caminho_projeto.absolute())

# ***__file__ -> puxa o caminho do arquivo***
caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# ***parent -> chama a pasta pai (acima) do arquivo/pasta***
# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)

# ***gerando novo caminho (não cria pastas ou arquivos)***
ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivos.txt')

# ***Path.home() pega a home da máquina do cliente***
# print(Path.home() / 'Desktop' )

# *touch cria o arquivo, unlick apaga o arquivo, write_text escreve (limpa)*
# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch(exist_ok=True)
# print(arquivo)
# arquivo.write_text('Olá mundo')
# print(arquivo.read_text())
# arquivo.unlink()

# ***outra forma para criar e escrever no arquivo***
# caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# caminho_arquivo.write_text('')  # para apagar o que tá escrito no arquivo
# with caminho_arquivo.open('a+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
# print(caminho_arquivo.read_text())

# ---------------------------------------------------------
# caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# caminho_arquivo.touch(exist_ok=True)
# caminho_arquivo.write_text('Olá mundo')
# caminho_arquivo.unlink()

# ***mkdir -> cria pasta (diretorio)***
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey 2')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')


# função utilizando o shutil para apagar pasta com outras pastas
# rmtree(caminho_pasta)

# apagando pasta com mais pastas com função própria(mais facil utilizar shutil)
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE:', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
