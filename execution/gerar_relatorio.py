
"""
Script de Execução: Gerar Relatório Reddit

Lê o arquivo JSON de posts e gera um relatório Markdown formatado em Português.
"""

import json
import os
import sys
from datetime import datetime

INPUT_FILE = os.path.join('.tmp', 'reddit_top_posts.json')
OUTPUT_FILE = 'relatorio_reddit.md'

def format_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M')

def main():
    # Forçar saída utf-8
    sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(INPUT_FILE):
        print(f"Erro: Arquivo {INPUT_FILE} não encontrado. Execute o scraper primeiro.")
        return

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Erro ao ler arquivo JSON: {e}")
        return

    md_content = "# Relatório de Destaques do Reddit\n\n"
    md_content += f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"

    for subreddit, posts in data.items():
        md_content += f"## r/{subreddit}\n\n"
        
        if not posts:
            md_content += "Nenhum post relevante encontrado na última semana.\n\n"
            continue

        md_content += "| Título | Engajamento | Data |\n"
        md_content += "| :--- | :---: | :---: |\n"

        for post in posts:
            title = post.get('title', 'Sem título').replace('|', '-') # Escapar pipes
            url = post.get('permalink', '#')
            engagement = post.get('engagement', 0)
            date = format_date(post.get('created_utc', 0))
            
            md_content += f"| [{title}]({url}) | {engagement} | {date} |\n"
        
        md_content += "\n"

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Relatório gerado com sucesso: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Erro ao salvar relatório: {e}")

if __name__ == "__main__":
    main()
