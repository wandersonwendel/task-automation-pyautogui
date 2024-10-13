# Automação de Cadastro de Produtos

Este projeto tem como objetivo realizar a automação do cadastro de produtos em um sistema web, utilizando a biblioteca **PyAutoGUI** para controlar o mouse e o teclado, de modo a interagir com o navegador e preencher formulários automaticamente. O projeto foi desenvolvido como parte do curso **Python Power Up** da **Hashtag Treinamentos**.

## Funcionalidades e Fluxo de Trabalho

O script automatiza o processo de login e cadastro de produtos em um sistema web, a partir de uma planilha de dados CSV. Aqui está o fluxo de trabalho completo:

1. **Abrir o navegador Chrome**: Simula a abertura do navegador por meio de comandos de teclado.
2. **Arquivo auxiliar para captura de coordenadas do mouse**: O arquivo `auxiliar.py` ajuda a capturar as coordenadas exatas do mouse para ajustar os pontos de clique durante a automação. Ele exibe as coordenadas no terminal após 2 segundos, permitindo configurar o script de acordo com a sua tela.
3. **Login no sistema**: Preenche automaticamente o campo de e-mail e senha e clica no botão de login.
4. **Leitura da planilha CSV**: Utiliza o **Pandas** para ler a planilha `produtos.csv` que contém as informações dos produtos a serem cadastrados.
5. **Cadastro de produtos**: Para cada linha da planilha:
   - Preenche os campos de código, marca, tipo, categoria, preço, custo e observações (se houver).
   - Simula o clique no botão de cadastrar.
   - Faz um scroll na tela para possibilitar o cadastro do próximo item.
6. **Tratamento de Observações**: O campo de observações (`obs`) é opcional. Se estiver vazio ou contiver um valor `NaN`, ele será ignorado. Caso tenha um valor, será preenchido no campo correspondente.

### Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal utilizada.
- **PyAutoGUI**: Biblioteca usada para controlar o mouse e o teclado.
- **Pandas**: Biblioteca utilizada para manipulação e leitura de arquivos CSV contendo os dados dos produtos.
- **Time**: Biblioteca do python usada para criar pausas específicas durante a execução do script, simulando um comportamento mais humano.

### Comportamento do Campo `obs` (Observações)

O campo de **observações** (`obs`) pode conter valores em branco ou nulos (`NaN`). O script foi programado para verificar se esse campo contém algum valor antes de tentar preenchê-lo.

## Como executar

### 1. Instale as dependências

Instale as bibliotecas necessárias:

```bash
pip install pyautogui pandas
```

### 2. Coordenadas de acordo com sua tela

O arquivo **auxiliar.py** pode ser executado isoladamente e vai retornar as coordenadas exatas de onde você está posicionado seu mouse.

Para executar:

```bash
python auxiliar.py
```

Após 2 segundos, o script exibirá as coordenadas X e Y do mouse no terminal. Use essas coordenadas para ajustar os pontos de clique no script principal, conforme a resolução e o layout da sua tela.

### 3. Execute o código

```bash
python main.py
```

## Contribuição

Este projeto foi desenvolvido como parte da Jornada Python – Python Power Up, da Hashtag Treinamentos, mas está aberto para melhorias. Sinta-se à vontade para contribuir e enviar pull requests.
