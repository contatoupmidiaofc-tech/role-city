# Rolê City — protótipo do jogo de skate

Jogo 3D low-poly que roda no navegador do celular e do computador. Tudo está em um único arquivo: `index.html` (usa Three.js r147 via CDN).

Para jogar localmente com os personagens 3D realistas, sirva a pasta por HTTP (o navegador bloqueia carregar modelos direto do disco): `npm run dev` e abra http://localhost:3000. Abrindo o arquivo direto, o jogo funciona com os personagens simples.

## Publicação na HostGator

Cada push na `main` publica o jogo pela Action `Deploy HostGator` (FTP), usando uma conta FTP exclusiva cujo diretório é `public_html/role-city`. Para ligar, cadastre em **Settings → Secrets and variables → Actions** do GitHub:

- `FTP_SERVER`: servidor FTP da hospedagem (aparece em cPanel → Contas FTP → Configurar cliente FTP)
- `FTP_USERNAME`: usuário FTP completo (ex.: `rolecity@dominio`)
- `FTP_PASSWORD`: senha FTP

Endereço do jogo: `https://upmidiaoficial1789521775000.1370262.meusitehostgator.com.br/role-city/`

## Personagens 3D

- `modelos/Michelle.glb` (skatista feminina) e `modelos/readyplayer.me.glb` (masculino) vêm dos exemplos do three.js. A Michelle é um personagem Mixamo (Adobe); o masculino é um avatar Ready Player Me.
- O jogo anima os ossos do esqueleto por código (andar, postura de skate, manobras, emotes) e recolore roupas, pele e cabelo pela loja.
- **Antes de lançar comercialmente**, confirme a licença desses dois modelos ou troque por modelos próprios/licenciados. Qualquer avatar no padrão Ready Player Me ou personagem Mixamo funciona com o mesmo código.

## O que já funciona

