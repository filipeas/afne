## AFNe

## Descrição
- Trabalho da disciplina de Teoria da Computação - UFPI que implementa reconhecimento e conversáo de um AFNe em um AFN.

## Dependências
- Para executar esse projeto, você precisa ter as seguintes dependências instaladas junto ao python:
    - python v3
    - sys
    - os
    - yaml

## Recomendações
- Utilize o anaconda para facilitar a instalação dos pacotes. [Utilize esse link para ir direto ao site oficial do Anaconda.](https://www.anaconda.com/) Baixe de acordo com o SO do seu computador. 

## Como executar
Após a instalação do python na sua máquina (ou o anaconda), execute os seguintes comandos:

**PS: Os seguintes comando são para utilizar com o anaconda. Caso não use o anaconda, NÃO USE OS COMANDOS ABAIXO QUE INICIAM COM ``` conda ```.**

- ``` conda create --name afne python=3 ```
- ``` conda activate afne ```
- ``` conda install -c anaconda yaml ```
- ``` pip install PyYAML ```

1) Vá até o arquivo ./languages/afn-e.yml. Abra-o e modifique de acordo com o AFNe que desejar testar. **Siga o padrão definido pelo arquivo.**
2) Abra o terminal dentro do diretório raíz e execute: ``` python main.py ```. Ele irá mostrar o autômato e a 5-upla do mesmo. Informe uma linguagem e ele irá informar se é aceita ou não. Após isso ele irá perguntar se você deseja converter o AFNe para um AFN. E por fim perguntará se deseja executar o teste novamente.