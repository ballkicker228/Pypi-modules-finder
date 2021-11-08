# Pypi-modules-finder

Позволяет прямо из терминала искать модули для языка программирования python на сайте pypi.org.

* Использует pyfzf для выбора модуля из предложенных при поиске
* Работает очень быстро так как все работает через простые GET запросы и работает асинхронно
* Отображает команду для установки модуля и дает ссылку на домашнюю страницу модуля

## Установка

```
git clone https://notabug.org/wr/Pypi-modules-finder
```
```
cd Pypi-modules-finder
```
```
pip install beautifulsoup4
```
```
pip install asyncio
```
```
pip install aiohttp
```
```
pip install lxml
```
```
pip install pyfzf
```

Далее устанавливаете fzf через ваш пакетный менеджер:

Arch gnu/linux:
```
sudo pacman -S fzf
```

Debian/Ubuntu:
```
sudo apt install fzf
```

Fedora:
```
sudo dnf install fzf
```

На Windows можете скачать по ссылке:

https://github.com/junegunn/fzf/releases

Остальные виды установки:

https://github.com/junegunn/fzf#installation


### Запуск

Для запуска прописываете:

```
python3 main.py
```