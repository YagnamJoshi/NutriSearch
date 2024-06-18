import kivy_config  # Ensure this is the first import
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import requests

class NutritionApp(App):
    def build(self):
        # Use FloatLayout to layer widgets on top of the background image
        self.layout = FloatLayout()

        # Add background image
        self.background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.background)

        # Create a box layout for the UI elements
        ui_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.title_label = Label(text="Nutri Search", font_size='24sp', size_hint=(1, 0.1), color=(0, 0, 0, 1))
        ui_layout.add_widget(self.title_label)
        
        self.food_input = TextInput(hint_text='Search', size_hint=(1, 0.1), font_size='18sp', multiline=False)
        ui_layout.add_widget(self.food_input)
        
        self.search_button = Button(text='Search', size_hint=(1, 0.1), font_size='18sp', background_color=(0.1, 0.5, 0.8, 1))
        self.search_button.bind(on_press=self.get_nutrition)
        ui_layout.add_widget(self.search_button)
        
        # ScrollView for the results
        self.scrollview = ScrollView(size_hint=(1, 0.7))
        self.result_layout = GridLayout(cols=1, size_hint_y=None)
        self.result_layout.bind(minimum_height=self.result_layout.setter('height'))
        self.scrollview.add_widget(self.result_layout)
        ui_layout.add_widget(self.scrollview)

        # Add the UI layout on top of the background
        self.layout.add_widget(ui_layout)

        return self.layout

    def get_nutrition(self, instance):
        food_item = self.food_input.text.strip().lower()
        response = requests.get(f'http://127.0.0.1:5000/get_nutrition?food_item={food_item}')
        self.result_layout.clear_widgets()  # Clear previous results

        if response.status_code == 200:
            data = response.json()
            result_label = Label(text=f"Nutritional Information for {self.food_input.text}:", font_size='20sp', color=(0, 0, 0, 1), size_hint_y=None, height=40)
            self.result_layout.add_widget(result_label)
            for key, value in data[0].items():
                info_label = Label(text=f"{key}: {value}", font_size='18sp', color=(0.1, 0.1, 0.1, 1), size_hint_y=None, height=30)
                self.result_layout.add_widget(info_label)
        else:
            result_label = Label(text='Food item not found', font_size='20sp', color=(1, 0, 0, 1), size_hint_y=None, height=40)
            self.result_layout.add_widget(result_label)

        self.scrollview.scroll_y = 1  # Scroll to the top of the results

if __name__ == '__main__':
    NutritionApp().run()
