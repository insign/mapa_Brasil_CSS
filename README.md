# Mapa Interativo do Brasil em SVG

Este projeto exibe um mapa do Brasil totalmente responsivo e interativo usando SVG, CSS e JavaScript. Ele permite a interação fácil com cada estado.

## Funcionalidades

- **Estados Interativos**: Passe o mouse sobre qualquer estado para vê-lo destacar.
- **Eventos de Clique**: Clique em qualquer estado para acionar um alerta JavaScript com sua abreviação.
- **Design Responsivo**: O mapa se ajusta automaticamente ao tamanho da tela.
- **Tecnologias Modernas**: Construído com tecnologias web modernas (SVG, CSS3, JavaScript ES6), substituindo uma implementação desatualizada de 2012 baseada em CSS sprites.

## Como Executar Localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Inicie um servidor web local:**
    Como o projeto usa `fetch` para carregar o SVG, você precisa executá-lo em um servidor local para evitar problemas de CORS. Uma maneira simples de fazer isso é com o servidor HTTP embutido do Python.

    ```bash
    python3 -m http.server 8000
    ```

3.  **Abra no seu navegador:**
    Navegue para `http://localhost:8000/map.html`.

## Captura de Tela

Aqui está uma prévia do mapa interativo com o efeito de hover ativo em um estado:

![Captura de Tela do Mapa Interativo do Brasil](screenshot.png)

## Estrutura de Arquivos

- `map.html`: O arquivo HTML principal que exibe o mapa.
- `assets/map.svg`: O arquivo SVG limpo e otimizado contendo os caminhos para cada estado brasileiro.
- `assets/style.css`: A folha de estilos para a estilização do mapa e efeitos de hover.
- `assets/script.js`: O arquivo JavaScript que carrega dinamicamente o SVG e adiciona interatividade.
- `sources/`: Contém o arquivo SVG original antes do processamento.
- `add_ids_to_svg.py`: O script Python usado para processar o SVG de origem e atribuir IDs únicos a cada estado.

## Histórico

Este projeto é uma modernização completa de um mapa antigo do Brasil criado originalmente em 2012 usando CSS sprites e GIFs. A nova versão é mais fácil de manter, escalável e construída com os padrões web atuais.
