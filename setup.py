from setuptools import setup

APP = ['app.py']
DATA_FILES = ['menu_icon.ico']
OPTIONS = {
    'iconfile': 'app_icon.icns',
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'NSHumanReadableCopyright': 'Copyright (c) 2020 Wai Lam Fergus Yip',
        'CFBundleGetInfoString':
        'DrinkMore is a menu bar app for Mac to remind you to drink more water.',
        'CFBundleVersion': '1.3.0',
        'CFBundleIdentifier': 'org.pythonmac.DrinkMore'
    },
    'packages': ['rumps'],
}

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    app=APP,
    name='DrinkMore',
    author='Fergus Yip',
    author_email='fergus.yipwailam@gmail.com',
    url='https://github.com/FergusYip/DrinkMoreApp',
    description=
    'DrinkMore is a Python 3 app for Mac to remind you to drink more water.',
    long_description=long_description,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps'],
    classifiers=["License :: OSI Approved :: MIT License"],
)
