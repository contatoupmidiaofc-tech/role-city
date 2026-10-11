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
