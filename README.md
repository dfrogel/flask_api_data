<h1> Projeto: API Flask e Processamento de Arquivos CSV </h1>

<h2>Descrição</h2>

Este projeto contém duas funcionalidades principais:

1. Script de processamento de dados que descompacta arquivos ZIP, processa dados CSV e gera um arquivo SQL com consultas.
2. API Flask para consultar dados de tipos a partir de um CSV.

<h2> Requisitos </h2>
Antes de executar os scripts, instale os seguintes pacotes: 

``` 
pip install --upgrade flask pandas
``` 
<h2> Instruções de uso </h2>
<h3> Script de Processamento (arquivo: script_python.py) </h3>

<b>Descrição</b>

Este script descompacta um arquivo ZIP, processa os dados dos arquivos descompactados, 
filtra registros críticos, gera um arquivo SQL com comandos de inserção e query de agrupamento.

<b> Estrutura do Projeto </b>

- Local do ZIP: `script_python\dados (2).zip`
- O ZIP deve conter:
    - `origem-dados.csv`
    - `tipos.csv`

  
<b>Como Executar</b>

Execute o seguinte comando no terminal:
```
python .\script_python\script.py
```
<b>Funcionalidade</b>

- Descompactação: Extrai os arquivos do ZIP.
- Processamento:
  - Adiciona a coluna `nome_tipo` ao `origem-dados.csv`.
  - Filtra registros com status igual a `CRITICO`.
  - Ordena os registros por `created_at` de forma decrescente.
- SQL:
  - Gera o arquivo `insert-dados.sql` no mesmo diretório do script.
  - Adiciona uma query de agrupamento no final do arquivo SQL.

<h3> API Flask (arquivo: api_flask.py) </h3>

<b> Descrição </b>

Este script cria uma API simples que permite consultar tipos com base no `ID`, utilizando dados armazenados em `tipos.csv`.

<b> Configuração </b>

Verifique se o arquivo `tipos.csv` está localizado no seguinte caminho: 
```
api_flask\tipos.csv
```

<b> Como Executar </b>

1. Execute o seguinte comando no terminal:
```
python .\api_flask\api.py
```

2. Acesse a API no navegador ou via ferramentas como Postman:
  - Rota inicial: http://localhost:5000/
    - Exibe uma mensagem explicando como utilizar a API.
  - Consultar tipo: http://localhost:5000/tipos/1
    - Retorna o tipo associado ao ID informado.

<h2> Estrutura de Arquivos e Diretórios </h2>

```
flask_api_data/
│
├── api_flask/
│   ├── api.py
│   └── tipos.csv
│
├── script_python/
│   ├── script.py
│   └── dados (2).zip
│   └── insert-dados.sql (gerado após a execução do script)
│

``` 


