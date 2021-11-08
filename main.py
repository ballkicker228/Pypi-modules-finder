import aiohttp
import asyncio
from bs4 import BeautifulSoup
from pyfzf.pyfzf import FzfPrompt

HREFX = 'https://pypi.org/search/?q='

PYPIHREF = 'https://pypi.org'

async def check(x, y):
    for i in range(len(y)):
        if x == y[i]:
            return i
            break
        else:
            continue
    return 404 # Ошибка

async def get_html(href):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=href) as resp:
            return await resp.read()

async def main():
    modulename = input('Введите название модуля который хотите найти: ').replace(' ', '+')

    href = f'{HREFX}{modulename}'

    html = await get_html(href)

    soup = BeautifulSoup(html, 'lxml')

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

    i = await check(selectedmodule, namesofresults)

    href = hrefsofresults[i]

    html = await get_html(href)

    soup = BeautifulSoup(html, 'lxml')

    header_pip_instructions = soup.find('p', class_='package-header__pip-instructions')
    comand = header_pip_instructions.find('span', id='pip-command').text

    print('============================\n\nКомманда для установки:')
    print(f'---- {comand}\n\n============================\n')

    releasedp = soup.find('p', class_='package-header__date')
    releaseddate = releasedp.find('time').text

    print('Последнее обновление модуля:')
    print(f'{releaseddate}\n\n============================\n')

    try:
        homepagea = soup.find('a', class_='vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed')
        homepage = homepagea.get('href')

        print('Ссылка на домашнюю страницу:')
        print(f'---- {homepage}')
    except:
        print('У данного модуля нет домашней страницы!')
    

if __name__ == '__main__':
    asyncio.run(main())