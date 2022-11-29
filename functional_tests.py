from selenium import webdriver

## Não consegui fazer com que o webdriver abrisse de jeito nenhum, este erro acontecia
## toda vez: "raise WebDriverException(
## selenium.common.exceptions.WebDriverException: Message: 'C:\\Users\\thiag\\Documents\\GitHub\\tdd-project\\geckodriver-v0.32.0-win64\\geckodriver.exe' executable needs to be in PATH."
## Editei também as variáveis de ambiente do windows e coloquei o caminho do executável no
## PATH do sistema, mas não adiantou.
## Tentei também passando o paarâmetro "executable_path", escrevendo o path para o executável
## de várias formas diferentes, mas também não adiantou.

browser = webdriver.Firefox()

assert 'Django' in browser.title