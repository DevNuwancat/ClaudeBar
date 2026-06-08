import rumps
from api import get_claude_data, time_unit
from keychain import get_token, save_token
from datetime import datetime
import webbrowser

class ClaudeBar(rumps.App):
    def __init__(self):
        super().__init__("", icon="assets/claudecode.png", template=True)
        self.state_item  = rumps.MenuItem("Claude")
        self.session_item = rumps.MenuItem("5hr: —")
        self.weekly_item  = rumps.MenuItem("Weekly: —")
        self.reset_main_item = rumps.MenuItem("◎ Reset")
        self.reset_item   = rumps.MenuItem("Resets: —")
        self.session_reset_item = rumps.MenuItem("  ↳ Resets in: —")
        self.weekly_reset_item = rumps.MenuItem("  ↳ Resets in: —")
        self.weekly_reset_date_item = rumps.MenuItem("↳ Resets Date: —")
        self.last_update_item = rumps.MenuItem("Updated: -")
        self.refresh_item = rumps.MenuItem("↻ Refresh Now", callback=self.refresh)
        self.set_token_item = rumps.MenuItem("❏ Set Session Token...", callback=self.prompt_for_token)
        self.github_item = rumps.MenuItem("◉ Github ◦ nuwancat", callback=self.open_github)
        self.ko_fi_item = rumps.MenuItem("♡ Buy me a coffee ◦ $1", callback=self.open_coffee)

        self.menu = [
            self.state_item, 
            None,
            self.session_item,
            self.weekly_item, 
            None,
            self.reset_main_item,
            self.session_reset_item,
            self.weekly_reset_item,
            self.weekly_reset_date_item,
            None,
            self.last_update_item,
            self.refresh_item,
            None,
            self.set_token_item,
            None,
            self.github_item,
            self.ko_fi_item,
            None,
            ]
        
        self.refresh(None)
        rumps.Timer(self.refresh, 120).start()

    def prompt_for_token(self, _=None):
        response = rumps.Window(
            title="Claude Bar",
            message="Paste your Claude AI session token (sessionKey):",
            default_text="",
            ok="Save",
            cancel="Cancel",
        ).run()
        if not response.clicked:
            return None
        token = response.text.strip()
        if not token:
            return None
        save_token(token)
        return token
    
    def open_coffee(self, _):
        webbrowser.open("https://ko-fi.com/nuwancat")

    def progress_bar(self, pct, width=12):
        filled = int(width * pct / 100)
        empty = width - filled
        return "▰" * filled + "▱" * empty
    
    def open_github(self, _):
        webbrowser.open("https://github.com/DevNuwancat")

    def refresh(self, _):
        token = get_token()
        if token is None:
            token = self.prompt_for_token()
            if token is None:
                self.title = "🤖 ⚠️"
                return 

        data = get_claude_data(token)
        if data is None:
            self.title = "🤖 ⚠️"
            return
        plan    = data['plan']
        session = data["five_hour"]["utilization"]
        weekly  = data["seven_day"]["utilization"]
        reset   = data["seven_day"]["resets_at"]

        session_reset = time_unit(data["five_hour"]["resets_at"])
        weekly_reset  = time_unit(reset)

        reset_dt = datetime.fromisoformat(reset)
        formatted = reset_dt.astimezone().strftime("%a %-I:%M %p")

        self.title = f" {session:.0f}%"

        self.state_item.title  = f"Claude {plan}"
        self.session_item.title = f"5hr       {self.progress_bar(session)}     {session:.0f}%"
        self.weekly_item.title  = f"Week    {self.progress_bar(weekly)}     {weekly:.0f}%"
        self.reset_item.title   = f"Resets in:    {time_unit(reset)}"
        self.session_reset_item.title     = f"↳ 5hr                    {session_reset}"
        self.weekly_reset_item.title      = f"↳ Week                {weekly_reset}"
        self.weekly_reset_date_item.title = f"↳ Week (date)     {formatted}"
        self.last_update_item.title = f"◔ Last Updated    {datetime.now().strftime('%-I:%M %p')}"


       

ClaudeBar().run() 