# Basic Automation
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&labelColor=11111b&color=B5E8E0&logoColor=e0e0e0)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&labelColor=11111b&color=B5E8E0&logoColor=e0e0e0)

A classe `BasicAutomation` fornece métodos para agilizar o desenvolvimento de automações com Selenium.

##
```
__init__(self,
        selenium_initial_site: str,
        selenium_wait_time: int,
        chrome_driver_directory: str = None,
        chrome_driver_file: str = 'chromedriver.exe',
        chrome_exe_path: str = None
        )
```

**Parâmetros:**
- `selenium_initial_site`: URL do site que o selenium irá inicializar o navegador.
> Ao instanciar a classe, o navegador já será aberto.
- `selenium_wait_time`: Timeout que o selenium espera até lançar uma `Exception`, ao esperar algum elemento html.
- `chrome_driver_directory`: Caminho para a pasta que está o driver do chrome. Caso esse argumento seja omitido, o caminho descrito na variável de ambiente `PyPath` será utilizada.
- `chrome_driver_file`: Nome do arquivo de driver do chrome. Caso seja omitido, será `chromedriver.exe`.
- `chrome_exe_path`: Caminho do executável de um chrome específico.

**Exemplo de uso:**

```python
automation = Automation(
    'https://www.google.com.br',
    5,
    chrome_driver_directory='caminho/para/o/arquivo',
    chrome_driver_file='nome_do_arquivo.exe',
    chrome_exe_path='caminho/para/executavel/do/chrome'
)
```

## Lista de métodos

### `explicit_wait(wait_time: int) -> None`

Faz um sleep explicito, conforme passado por parâmetro

**Parâmetros:**
- `wait_time`: Quantidade de tempo em segundos.

**Exemplo de uso:**

```python
Automation.explicit_wait(10)
```

### `start_browser(self) -> None`

Esse método abre o navegador no site inicial descrito no atributo do objeto.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
```

### `close_driver(self) -> None`

Esse método fecha o driver.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.close_driver()
```

### `reset_frame(self) -> None`

Esse método altera para o frame inicial da página que o driver controla.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.reset_frame()
```

### `switch_frame(self, xpath_nw_frame: str) -> None`

Esse método altera para o frame passado por parâmetro.

**Parâmetros:**
- `xpath_nw_frame`: XPATH do novo frame.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.switch_frame('xpath/do/iframe')
```

### `reset_to_default_window(self) -> None`

Esse método altera para a primeira janela do hadler.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.reset_to_default_window()
```

### `goto_last_window_handler(self) -> None`

Esse método altera para a última janela do hadler.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.goto_last_window_hadler()
```

### `wait_number_window(self, number_of_window: int) -> None`

Esse método espera a quantidade de janelas abertas pelo driver ser um número específico.

**Parâmetros:**
- `number_of_window`: Número de janelas a se esperar.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.wait_number_window(2)
```

### `goto_window_handler(self, index_window: int) -> None`

Esse método altera para uma janela especifica.

**Parâmetros:**
- `index_window`: Index da janela a ser alterada.

```python
automation = Automation(**params)
automation.start_browser()
automation.goto_window_handler(1)
```

### `switch_url(self, nw_endereco: str) -> None`

Esse método muda o endereço aberto no driver do selenium.

**Parâmetros:**
- `nw_endereco`: Novo endereço.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.switch_url('https://github.com/')
```

### `back_to_initial_site(self) -> None`

Esse método volta a página do driver para o endereco inicial.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.back_to_initial_site()
```

### `qtde_windows(self) -> int`

Esse método retorna a quantidade de janelas abertas no driver do objeto.

**Retorno:**
- Retorna quantidade de janelas abertas no driver.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
qtde_open_windows = automation.qtde_windows()
```

### `verify_if_exists(self, xpath_to_verify: str) -> None`

Esse método verifica a existencia de um elemento pelo seu xpath.

**Parâmetros:**
- `xpath_to_verify`: XPATH do elemento.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.verify_if_exists('xpath/do/elemento')
```

### `verify_invisibility(self, xpath_to_verify: str) -> None`

Esse método espera a invisibilidade de um elemento (espera ele sumir).

**Parâmetro:**
- `xpath_to_verify`: XPATH do elemento.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.verify_invisibility('xpath/do/elemento')
```

### `click_by_xpath(self, xpath_to_click: str) -> None`

Método genérico que clica em um elemento.

**Parâmetros:**
- `xpath_to_click`: XPATH do elemento que deve ser clicado.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.click_by_xpath('xpath/do/elemento')
```

### `click_clickable_method_by_xpath(self, xpath_to_click: str) -> None`

Método genérico que clica em um elemento. Obs.: método de espera diferente do método 'click_by_xpath'.

**Parâmetros:**
- `xpath_to_click`: XPATH do elemento que deve ser clicado.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.click_clickable_method_by_xpath('xpath/do/elemento')
```

