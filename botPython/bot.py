# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    bot = DesktopBot()

    name_of_the_music = "olivia rodrigo bad idea right"

    # variáveis de ambiente com dados de login no sistema operacional
    username = os.getenv("EMAIL_SPOTIFY")
    password = os.getenv("PASSWORD_SPOTIFY")   

    # abrindo o aplicativo spotify
    bot.type_windows()
    bot.wait(1000)    
    bot.type_keys("spotify")
    bot.enter()
    
    # começo do login no spotify
    if not bot.find( "login", matching=0.97, waiting_time=10000):
        not_found("login")
    bot.click()
    
    # muda para o navegador para fazer o login    
    if not bot.find( "email_username", matching=0.97, waiting_time=10000):
        not_found("email_username")
    bot.click_relative(67, 66)
    bot.type_keys(username)
    
    # entrando com a senha
    bot.tab()
    bot.type_keys(password)
    
    # configurar para não guardar o login (atrapalha as execuções seguintes)
    if not bot.find( "remember", matching=0.97, waiting_time=10000):
        not_found("remember")
    bot.click_relative(-35, 8)    
    bot.tab()
    bot.enter()
    bot.wait(1000)
    
    # após o processo de login, o navegador diz para abrir o aplicativo do spotify
    if not bot.find( "open_app", matching=0.97, waiting_time=10000):
        not_found("open_app")
    bot.click()
    
    # inicia o processo para encontrar música pelo botão de buscar
    if not bot.find( "search_music", matching=0.97, waiting_time=10000):
        not_found("search_music")
    bot.click()
    
    if not bot.find( "what_to_hear", matching=0.97, waiting_time=10000):
        not_found("what_to_hear")
    bot.click()
    
    bot.type_keys(name_of_the_music)
    bot.wait(2000)
    
    # movimenta o mouse para ficar em cima do card da música, ativando o botão play
    bot.move_relative(x=0, y=300)
    
    if not bot.find( "play_button", matching=0.97, waiting_time=10000):
        not_found("play_button")
    bot.click()    
      
    #if not bot.find( "music_label", matching=0.97, waiting_time=10000):
    #    not_found("music_label")
    #bot.click_relative(298, 1)
    
    if not bot.find( "three_points_menu", matching=0.97, waiting_time=10000):
        not_found("three_points_menu")
    bot.click()
    
    if not bot.find( "add_to_playlist", matching=0.97, waiting_time=10000):
        not_found("add_to_playlist")
    bot.click()
    
    if not bot.find( "the_playlist_name", matching=0.97, waiting_time=10000):
        not_found("the_playlist_name")
    bot.click()

    # deixando a música tocar por um tempo
    bot.wait(6000)
    
    # começa o processo de logout
    if not bot.find( "profile", matching=0.97, waiting_time=10000):
        not_found("profile")
    bot.click()
    
    if not bot.find( "logout_button", matching=0.97, waiting_time=10000):
        not_found("logout_button")
    bot.click()    
    
    bot.wait(1000)
    
    # fecha o spotify
    bot.alt_f4()

    # fecha o navegador
    # bot.alt_f4()
    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()




