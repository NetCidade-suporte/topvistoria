
# Diretriz: Visualizar Logs de Automação

## Objetivo
Consolidar e exibir os logs de execução de todas as automações em um único arquivo Markdown para fácil leitura.

## Entradas
- Arquivos `.txt` no diretório `.tmp/` (ex: `fetch_log.txt`).

## Ferramentas
- `execution/visualizar_logs.py`

## Instruções
1.  Execute `execution/visualizar_logs.py`.
2.  O script irá:
    - Procurar por todos os arquivos `.txt` em `.tmp/` que contenham "log" no nome.
    - Ler o conteúdo de cada arquivo.
    - Criar um arquivo `logs_consolidados.md` na raiz.
    - Adicionar o conteúdo de cada log em uma seção separada.
3.  Verifique o arquivo `logs_consolidados.md` gerado.

## Tratamento de Erros
- Se nenhum log for encontrado, o script deve informar isso no arquivo de saída.
