import subprocess
import sys

# Lista de bibliotecas a serem instaladas
pacotes = ['pandas', 'numpy', 'seaborn', 'matplotlib']

def instalar(pacote):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', pacote])

if __name__ == '__main__':
    for pacote in pacotes:
        try:
            print(f"Instalando {pacote}...")
            instalar(pacote)
            print(f"{pacote} instalado com sucesso!\n")
        except Exception as e:
            print(f"Erro ao instalar {pacote}: {e}\n")
