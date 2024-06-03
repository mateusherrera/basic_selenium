"""
Amostra de utilização da classe automation usando orientação a objetos.

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

class GithubAutomation(BasicAutomation):
    """
    Classe de automação de exemplo para Github.
    """

    def __init__(self):
        """
        Construtor da classe.
        """

        selenium_initial_site = 'https://github.com/'
        selenium_wait_time = 5
        chrome_exe_path = r'C:\ini\chrome-win64\chrome.exe'

        super().__init__(
            selenium_initial_site
            , selenium_wait_time
            , chrome_exe_path=chrome_exe_path
            # , headless=True
        )

    def get_first_repository(self, user: str) -> list:
        """
        Realiza uma busca do primeiro repositório no github de um usuário.

        :param user: Usuário do github.

        :return: Primeiro repositório do usuário.
        """

        xpath_repositories = '/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]'
        xpath_first_repo = (
            '/html/body/div[1]/div[4]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[1]/div[1]/div[1]/h3/a'
        )

        self.driver.get(f'{self.selenium_initial_site}{user}')
        self.click_by_xpath(xpath_repositories)
        return self.get_attribute_by_xpath(xpath_first_repo, 'href')


if __name__ == '__main__':
    github_automation = GithubAutomation()
    github_automation.start_browser()

    gh_username = input('Digite um nome de usuário do Github: ')
    result = github_automation.get_first_repository(gh_username)

    os.system('cls')
    print(f'Link do primeiro repositório na página do perfil: {result}')

    github_automation.close_driver()
    pass
