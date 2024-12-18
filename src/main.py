import flet as ft
import math  # 引入數學模組，處理科學計算

class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=24)

        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.expand = 1
        self.content = self.ui()

    def ui(self):
        ui = ft.Column(
            controls=[
                ft.Row(
                    expand=True,
                    controls=[self.result],
                    alignment="end"
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="AC", on_click=self.button_clicked, data="clear"),
                        ft.Button(text="+/-", on_click=self.button_clicked, data="negate"),
                        ft.Button(text="%", on_click=self.button_clicked, data="percent"),
                        ft.Button(text="÷", on_click=self.button_clicked, data="div"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="7", on_click=self.button_clicked, data="7"),
                        ft.Button(text="8", on_click=self.button_clicked, data="8"),
                        ft.Button(text="9", on_click=self.button_clicked, data="9"),
                        ft.Button(text="×", on_click=self.button_clicked, data="mul"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="4", on_click=self.button_clicked, data="4"),
                        ft.Button(text="5", on_click=self.button_clicked, data="5"),
                        ft.Button(text="6", on_click=self.button_clicked, data="6"),
                        ft.Button(text="-", on_click=self.button_clicked, data="sub"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="1", on_click=self.button_clicked, data="1"),
                        ft.Button(text="2", on_click=self.button_clicked, data="2"),
                        ft.Button(text="3", on_click=self.button_clicked, data="3"),
                        ft.Button(text="+", on_click=self.button_clicked, data="add"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="0", expand=1, on_click=self.button_clicked, data="0"),
                        ft.Button(text=".", on_click=self.button_clicked, data="."),
                        ft.Button(text="⌫", on_click=self.button_clicked, data="backspace"),
                        ft.Button(text="=", on_click=self.button_clicked, data="calculate"),
                    ]
                ),
                # 這一行是科學計算器的部分
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="sin", on_click=self.button_clicked, data="sin"),
                        ft.Button(text="cos", on_click=self.button_clicked, data="cos"),
                        ft.Button(text="tan", on_click=self.button_clicked, data="tan"),
                        ft.Button(text="log", on_click=self.button_clicked, data="log"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="x²", on_click=self.button_clicked, data="square"),
                        ft.Button(text="√", on_click=self.button_clicked, data="sqrt"),
                        ft.Button(text="1/x", on_click=self.button_clicked, data="inverse"),
                        ft.Button(text="π", on_click=self.button_clicked, data="pi"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Button(text="x³", on_click=self.button_clicked, data="cube"),
                        ft.Button(text="ln", on_click=self.button_clicked, data="ln"),
                    ]
                )
            ]
        )
        return ui

    def button_clicked(self, e):
        action = e.control.data

        if action.isdigit() or action == ".":
            if self.result.value == "0" or self.new_operand:
                self.result.value = action
                self.new_operand = False
            else:
                self.result.value += action
        elif action in ["add", "sub", "mul", "div"]:
            self.operator = action
            self.operand1 = float(self.result.value)
            self.new_operand = True
        elif action == "calculate":
            if self.operator and self.result.value:
                self.result.value = str(self.calculate(self.operand1, float(self.result.value), self.operator))
                self.reset()
        elif action == "clear":
            self.result.value = "0"
            self.reset()
        elif action == "negate":
            self.result.value = str(float(self.result.value) * -1)
        elif action == "percent":
            self.result.value = str(float(self.result.value) / 100)
        elif action == "backspace":
            self.result.value = self.result.value[:-1] if len(self.result.value) > 1 else "0"
        elif action == "sin":
            self.result.value = str(math.sin(math.radians(float(self.result.value))))
        elif action == "cos":
            self.result.value = str(math.cos(math.radians(float(self.result.value))))
        elif action == "tan":
            self.result.value = str(math.tan(math.radians(float(self.result.value))))
        elif action == "log":
            if float(self.result.value) > 0:
                self.result.value = str(math.log10(float(self.result.value)))
            else:
                self.result.value = "Error"
        elif action == "ln":
            if float(self.result.value) > 0:
                self.result.value = str(math.log(float(self.result.value)))
            else:
                self.result.value = "Error"
        elif action == "square":
            self.result.value = str(float(self.result.value) ** 2)
        elif action == "cube":
            self.result.value = str(float(self.result.value) ** 3)
        elif action == "sqrt":
            if float(self.result.value) >= 0:
                self.result.value = str(math.sqrt(float(self.result.value)))
            else:
                self.result.value = "Error"
        elif action == "inverse":
            if float(self.result.value) != 0:
                self.result.value = str(1 / float(self.result.value))
            else:
                self.result.value = "Error"
        elif action == "pi":
            self.result.value = str(math.pi)
        
        self.update()

    def calculate(self, operand1, operand2, operator):
        try:
            if operator == "add":
                return operand1 + operand2
            elif operator == "sub":
                return operand1 - operand2
            elif operator == "mul":
                return operand1 * operand2
            elif operator == "div":
                if operand2 == 0:
                    return "Error"
                return operand1 / operand2
        except Exception as e:
            print(f"Error calculating: {e}")
            return "Error"

    def reset(self):
        self.operator = None
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "科學計算器"
    page.bgcolor = "#6C6C6C"
    page.window_width = 400
    page.window_height = 650
    calc = CalculatorApp()
    page.add(calc)

ft.app(target=main)
