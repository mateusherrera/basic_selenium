"""
Amostra de script para utilização da classe automation.

:author: Mateus Herrera Gobetti Borges
:github: mateusherrera
:date: 2024-05-27
"""

# Adicionando o diretório pai ao path
import os
import sys

# Obtenha o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtenha o diretório pai
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Adicione o diretório pai ao sys.path
sys.path.append(parent_dir)

# Importando a classe Automation
from automation.basic_automation import BasicAutomation


if __name__ == '__main__':
    selenium_initial_site = 'https://github.com/'
    selenium_wait_time = 5
    chrome_exe_path = r'C:\ini\chrome-win64\chrome.exe'

    github_user = 'mateusherrera'

    xpath_repositories = '/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]'
    xpath_first_repo = (
        '/html/body/div[1]/div[4]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[1]/div[1]/div[1]/h3/a'
    )

    github_automation = BasicAutomation(
        selenium_initial_site
        , selenium_wait_time
        , chrome_exe_path=chrome_exe_path
        # , headless=True
    )
    github_automation.start_browser()

    github_automation.driver.get(f'{github_automation.selenium_initial_site}{github_user}')
    github_automation.click_by_xpath(xpath_repositories)
    result = github_automation.get_attribute_by_xpath(xpath_first_repo, 'href')

    os.system('cls')
    print(f'Link do primeiro repositório na página do perfil: {result}')

    github_automation.close_driver()
    pass
