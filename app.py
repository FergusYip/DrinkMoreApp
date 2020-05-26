import rumps


class DrinkMoreWaterApp(rumps.App):
    def __init__(self):
        super(DrinkMoreWaterApp, self).__init__("🚰")
        self.menu = [
            'Remind Me',
            "Settings",
        ]
        self.config = {"interval": 5}
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

        interval = self.config['interval']
        response = rumps.Window(message='',
                                title='Enter reminder frequency in seconds',
                                default_text=f'{interval}',
                                ok='Apply',
                                cancel='Cancel').run()

        if response.clicked:
            try:
                new_interval = int(response.text)
                self.config['interval'] = new_interval
            except:
                rumps.alert(
                    title='Incorrect input',
                    message='Input must be a number',
                )
                self.prefs(self)  # Reopen settings window


if __name__ == "__main__":
    DrinkMoreWaterApp().run()
