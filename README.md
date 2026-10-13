# Rolê City — protótipo do jogo de skate

Jogo 3D low-poly que roda no navegador do celular e do computador. Tudo está em um único arquivo: `index.html` (usa Three.js r147 via CDN).

Para jogar localmente com os personagens 3D realistas, sirva a pasta por HTTP (o navegador bloqueia carregar modelos direto do disco): `npm run dev` e abra http://localhost:3000. Abrindo o arquivo direto, o jogo funciona com os personagens simples.

## Publicação na HostGator

Cada push na `main` publica o jogo pela Action `Deploy HostGator` (FTP), usando uma conta FTP exclusiva cujo diretório é `public_html/role-city`. Para ligar, cadastre em **Settings → Secrets and variables → Actions** do GitHub:

- `FTP_SERVER`: servidor FTP da hospedagem (aparece em cPanel → Contas FTP → Configurar cliente FTP)
- `FTP_USERNAME`: usuário FTP completo (ex.: `rolecity@dominio`)
- `FTP_PASSWORD`: senha FTP

Endereço do jogo: `https://upmidiaoficial1789521775000.1370262.meusitehostgator.com.br/role-city/`

## Publicação no Cloudflare Pages (em teste)

O projeto `role-city` do Cloudflare Pages está ligado a este repositório (ramo `main`, sem framework, sem comando de build, saída na raiz). Cada push na `main` publica sozinho em `https://role-city.pages.dev`, ao mesmo tempo que a HostGator.

- O arquivo `_redirects` só vale no Cloudflare: manda `README.md`, `package.json`, `.htaccess`, `.gitignore` e `.github/` de volta para o jogo, para não ficarem à mostra. A Action da HostGator não envia esse arquivo.
- O `.htaccess` só vale na HostGator. No Cloudflare a página já é sempre revalidada.
- Supabase (`ndcahlwnkynphfilvenw`): `https://role-city.pages.dev/**` está em Authentication → URL Configuration → Redirect URLs, para o e-mail de confirmação de conta voltar ao endereço novo. O Site URL continua na HostGator até a migração ser confirmada.
- A HostGator continua no ar até o Cloudflare ser aprovado.

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
- **3 cidades diferentes**: **São Paulo** (asfalto, Av. Paulista com ciclovia e faixa de ônibus, prédios altos, MASP, Ponte Estaiada), **Rio de Janeiro** (calçadas de ondas de pedra portuguesa, palmeiras, praia, Cristo Redentor, Pão de Açúcar, morro e comunidade com vielas) e **Salvador** (ruas de paralelepípedo, casarões coloniais com telhado de barro, favela com vielas, morro com casinhas, Elevador Lacerda, Farol da Barra). As lojas ficam em quarteirões diferentes em cada cidade. Viagem pela Rodoviária (de carro/moto grátis ou ônibus $ 150) ou pelo mapa, que tem uma aba para cada cidade. Cada cidade tem a sua praça online.
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
- **Áudio entre jogadores**: segure o botão Áudio (ou tecla B), fale e solte; quem está na mesma cidade ouve (mais alto perto). Dá para silenciar nas Configurações.
- **Camisas de time** (Seleção amarela e azul e clubes de vários estados, com listras, faixas e três cores) e **shorts/bermudas** (a canela aparece).
- **Botões editáveis** (Configurações → Botões da tela) e botões próprios no carro/moto: buzina, farol e setas.
- **Instalar no celular**: o jogo é um app instalável (PWA). Android: botão "Baixar o jogo no celular" ou menu ⋮ → Instalar app. iPhone: Safari → Compartilhar → Adicionar à Tela de Início.
- **Morro com favela em cada cidade** (SP ao sul, Rio a oeste, Salvador a leste): dá para subir a pé, de skate, carro ou moto. Terreno que sobe, escadaria de cimento, centenas de casas de tijolo e coloridas, lajes com caixa d'água, fios, bandeiras do Brasil e varais de bandeirinhas. Aparece no mapa.
- **Profissões** (Agência de Empregos): entregador, grafiteiro, instrutor, **motoboy** (precisa de moto), **taxista** (precisa de carro), **catador/gari**, **bombeiro** (apagar incêndios), **policial** (só depois de passar na prova da Delegacia: 10 perguntas, precisa acertar 7) e **traficante** (só para quem está numa facção: corre da encomenda, fica procurado enquanto carrega).
- **Figurantes por profissão**: PMs a pé e viatura com giroflex, bombeiros, garis, contenção armada no morro, táxi e motoboy no trânsito. Cada jogador real da mesma profissão na cidade substitui um figurante; os skatistas de mentira também vão sumindo quando entram jogadores reais.
- **Procurado (estrelas)**: atirar, atacar policial, pichar ou carregar encomenda deixa você procurado; a PM persegue e prende (multa). Policiais reais prendem jogadores procurados. Na Delegacia dá para se entregar.
- **Facções**: crie (nome, emoji e cor, $ 2.000) ou entre num grupo no QG da Comunidade (no morro). Membros pintam a marca do grupo nos muros e fincam bandeiras; tudo fica salvo no servidor e todos veem.
- **Armas de fogo** (Taser, Revólver, Pistola, Escopeta, Fuzil): só com tokens (dinheiro real). Derrubam por alguns segundos (sem sangue).
- **Carona**: chegue perto do veículo de outro jogador e aperte Ação. Moto leva 1 na garupa, carro leva até 3 passageiros.
- **Direção por botões**: no carro/moto aparecem ◀ ▶, Acelerar e Ré (ou joystick, nas Configurações), além de buzina, farol e setas.

