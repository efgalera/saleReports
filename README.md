# Instalação
## Crie um ambiente virtual e ative-o
* $ `python3 -m venv env`
* $ `source env/bin/activate`

## Instale a aplicação
* $ `pip install -e .`

## Teste
* $ `pytest`


# Uso
* vendas-cli \<nome do csv\> --format \<formato suportado\> [--start <data no formato %Y/%m/%d>, --end <data no formato %Y/%m/%d>]

# TODOs:
* Adicionar loggin na aplicação
* Implementar filtro por datas
* Dataprocessor está com um claro problema de arquitetura - está lidando com nome de colunas e index diretamente.
    * Isso precisa ser removido: passar o nome da coluna para quem chama DataProcessor, assim o método será capaz de funcionar com qualquer coluna. Passar o indice da coluna hard coded para dentro do data handler.


# Importante
* $ `vendas-cli --help` mostra como vendas-cli deve ser chamado na linha de comando.
* esta aplicação foi testada com python 3.13