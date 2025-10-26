# ClashRoyale
Manpulação da API de cartas do Clash Royale

🃏 Cartas Clash Royale (API + Python)
📘 Descrição

Este projeto em Python consome a API oficial do Clash Royale e permite ao usuário visualizar e filtrar todas as cartas do jogo, com base em raridade, custo de elixir e nome da carta.
O código também implementa busca binária e ordenação alfabética, tornando as pesquisas mais eficientes.

O programa é totalmente interativo no terminal (CMD), com menus e opções numeradas.

⚙️ Funcionalidades

✅ Listar todas as cartas do jogo
✅ Filtrar por raridade (Comum, Raro, Épico, Lendário, Campeão)
✅ Filtrar por custo de elixir
✅ Filtrar por raridade + custo de elixir
✅ Buscar carta pelo nome (usando busca binária)
✅ Interface interativa de menu no terminal

🧠 Estrutura das Funções
Função	Descrição
inicio()	Exibe o cabeçalho principal do programa
ordenar_cartas(dados)	Ordena as cartas alfabeticamente pelo nome
busca_binaria(cartas, nome_escolhido)	Realiza uma busca binária pelo nome da carta
raridade_cartas(dados)	Mostra as cartas de uma raridade específica
custo_cartas(dados)	Mostra as cartas que custam um determinado valor de elixir
filtrar_cartas(dados)	Filtra cartas por raridade e custo de elixir simultaneamente
voltar_sair()	Permite voltar ao menu principal ou encerrar o programa
🔗 API Utilizada

Clash Royale API Oficial:
https://developer.clashroyale.com

🧾 Como gerar seu Token:

Crie uma conta no site da Supercell Developer Portal
.

Vá até seu perfil e clique em Create New Key.

Dê um nome para a chave (ex: "Meu Projeto Python").

Adicione seu IP Address (use o IP público atual).

Copie o Token gerado e cole no campo token do código:

token = "SEU_TOKEN_AQUI"


⚠️ Importante:

Nunca compartilhe seu token publicamente. Ele é pessoal e dá acesso à sua conta de desenvolvedor.

🎯 Objetivos

O principal objetivo deste projeto foi aprimorar minhas habilidades em Python, especialmente no uso de requisições HTTP e na manipulação de APIs.
Busquei compreender na prática como consumir dados em formato JSON, trabalhar com filtros e buscas eficientes (como a busca binária), e organizar o código de forma modular e interativa.

Além disso, o projeto serviu como uma oportunidade para reforçar boas práticas de programação estruturada, tratamento de erros e interação com o usuário via terminal, criando um programa funcional, educativo e divertido.