### Banco de dados (Supabase)
- `jogadores`: progresso de cada conta.
- `grupos`: facções (nome único, emoji, cor, dono). Todos leem; só o dono altera/apaga.
- `marcas`: pinturas e bandeiras por cidade. Todos leem; cada um cria/apaga só as suas.
- **Skatepark grande** ao lado de cada cidade: half-pipe, bowl, quarter pipe gigante, funbox, kickers, corrimãos e ledge, tudo pintado com desenhos. Física de verdade: a gravidade puxa na subida e na descida, a beirada da rampa lança no ar, no quarter pipe/half-pipe/bowl dá aéreo e volta de frente, perde velocidade e volta de ré (fakie), e cai em cima do corrimão para dar grind (50-50, boardslide). A praça central também tem rampas e quarter pipes de verdade.
- **Morro só para moradores**: para subir é preciso ser morador (R$ 500 no QG, na entrada), estar numa facção ou ser policial em serviço. O **Ajbz (ADM) é o chefe de todos os morros**: a contenção, os pedestres e a PM cumprimentam, ninguém assalta nem prende o chefe, e os outros jogadores recebem aviso quando ele chega.
- **Contenção do morro** fuma e de vez em quando dá rajada para o alto.
- **Assaltos**: com arma de fogo você pode assaltar pedestres e outros jogadores (fica procurado). Assaltantes de mentira roubam pela cidade; a PM persegue e prende.
- **Delegacia e cadeia**: quem é preso fica na cela de 50 a 100 segundos (pelas estrelas) ou paga fiança. Policiais prendem bandidos (assaltantes e traficantes derrubados), que aparecem presos nas celas.
- **Conta ADM**: todas as armas (das pistolas ao fuzil) e botão Trocar (tecla Y) para mudar de arma.
- **Mira**: botão Mirar (ou segurar o botão direito do mouse / tecla N). A câmera vai para o ombro, aparece a mira no centro (fica vermelha em cima do alvo) e o tiro vai exatamente onde ela aponta; paredes e o chão seguram a bala. Arrastar o dedo mira mais devagar para ter precisão.
- **Rádio** (botão Rádio): canal do seu grupo (facção), da PM (policial em serviço) ou do chefe. Mensagens e áudios com o rádio aberto vão só para o grupo.
- **Chamado**: manda sua localização para o grupo (os membros recebem o GPS marcado) e chama a tropa (4 homens; 6 para o chefe Ajbz) que vem te proteger. Policial em serviço chama reforço da PM.
- **Ordens pelo rádio**: escreva e a tropa entende — "segue eu", "fica aí", "protege", "ataca", "ataca a polícia", "pega o ladrão", "espalha", "atira pro alto", "quantos tem aí?", "vai embora".
- **Munição real**: cada arma tem o seu carregador (Taser 1, Revólver .38 6, Pistola 9mm 17, Escopeta 8, Fuzil 30 automático) e recarga (botão Recarregar / tecla I).
- **Vida (0 a 100%)**: tiro, atropelamento, tombo feio e queda na corrida tiram vida. Em 0% você cai, o **SAMU** chega de ambulância com os socorristas e leva você para o **Hospital**, onde você acorda. Profissões novas: **Socorrista do SAMU** e **Médico**.
- **Bicicletas**: BMX, Mountain bike e Speed na Concessionária, com pedal e raios girando.
- **Corpo e cabelo**: magro, normal, forte ou gordo; baixinho, médio ou alto; vários estilos de cabelo (careca, moicano, black, dread, coque, tranças...).
- **Roupa exclusiva do Ajbz**: camisa e calça com o símbolo do grupo e o boné-coroa, só para a conta do chefe.
- **Lojas e prédios por dentro**: entre nas lojas, Concessionária, Delegacia, Bombeiros, Hospital, Prefeitura, Igreja etc.; cada uma tem decoração própria, atendentes e balcão.
- **Teste para todas as profissões**: 5 perguntas sobre a profissão (precisa de 4 acertos). Quem reprova espera 2 minutos para tentar de novo.
- **Prefeitura e comércios**: passe no teste de Comerciante, tire o alvará ($ 5.000) e abra lanchonete, farmácia, barbearia, bar, loja de roupas ou oficina num dos 12 pontos comerciais da cidade. A placa e a vitrine mudam para todos; quem compra no seu comércio paga 60% para você na hora, e o balcão fatura $ 300 por dia do jogo.
- **Casamento na Igreja**: compre a aliança ($ 500) e peça em casamento um jogador online ou um amigo da cidade. Sinos, confete e fogos; a cidade toda recebe o aviso e o nome fica com 💍.

### Tabela `comercios` (Supabase)
- Um comércio por ponto de cada cidade (`unique(cidade, slot)`). Todos leem; só o dono cria e fecha o seu.

### Polícia, bases e mansão do chefe
- **Abordagem policial**: policial em serviço tem pistola 9mm da corporação e algemas. Chegue perto de alguém e aperte Ação: "Parado! Polícia!" — a pessoa para com as mãos na cabeça (jogador real fica travado). Peça o **documento** (carteira de identidade com nome, RG e nascimento), consulte o sistema, **reviste** (acha arma sem registro), **algeme** quem tem crime e leve até a Delegacia: o preso vai seguindo você algemado.
- **Delegacia por dentro com 3 celas**: grades, porta de cela que fecha, cama de concreto. Coloque o preso na cela e tranque; jogador real vai para a cadeia e cumpre a pena.
- **Veículos e bases das profissões** (de graça para quem está no turno, na garagem da base): Viatura e Moto da PM (Delegacia), Ambulância e Motolância do SAMU e carro do Médico (Hospital), Auto Bomba dos Bombeiros (Quartel), Caminhão da Coleta Seletiva (Reciclagem), Táxi da Cooperativa (Rodoviária), Moto com baú e Bike de entrega (Agência), Kombi do Grafite e Moto do Movimento (QG). Sirene pisca enquanto dirige.
- **Mansão do Ajbz** no alto do morro, no meio da favela: 3 andares de ouro, colunas, coroa no telhado, piscina, coqueiros, seguranças armados e bandeiras do Brasil e do estado (Bahia em Salvador). Só o chefe entra. 1º andar: sinuca, bar, fliperamas, TV gigante com videogame (mini-jogos de sinuca, reflexo e pênaltis). 2º andar: cofres, montanhas de dinheiro e barras de ouro (cofre guarda dinheiro que não pode ser roubado). 3º andar: cobertura com cama king, hidromassagem, closet, aquário e trono de ouro. Elevador entre os andares.

### Vitrine, turismo, praia, tempo e helicóptero
- **Vitrine das lojas**: cada roupa, calçado, boné, óculos e acessório aparece com a **foto da peça vestida** (gerada no próprio jogo) e o botão **👁 Ver**: abre a foto grande, a descrição, o botão **Provar no personagem** e **Comprar**.
- **Pontos turísticos** (Mapa ou Rodoviária → Pontos turísticos): SP — MASP, Ponte Estaiada, Ibirapuera e Obelisco, Catedral da Sé, Theatro Municipal; RJ — Cristo Redentor, Pão de Açúcar, Maracanã, Escadaria Selarón, Arcos da Lapa; Salvador — Pelourinho, Elevador Lacerda, Farol da Barra, Mercado Modelo, Igreja do Bonfim, Dique do Tororó. Qualquer um visita pagando a **taxa do Bonde do AJBZ** (o chefe recebe quando está online e não paga). Câmera de cartão-postal, foto para o feed e passaporte com carimbos (todos os da cidade = $ 800).
- **Praia** (Rio e Salvador): botão para colocar **biquíni / sunga / ficar sem camisa** (moda praia também na Drip Store: biquíni, sunga, cueca box), **deitar na toalha** com guarda-sol e **entrar no mar** nadando. Água transparente com **peixes**. Área com bandeira vermelha e placa **"Cuidado: tubarão"** — quem nada lá é atacado pelo tubarão e vai de SAMU para o hospital.
- **Tempo**: sol, nublado, chuva e **temporal com raios e trovões**, igual para todos na cidade (muda a cada 6 minutos). **Dia mais longo**: um dia do jogo dura 1 hora real (uns 40 minutos de dia claro).
- **Heliponto e helicóptero do chefe** no telhado da mansão (3º andar → Subir para o heliponto). Só o ADM pilota: Subir/Descer, Frente/Trás e virar; pousa em qualquer lugar.

