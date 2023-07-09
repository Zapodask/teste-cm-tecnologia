# Teste Técnico - CM Tecnologia

## Descrição

O teste consiste na implementação de duas funções com matrizes, sendo uma para inverter as diagonais de uma matriz quadrada e outra para calcular a quantidade de vezes que uma submatriz aparece dentro de uma matriz.

## Estrutura do projeto

Dentro da pasta functions estão as funções de forma simples sendo 1.py a função de inverter as diagonais e 2.py a função de contar as submatrizes.
Dentro das pastas 1 e 2 estão as mesmas funções porém mais organizadas utilizando classes e testes unitários.

## Requisitos

- Python 3.11

## Instalação

Utilize o ambiente virtual de sua preferência e instale as dependências do projeto com o comando:

```bash
$ pip install -r requirements.txt
```

## Execução

### Para executar os arquivos na pasta functions

Utilize os comandos(Obs: não necessita a instalação de dependências):

```bash
$ python functions/1.py

$ python functions/2.py
```

### Para executar os projetos nas pastas 1 e 2

Altere o arquivo input.txt com a matriz que deseja utilizar e execute os comandos:

```bash
$ cd 1 # ou 2

# Executar testes unitários
$ pytest

# Executar projeto
$ python src/main.py
```
