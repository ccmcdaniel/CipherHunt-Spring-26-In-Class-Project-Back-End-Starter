from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty

class DashboardScreen(Screen):
    username = StringProperty("Guest")
    rank = StringProperty("Bystander")
    current_points = NumericProperty(45)

    def __init__(self, **kw):
        super().__init__(**kw)
        
        path = App.get_running_app().base_path
        Builder.load_file(path + "\\screens\\dashboard\\dashboard.kv")
        
      
    def set_dashboard(self):
        app = App.get_running_app()
        self.username = app.user.username
        self.rank = app.user.rank.current_rank
        self.current_points = app.user.rank.current_points
