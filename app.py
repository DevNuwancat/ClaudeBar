import rumps
from api import get_claude_data, time_unit
from keychain import get_token, save_token

class ClaudeBar(rumps.App):
    def __init__(self):
        super().__init__("", icon="assets/claudecode.png", template=True)
        self.state_item  = rumps.MenuItem("Claude")
        self.session_item = rumps.MenuItem("5hr: —")
        self.weekly_item  = rumps.MenuItem("Weekly: —")
        self.reset_item   = rumps.MenuItem("Resets: —")

        self.menu = [
            self.state_item, 
            None,
            self.session_item,
            self.weekly_item, 
            self.reset_item]
        
        self.refresh(None)

        rumps.Timer(self.refresh, 120).start()

    def prompt_for_token(self):
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

        self.title = f" {session:.0f}%"

        self.state_item.title  = f"Claude {plan} · Session Active {session:.0f}%"
        self.session_item.title = f"5hr session:  {session:.0f}%"
        self.weekly_item.title  = f"Weekly:       {weekly:.0f}%"
        self.reset_item.title   = f"Resets in:    {time_unit(reset)}"

ClaudeBar().run()