
"""
Script de Execução: Rodar Tudo

Executa a sequência completa de automação:
1. Fetch Reddit Posts
2. Gerar Relatório
3. Visualizar Logs
"""

import subprocess
import sys
import os

def run_script(script_path, args=[]):
    print(f"--- Executando {script_path} ---")
    cmd = [sys.executable, script_path] + args
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    print(result.stdout)
    if result.stderr:
        print("Erros:", result.stderr)
    return result.returncode == 0

def main():
    # Forçar saída utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    scripts_dir = os.path.join(os.path.dirname(__file__))
    
    # 1. Fetch Reddit Posts
    fetch_script = os.path.join(scripts_dir, 'fetch_reddit_posts.py')
    if not run_script(fetch_script, ['n8n', 'automation']):
        print("Falha ao buscar posts. Abortando.")
        return

    # 2. Gerar Relatório
    report_script = os.path.join(scripts_dir, 'gerar_relatorio.py')
    if not run_script(report_script):
        print("Falha ao gerar relatório.")
    
    # 3. Visualizar Logs
    logs_script = os.path.join(scripts_dir, 'visualizar_logs.py')
    if not run_script(logs_script):
        print("Falha ao consolidar logs.")

    print("\n--- Automação Completa Finalizada ---")

if __name__ == "__main__":
    main()
