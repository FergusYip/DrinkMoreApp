''' DrinkMore is a MacOS menu bar app to remind you to drink more water '''

import os
import json
import rumps


class DrinkMoreApp(rumps.App):
    ''' DrinkMoreApp '''
    def __init__(self):
        super(DrinkMoreApp, self).__init__('DrinkMore')
        self.icon = 'menu_icon.ico'
        self.template = True

        remindme = rumps.MenuItem(title='Remind Me')

        self.menu.add(remindme)
        self.menu.add(rumps.MenuItem(title='Settings'))
        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem(title='About'))

        self.config_filename = 'config.json'
        self.default_config = {"interval": 7200, "reminding": False}
        self.config = self.read_config()

        self.timer = rumps.Timer(self.remind, self.config['interval'])
        self.reminding = False

        if self.config['reminding'] is True and not self.timer.is_alive():
            print('Timer started (config specified)')
            self.timer.start()
            remindme.state = 1

    def remind(self, _):
        ''' Send a notification to the user reminding them to drink water'''
        if self.reminding is False:
            self.reminding = True
        else:
            print('Sending reminder')
            rumps.notification(title='It\'s time to drink a cup of water',
                               subtitle='Just a friendly reminder',
                               message='')

    @rumps.clicked('Remind Me')
    def toggle(self, sender):
        ''' Toggle reminders '''
        if sender.state == 0:
            print('Switched ON')
            self.reminding = False
            self.config['reminding'] = True
            self.timer.start()
        else:
            print('Switched OFF')
            self.config['reminding'] = False
            self.timer.stop()
        sender.state = int(self.timer.is_alive())
        self.save_config()

    @rumps.clicked('Settings')
    def settings(self, _):
        ''' Open the settings window '''
        self.prefs(self)

    def prefs(self, _):
        ''' Settings window '''
        if self.timer.is_alive():
            print('ERROR: Reminders are still active')
            rumps.alert(
                title='Please disable reminders before changing settings.',
                message='')
            return

        print('Opened settings window')

        current_interval = int(self.config['interval'] / 60)
        settings_window = rumps.Window(
            message='',
            title='Enter reminder frequency in minutes:',
            default_text=f'{current_interval}',
            ok='Apply',
            cancel='Cancel',
            dimensions=(250, 20),
        )
        settings_window.add_button('Reset')  # Button index 2
        response = settings_window.run()

        if response.clicked == 2:  # reset
            self.config = self.default_config
            minutes = int(self.config['interval'] / 60)
            print('Reset Settings')
            self.save_config()
            rumps.alert(
                title='Settings have been reset',
                message=
                f'Reminder frequency has been changed to {minutes} minutes.')
            return

        if response.clicked == 1:  # ok

            if not response.text.isdecimal():
                print('ERROR: New interval is not integer')
                rumps.alert(
                    title='Incorrect input',
                    message='Input must be an integer.',
                )
                self.prefs(self)  # Reopen settings window
                return

            minutes = int(response.text)

            if minutes < 1:
                rumps.alert(title='Incorrect input',
                            message=f'Input cannot be less than 1.')
                self.prefs(self)  # Reopen settings window
                return

            print(f'Successfully changed interval to {minutes} minutes')

            seconds = int(minutes * 60)
            self.config['interval'] = seconds
            self.save_config()

            rumps.alert(
                title='Success!',
                message=
                f'Reminder frequency has been changed to {minutes} minutes.')

    @rumps.clicked('About')
    def about(self, _):
        print('Opened about window')

        rumps.alert(
            title='About',
            message=(
                'Developed by Wai Lam Fergus Yip.\n'
                'Icon by Daniel Bruce, reused under the CC BY License.\n\n'
                'https://github.com/FergusYip/DrinkMoreApp'))

    def save_config(self):
        ''' Save the config to a JSON file in the application support folder '''
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        with open(filepath, mode='w') as config_file:
            print('Saving config')
            json.dump(self.config, config_file)

    def read_config(self):
        ''' Load the config to a JSON file in the application support folder '''
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        try:
            with open(filepath, mode='r') as config_file:
                print('Loading USER config')
                return json.load(config_file)
        except:
            print('Loading DEFAULT config')
            return self.default_config


if __name__ == '__main__':
    DrinkMoreApp().run()
