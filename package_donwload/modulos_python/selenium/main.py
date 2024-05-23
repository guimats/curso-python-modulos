# pip install selenium
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging']
        )
    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Infomoney')
    search_input.send_keys(Keys.ENTER)
    search = browser.find_element(By.ID, 'search')
    links = search.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    header_after = browser.find_element(By.CLASS_NAME, 'after-header')
    page_link = header_after.find_elements(By.TAG_NAME, 'a')
    bitcoin = page_link[2].find_elements(By.TAG_NAME, 'span')
    bitcoin_value = bitcoin[1].text
    bitcoin_variation = bitcoin[2].text
    bitcoin_format = {'bitcoin_value:': bitcoin_value, 'bitcoin_variation:':
                      bitcoin_variation}

    CVS_FILE = ROOT_FOLDER / 'bitcoin.txt'
    with open(CVS_FILE, 'a+', encoding='utf8', newline='') as arquivo:
        arquivo.write(f'{bitcoin_value};')
        arquivo.write(f'{bitcoin_variation}\n')

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
