from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Click Me')
        button.bind(on_press=self.show_message)
        layout.add_widget(button)
        return layout

    def show_message(self, button):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Hello, Kivy!'))

        ok_button = Button(text='OK')
        ok_button.bind(on_press=lambda x: self.dismiss_popup(popup))
        content.add_widget(ok_button)

        popup = Popup(title='Message',
                      content=content,
                      size_hint=(None, None), size=(200, 200))
        popup.open()

    def dismiss_popup(self, popup):
        popup.dismiss()


if __name__ == '__main__':
    MyApp().run()
