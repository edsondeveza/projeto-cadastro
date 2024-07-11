# Cadastro e Consulta de Clientes usando Streamlit e Pandas

Este projeto é um aplicativo web desenvolvido com Streamlit para consulta e exibição de clientes cadastrados a partir de um arquivo CSV. O projeto foi inspirado na aula "Desenvolvendo aplicações Web com Streamlit - Projeto prático" ministrada pelo professor Vinícius Rocha Lima da Empowerdata, com melhorias e adaptações adicionais realizadas com o auxílio do ChatGPT.

## Funcionalidades

- **Carregar Dados**: A função `carregar_dados()` carrega os dados do arquivo CSV `clientes.csv`. Se o arquivo não existir ou estiver vazio, um DataFrame vazio é retornado.
- **Formatação de Telefone e CPF/CNPJ**: As funções `formatar_telefone()` e `formatar_cpf_cnpj()` formatam números de telefone e CPF/CNPJ para exibição na tabela.
- **Configuração da Página**: Utiliza o Streamlit para configurar o título da página como "Consulta de Clientes", ícone da página e layout centralizado.
- **Exibição de Clientes**: Exibe uma tabela interativa com os clientes cadastrados. Se não houver clientes, exibe uma mensagem informativa.

## Tecnologias Utilizadas

- **Streamlit**: Biblioteca para criação de aplicativos web em Python de forma rápida e fácil.
- **Pandas**: Biblioteca para manipulação e análise de dados em Python.
- **Python**: Linguagem de programação utilizada para desenvolver o aplicativo.
- **Poetry**: Gerenciador de dependências e ambientes virtuais para Python.

## Como Executar

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**:
    ```bash
    git clone https://github.com/edsondeveza/projeto-cadastro.git
    cd projeto-cadastro
    ```

2. **Instale o Poetry** (caso não tenha instalado):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Instale as Dependências**:
    ```bash
    poetry install
    ```

4. **Ative o Ambiente Virtual**:
    ```bash
    poetry shell
    ```

5. **Execute o Aplicativo**:
    ```bash
    streamlit run consulta_clientes.py
    ```

## Estrutura do Projeto

* consulta_clientes.py    # Arquivo principal do aplicativo
* clientes.csv            # Arquivo CSV com dados dos clientes
* README.md               # Documentação do projeto
* pyproject.toml          # Arquivo de configuração do Poetry com as dependências do projeto.


## Contribuições

Contribuições são bem-vindas! Para sugestões ou correções, por favor abra uma issue ou envie um pull request.

---

Licença [MIT](LICENSE)
