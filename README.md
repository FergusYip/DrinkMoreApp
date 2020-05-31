# DrinkMore

DrinkMore is a Python 3 app for Mac to remind you to drink more water. When it's open you can choose whether or not to be reminded and change the frequency of which you would like to be reminded.

<div align="center">
<img src="https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/images/app_demo/menubar_icon.png" width=400/>
<br/>
<img src="https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/images/app_demo/menubar_open.png" width=400/>
<br/>
<img src="https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/images/app_demo/notification.png" width=400/>

</div>

# Running the app

## Pre-Bundled

Download the latest precompiled version of the app - [here](https://github.com/FergusYip/DrinkMoreApp/releases).

Note: If you are running MacOS 10.15 or later, it will display a [popup](https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/images/security_warning/warning.png) and prevent you from opening the app. You can still [open](https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/images/security_warning/preferences.png) it by going to the General tab of the Security & Privacy section in System Preferences.

## Bundle it yourself

Clone the repository

`git clone https://github.com/FergusYip/DrinkMoreApp.git`

Enter the directory

`cd DrinkMoreApp`

Install requirements

`pip3 install -r requirements.txt`

Bundle app

`python setup.py py2app`

The compiled app will be found in the `dist` folder

## Run from source

Clone the repository

`git clone https://github.com/FergusYip/DrinkMoreApp.git`

Enter the directory

`cd DrinkMoreApp`

Install requirements

`pip3 install -r requirements.txt`

Run the app

`python3 app.py`

Note: The settings window will not display the app icon as it is the python interpreter that is running the application.

# Dependencies

[rumps](https://pypi.org/project/rumps/) by Jared Suttles and Dan Palmer

[py2app](https://pypi.org/project/py2app/) by Bob Ippolito and Ronald Oussoren

# Credits

Developed by Fergus Yip, 2020

[Droplet, of, water Free Icon](https://icon-icons.com/icon/droplet-of-water/83794) by [Daniel Bruce](www.danielbruce.se), reused under the [CC BY License](https://creativecommons.org/licenses/by/4.0/). Modifications to the color and the addition of an outline and drop shadow have been made.
