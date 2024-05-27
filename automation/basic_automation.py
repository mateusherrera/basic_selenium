"""
Módulo para métodos genéricos que agilizam o desenvolvimento de automações com
a biblioteca Selenium.

:author: Mateus Herrera Gobetti Borges
:github: mateusherrera
:date: 2024-04-26
"""

# Bibliotecas
from os import getenv, path
from time import sleep

# Selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class BasicAutomation:
    """
    Classe para métodos genéricos que agilizam o desenvolvimento de automações
    com a biblioteca Selenium.
    """

    # INI: Fields

    selenium_initial_site: str
    selenium_wait_time: int

    chrome_driver_path: str
    chrome_exe_path: str

    headless: bool

    driver: WebDriver
    wait: WebDriverWait

    # END: Fields

    # INI: Constructor

    def __init__(self,
                 selenium_initial_site: str,
                 selenium_wait_time: int,
                 chrome_driver_directory: str = None,
                 chrome_driver_file: str = 'chromedriver.exe',
                 chrome_exe_path: str = None,
                 headless: bool = False
                 ):
        """
        Construtor da Classe.

        :param selenium_initial_site: Site inicial a ser aberto.
        :param selenium_wait_time: Tempo de espera do selenium.
        :param chrome_driver_directory: Caminho do chromedriver.
        :param chrome_driver_file: Nome do arquivo chromedriver.
        :param chrome_exe_path: Caminho do executável do Chrome.
        :param headless: Indicativo se o navegador deve ser aberto em modo headless.
        """

        if chrome_driver_directory is None:
            env_path = getenv('PyPath')

            if env_path is None:
                raise KeyError('Variável de ambiente "PyPath" não está definida.')

            else:
                chrome_driver_path = path.join(env_path, chrome_driver_file)

        else:
            chrome_driver_path = path.join(chrome_driver_directory, chrome_driver_file)

        self.selenium_wait_time = selenium_wait_time
        self.selenium_initial_site = selenium_initial_site

        self.chrome_driver_path = chrome_driver_path
        self.chrome_exe_path = chrome_exe_path

        self.headless = headless

        self.driver = None
        self.wait = None

    # END: Constructor

    # INI: Static Methods

    @staticmethod
    def explicit_wait(wait_time: int) -> None:
        """
        Faz um sleep explicito, conforme passado por parâmetro.

        :param wait_time: Quantidade de tempo em segundos.
        """

        sleep(wait_time)

    # END: Static Methods

    # INI: Generic Selenium-based Methods

    def start_browser(self):
        """
        Esse método abre o navegador.

        :param url_site: URL do site a ser aberto.
        """

        # Desabilita popup de senha
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option(
            "excludeSwitches",
            ['enable-automation']
        )
        if self.headless:
            chrome_options.add_argument('--headless')
        if self.chrome_exe_path is not None:
            chrome_options.binary_location = self.chrome_exe_path

        # Preparando chromedriver
        service = ChromeService(executable_path=self.chrome_driver_path)

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, self.selenium_wait_time)

        self.driver.get(self.selenium_initial_site)
        self.maximize_browser()

    def close_driver(self):
        """
        Esse método fecha o driver.
        """

        try:
            self.driver.close()

        finally:
            pass

    def reset_frame(self):
        """
        Esse método altera para o frame inicial da página que o driver controla.
        """

        self.driver.switch_to.default_content()

    def switch_frame(self, xpath_nw_frame: str):
        """
        Esse método altera para o frame passado por parâmetro.

        :param xpath_nw_frame: XPATH do novo frame.
        """

        self.wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, xpath_nw_frame)))

    def reset_to_default_window(self):
        """
        Esse método altera para a primeira janela do hadler.
        """

        self.driver.switch_to.window(self.driver.window_handles[0])

    def goto_last_window_handler(self):
        """
        Esse método altera para a última janela do hadler.
        """

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_number_window(self, number_of_window: int):
        """
        Esse método espera a quantidade de janelas abertas pelo driver ser um
        número específico.

        :param number_of_window: Número de janelas a se esperar.
        """

        self.wait.until(ec.number_of_windows_to_be(number_of_window))

    def goto_window_handler(self, index_window: int):
        """
        Esse método altera para uma janela especifica.

        :param index_window: Index da janela a ser alterada.
        """

        try:
            self.driver.switch_to.window(
                self.driver.window_handles[index_window])

        except Exception as error:
            raise error

    def switch_url(self, nw_endereco: str):
        """
        Esse método muda o endereço aberto no driver do selenium.

        :param nw_endereco: Novo endereço.
        """

        self.driver.get(nw_endereco)

    def back_to_initial_site(self):
        """
        Esse método volta a página do driver para o endereco inicial.
        """

        self.switch_url(self.selenium_initial_site)

    def qtde_windows(self) -> int:
        """
        Esse método retorna a quantidade de janelas abertas no driver do objeto.

        :return: Quantidade de janelas no driver.
        """

        return int(len(self.driver.window_handles))

    def verify_if_exists(self, xpath_to_verify: str) -> bool:
        """
        Esse método verifica a existencia de um elemento pelo seu xpath.

        :param xpath_to_verify: XPATH do elemento.
        """

        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_verify)))
            return True

        except:
            return False

    def verify_invisibility(self, xpath_to_verify: str):
        """
        Esse método espera a invisibilidade de um elemento (espera ele sumir).

        :param xpath_to_verify: XPATH do elemento.
        """

        self.wait.until(ec.invisibility_of_element_located((By.XPATH, xpath_to_verify)))

    def click_by_xpath(self, xpath_to_click: str):
        """
        Método genérico que clica em um elemento.

        :param xpath_to_click: XPATH do elemento que deve ser clicado.
        """

        self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, xpath_to_click)))
        self.driver.find_element(By.XPATH, xpath_to_click).click()

    def click_clickable_method_by_xpath(self, xpath_to_click: str):
        """
        Método genérico que clica em um elemento.
        Obs.: método de espera diferente do método 'click_by_xpath'.

        :param xpath_to_click: XPATH do elemento que deve ser clicado.
        """

        self.wait.until(ec.element_to_be_clickable((By.XPATH, xpath_to_click)))
        self.driver.find_element(By.XPATH, xpath_to_click).click()

    def select_by_value(self, xpath_to_select: str, value: str):
        """
        Método genérico que seleciona uma option.

        :param xpath_to_select: XAPTH do elemento select.
        :param value: Valor visível do option.
        """

        select = Select(self.driver.find_element(By.XPATH, xpath_to_select))
        select.select_by_value(value)

    def send_by_xpath(self, xpath_to_send: str, key_to_send: str):
        """
        Método genérico que envia uma string para um elemento.

        :param xpath_to_send: XPATH do elemento que deve ser escrito.
        :param key_to_send: String que deve ser enviada ao elemento.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_send)))
        self.driver.find_element(By.XPATH, xpath_to_send).send_keys(key_to_send)

    def deal_alert(self, confirm=True):
        """
        Esse método confirma um alerta.

        :param confirm: Indicativo se deve aceitar ou recusar o alerta, o padrão
        é aceitar.
        """

        try:
            alert = self.wait.until(ec.alert_is_present())

            if confirm:
                alert.accept()
            else:
                alert.dismiss()

        finally:
            pass

    def press_down_input(self, xpath_to_press: str):
        """
        Método genérico para apertar para baixo em um input.

        :param xpath_to_press: String com o caminho a ser enviado o comando.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_press)))
        self.driver.find_element(By.XPATH, xpath_to_press).send_keys(Keys.DOWN)

    def press_up_input(self, xpath_to_press: str):
        """
        Método genérico para apertar para cima em um input.

        :param xpath_to_press: String com o caminho a ser enviado o comando.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_press)))
        self.driver.find_element(By.XPATH, xpath_to_press).send_keys(Keys.UP)

    def press_left_input(self, xpath_to_press: str):
        """
        Método genérico para apertar para esquerda em um input.

        :param xpath_to_press: String com o caminho a ser enviado o comando.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_press)))
        self.driver.find_element(By.XPATH, xpath_to_press).send_keys(Keys.LEFT)

    def press_right_input(self, xpath_to_press: str):
        """
        Método genérico para apertar para direita em um input.

        :param xpath_to_press: String com o caminho a ser enviado o comando.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_press)))
        self.driver.find_element(By.XPATH, xpath_to_press).send_keys(Keys.RIGHT)

    def press_tab_input(self, xpath_to_press: str):
        """
        Método genérico para apertar TAB em um input.

        :param xpath_to_press: String com o caminho a ser enviado o comando.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_press)))
        self.driver.find_element(By.XPATH, xpath_to_press).send_keys(Keys.TAB)

    def confirm_input(self, xpath_to_confirm: str):
        """
        Método genérico para confirmar input de formulário (Pressiona ENTER).

        :param xpath_to_confirm: String com o caminho a ser confirmado.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_confirm)))
        self.driver.find_element(By.XPATH, xpath_to_confirm).send_keys(Keys.ENTER)

    def clear_input(self, xpath_to_clear: str):
        """
        Método genérico que limpa um input.

        :param xpath_to_clear: XPATH do input que deve ser limpo.
        """

        self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath_to_clear)))
        self.driver.find_element(By.XPATH, xpath_to_clear).clear()

    def get_attribute_by_xpath(self, xpath_element: str, attribute: str) -> str:
        """
        Esse método retorno um dado atributo de um elemento identificado pelo
        seu XPATH no documento HTML.

        :param xpath_element: XPATH do elemento.
        :param attribute: Nome do atributo que deve ser retornado.

        :return: Contéudo do atributo no elemento do HTML.
        """

        self.wait.until(ec.presence_of_element_located((By.XPATH, xpath_element)))
        return self.driver.find_element(By.XPATH, xpath_element).get_attribute(attribute)

    def get_element(self, xpath_element: str) -> WebElement:
        """
        Esse método retorna o objeto do elemento HTML.

        :param xpath_element: XPATH do elemento.

        :return: Objeto do elemento HTML.
        """

        self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, xpath_element)))
        return self.driver.find_element(By.XPATH, xpath_element)

    def execute_js(self, script_js: str):
        """
        Esse método executa um scipt em JavaScript passado como parâmetro.

        :param script_js: Script JavaScript.
        """

        self.driver.execute_script(script_js)

    def get_current_url(self) -> str:
        """
        Esse método captura a url atual do navegador.

        :return: URL atual.
        """

        url = self.driver.current_url
        return url

    def is_browser_open(self) -> bool:
        """
        Esse método verifica se o navegador está aberto.

        :return: True se estiver aberto, False, caso contrário.
        """

        try:
            self.driver.current_window_handle
            return True

        except WebDriverException:
            return False

    def minimize_browser(self):
        """
        Esse método minimiza o browser.
        """

        try:
            self.driver.minimize_window()

        finally:
            pass

    def maximize_browser(self):
        """
        Esse método maximiza o browser.
        """

        try:
            self.driver.maximize_window()

        finally:
            pass

    def to_up_browser(self):
        """
        Esse método tenta trazer o browser para frente.
        """

        self.minimize_browser()
        self.maximize_browser()

    # END: Generic Selenium-based Methods

    # END: Automation #
