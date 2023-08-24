pyinstaller --clean -w -F --icon=icon.ico --add-data="./conf.ini;." --hidden-import configparser AutoCheck.py


pyinstaller --clean -w --icon=icon.ico --add-data="./conf.ini;." --hidden-import configparser AutoCheck.py
