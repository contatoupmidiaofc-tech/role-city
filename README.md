# Rolê City — protótipo do jogo de skate

Jogo 3D low-poly que roda no navegador do celular e do computador. Tudo está em um único arquivo: `index.html` (usa Three.js r147 via CDN).

Para jogar localmente com os personagens 3D realistas, sirva a pasta por HTTP (o navegador bloqueia carregar modelos direto do disco): `npm run dev` e abra http://localhost:3000. Abrindo o arquivo direto, o jogo funciona com os personagens simples.

## Publicação na HostGator

Cada push na `main` publica o jogo em `public_html/role-city` pela Action `Deploy HostGator` (FTP). Para ligar, cadastre em **Settings → Secrets and variables → Actions** do GitHub:

- `FTP_SERVER`: servidor FTP da hospedagem (aparece em cPanel → Contas FTP → Configurar cliente FTP)
- `FTP_USERNAME`: usuário FTP
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

## O que falta para virar um jogo online de verdade

1. **Multiplayer em tempo real**: hoje os outros skatistas são simulados. Para ver pessoas reais, falta um servidor com WebSocket (por exemplo Node + Socket.IO ou Colyseus) que sincronize posição, chat e corridas. Também precisa de "salas" por mapa e de validação no servidor das corridas e dos prêmios, para impedir trapaça.
2. **Contas de verdade**: cadastro com e-mail ou Google e progresso salvo no banco de dados (o projeto já usa Postgres), não só no navegador.
3. **Pagamentos (tokens)**: a Casa de Tokens está em modo demonstração. Para receber na sua conta:
   - criar uma conta no Mercado Pago (Pix e cartão) ou no Stripe e pegar as chaves de API;
   - criar no servidor uma rota que gera o checkout e um webhook que, ao confirmar o pagamento, credita os tokens na conta do jogador;
   - os tokens nunca podem ser creditados pelo navegador, só pelo servidor.
4. **Lojas de apps**: para publicar na Play Store ou na App Store, empacotar como PWA ou com Capacitor. Nas lojas, compras dentro do app costumam ter que passar pelo sistema de pagamento da própria loja.