### Cômodos separados, aeroporto, Hangar AJBZ e viagens com percurso
- **Correção**: todas as lojas e prédios por dentro ficam no mesmo lugar do mapa; agora cada jogador só vê quem está no **mesmo cômodo** (quem está na farmácia não aparece para quem está na delegacia).
- **Aeroporto em cada cidade** (Mapa → Aeroporto, ou Rodoviária): pista com luzes, terminal, torre de controle, biruta, aviões no pátio, heliponto e o **Hangar AJBZ** (dono: Ajbz).
- **Hangar AJBZ** (do mais barato ao mais caro): helicópteros Robinson R22 ($ 60 mil), Robinson R44 ($ 120 mil), Esquilo ($ 250 mil), Agusta Executivo ($ 500 mil); aviões Paulistinha ($ 40 mil), Cessna 172 ($ 90 mil), King Air ($ 300 mil), Jato Executivo ($ 800 mil) e Jatão AJBZ ($ 2 milhões). Também em tokens. O chefe tem todos; nas vendas ele recebe 10% quando está online.
- **Viagens com percurso** (sem teletransporte): de **carro, moto ou ônibus** pela BR (BR-116 / BR-101 / Via Dutra) com placas de km, placas verdes, pedágio (para e paga), posto de gasolina, serra, pontes sobre rios, caminhões e carros na estrada, ultrapassagem, saída e chegada com a cidade no horizonte. De **avião ou helicóptero**: decola na pista, sobrevoa a cidade, voa acima das nuvens, sobrevoa a cidade de destino e pousa no aeroporto. Voo comercial pago ou na sua aeronave de graça. Segure "⏩" para ir mais rápido.
- **Passeio aéreo** sobre a cidade com seu avião/helicóptero, e helicóptero para pilotar livre a partir do heliponto do aeroporto.
- **Hangar AJBZ na cidade**: porta dourada na lateral da Rodoviária (com um helicóptero no telhado) abre a loja direto; dali tem botão para ir ao aeroporto.
- **Helicóptero do chefe sempre visível** no heliponto do telhado da mansão; o elevador da mansão tem o botão "Telhado · Heliponto".
- O app instalado (PWA) agora sempre busca a versão nova da página (sem cache velho).
- **Heliponto em casa**: quem tem helicóptero (e o chefe) ganha uma laje com heliponto em cima da casa, com **elevador de vidro direto para cima** e o helicóptero estacionado. Lá em cima: "Pilotar o helicóptero" ou "Descer pelo elevador". O telhado da mansão também tem o botão "Pilotar".
- **Controles do helicóptero**: os botões normais do veículo (Subir e Descer no lugar das setas, Frente/Trás e ◀ ▶). No PC: Espaço ou R sobe, Shift, Q ou F desce, setas/WASD direção.

### Morros com dono, guerra, vida na favela, pátio da PM e a Hilux do chefe
- **Tiroteio entre jogadores**: todo mundo por perto vê o disparo e escuta o tiro (antes só quem era atingido percebia).
- **Favelas da região** (Mapa → Favelas da região): 3 em cada cidade, longe do centro, todas do **comando do chefe Ajbz**. Quem quiser um morro **negocia o valor com o chefe**: o chefe manda a oferta pelo jogo, o jogador aceita e o dinheiro vai para o chefe. O dono tem bandeira, contenção, usuários comprando na boca e caixa de $ 450 por dia. Morros vendidos podem ser tomados na **guerra** por outro jogador (60 s na bandeira sem cair); o que é do chefe ninguém toma, e o chefe pode retomar os que vendeu. Tudo salvo no servidor (tabela `morros`).
- **Dinheiro infinito do chefe**: o saldo do ADM é completado sempre que baixa.
- **Vida na favela**: traficantes e as mulheres dançando perto do **paredão** (caixas de som com LED tocando um beat de trap), usuários subindo até a boca; o mesmo no morro do chefe.
- **Crianças** brincando de bola na praça. **Carros de som** no trânsito.
- **Pátio da PM**: 3 viaturas (PM, Força Tática, Caminhonete) e 3 motos (Rocam, Patrulha, Rocam Esportiva) sempre estacionadas na frente da Delegacia; policial em serviço chega perto e escolhe. **Cassetete** na mão dos policiais.
- **Casa do chefe de ouro** (a da Imobiliária), com o retrato dele na frente e a bandeira dele.
- **Hilux de Ouro do Chefe** (Concessionária → Usar) com paredão na caçamba tocando o "Trap do Chefe" (beat original do jogo). Tocando no chip de música dentro da Hilux, o chefe escolhe uma música do próprio celular para tocar no som dela.

### Cidade grande, viagem dirigindo, tatuagem e vida na cidade
- **Viagem dirigindo**: indo para outra cidade com o seu carro ou moto, quem dirige na BR é você (acelera, freia, troca de faixa, desvia dos carros e caminhões, para no pedágio). Ônibus e avião continuam com o percurso automático.
- **Dar dinheiro**: chegue perto de outro jogador e aperte Ação → "Dar dinheiro", digite o valor e toque em Dar. O dinheiro sai da sua conta e cai na hora para a pessoa.
- **Roupas novas**: bermudões compridos e largos (passam do joelho), regatas, camisetas de manga curta e **Sem camisa** (mostra o corpo). **Relógios** e **brincos** (novas seções na Drip Store).
- **Revólver na cintura**: a arma de fogo fica no coldre; o botão da arma tira da cintura (o próximo toque atira) e ela volta para a cintura sozinha depois de um tempo.
- **Estúdio de Tatuagem** (calçada do centro, perto da praça): escolha o lugar (antebraços, ombros, peito, costas, pescoço, panturrilha) e o desenho (tribal, rosa, coroa, estrelas, terço, seu nome, "Fé", "157", "Família", carpa, leão, asas), pague e o tatuador faz na hora. Todo mundo vê.
- **Incêndios**: de tempos em tempos um prédio pega fogo; o caminhão dos bombeiros sai do Quartel pelas ruas com sirene e os bombeiros apagam. Bombeiro em serviço pode ajudar jogando água.
- **Operação policial no morro**: de tempos em tempos a PM chega de viatura, sobe o morro e os traficantes trocam tiro com ela.
- **Cidades maiores**: a cidade continua para fora do centro, com avenidas, quarteirões, prédios, pracinhas e placas dos bairros (Av. Paulista, Ibirapuera, Pinheiros...; Centro, Lapa, Copacabana...; Pelourinho, Barra, Bonfim...). Mapa com "Ver a cidade toda" / "Ver o centro".
- **Pontos turísticos dentro da cidade**: cada um no seu bairro, cercado, com bilheteria e **dois seguranças na entrada** — só passa quem paga a taxa do Bonde do AJBZ (vale o dia do jogo; o chefe não paga). Cristo, Pão de Açúcar, Elevador Lacerda, Farol e Ponte Estaiada têm a entrada embaixo (trem, bondinho, elevador). Mapa → Pontos turísticos tem GPS até a entrada.

