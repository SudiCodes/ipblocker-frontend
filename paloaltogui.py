from cgitb import text
from imp import reload
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.image import AsyncImage


class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logo = Image(source="aa_logo.png", size_hint=(0.5, 0.25), pos=(-120, 500))
        self.add_widget(self.logo)

        self.label = Label(
            text="Palo Alto Firewall Helper Tool", size_hint=(0.5, 0.25), pos=(220, 0)
        )
        self.add_widget(self.label)
        self.button_disable = Button(
            text="Disable",
            size_hint=(0.1, 0.05),
            pos=(320, 290),
            background_color=(0, 0, 1, 1),
        )
        self.add_widget(self.button_disable)

        self.button_delete = Button(
            text="Delete",
            size_hint=(0.1, 0.05),
            pos=(420, 290),
            background_color=(0, 0, 1, 1),
        )
        self.add_widget(self.button_delete)

        self.input_field = TextInput(
            hint_text="Enter the rule ID",
            size_hint=(0.35, 0.05),
            pos=(280, 350),
            multiline=False,
        )
        self.add_widget(self.input_field)

        self.button_browse = Button(
            text="Browse", size_hint=(0.1, 0.05), pos=(580, 350)
        )
        self.add_widget(self.button_browse)

        self.toggle_id = ToggleButton(
            text="ID",
            group="input_type",
            size_hint=(0.065, 0.05),
            pos=(170, 350),
            state="down",
        )
        self.toggle_id.bind(on_press=self.change_placeholder)
        self.add_widget(self.toggle_id)
        self.toggle_name = ToggleButton(
            text="Name",
            group="input_type",
            size_hint=(0.065, 0.05),
            pos=(221, 350),
        )
        self.toggle_name.bind(on_press=self.change_placeholder)
        self.add_widget(self.toggle_name)

        self.button_fetch_disable_rule = Button(
            text="Fetch Disabled Rules",
            size_hint=(0.225, 0.05),
            pos=(320, 240),
            background_color=(0, 1, 0, 1),
        )
        self.button_fetch_disable_rule.bind(on_press=self.print_path)
        self.add_widget(self.button_fetch_disable_rule)

    def print_path(self, instance):
        self.button_fetch_disable_rule.height = 0
        self.button_fetch_disable_rule.width = 0
        self.button_fetch_disable_rule.opacity = 0
        self.button_fetch_disable_rule.disabled = True

        self.path_label = Label(
            text="report fetched!",
            size_hint=(0.225, 0.05),
            pos=(300, 240),
        )
        self.add_widget(self.path_label)
        self.open_link = Button(text="->", size_hint=(0.01, 0.05), pos=(400, 240))
        self.add_widget(self.open_link)
        self.reload_button = Button(
            text="Reload", size_hint=(0.01, 0.05), pos=(500, 240)
        )
        # self.reload_button.bind(
        #     on_press=self.add_widget(self.button_fetch_disable_rule)
        # )
        self.add_widget(self.reload_button)

    def change_placeholder(self, instance):
        if self.toggle_id.state == "down":
            self.input_field.hint_text = "Enter the rule ID"
        elif self.toggle_name.state == "down":
            self.input_field.hint_text = "Enter the rule name"
        else:
            self.input_field.hint_text = "Please choose the input type"


class Tool(App):
    def build(self):
        return CustomLayout()


if __name__ == "__main__":
    Tool().run()
