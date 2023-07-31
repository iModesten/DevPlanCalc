from tkinter import *
from tkinter.ttk import Combobox
import re


def replace_comma(number):
    new_number = ''
    if ',' in number:
        new_number = number.replace(',', '.')
        return new_number
    return number


def clicked():
    result_field.configure(text='...')
    first_number = replace_comma(first_field.get())
    second_number = replace_comma(second_field.get())
    if first_number == '':
        result_field.configure(
            text='Введите первое число...', foreground="red")
    elif second_number == '':
        result_field.configure(
            text='Введите второе число...', foreground="red")
    elif operation.get() == '+':
        result = float(first_number) + float(second_number)
    elif operation.get() == '-':
        result = float(first_number) - float(second_number)
    elif operation.get() == '/':
        result = float(first_number) / float(second_number)
    elif operation.get() == '*':
        result = float(first_number) * float(second_number)
    elif operation.get() == 'Выберите действие...':
        result_field.configure(
            text='Выберите действие для продолжения...', foreground="red")
    if result == int(result):
        result_field.configure(text=int(result), foreground="black")
    else:
        result_field.configure(text=result, foreground="black")


def is_valid_field_one(new_value):
    result = re.match("^[+-]{,1}\d+[,.]?\d+$", new_value) is not None
    if not result:
        first_error_message.set("Введено неверное значение")
    else:
        first_error_message.set("")
    return result


def is_valid_field_two(new_value):
    result = re.match("^[+-]{,1}\d+[,.]?\d+$", new_value) is not None
    if not result:
        second_error_message.set("Введено неверное значение")
    else:
        second_error_message.set("")
    return result


def press_button(event):
    get_result_button.focus_set()


window = Tk()
window.title("DevelopmentPlan - Калькулятор")
window.geometry('305x290')

check_first_field = (window.register(is_valid_field_one), "%P")
check_second_field = (window.register(is_valid_field_two), "%P")
first_error_message = StringVar()
second_error_message = StringVar()

just_first_text = Label(window, width=30, text='Введите первое число:')
just_first_text.grid(column=0, row=0)

first_field = Entry(window, width=36, validate="focusout",
                    validatecommand=check_first_field)
first_field.grid(column=0, row=1, padx=5, pady=0)

error_label_one = Label(
    foreground="red", textvariable=first_error_message, wraplength=250)
error_label_one.grid(column=0, row=2, padx=5, pady=0)

operation = Combobox(window, width=32, state='readonly')
operation['values'] = ("Выберите действие...", '+', '-', '/', '*')
operation.current(0)
operation.grid(column=0, row=3, padx=5, pady=15)

just_second_text = Label(window, width=30, text='Введите второе число:')
just_second_text.grid(column=0, row=4)

second_field = Entry(window, width=36, validate="focusout",
                     validatecommand=check_second_field)
second_field.grid(column=0, row=5, padx=5, pady=5)

error_label_two = Label(
    foreground="red", textvariable=second_error_message, wraplength=250)
error_label_two.grid(column=0, row=6, padx=5, pady=0)

get_result_button = Button(window, text="Результат", command=clicked, width=30)
get_result_button.grid(column=0, row=7, padx=5, pady=15)

get_result_button.bind("<ButtonPress>", press_button)

result_field = Label(window, width=35, text='...', relief="groove")
result_field.grid(column=0, row=8, padx=5, pady=5)

window.resizable(False, False)
window.mainloop()
