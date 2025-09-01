import subprocess

# Lista de scripts na ordem desejada
scripts = ["etl.py", "analytics.py"]

for script in scripts:
    print(f"Executando: {script}")
    try:
        # Executa o script e aguarda sua conclusão
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {script}: {e}")
        break  # Para a execução se algum script falhar