### `select_by_value(self, xpath_to_select: str, value: str) -> None`

Método genérico que seleciona uma option.

**Parâmetros:**
- `xpath_to_select`: XAPTH do elemento select.
- `value`: Valor visível do option.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.select_by_value('xpath/do/elemento', 'nome da opção')
```

### `send_by_xpath(self, xpath_to_send: str, key_to_send: str) -> None`

Método genérico que envia uma string para um elemento.

**Parâmetros:**
- `xpath_to_send`: XPATH do elemento que deve ser escrito.
- `key_to_send`: String que deve ser enviada ao elemento.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.send_by_xpath('xpath/do/elemento', 'string que deve ser enviada para o elemento')
```

### `deal_alert(self, confirm=True) -> None`

Esse método confirma um alerta.

**Parâmetros:**
- `confirm` Indicativo se deve aceitar ou recusar o alerta, o padrão é True (aceitar).

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.deal_alert()
# automation.deal_alert(confirm=False)
```

### `press_down_input(self, xpath_to_press: str) -> None`

Método genérico para apertar para baixo em um input.

**Parâmetros:**
- `xpath_to_press`: String com o caminho a ser enviado o comando.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.press_down_input('xpath/do/elemento')
```

### `press_up_input(self, xpath_to_press: str) -> None`

Método genérico para apertar para cima em um input.

**Parâmetros:**
- `xpath_to_press`: String com o caminho a ser enviado o comando.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.press_up_input('xpath/do/elemento')
```

### `press_left_input(self, xpath_to_press: str) -> None`

Método genérico para apertar para esquerda em um input.

**Parâmetros:**
- `xpath_to_press`: String com o caminho a ser enviado o comando.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.press_left_input('xpath/do/elemento')
```

### `press_right_input(self, xpath_to_press: str) -> None`

Método genérico para apertar para direita em um input.

**Parâmetros:**
- `xpath_to_press`: String com o caminho a ser enviado o comando.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.press_right_input('xpath/do/elemento')
```

### `press_tab_input(self, xpath_to_press: str) -> None`

Método genérico para apertar TAB em um input.

**Parâmetros:**
- `xpath_to_press`: String com o caminho a ser enviado o comando.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.press_tab_input('xpath/do/elemento')
```

### `confirm_input(self, xpath_to_confirm: str) -> None`

Método genérico para confirmar input de formulário (Pressiona ENTER).

**Parâmetros:**
- `xpath_to_confirm`: String com o caminho a ser enviado o comando.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.confirm_input('xpath/do/elemento')
```

### `clear_input(self, xpath_to_clear: str) -> None`

Método genérico que limpa um input.

**Parâmetros:**
- `xpath_to_clear`: String com o caminho a ser limpo.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.clear_input('xpath/do/elemento')
```

### `get_attribute_by_xpath(self, xpath_element: str, attribute: str) -> str`

Esse método retorno um dado atributo de um elemento identificado pelo seu XPATH no documento HTML.

**Parâmetros:**
- `xpath_element`: XPATH do elemento.
- `attribute`: Nome do atributo que deve ser retornado.

**Retorno:**
- Contéudo do atributo no elemento do HTML.

**Exemlo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
src_element = automation.get_attribute_by_xpath('xpath/do/elemento', 'src')
print(src_element)
```

### `get_element(self, xpath_element: str) -> WebElement`

Esse método retorna o objeto do elemento HTML.

**Parâmetros:**
- `xpath_element`: XPATH do elemento.

**Retornos:**
- Objeto do elemento HTML.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
html_element = automation.get_element('xpath/do/elemento')
```

### `execute_js(self, script_js: str) -> None`

Esse método executa um scipt em JavaScript passado como parâmetro.

**Parâmetro:**
- `script_js`: Script JavaScript.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
js_script = 'script JavaScript'
automation.execute_js(js_script)
```

### `get_current_url(self) -> str`

Esse método captura a url atual do navegador.

**Retorno:**
- URL atual.

**Exemplo de us:**

```python
automation = Automation(**params)
automation.start_browser()
current_url = automation.get_current_url()
print(current_url)
```

### `is_browser_open(self) -> bool`

Esse método verifica se o navegador está aberto.

**Retorno:**
- True se estiver aberto, False, caso contrário.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
is_open = automation.is_browser_open()
print(is_open)
```

### `minimize_browser(self) -> None`

Esse método minimiza o browser.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.minimize_browser()
```

### `maximize_browser(self) -> None`

Esse método maximiza o browser.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.miximize_browser()
```

### `to_up_browser(self) -> None`

Esse método tenta trazer o browser para frente.

**Exemplo de uso:**

```python
automation = Automation(**params)
automation.start_browser()
automation.to_up_browser()
```