### Movimentos de gente de verdade (etapa 1)
- Os personagens agora usam **movimentos gravados de pessoas reais (captura de movimento)**: parado respirando e com variações (olha em volta, olha o relógio, apoia o peso, se alonga), **andar, trotar e correr** com a passada no ritmo exato da velocidade (sem "patinar"), **conversar gesticulando** (quando fala ou aparece o balão) e **dançar** (várias danças; samba para as mulheres).
- A transição entre parado, andando e correndo é suave. A cabeça continua virando para quem chega perto.
- Braços com arma apontada, spray, soco, celular, cigarro, aceno e comemoração continuam com o movimento do jogo por cima; skate, carro, moto, natação, algemas e quedas também continuam como antes.
- Homem: biblioteca de animações da Ready Player Me (o modelo masculino é Ready Player Me). Mulher: animações do Mixamo adaptadas ao esqueleto dela. Arquivos `modelos/anim_m.bin` e `modelos/anim_f.bin`.

### Corpos novos e mais realistas (etapa 2)
- Homens e mulheres agora usam corpos completos da Ready Player Me (`modelos/rpm_m.glb` e `modelos/rpm_f.glb`), com rosto realista, pele com luz e relevo (normal map) e camiseta, calça e tênis de verdade.
- Todas as roupas da loja continuam: a textura de cada personagem é pintada por região (camiseta, calça, tênis, pele, cabelo) com a cor e a estampa de cada peça; logomarca original apagada. Short, bermudão, regata, biquíni e **sem camisa** (com peitoral, abdômen e costas desenhados) usam máscaras no próprio corpo.
- Cor da pele e do cabelo de cada um, careca, penteados (black power, dreads, tranças, moicano, rabo, coque), bonés, chapéus, óculos, brincos, corrente, mochila, asas, relógio, coldre e tatuagens ajustados aos corpos novos.
- Mulheres ganharam os movimentos gravados por atrizes: parada com variações, andar, trotar, correr, conversar gesticulando e 6 danças.
- Moradores usam textura mais leve (melhor para o celular); o seu personagem fica em alta qualidade.

## Rádio do Rolê (músicas de verdade)

- 6 instrumentais originais feitos para o jogo (pasta `musicas/`): **Trap do Chefe**, **Coroa de Ouro** (trap), **Baile do Morro** (funk mandelão), **Tamborzão da Vila** (funk), **Rap de Quebrada** (rap) e **Madrugada na Favela** (trap lento).
- Tocam nos paredões, nas caixas da favela, nos carros de som e na Hilux. Todo mundo ouve a mesma música no mesmo trecho (a programação segue o relógio).
- Toque no aviso 🔊 da música para abrir a rádio. O chefe (ADM) pode escolher a música que toca para todos.
- Para adicionar músicas próprias (com direito de uso): envie o MP3 para `musicas/` e acrescente uma linha em `musicas/lista.json` (`id` = nome do arquivo sem `.mp3`, `n` = nome, `g` = estilo, `dur` = duração em segundos).

## Rádio mais alta
- O som da rádio passa por um amplificador com limitador (bem mais alto e sem distorcer) e alcança mais longe. No painel da rádio há os botões "Mais baixo / Mais alto".

## Carros realistas
- Carroceria lisa feita de seções arredondadas (capô, porta-malas, caixas de roda recortadas), vidros escuros com colunas, linhas das portas e maçanetas, faróis com projetor e LED, lanternas, grade colmeia, placa Mercosul na frente e atrás, retrovisores, rodas de liga com pneu de perfil, disco e pinça de freio, escapamento e sombra no chão. Vale para Fusca, Kombi, Gol, Sedã/Táxi, Picape, SUV, Esportivo e Supercarro (e as viaturas das profissões).

## Banco Rolê
- Prédio do banco ao lado do centro (leste) e caixas eletrônicos 24h espalhados. Abrir conta é grátis e dá na hora o cartão de crédito Rolê.
- Com o cartão, qualquer compra do jogo passa: sai primeiro da carteira, depois do saldo do banco e por último do limite do cartão. Dinheiro no banco não é levado em assalto e rende 0,5% por dia do jogo. Fatura com juros de 1% ao dia; com 3 dias de atraso o cartão bloqueia.

## Casas para alugar e vender
- Vila Residencial (6 casas com quintal) e todas as casas do morro. Toda casa tem morador; algumas têm placa ALUGA-SE ou VENDE-SE. O dono de todas é o chefe (ADM): aluguel e venda vão para ele.
- Quem aluga ou compra entra na casa (com cama, sofá, TV e cozinha). Casa no morro deixa a pessoa morador do morro. Moradores (figurantes) saem e entram das casas.

## Cidade viva
- Praça dos Coroas com mesas de dominó (também nas favelas): os coroas batem as pedras, falam e dá para apostar em quem ganha.
- Crianças andando pelas calçadas, mães de mão dada com os filhos, casais de mãos dadas. Jogadores casados andam de mãos dadas quando estão juntos.

## Ringue Rolê Fight
- Arena com ringue, cordas, arquibancada, luzes e plateia que vibra. Fila de lutadores: com gente online, o ringue chama de dois em dois (a próxima dupla espera); sozinho, luta contra um figurante.
- 4 rounds de 45 s com intervalo; vence por nocaute ou por pontos. Controles próprios: Jab, Direto, Chute, Defesa e Esquiva. Loja do Lutador com calções, regatas e luvas.

## Quadra de Futsal
- Quadra com gols, rede, alambrado, arquibancada e placar. Times pela camisa (Azul do Rolê, Vermelho da Vila, Verde do Morro, Amarelo da Praça), vendidas do lado da quadra.
- Com 10 jogadores online na fila vira campeonato (com 20, semifinais e final); com menos, pelada 5 contra 5 completada com figurantes. Controles próprios: Chutar, Passe, Carrinho, Correr e Pular.

## Tiroteio, tropa, hospital e caronas
- Todo tiro tira vida (jogadores, figurantes, policiais e traficantes), inclusive os tiros do ADM, com o número do dano subindo. Outros jogadores machucados mostram uma barrinha de vida.
- Com a vida zerada a pessoa cai, o SAMU leva para o hospital e ela sai de lá: o carro/moto dela fica esperando na porta (sem teletransporte; quem não tem veículo volta a pé).
- Tiroteio perto do chefe (ou de quem é de facção): a tropa chega sozinha, cerca a pessoa em volta e atira em quem começou.
- Futsal: a bola fica no pé de quem conduz; só sai no chute, no passe (vai para o parceiro do lado e gruda no pé dele), no carrinho ou quando o adversário entra na frente.
- Carro com 4 lugares e moto com garupa. Botão 🔒 (tecla U) tranca ou destranca: trancado ninguém entra.

## Jogo mais leve no celular
- Qualidade **Automática** (padrão): mede a fluidez a cada segundo e ajusta sozinha a resolução e as sombras; as sombras atualizam um quadro sim, outro não.
- Peças paradas de cada carro e das rodas viraram uma malha só por material (menos chamadas de desenho).
- Personagens fora da tela ou longe atualizam a animação menos vezes; avisos da tela só são reescritos quando mudam.

## Vozes e sons
- Os figurantes falam o que aparece no balão, com a voz do próprio celular em português (traficantes dando "Salve, Ajbz!", crianças, plateia, moradores...). Dá para desligar em Configurações → Vozes dos figurantes.
- Gol no futsal: narrador gritando "Goooool!" e a torcida vibrando. Golpes no ringue fazem a plateia reagir.
- Atropelou alguém (ou foi atropelado): grito. Cachorros latem e correm atrás de quem passa a pé. Helicóptero voando faz o barulho das pás.

