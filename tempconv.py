from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TemperatureConverterApp(App):
    def build(self):
        self.title = 'Temperature Converter'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.input_label = Label(text='Enter temperature in Celsius:')
        self.input_text = TextInput(hint_text='Celsius', input_filter='float')
        
        self.result_label = Label(text='Converted temperature: ')
        
        convert_button = Button(text='Convert')
        convert_button.bind(on_press=self.convert_temperature)

        layout.add_widget(self.input_label)
        layout.add_widget(self.input_text)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)

        return layout

    def convert_temperature(self, instance):
        try:
            celsius = float(self.input_text.text)
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.text = f'Converted temperature: {fahrenheit:.2f} °F'
        except ValueError:
            self.result_label.text = 'Invalid input. Please enter a valid number.'

if __name__ == '__main__':
    TemperatureConverterApp().run()
