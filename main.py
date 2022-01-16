from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class MainWidget(GridLayout):
    label = 1
    my_text = StringProperty(str(label))

    def onclick(self):
        self.label += 1
        self.my_text = str(self.label)



class KivyLearnApp(App):
    pass


KivyLearnApp().run()