- **Cadastro**: apelido, sexo (masculino ou feminino), tom de pele e cor de cabelo. Começa a pé, com roupa básica, celular tijolão e $ 0.
- **A pé ou de skate**: o primeiro skate vem na primeira missão (ou compre na Shape & Truck). Tecla R / botão Skate sobe e desce.
- **Cidade aberta** com minimapa fixo no canto superior esquerdo (M ou toque abre o mapa completo), praça com rampas e logo, grafites nas paredes, carros, skatistas e lojas.
- **9 manobras** que liberam com missões concluídas: Kickflip, Heelflip, Pop Shove-it, Varial Kickflip, 360 Flip, Hardflip, Impossible, 540 Shove-it e Laser Flip. No ar, Pular + direção escolhe a manobra; a tecla Q / botão Truque faz a especial escolhida no Perfil. Várias no mesmo pulo viram combo com multiplicador.
- **Itens com raridade** (comum, raro, lendário): roupas, tênis, shapes, rodas, estampas e celulares. Lendários exclusivos saem em eventos, caixas e no ranking semanal.
- **Oficina**: skate customizado (shape, cor do shape, estampa, rodas, cor da lixa e dos trucks), com prévia.
- **Evolução do skatista**: cada nível dá 2 pontos para Velocidade, Impulsão, Técnica e Equilíbrio, que mudam a física.
- **Liga Rolê**: divisões Amador, Intermediário, Semi-Profissional e Profissional por reputação; ranking semanal que fecha toda segunda com prêmios.
- **Campeonato de Manobras**: 60 s na praça contra 7 rivais da sua divisão.
- **Corridas em 5 países** (Brasil, EUA, Japão, França, Portugal) com combate, itens e manobras que dão turbo.
- **Mundo social**: Rolêgram (feed com curtidas), chat da praça com balões sobre a cabeça, amigos online que você chama para o rolê, emotes (acenar, dançar, comemorar, sentar), crew e celular.
- **Replays**: os 6 melhores combos ficam gravados; assista com câmera cinematográfica em 1x, 0,5x e 0,25x e poste no feed.
- **Eventos temporários**: um evento novo por semana (Semana do Flip, Copa Relâmpago, Festival da Praça) com prêmio lendário, fim de semana em dobro e Hora do Rush (XP dobrado das 18h às 21h).
- **Caixas** rara e lendária, ganhas em competições (não são vendidas).
- **Visual**: personagens 3D realistas com esqueleto animado (com personagens simples como reserva), iluminação com tone mapping, céu com nuvens, sombras, pop-ups de manobra estilo adesivo e linhas de velocidade.
- **Progresso salvo** no navegador (localStorage).
- **Lojas de roupa variadas** (Drip Store): camisetas com estampas de verdade (listrada, xadrez, camuflada, havaiana, tie-dye, galáxia, raio, camisa de time), calças (jeans, rasgada, camuflada, listra lateral), tênis, chinelo, sandália papete, bota, chapéus (boné, aba reta, gorro, bandana, bucket, palha, viseira, coroa), óculos (escuro, redondo, coração, esportivo, aviador, visor neon) e acessórios (mochila, corrente, fone, asas). **Comum** só com grana de missões/trampos; **raro** com grana ou tokens; **lendário** só com tokens (dinheiro real).
- **Caminhada suave**: passada por fase ligada à velocidade (joelho dobra no balanço, quadril sobe e desce, braços opostos), respiração parado e transição suave entre andar, skate e emotes.
- **Missões mais difíceis**: tempo apertado, vidas (cair demais falha), entrega frágil com várias paradas, combos obrigatórios, rota de checkpoints e pódio só em 1º ou 2º.
- **Profissões** na Agência de Empregos: Entregador RolêFood (mochila térmica nas costas, gorjeta por rapidez), Grafiteiro de Aluguel e Instrutor de Skate. Cada 5 pedidos sobe de nível (+15% de pagamento).
- **Moradia** na Imobiliária: alugar ou comprar quarto, kitnet, casa ou mansão (mansão também com tokens). Aluguel cobrado por dia do jogo, despejo após 2 dias sem pagar, bônus de grana e XP e nascer em casa.
- **Dia e noite** sincronizados para todos (1 dia do jogo = 24 min): céu, sol/lua, estrelas, janelas acesas e luz dos postes.
- **Cidade viva**: pedestres nas calçadas, motos, cachorros que latem, gatos que fogem, pombos que voam quando você passa e bandos de pássaros.
- **Sons**: motores de carros e motos pela distância, rodinhas no asfalto, vento, passarinhos de dia, grilos à noite, cachorros, buzinas e efeitos das armas.
- **Pistas urbanas**: vielas estreitas entre casas, curvas fechadas de esquina, escadarias (pule antes ou capota) e muros/casas que exigem descer do skate e escalar pela corda, com bichos de cada país.
- **Personagens com vida**: dedos curvados naturais (mão relaxada, punho no soco, mão aberta no aceno), olhar que segue quem está perto e a câmera, olhos com pequenos movimentos, boca que mexe ao falar e sorri ao acertar manobra, gestos espontâneos parado (olhar o celular, coçar a cabeça, mão na cintura, braços cruzados, alongar), gestos de mão ao conversar, inclinação nas curvas e ao arrancar. Cabelo do personagem masculino gerado a partir do couro cabeludo do modelo.
- **Câmera de rosto** (botão Rosto): close no rosto com giro (arrastar) e zoom (rodinha/pinça); zoom da câmera normal até ficar sobre o ombro. Qualidade **Ultra** com resolução máxima e sombras finas.
- **3 cidades** com o mesmo traçado de ruas e cara própria: **São Paulo** (MASP, prédios altos, Ponte Estaiada), **Rio de Janeiro** (praia, calçadão de ondas, Cristo Redentor, Pão de Açúcar, morro) e **Salvador** (casarões coloridos, Elevador Lacerda, Farol da Barra). Viagem pela Rodoviária (de carro/moto grátis ou ônibus $ 150). Cada cidade tem a sua praça online.
- **Carros e motos** na Concessionária: 9 carros (Fusca, Kombi, Gol, Táxi, Sedã, Picape, SUV, Esportivo GT, Supercarro) e 6 motos (Biz, CG, XRE, Chopper, Esportiva, Superbike), com carroceria curva, pintura metálica com verniz, vidros, rodas de liga e faróis (comuns com grana; raros e lendários só com tokens; a conta ADM tem todos). Botão Carro / tecla V chama o veículo; Ação entra e sai; dirigir com joystick/WASD. Outros jogadores veem seu veículo.
- **GPS**: toque no mapa (ou num lugar da lista) para marcar o destino; linha azul no chão e no mapa mostra o caminho pelas ruas. Missões também mostram a rota.
- **Entrar em casa**: a porta abre, você entra e anda pelos cômodos (cama para descansar com bônus de XP, guarda-roupa, TV, geladeira).
- **Economia**: peças comuns só com grana de missões e trampos (preços mais altos); raras e lendárias só com tokens. Caixas dão peças comuns ou grana.
- **Figurantes realistas**: pedestres usam os mesmos modelos 3D dos personagens, com roupas sorteadas.
- **Armas de corrida** (Terminal Mundial → Arsenal): banana, estilingue, fumaça, spray de tinta e rojão teleguiado. Uma arma por corrida, 2 usos (tecla G / botão Arma). Bots também usam; funciona na corrida online.

