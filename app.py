''' DrinkMore is a MacOS menu bar app to remind you to drink more water '''

import os
import json
import logging
import datetime
import rumps


class DrinkMoreApp(rumps.App):
    ''' DrinkMoreApp '''
    def __init__(self):
        super(DrinkMoreApp, self).__init__('DrinkMore')

        self.logger = self.logger_init()

        self.logger.info('Starting application...')

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
            self.logger.info('Timer started (config specified)')
            self.timer.start()
            remindme.state = 1

        self.save_config()

    def remind(self, _):
        ''' Send a notification to the user reminding them to drink water'''
        self.logger.info('Ran timer function')
        if self.reminding is False:
            self.logger.info('Omitting first reminder')
            self.reminding = True
        else:
            self.logger.info('Sending reminder')
            rumps.notification(title='It\'s time to drink a cup of water',
                               subtitle='Just a friendly reminder',
                               message='')

    @rumps.clicked('Remind Me')
    def toggle(self, sender):
        ''' Toggle reminders '''
        if sender.state == 0:
            self.logger.info('Enabled reminders')
            self.reminding = False
            self.config['reminding'] = True
            self.timer.start()
        else:
            self.logger.info('Disabled reminders')
            self.config['reminding'] = False
            self.timer.stop()
        sender.state = int(self.timer.is_alive())
        self.save_config()

    def refresh_timer(self):
        ''' Refresh the timer '''
        self.logger.info(f'Refreshing timer')

        if self.timer.is_alive():
            self.logger.info(f'Stopping timer')

            self.timer.stop()
            self.reminding = False
            self.timer.interval = self.config['interval']

            self.logger.info(f'Restarting timer')
            self.timer.start()  # restart timer

        else:
            self.timer.interval = self.config['interval']

    @rumps.clicked('Settings')
    def settings(self, _):
        ''' Open the settings window '''
        self.logger.info('Clicked \"Settings\" button')
        self.prefs(self)

    def prefs(self, _):
        ''' Settings window '''

        self.logger.info('Opened settings window')

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
            self.logger.info('Reset Settings')
            self.config = self.default_config

        elif response.clicked == 1:  # ok

            if not response.text.isdecimal():
                self.logger.error('New interval is not integer')
                rumps.alert(
                    title='Incorrect input',
                    message='Input must be an integer.',
                )
                self.prefs(self)  # Reopen settings window
                return

            minutes = int(response.text)

            if minutes < 1:
                self.logger.error('New interval is less than 1')
                rumps.alert(title='Incorrect input',
                            message=f'Input cannot be less than 1.')
                self.prefs(self)  # Reopen settings window
                return

            seconds = int(minutes * 60)
            self.config['interval'] = seconds

        minutes = int(self.config['interval'] / 60)

        self.logger.info(f'Interval changed to {minutes} minutes')

        self.save_config()
        rumps.alert(
            title='Success!',
            message=f'Reminder frequency has been changed to {minutes} minutes.'
        )
        self.refresh_timer()

    @rumps.clicked('About')
    def about(self, _):
        self.logger.info('Opened about window')

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
            self.logger.info('Saving config')
            json.dump(self.config, config_file)

    def read_config(self):
        ''' Load the config to a JSON file in the application support folder '''
        filename = self.config_filename
        filepath = os.path.join(rumps.application_support(self.name), filename)
        try:
            with open(filepath, mode='r') as config_file:
                self.logger.info('Loading USER config')
                config = json.load(config_file)
                if config.keys() != self.default_config.keys():
                    rumps.alert(title='Error when loading config',
                                message='Default settings have been applied')
                    return self.default_config
                return config
        except:
            self.logger.exception('Loading DEFAULT config')
            return self.default_config

    def logger_init(self):
        logger = logging.getLogger('DrinkMore')
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        steam_handler = logging.StreamHandler()
        steam_handler.setFormatter(formatter)
        logger.addHandler(steam_handler)

        filename = f'DrinkMore.log'
        filepath = os.path.join(rumps.application_support(self.name), filename)

        file_handler = logging.FileHandler(filepath, mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger


if __name__ == '__main__':
    DrinkMoreApp().run()
