from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class LaserCalcApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Поля ввода (аналогично вашему коду)
        self.entries = {}
        inputs = [
            ("Мощность лазера (Вт):", "power"),
            ("Глубина проплавления (мм):", "depth"),
            # ... остальные поля
        ]
        
        for text, name in inputs:
            layout.add_widget(Label(text=text))
            self.entries[name] = TextInput(multiline=False)
            layout.add_widget(self.entries[name])
        
        # Кнопка и результат
        btn = Button(text="Рассчитать", size_hint=(1, 0.2))
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)
        
        self.result_label = Label(text="", size_hint=(1, 0.3))
        layout.add_widget(self.result_label)
        
        return layout

    def calculate(self, instance):
        try:
            P = float(self.entries["power"].text)
            D = float(self.entries["depth"].text)
            # ... остальные вычисления (как в вашем коде)
            
            # Ваши формулы
            v_sv = (eta_effective * P) / denominator if denominator != 0 else 0
            # ...
            
            self.result_label.text = (
                f"Скорость сварки: {v_sv:.1f} мм/мин\n"
                f"Угловая скорость: {angular_speed:.1f} °/мин\n"
                f"Скорость проволоки: {v_wire_cm_min:.1f} см/мин"
            )
        except Exception as e:
            self.result_label.text = f"Ошибка: {str(e)}"

if __name__ == "__main__":
    LaserCalcApp().run()