## Online (Supabase)

- **Projeto Supabase:** `ndcahlwnkynphfilvenw` (tabela `jogadores` com RLS: cada conta lê e grava só o próprio save).
- **Conta:** e-mail e senha no menu inicial. Sem conta, o jogo funciona offline com save no aparelho.
- **Save na nuvem:** sincroniza a cada 10 s quando há mudança e ao sair da página.
- **Praça multiplayer:** canal Realtime `praca` com presença (quem está online e a aparência) e broadcast de posição (~8 por segundo) e chat. Jogadores reais aparecem com nome azul-claro e no minimapa.
- **Ranking semanal:** junta os jogadores reais da mesma divisão (função `ranking_semana`) com os rivais simulados.
- **Corrida online:** no Terminal Mundial, "Correr online" entra na fila do país (canal `fila_<país>` com presença). O primeiro da fila dá a largada; todos correm no mesmo mapa (pista e obstáculos gerados pela mesma semente) e trocam estado pelo canal `corrida_<id>` (posição ~10x/s, derrubadas e óleo). Quem fica 12 s sem sinal sai da corrida.
- **Limitações atuais:** o próprio jogo grava os pontos (falta validação no servidor contra trapaça); na corrida online não há bots, e a pedra de outro jogador só aparece quando acerta.

## O que falta para virar um jogo online de verdade

1. **Multiplayer em tempo real**: hoje os outros skatistas são simulados. Para ver pessoas reais, falta um servidor com WebSocket (por exemplo Node + Socket.IO ou Colyseus) que sincronize posição, chat e corridas. Também precisa de "salas" por mapa e de validação no servidor das corridas e dos prêmios, para impedir trapaça.
2. **Contas de verdade**: cadastro com e-mail ou Google e progresso salvo no banco de dados (o projeto já usa Postgres), não só no navegador.
3. **Pagamentos (tokens)**: a Casa de Tokens está em modo demonstração. Para receber na sua conta:
   - criar uma conta no Mercado Pago (Pix e cartão) ou no Stripe e pegar as chaves de API;
   - criar no servidor uma rota que gera o checkout e um webhook que, ao confirmar o pagamento, credita os tokens na conta do jogador;
   - os tokens nunca podem ser creditados pelo navegador, só pelo servidor.
4. **Lojas de apps**: para publicar na Play Store ou na App Store, empacotar como PWA ou com Capacitor. Nas lojas, compras dentro do app costumam ter que passar pelo sistema de pagamento da própria loja.