## Família e seguranças do chefe
- Dois seguranças altos e fortes, de terno preto e óculos escuros, andam sempre ao lado do chefe. Ninguém chega perto: só quem o chefe liberar (botão 🕶️ Seguranças), a esposa e as filhas. Figurantes que encostam são barrados.
- Jasmim (6 anos) e Helena (2 anos) ficam brincando no quintal da mansão (e no quarto rosa, 4º andar, cheio de brinquedos). O chefe vai lá e aperta 👧 Filhas para levar; elas ficam pertinho brincando, correndo, pulando e falando "Papai!". Apertando de novo, os seguranças levam para casa. Os outros jogadores também veem as meninas e os seguranças.

## Cinema e parquinho (todas as cidades)
- Cine Rolê: ingresso de $ 15, três filmes passando no telão com plateia, pipoca.
- Parquinho com balanço, escorregador, gangorra, gira-gira e caixa de areia, cheio de crianças brincando e mães olhando.
- **Seguranças – liberar** (build 2026.10.11-26): no painel 🕶️ Seguranças dá pra escolher "Comigo (do lado)", "Esperar aqui na porta" ou "Se afastar um pouco". Ao entrar em lojas, casas ou cinema eles esperam sozinhos na porta. Só barram quem chega perto no modo "Comigo". Outros jogadores veem o mesmo modo (presença `segm`/`sa`).
- **Build 2026.10.12-27**
  - 🚪 Botão **Sair** (vermelho, no topo) aparece em qualquer lugar fechado: cinema, lojas/comércios e casas.
  - 🛝 Filhas: no parquinho ou na pista de skate aparece o botão **Brincar**. As meninas ficam brincando sozinhas até você tocar em **Voltar, filhas**. Se você se afastar muito, um segurança traz as duas de volta.
  - 👗 Moda feminina: vestidos (mini, midi e longo, com saia de verdade no corpo), saias, saltos, bolsas (novo item "Bolsas": de mão, transversal e clutch) e brincos novos (pérola, gota, argolão e esmeralda). As figurantes também usam.
  - ⚽ Torneio de futsal: com 10 ou mais na fila começa sozinho em 20s, com 2 a 4 times (semifinal e final; empate vai pros pênaltis). Prêmios: campeão $ 5.000 + Medalha de Ouro do Futsal; vice $ 1.500.
  - 🥊 Luta mais rápida: anda mais rápido, gingado na guarda, golpes mais curtos, esquiva com o direcional (para os lados, para trás ou abaixando) e combos (jab+jab = gancho, esquiva+direto = uppercut, chute colado = joelhada). O figurante circula, esquiva e contra-ataca.
  - 🛹 Corridas com vários mapas por país, escolhidos no painel ou sorteados. Brasil: SP Consolação, Rio Santa Teresa, Salvador Pelourinho e Paulista à noite; também São Francisco, Kyoto, Champs-Élysées e Porto.
  - 🛹 Torneio de Skate nas pistas de SP, Rio e Salvador: inscrição na barraca roxa, começa com 5 inscritos (ou completa com figurantes). São 75s de sessão; cada queda tira 150 pts e quem acerta mais ganha bônus. Prêmios: 1º $ 3.000 + Medalha de Ouro do Skate, 2º $ 1.000, 3º $ 500.
- **Build 2026.10.12-28**
  - 🗺️ HUD mais limpo: o minimapa e o quadro de nível, dinheiro e vida ficaram menores, e os chips do canto esquerdo estão mais compactos.
  - 🎮 Em Configurações > "Tamanho dos botões" dá para diminuir ou aumentar os controles (60% a 150%) e os botões do topo (60% a 140%).
  - 💇 Cabelos femininos: solto longo, solto ondulado, solto com franja, chanel, cacheado volumoso, rabo alto, maria-chiquinha, trança de lado, coque alto e coque baixo. As figurantes também usam.
  - 🏠 Cada casa tem um endereço único:
    - O lote da mansão do ADM é só do chefe. Os outros jogadores veem a "Mansão do chefe · particular" e não moram lá.
    - Novos imóveis em cada cidade: 2 condomínios com 4 mansões cada (Alto da Colina e Jardim Imperial) e a Vila Nova (6 casas), além da Vila Residencial e das casas do morro.
    - Toda casa pode ser alugada ou comprada por jogadores reais. Se mora um figurante, ele se muda. O banco impede que duas pessoas peguem a mesma casa.
    - A Imobiliária lista as casas livres por tipo e marca no GPS a mais próxima.
    - Quem já morava no lote antigo ganha, sem pagar de novo, uma casa própria do mesmo padrão em outro endereço. O jogador acorda na porta da própria casa.
- **Build 2026.10.12-29**
  - 🚗 O carro chamado ou estacionado agora aparece em tempo real para todos os jogadores online por perto. Antes só aparecia para os outros enquanto alguém dirigia.
  - 🏠 Casa aberta ou fechada:
    - O botão 🔓/🔒 aparece perto da sua casa e dentro dela. Também está no painel da casa.
    - Liberada: qualquer jogador online entra e todos se veem lá dentro.
    - Fechada: ninguém entra, e quem estiver visitando sai na hora.
    - Vale também para a mansão do ADM: os outros jogadores entram pela porta quando ela está liberada.
