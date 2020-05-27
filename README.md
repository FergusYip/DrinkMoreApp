# DrinkMore

DrinkMore is a Python 3 app for Mac to remind you to drink more water. When it's open you can choose whether or not to be reminded and change the frequency of which you would like to be reminded.

![alt text][menubar_expand]
![alt text][notification]

# Running the app

## Precompiled

Download the latest precompiled version of the app - [here](https://github.com/FergusYip/DrinkMoreApp/releases)

## Compile it yourself

Install requirements

`pip3 install -r requirements.txt`

Build app

`python setup.py py2app`

The compiled app will be found in the `dist` folder

## Run without compiling

Install requirements

`pip3 install -r requirements.txt`

Run the app

`python3 app.py`

Note that the settings window will not display the app icon and it is the python interpreter that is running the application.

# Dependencies

[rumps](https://pypi.org/project/rumps/) by Jared Suttles and Dan Palmer

[py2app](https://pypi.org/project/py2app/) by Bob Ippolito and Ronald Oussoren

# Credits

Developed by Fergus Yip, 2020

[Droplet, of, water Free Icon](https://icon-icons.com/icon/droplet-of-water/83794) by [Daniel Bruce](www.danielbruce.se), reused under the [CC BY License](https://creativecommons.org/licenses/by/4.0/). Modifications to the color and the addition of an outline and drop shadow have been made.

[menubar_expand]: https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/imgs/menubar_expand.png "Menu bar open"
[notification]: https://raw.githubusercontent.com/FergusYip/DrinkMoreApp/master/imgs/notification.png "Notification"
