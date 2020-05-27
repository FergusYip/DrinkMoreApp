''' DrinkMore is a MacOS menu bar app to remind you to drink more water '''
import os
import json
import rumps

# https://icon-icons.com/icon/droplet-of-water/83794


class DrinkMoreApp(rumps.App):
    ''' DrinkMoreApp '''
    def __init__(self):
        super(DrinkMoreApp, self).__init__("DrinkMore")
        self.icon = 'menu_icon.ico'
        self.template = True
        self.menu = [
            'Remind Me',
            'Settings',
        ]
        self.config_filename = 'config.json'
        self.default_config = {
            "interval": 7200,
        }
        self.config = self.read_config()
        self.timer = rumps.Timer(self.remind, self.config['interval'])

    def remind(self, _):
        ''' Send a notification to the user reminding them to drink water'''
        rumps.notification(title='It\'s time to drink a cup of water',
                           subtitle='Just a friendly reminder',
                           message='')

    @rumps.clicked('Remind Me')
    def toggle(self, sender):
        ''' Toggle reminders '''
        if sender.state is False:
            print("Switched on")
            self.timer.start()
        else:
            print("Switched off")
            self.timer.stop()
        sender.state = self.timer.is_alive()

    @rumps.clicked("Settings")
    def settings(self, _):
        ''' Open the settings window '''
        self.prefs(self)

    def prefs(self, _):
        ''' Settings window '''
        if self.timer.is_alive():
            rumps.alert(title='Disable reminders before changing settings',
                        message='')
            return

        interval = int(self.config['interval'] / 60)
        settings_window = rumps.Window(
            message='',
            title='Enter reminder frequency in minutes',
            default_text=f'{interval}',
            ok='Apply',
            cancel='Cancel',
            dimensions=(250, 20),
        )
        response = settings_window.run()

        if response.clicked:
            try:
                new_interval = int(int(response.text) * 60)
                self.config['interval'] = new_interval
                self.save_config()
            except:
                rumps.alert(
                    title='Incorrect input',
                    message='Input must be a number',
                )
                self.prefs(self)  # Reopen settings window

    def save_config(self):
        ''' Save the config to a JSON file in the application support folder '''
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        with open(filepath, mode='w') as config_file:
            json.dump(self.config, config_file)

    def read_config(self):
        ''' Load the config to a JSON file in the application support folder '''
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        try:
            with open(filepath, mode='r') as config_file:
                return json.load(config_file)
        except:
            return self.default_config


if __name__ == "__main__":
    DrinkMoreApp().run()