- **Build 2026.10.12-30**
  - 💰 **Assalto do bonde** (só o ADM):
    - No 📻 Rádio, toque em "Solicitar assalto" e escolha o alvo: o Banco Rolê, as lojas, ou o banco de outra cidade (nesse caso vão pela BR).
    - Chegam 3 Hilux pretas com 5 caras cada (15 no total). Você entra na da frente e eles dirigem até o alvo.
    - Lá, todo mundo desce: 2 ficam na porta e o resto entra com você. Os reféns deitam no chão e os funcionários ficam de mãos para cima.
    - No banco: dinheiro dos caixas e o cofre arrombado, com barras de ouro e diamantes.
    - As estrelas sobem com o tempo lá dentro. Na fuga, viaturas vêm atrás, tem troca de tiros e o helicóptero Águia acompanha.
    - Para escapar: subir o morro (a polícia não sobe) ou fugir pela BR, acelerando para despistar as viaturas.
    - A Hilux Preta também está à venda na concessionária.
  - 🚓 **Polícia**:
    - Farda nova em cada estado (PMESP cinza, PMERJ azul, PMBA cáqui), com colete escrito POLÍCIA, boina e coturno.
    - O helicóptero Águia faz ronda no céu e persegue com holofote quem está procurado.
  - 👊 **Na rua**:
    - O botão Bater funciona andando (soco). Com a Faca equipada (Arsenal, slot de arma), o golpe vira facada.
    - Dá para acertar figurantes, policiais, traficantes e jogadores.
  - 🤜 **Dar o toque**: perto dos meninos do morro, o chefe tem o botão para o cumprimento de faccionado.
  - 🪑 **Sentar**:
    - Bancos na praça central, na praça do dominó, no parquinho e nas calçadas, alguns com figurantes sentados.
    - Cadeiras de plástico nas vielas do morro, com os meninos sentados.
    - Sofá de casa e cadeiras e sofás dos comércios.
  - 🏦 **Banco por dentro**: dá para entrar no Banco Rolê. Tem 4 caixas, fila que anda, segurança, cofre, e gente entrando e saindo na porta nas 3 cidades.
  - 🏪 **Rua do Comércio** em cada cidade:
    - Sorveteria (cardápio e mesas).
    - Bar do Zé (balcão, sinuca com aposta, TV com futebol).
    - Brega do Rolê (pista colorida, DJ, galera dançando, botão de dançar).
    - Empréstimos AJBZ.
    - Também um Boteco no morro.
  - 💼 **Empréstimos AJBZ a 40%**:
    - Na loja, a pessoa preenche valor, parcelas e proposta, e o pedido vai com o documento (RG, CPF, profissão, renda).
    - O chefe recebe em "💼 Empréstimos", vê se é 👤 JOGADOR REAL ou 🎭 FIGURANTE, e aprova ou recusa.
    - Aprovado, a pessoa recebe o dinheiro e paga as parcelas para o chefe. Os figurantes também pagam as parcelas sozinhos.
    - Funciona pela conexão em tempo real: o pedido chega quando os dois estiverem online na mesma cidade.
  - ✈️ **Aviões**:
    - No Hangar, "Pilotar eu mesmo" coloca o avião na cabeceira da pista. Você acelera, passa de 25 m/s e decola.
    - Voando de avião ou helicóptero, o botão 🧭 Rota desenha anéis dourados no céu até o corredor aéreo da cidade escolhida. Passando pelo corredor, a viagem começa.
  - 🏘️ Os lotes das casas novas, do cinema, do parquinho e do comércio agora são sempre os mesmos para todos os jogadores. Antes podiam mudar de um aparelho para outro.

### Build 2026.10.12-31
  - 🛣️ **Chegada natural nas cidades** (sem tela preta):
    - De carro: a BR termina na entrada da cidade, com o pórtico "Bem-vindo", e você entra dirigindo.
    - De avião próprio: você chega no céu alinhado com a pista e pousa sozinho. Anéis verdes guiam a descida. Pousar fora da pista é pouso forçado e tira vida.
    - De helicóptero: você chega no céu e pousa onde quiser, inclusive no telhado dos prédios. Saindo no telhado, você desce pela escada do prédio.
    - Voo de linha continua com pouso automático, agora sem a tela preta.
  - 🚔 **Assalto**:
    - Botão 🏃 Fugir quando o assalto termina.
    - Na fuga, botão 🔫 Atirar nas viaturas e câmera mais afastada para ver a polícia.
    - A câmera do chefe segue o carro normalmente.
    - Chegando na favela, as Hilux ficam estacionadas em fileira e os caras descem e ficam por lá. O chefe pode dispensar o bonde no painel.
  - ☰ **Menu tracinho**: os botões de cima (rádio, filhas, etc.) ficam recolhidos num ☰. Os controles continuam à mostra.
  - 🪑 Bancos só nas calçadas e praças, nunca no meio da rua.
  - 🎯 **Mira exata**: o tiro sai da ponta da arma e vai direto no alvo.
  - 🪖 **Tanque de guerra do chefe**: na Concessionária, em "Usar". A torre gira para o alvo e o botão 💥 Canhão dispara. A explosão derruba quem está perto e explode carros e viaturas.
  - 👶 **Filhos para casados**:
    - Depois de casar na igreja aparece "👶 Ter filhos".
    - Você cria até 4 filhos: nome, menino ou menina, idade, roupa, cabelo e pele.
    - Eles funcionam igual às filhas do chefe: ficam em casa, andam com você, brincam no parque e aparecem para todos online.

### Build 2026.10.12-32
  - 🛹 **Guardar o skate**: no menu ☰ tem o botão "Guardar skate" / "Pegar skate". Guardado, o personagem anda sem o skate nas costas, e os outros jogadores também veem assim. Nos torneios e corridas de skate ele volta sozinho.
  - ✈️ **Câmera do avião e do helicóptero**: voando, a câmera fica acima e atrás, olhando de cima para baixo para onde você vai. Não pega mais a aeronave por baixo quando ela sobe.
  - 🔫 **Bonde depois do assalto**: quando o bonde chega, abre o painel com duas ordens:
    - ⛰️ **Liberar pra subir o morro**: eles sobem pela escadaria e ficam espalhados nas vielas e ruas do morro.
    - 🔫 **Ficar na ativa**: um terço vira sniper em cima das lajes, vigiando a entrada; o resto faz a contenção nas ruas com armamento pesado, andando de um lado para o outro.

### Build 2026.10.12-33
  - 🫡 **Liberar a tropa**: quando a tropa vem proteger (por exemplo, depois de bater em alguém), aparece o botão "Liberar tropa". Eles voltam pro morro.
  - 🎯 **Dano de verdade**:
    - Cada tiro certeiro tira vida, com a barrinha de vida em cima da cabeça. Quando a vida zera, o policial (ou o traficante, ou o figurante) morre e fica caído.
    - Só tira vida quando o tiro acerta. O tiro que erra passa raspando, e o traçante mostra isso.
    - Os mortos voltam depois de uns 3 minutos.
  - ⛰️ **Polícia subindo o morro**:
    - Todos os traficantes que estão no morro trocam tiro com a PM: os do morro (que descem para a linha de tiro), o bonde (os snipers nas lajes atiram de longe) e a tropa da facção.
    - Cada lado tem vida, e quem perder a vida primeiro morre.
  - 📻 **Rádio**: aberto, ele não cobre mais os botões de baixo. No celular deitado ele fica em cima, no meio da tela.
  - 🚗 **Botão Carros**: abre a lista de todos os seus veículos para escolher qual usar. Ele aparece estacionado do seu lado, sem precisar ir na Concessionária.

### Build 2026.10.12-34
  - ❤️ **Vida de verdade**:
    - Tiro, soco, facada, atropelamento e queda tiram vida, e a vida não volta sozinha.
    - Para recuperar, faça a consulta no Hospital ou compre remédio na Farmácia, que fica no Hospital: Analgésico +20%, Anti-inflamatório +40% e Kit de primeiros socorros +70%.
    - Os remédios ficam guardados na bolsa. Quando você está machucado aparece o botão 💊 Remédio para tomar.
    - Comida e bebida não curam mais.
  - 🚑 **SAMU para quem morre**:
    - Figurante, policial ou traficante que morre fica caído até a ambulância do SAMU chegar. Os socorristas descem com a maca e levam para o hospital, e depois de um tempo a pessoa volta.
    - Jogador real que zera a vida continua caído até o SAMU levar.
  - 🛣️ **BR**: as montanhas da serra não ficam mais em cima da pista.
  - 🧱 **Paredes de verdade**:
    - Pontos turísticos, pilares, torres, mastros, aeroporto e prédios soltos agora são sólidos e não dá mais para atravessar.
    - No skate, caixote, ledge, a lateral das rampas e os corrimãos são obstáculos: batendo neles, você cai e perde um pouco de vida. Para subir, tem que pular (ollie) por cima e fazer a manobra lá em cima.
  - 🛹 **Manobras por gesto**:
    - Primeiro pule. No ar, deslize ↑ (360 Flip), ↓ (Varial Kickflip), ← (Heelflip) ou → (Pop Shove-it).
    - Ou toque 1 vez (Kickflip), 2 vezes (Hardflip) ou 3 vezes (Impossible).
    - No ar o dedo faz manobra e não gira a câmera.

