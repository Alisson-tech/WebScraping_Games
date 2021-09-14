# WebScraping_Games Request

Este projeto foi construído baseado em uma das funções de trabalho de um amigo, 
vale ressaltar que o projeto está adaptado a ambiente totalmente fictício, e não sera utilizado comercialmente.

## Tarefa:

O funcionário de uma loja de venda de games, deve contar a quantidade de produtos no estoque e criar uma planilha com os seguintes dados:

- Distribuidora
- Jogo
- Plataforma
- Quantidade no estoque
- Imagem do Produto (pesquisa no google)

## Aplicativo:

Esse Aplicativo tem o objetivo de pesquisar as imagens dos games no google e criar nossa planilha formatada.
<br />
site para pesquisar os games: https://www.grouvee.com/

Primeiro o usuário deve cadastrar todos os games

![img](https://github.com/Alisson-tech/WebScraping_Games/blob/master/imagens_Tutorial/Interface.PNG)

Depois basta clicar em 'Confirmar' que o google será aberto, após as pesquisas o aplicativo criará a planilha:

![img](https://github.com/Alisson-tech/WebScraping_Games/blob/master/imagens_Tutorial/Planilha.PNG)

## Atualização

Essa é a segunda versão do aplicativo, a unica modificação foi o uso da biblioteca Request no lugar do Selenium. <br />
Com essa mudança o aplicativo teve um ganho de performance, sendo mais rápido para realizar as buscas das imagens.
