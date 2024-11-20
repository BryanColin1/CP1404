from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super(DynamicLabelsApp, self).__init__(**kwargs)
        self.names = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']

    def build(self):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Dynamically add a Label for each name in the list
        for name in self.names:
            label = Label(text=name, font_size=24)
            box.add_widget(label)

        return box


if __name__ == '__main__':
    DynamicLabelsApp().run()