### Build 2026.10.12-35
  - 📡 **Tudo ao vivo para quem está online na mesma cidade**:
    - Dano e morte de figurantes, policiais e traficantes: todo mundo vê a pessoa cair no mesmo lugar, com a barrinha de vida, e o SAMU vem buscar em todas as telas.
    - Tropa da facção (ou reforço da PM) andando com você, o bonde do assalto (as 3 Hilux e os 15, inclusive os snipers nas lajes), as viaturas da perseguição e a ambulância do SAMU com os socorristas.
    - Explosões do canhão do tanque.
    - Operação no morro: um dos jogadores online decide quem acerta quem e manda para os outros, então todo mundo vê o mesmo resultado (quem morre, morre para todos).

### Build 2026.10.12-36
  - 🍻 **Bares e Brega em todas as cidades**:
    - Salvador não tinha a Rua do Comércio. Agora as 3 cidades têm Bar do Zé, Brega do Rolê, Sorveteria e Empréstimos, além do Boteco do Morro.
    - Novo botão "🍻 Bares e Brega" no menu ☰ mostra a distância de cada lugar e marca o GPS até a porta.
  - 🍺 **Bar**: música tocando, gente bebendo no balcão e nas mesas com garrafas, e alguns bêbados cambaleando e falando besteira.
  - 💃 **Brega**:
    - Palco com duas barras de pole dance e dançarinas de lingerie dançando.
    - Bebidas nas mesinhas e no balcão, e batida de brega tocando.

### Build 2026.10.12-37
  - 🚑 **SAMU de verdade**:
    - Busca o corpo de todo mundo: traficante, policial, morador e quem mais morrer.
    - A ambulância sai do Hospital e vai pelas ruas, sem atravessar parede. Os socorristas buscam com a maca os corpos que estão por perto, um de cada vez, e a ambulância volta pelas ruas para o Hospital. Podem sair até 2 ambulâncias ao mesmo tempo.
    - Socorrista de verdade online: recebe o aviso com GPS, coloca a vítima na maca e entrega no Hospital (ganha por vítima). Enquanto ele estiver online, o SAMU robô espera 45 s para dar a vez a ele.
  - 👮 **Polícia**:
    - Depois da prova, o policial escolhe a área (SP, Rio ou Salvador) e só trabalha lá.
    - Recebe o **Manual do Policial** com a tabela de penas: homicídio 12 min, roubo 10, atacar policial 8, tráfico 8, mandado 6, agressão 5, porte ilegal 4, disparo 3. Os crimes somam até 20 minutos.
    - O preso vê o tempo que falta e pode pagar fiança, comprar a 🔑 chave com tokens ou chamar ⚖️ advogado.
  - ⚖️ **Advogado (nova profissão)**:
    - Tem teste para entrar.
    - O preso contrata e paga os honorários. O advogado monta a defesa (3 perguntas) e o delegado decide. Sem advogado de verdade online, há 2 escritórios robôs com chances diferentes.
  - ⭐ **Delegado**:
    - Os policiais online da cidade votam, e o mais votado é o delegado. Se só tem um policial, é ele.
    - Painel do Delegado: chamar o batalhão, ronda, operação no morro na hora, mandado de prisão e alvará de soltura pelo nome, e julgar as defesas dos advogados.
  - 🚒 **Bombeiro**:
    - Também escolhe a área.
    - Quando pega fogo, recebe o alarme com GPS. O caminhão chega, a escada Magirus gira para o prédio e sobe, e a mangueira joga água.
    - Tem Manual do Bombeiro.
  - 🧹 **Rua**: garis varrendo as calçadas, e carroceiros com burro e carroça de sucata na entrada do morro e nas favelas.
  - 💼 **Salários**:
    - Pagos a cada 10 minutos de plantão, com base no salário médio real de cada profissão no Brasil, na escala da grana do jogo.
    - Gari $50, Entregador $55, Grafiteiro $60, Motoboy $70, Instrutor $75, Taxista $85, Socorrista $100, Bombeiro $150, Policial $160, Advogado $175, Médico $370, Delegado $500.
  - 🤖 **Robôs saem quando entram jogadores**: para cada jogador de verdade em plantão de policial, bombeiro, gari, taxista ou motoboy na cidade, um robô daquela profissão sai.
  - 🏠 **Casa por cidade**: cada casa é de uma cidade só. Para ter em outra cidade, você compra outra. Ao viajar, a casa daquela cidade vira a sua casa.

### Build 2026.10.12-38 (desempenho, fase 1)
  - ⚡ **Só desenha o personagem que aparece na tela**:
    - Quem está atrás da câmera, ou longe e já sumindo na neblina, fica de fora do desenho e da sombra. A lógica do jogo continua igual: eles andam, falam e reagem normalmente.
    - Medido na praça: de 1,1 milhão para 315 mil triângulos por quadro (−72%), e o desenho ficou cerca de 30% mais rápido.
    - Medido no morro: de 1,37 milhão para 460 mil triângulos.
  - 🧹 **Memória**: o traço dos tiros, os números de dano, as explosões e os jatos d'água agora liberam a memória quando somem. Antes, cada tiro deixava lixo e o jogo ficava mais pesado quanto mais tempo se jogava.

### Build 2026.10.12-39 (desempenho, fase 2)
  - 🧱 **Peças paradas juntadas**: calçadas, postes, bancos, muros, enfeites e casas do morro que usam o mesmo material agora são desenhados de uma vez, em blocos de 48 m. Se alguma peça muda (porta abre, objeto some, cor muda), aquele bloco volta ao normal sozinho.
  - 🚗 **Carro longe simplificado**: a mais de 38 m (26 m na qualidade baixa), os carros parados ou dos bots viram uma versão leve com a mesma cor, vidro e rodas. De perto, voltam a ser o modelo completo. O carro que você dirige nunca é trocado.
  - 🏷️ **Placas e nomes distantes**: nomes e placas pequenas que estão longe, e quase ilegíveis, deixam de ser desenhados.
  - 🛞 **Rodas**: as peças de cada roda foram juntadas.
  - Medido na praça: de 1135 para 637 chamadas de desenho por quadro (−44%).
  - Medido no morro: de 2259 para 1138 chamadas, e de 460 mil para 196 mil triângulos.
  - A lógica do jogo não muda. Tudo isso só vale na hora de desenhar o quadro.

