from setuptools import setup

APP = ['app.py']
DATA_FILES = ['menu_icon.ico']
OPTIONS = {
    'iconfile': 'app_icon.icns',
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)