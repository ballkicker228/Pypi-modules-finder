# Pypi-modules-finder

Позволяет прямо из терминала искать модули для языка программирования python на сайте pypi.org.

* Использует pyfzf для выбора модуля из предложенных при поиске
* Работает очень быстро так как все работает через простые GET запросы
* Отображает команду для установки модуля и дает ссылку на домашнюю страницу модуля

## Установка

```
git clone https://notabug.org/wr/Pypi-modules-finder

cd Pypi-modules-finder

pip3 install beautifulsoup4

pip3 install requests

pip3 install lxml

pip3 install pyfzf
```

Далее устанавливаете fzf через ваш пакетный менеджер, у меня это:

```
sudo pacman -S fzf
```

И запускаете скрипт:

```
python3 main.py
```