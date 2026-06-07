import rumps
from api import main
from keychain import save_token, get_token


class ClaudeBar(rumps.App):
    def __init__(self):
        super().__init__("Claude Bar")
        
          # this shows in menu bar
        self.session_item = rumps.MenuItem("5h session : ")

        self.menu = [self.session_item]
        

ClaudeBar().run()