### Build 2026.10.12-40 (desempenho, fase 3)
  - 🧠 **Motor 3D atualizado**: three.js r147 → r186 (arquivo `lib/three-r186.min.js`, servido pelo próprio site).
    - Cores, luzes e sombras foram ajustadas para ficar iguais às de antes. Comparação lado a lado: a mesma imagem, com diferença média menor que 0,5 de 255 na iluminação.
    - Desenha cerca de 10% mais rápido e cria menos "programas de desenho" (menos engasgos quando algo aparece pela primeira vez).
    - Aparelhos antigos, sem WebGL 2, continuam com a r147. Para forçar a versão antiga: `?three=147` no endereço.
    - Como o arquivo é gerado: `ferramentas/three/` (ajustes de compatibilidade explicados no `build.mjs`).
  - 📦 **Personagens 61% menores**: as texturas dos modelos passaram de PNG para JPEG de alta qualidade (2,7 MB → 1,07 MB cada, sem diferença visível). Conversor: `ferramentas/modelos_jpeg.py`.
  - ⏩ **Carregamento por partes**:
    - Os personagens começam a baixar já no menu, enquanto a pessoa digita o nome.
    - As roupas dos figurantes são montadas aos poucos, de quem está mais perto para quem está mais longe. Quem está perto já aparece pronto no 1º quadro, e quem nunca chega perto não gasta nada. Na entrada: 42 roupas montadas em vez de 186.
    - O agrupamento de peças da fase 2 agora é feito em pedaços pequenos por quadro, sem travar a tela.
    - Pré-aquecimento dos programas de desenho em segundo plano nos aparelhos que compilam em paralelo.
  - 💾 **Menos download repetido**:
    - Modelos, animações e músicas só são baixados de novo quando mudam, e não mais a cada atualização do jogo.
    - A checagem de versão nova lê só o começo da página (antes baixava a página inteira, 1,5 MB, a cada 5 minutos).
    - O cache do celular guarda os arquivos pesados separados da página e apaga as versões velhas sozinho.

### Build 2026.10.13-41 (abertura nova)
  - 🎬 **Abertura no estilo dos jogos de celular**: pôr do sol com a cidade passando ao fundo, estrelas, skate cruzando a tela, logomarca entrando com animação e brilho, barra de carregamento com dicas e "TOQUE PARA COMEÇAR".
  - 🔑 **Entrar com Google** (precisa ativar o provedor Google no Supabase) ou **Entrar com e-mail** (o mesmo login de antes).
  - 🖼️ Logomarca nova (Canva) com fundo removido: `marca/logo.webp` (abertura e menu) e `marca/logo.png` (original em alta). Ícones do app (`icons/`) refeitos com ela. Para trocar, substitua os arquivos e aumente o `?v=`.

### Build 2026.10.13-43 (pagamentos de verdade pelo Mercado Pago)
  - 💳 **Casa de Tokens ligada ao Mercado Pago** (Pix e cartão). O botão "Pagar com Mercado Pago" abre a página segura do Mercado Pago; ao aprovar, os tokens entram sozinhos.
  - Como funciona (seguro): `supabase/functions/mp-checkout` cria o pedido na tabela `pagamentos` com o preço definido no servidor e gera o link; `supabase/functions/mp-webhook` recebe o aviso do Mercado Pago e confere o pagamento direto na API dele antes de aprovar; o jogo pega os tokens pela função `resgatar_tokens()` do banco, uma única vez por pedido.
  - O botão "Simular pagamento" ficou só para o ADM.
  - **Configuração:** colocar o Access Token de produção do Mercado Pago em Supabase → Edge Functions → Secrets, com o nome `MP_ACCESS_TOKEN`. Sem ele, o jogo avisa que os pagamentos ainda não foram configurados.

### Build 2026.10.13-44 (divulgação)
  - ✉️ **Checagem de e-mail no cadastro:** corrige erros comuns ("Você quis dizer @gmail.com?") e recusa e-mails temporários. Reduz os e-mails que voltam (aviso do Supabase).
  - 🌐 **Página de apresentação:** `apresentacao.html`, com logo animada, recursos, imagens do jogo, como instalar e botão "Jogar agora". Use como link da bio.
  - 🖼️ Prévia ao compartilhar o link (WhatsApp, Instagram etc.): `marca/og.jpg`. Imagens do jogo em `marca/print-*.jpg`.
  - 📣 Plano de Instagram (perfil, primeira semana, legendas, roteiros de Reels, hashtags): `divulgacao/instagram.md`.

### Build 2026.10.13-45 (entrar sem tela preta e portas visíveis)
  - 🚪 **Entrar e sair de casas e comércios na hora**, sem tela preta. A troca de lugar acontece no mesmo instante do toque.
  - ⚡ A causa da demora: a qualidade automática desligava e religava as sombras, e cada troca obrigava o celular a refazer os gráficos de tudo. Agora a sombra só fica transparente (nada é refeito). As luzes de dentro das casas e lojas também usam luzes que já existem na cidade, então entrar não muda mais a contagem de luzes.
  - 🎨 **Portas bem visíveis:** toda casa (vila, condomínios e morro) ganhou porta colorida com moldura branca e uma luzinha em cima. Lojas, prédios e pontos comerciais ganharam porta escura de vidro com moldura branca, que contrasta com qualquer fachada.

### Build 2026.10.13-46 (Coleção Drip da Quebrada)
  - 👕 **53 peças novas**, inspiradas no que mais faz sucesso nos jogos (Free Fire, GTA RP) e na moda de rua:
    - **Camisetas com desenho** no peito e nas costas: Caveira Coroada, Fé em Deus, Grana, SK8 em Chamas, Rosa da Lealdade e Dados da Sorte.
    - **Gola polo:** branca, preta, azul-marinho, listrada e Black & Gold, com gola, botões e bordado.
    - **Jaquetas e moletons:** corta-vento tricolor e neon, bufante prata, Skate Rat, College Rolê City, Rei do Rolê e a **Jaqueta Angelical** (asas nas costas).
    - **Calças e bermudas:** bermuda corta-vento, cargo, calça de skatista, jogger refletiva e Calça Angelical.
    - **Calçados:** tênis de mola, chunky, de skate, chinelo slide (preto e dourado), papete e Tênis Angelical.
    - **Bonés e toucas:** trucker, aba reta branco, touca preta, bandana preta e aba reta Black & Gold.
    - **Óculos:** Juliet espelhado e dourado, Lupa Vilão e Vilão Preto.
    - **Cordões e relógios:** cordão com crucifixo, cordão grumet de ouro, relógio ouro rosé e relógio cravejado prata.
  - 💇 **Cabelo pintado** (nova seção da Drip Store): Nevou (platinado), Amarelo Nevou, Luzes Douradas, Luzes Platinadas (mechas por cima da cor natural), Ruivo, Rosa, Azul e Verde. A sobrancelha continua na cor natural. Todo mundo online vê.
  - 💎 Raras e lendárias só com tokens: raras de 30 a 60 T e lendárias de 80 a 150 T. As comuns saem com a grana do jogo.
  - Tênis agora mostram a estampa (listras, xadrez etc.) no corpo novo.
  - Vitrine da loja: a miniatura mostra a roupa montada (antes podia aparecer o boneco sem a roupa).
