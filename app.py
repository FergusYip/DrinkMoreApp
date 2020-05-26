import os
import json
import rumps

# https://icon-icons.com/icon/droplet-of-water/83794


class DrinkMoreApp(rumps.App):
    def __init__(self):
        super(DrinkMoreApp, self).__init__("DrinkMore")
        self.icon = '/Users/fergus/Projects/drink-water-app/dropletofwater_83794.ico'
        self.template = True
        self.menu = [
            'Remind Me',
            "Settings",
        ]
        self.config_filename = 'config.json'
        self.default_config = {
            "interval": 7200,
        }
        self.config = self.read_config()
        self.timer = rumps.Timer(self.remind, self.config['interval'])

    def remind(self, _):
        rumps.notification(title='It\'s time to drink a cup of water',
                           subtitle='Just a friendly reminder',
                           message='')

    @rumps.clicked('Remind Me')
    def enable(self, sender):
        if sender.state is 0:
            print("Switched on")
            self.timer.start()
        else:
            print("Switched off")
            self.timer.stop()
        sender.state = self.timer.is_alive()

    @rumps.clicked("Settings")
    def settings(self, _):
        self.prefs(self)

    def prefs(self, _):
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
                new_interval = int(response.text)
                self.config['interval'] = new_interval * 60
                self.save_config()
            except:
                rumps.alert(
                    title='Incorrect input',
                    message='Input must be a number',
                )
                self.prefs(self)  # Reopen settings window

    def save_config(self):
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        with open(filepath, mode='w') as config_file:
            json.dump(self.config, config_file)

    def read_config(self):
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        try:
            with open(filepath, mode='r') as config_file:
                return json.load(config_file)
        except:
            return self.default_config


if __name__ == "__main__":
    DrinkMoreApp().run()
