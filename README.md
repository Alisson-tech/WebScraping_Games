# WebScraping_Games Request

Este projeto foi construído baseado em uma das funções de trabalho de um amigo, 
vale ressaltar que o projeto está adaptado a ambiente totalmente fictício, e não será utilizado comercialmente.

## Tarefa:

O funcionário de uma loja de venda de games deve contar a quantidade de produtos no estoque e criar uma planilha com os seguintes dados:

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

Depois basta clicar em 'Pesquisar' para iniciar o processo de pesquisa e gerar a planilha.

![img](https://github.com/Alisson-tech/WebScraping_Games/blob/master/imagens_Tutorial/Planilha.PNG)

## Atualização

Essa é a segunda versão do aplicativo. <br />

modificações:

- troca do selenium para o request (ganho de performance)
- troca da interface (interface mais agradável para o usuário)
- o uso de Threads para evitar o travamento da interface.
