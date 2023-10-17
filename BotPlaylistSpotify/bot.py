# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    bot.driver_path = r"resources\geckodriver.exe"

    # Opens the BotCity website.
    bot.browse("https://open.spotify.com/intl-pt")

    # Fazendo login
    entrar = bot.find_element(".LKFFk88SIRC9QKKUWR5u > button:nth-child(2)", By.CSS_SELECTOR)
    entrar.click()

    username = os.getenv("EMAIL_SPOTIFY")
    password = os.getenv("PASSWORD_SPOTIFY")
    
    login = bot.find_element("login-username", By.ID)
    login.click()
    login.send_keys(username)
    bot.tab()
    bot.paste(password)
    bot.enter()

    playlist = bot.find_element(".RowButton-sc-xxkq4e-0", By.CSS_SELECTOR)
    playlist.click()

    buscar_mais = bot.find_element("div.eoWRdH", By.CSS_SELECTOR)
    buscar_mais.click()

    alerta = bot.find_element("button.feKImU:nth-child(2)", By.CSS_SELECTOR)
    alerta.click()    

    campo_buscar_musicas = bot.find_element("input.Type__TypeElement-sc-goli3j-0", By.CSS_SELECTOR)
    campo_buscar_musicas.click()

    # necessário descer a tela para o botão de adicionar ser encontrado na próxima etapa
    bot.scroll_down(clicks=200)

    # dica: deixar o mais específico possível (nome da música e banda)
    campo_buscar_musicas.send_keys("dormi na praça bruno e marrone")
    
    botao_adicionar = bot.find_element("/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[4]/button", By.XPATH)
    botao_adicionar.click()


    # Wait 3 seconds before closing
    #bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    #bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
