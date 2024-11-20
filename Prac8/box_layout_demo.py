from kivy.app import App
from kivy.lang import Builder


class ButtonEventDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello"

    def handle_button_press(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_fields(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


if __name__ == '__main__':
    ButtonEventDemo().run()
