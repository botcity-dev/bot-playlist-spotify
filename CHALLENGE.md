## Desafio

Para participar do desafio você deverá criar um bot usando visão computacional para tocar uma musica no Spotify e adicionar a uma playlist.

> Para ver a lista completa de funções para desenvolver o seu bot, acesse a [documentação](https://documentation.botcity.dev/pt/frameworks/desktop/python/).

## Dicas

### Template
Disponibilizamos um template para você começar a desenvolver o seu bot, com algumas configurações prontas.

### Sugestão de implementação
- ### abrir o app do spotify
    - encontrar o executável do spotify e usar o comando `bot.execute(r"path/app.exe")`
    
    -- ou --
    - usar o teclado pressionando `bot.type_windows()`, `bot.type_keys("spotify")` e `bot.enter()`

1. ### logar com a conta botcity community (dados de acesso disponíveis no template)
    - usar o BotCity Studio para encontrar os elementos ([Guia rápido de uso](STUDIO.md))
    - buscar e clicar o botão de login (ação click)
    - buscar pelo texto "Email or username" e clicar no campo (ação click relativo)
    - digitar o email usando a função `bot.type_keys(username)`
    - usar a funcão `bot.tab()` para ir para o próximo campo
    - digitar a senha usando a função `bot.type_keys(password)`
    - buscar e clicar no elemento "remember me" (ação click)
    - usar a funcão `bot.tab()` para ir para o botão de login
    - usar a funcão `bot.enter()` para fazer o login
    - buscar e clicar no botão de retorno ao APP (ação click)

2. ### buscar e tocar uma música
    - buscar e clicar no icone "Buscar" (ação click)
    - usar a função `bot.type_keys("music_name")` para digitar o nome da musica
    - usar a função `bot.move_relative(x=100, y=100)` para mover o mouse até o card da música para aparecer o botão de play
    - buscar e clicar no botão play (ação click)
    - usar a função `bot.wait(10000)` para aguardar a música tocar por 10 segundos

3. ### adicionar a música em uma playlist
    - buscar e clicar no menu "..." no card da música (ação click)
    - buscar e clicar no botão "Adicionar a playlist" (ação click)
    - buscar e clicar na playlist desejada (ação click)

4. ### deslogar e fechar os aplicativos
    - buscar e clicar no icone de perfil (ação click)
    - buscar e clicar na opção sair (ação click)
    - usar a função `bot.alt_f4()` para fechar o app do spotify
    - usar a função `bot.alt_f4()` para fechar o app do navegador


