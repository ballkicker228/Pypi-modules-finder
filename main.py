import requests
from bs4 import BeautifulSoup
from pyfzf.pyfzf import FzfPrompt

HREFX = 'https://pypi.org/search/?q='

PYPIHREF = 'https://pypi.org'

def check(x, y):
    for i in range(len(y)):
        if x == y[i]:
            return i
            break
        else:
            continue
    return 404 # Ошибка

def get_html(href):
    resp = requests.get(href)
    return resp

def main():
    modulename = input('Введите название модуля который хотите найти: ').replace(' ', '+')

    href = f'{HREFX}{modulename}'

    html = get_html(href)

    soup = BeautifulSoup(html.text, 'lxml')

    packages = soup.find('ul', class_='unstyled')
    
    lis = packages.find_all('li')

    hrefsofresults = []

    namesofresults = []

    for li in lis:
        a = li.find('a')
        ahref = a.get('href')
        hrefsofresults.append(PYPIHREF + ahref)
        spanname = a.find('span', class_='package-snippet__name').text
        namesofresults.append(spanname)

    fzf = FzfPrompt()
    
    selectedmodule = fzf.prompt(namesofresults)[0]

    i = check(selectedmodule, namesofresults)

    href = hrefsofresults[i]

    html = get_html(href)

    soup = BeautifulSoup(html.text, 'lxml')

    header_pip_instructions = soup.find('p', class_='package-header__pip-instructions')
    comand = header_pip_instructions.find('span', id='pip-command').text

    print('============================\n\nКомманда для установки:')
    print(f'---- {comand}\n\n============================\n')

    releasedp = soup.find('p', class_='package-header__date')
    releaseddate = releasedp.find('time').text

    print('Модуль вышел:')
    print(f'{releaseddate}\n\n============================\n')

    homepagea = soup.find('a', class_='vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed')
    homepage = homepagea.get('href')

    print('Ссылка на домашнюю страницу:')
    print(f'---- {homepage}')
    


if __name__ == '__main__':
    main()