
# Diretriz: Gerar Relatório Reddit

## Objetivo
Transformar os dados brutos coletados do Reddit (`.tmp/reddit_top_posts.json`) em um relatório Markdown legível e formatado em Português.

## Entradas
- `.tmp/reddit_top_posts.json`: Arquivo JSON contendo os posts.

## Ferramentas
- `execution/gerar_relatorio.py`

## Instruções
1.  Execute `execution/gerar_relatorio.py`.
2.  O script irá:
    - Ler o arquivo JSON.
    - Iterar sobre cada subreddit.
    - Criar uma tabela Markdown para cada subreddit com as colunas: Título, Engajamento (Score + Comentários), Data.
    - Adicionar links para os posts originais.
    - Salvar o arquivo final como `relatorio_reddit.md` na raiz do projeto.
3.  Verifique se o arquivo `relatorio_reddit.md` foi criado e se o conteúdo está em Português.

## Tratamento de Erros
- Se o arquivo JSON não existir, o script deve alertar o usuário para rodar o scraper primeiro.
