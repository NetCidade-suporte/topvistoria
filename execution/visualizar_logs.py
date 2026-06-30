
"""
Script de Execução: Visualizar Logs Consolidados

Lê arquivos de log do diretório .tmp e os consolida em um único arquivo Markdown.
"""

import os
import glob
import sys
from datetime import datetime

LOG_DIR = '.tmp'
OUTPUT_FILE = 'logs_consolidados.md'

def main():
    # Forçar saída utf-8
    sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(LOG_DIR):
        print(f"Diretório {LOG_DIR} não encontrado.")
        return

    # Buscar arquivos de log
    log_files = glob.glob(os.path.join(LOG_DIR, '*log*.txt'))
    
    md_content = "# Logs de Automação Consolidados\n\n"
    md_content += f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"

    if not log_files:
        md_content += "Nenhum arquivo de log encontrado em .tmp/.\n"
    else:
        for log_file in log_files:
            filename = os.path.basename(log_file)
            md_content += f"## {filename}\n\n"
            md_content += "```text\n"
            
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    md_content += content if content else "(Arquivo vazio)"
            except Exception as e:
                md_content += f"Erro ao ler arquivo: {e}"
            
            md_content += "\n```\n\n"

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Logs consolidados em: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Erro ao salvar arquivo consolidado: {e}")

if __name__ == "__main__":
    main()
