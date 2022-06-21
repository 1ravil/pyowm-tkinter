import os #Импортирование библиотеки для функции перезагрузки программы.
import sys #Импортирование библиотеки для функции перезагрузки программы.
import tkinter as tk #Импортирование библиотеки графического интерфейса tkinter.
from tkinter import * #Импортирование библиотеки графического интерфейса tkinter.
from tkinter import messagebox #Импортирование модуля библиотеки графического интерфейса tkinter Messagebox для функционирования функции вывода ошибки.
import pyowm #Импортирование библиотеки для вывода прогноза погоды.
import pyttsx3 #Импортирование библиотеки для конвертации текста в речь.

window = tk.Tk() #Создаем окно.

window.title("Погода") #Пишем название.

window.geometry('500x500') #Устанавливаем размер окна

window.iconbitmap("D:\Proekt\icon\weather.ico") #Установил иконку для программы.

window.resizable(width=False, height=False) #Фиксация размера окна.

#Установливаем фоновое изображение.
C = Canvas(window, height=500, width=500) #Создаем, вписываем значения размера окна.
filename = PhotoImage(file = "D:\Proekt\icon\wackground\won.png") #Прописываем путь к файлу, в котором содержится наше фоновое изображение
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# Погода, pyowm
owm = pyowm.OWM('fabbffc9f66cad31e15af8ce6f3cbbfc') #Пишем свой бесплатный апи-ключ, который мы взяли с сайта openweathermap.org

def show_error(): #Функция, цель которой показать всплывающее окно в случае ошибки приложения.
    messagebox.showerror(title="Ошибка!", message="Введите название!")

def run(): #Функция, цель которой перезагрузить программу(используется в случае ошибки приложения).
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clicked(): #Пишем функцию для нажатия кнопки.
    city = vrbl.get() #С помощью метода "get" присваиваем значение из пользовательского ввода переменной city.
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(city) #Ищем текущую погоду в переменной city(тоесть тот населенный пункт, который нам нужен и получаем подробную информацию.
        w = observation.weather
        temperature = w.temperature('celsius') #Выставляем значение температуры в "Цельсиях".
        t1=temperature['temp'] #Показатели точной температуры.
        t2=temperature['feels_like'] #Показатели температуры "по ощущениям".
        t3 = w.wind()['speed'] #Скорость ветра.
        t4 = w.pressure['press'] #Влажность.
        t5 = w.humidity #Давление.
        t6 = w.visibility_distance #Видимость.
        box = tk.Frame(master=window, width=500, height=500, bg="light grey") #Создание  виджета, который находится на заднем фоне текста. Цель исключительно эстетическая, чтобы не было "пусто на фоне текста"
        box.place(y=240, x=1) #Местоположение виджета.
        bba = tk.Label(window, text = "Температура в пункте " + str(city) + ":" + " " + str(int(t1)) + "°C" + " \nОщущается как: " + str(int(t2)) + "°C" + "\nСкорость ветра: " + str(t3) + " м/с" + "\n" + "Влажность: " + str(t5) + "%" + "\n" "Давление: " + str(t4) + " мм.рт.ст" + "\n" + "Видимость: " + str(t6) + "  метров", font=("Bahnschrift_SemiLight_Condensed 19"), foreground="black", background="light grey")
        if len(city) <= 4: #Если длина названия нас. пункта меньше или равно 4 буквам, совершается условие:
            bba.place(y=270, x=55) #Стандартное положение, которые мы задали.
        elif len(city) > 4 < 8: #Если длина названия нас. пункта больше 4 букв и меньше 8, совершается условие:
            bba.place(y=270, x=40) #Смещение y на 15 единиц.
        elif len(city) > 8: #Если длина названия нас. пункта больше 4 букв и меньше 8, совершается условие:
            bba.place(y=270, x=0) #Выставляем значение x=0, тоесть смещаем максимально к крайнему левому положению.
    except:
        welcome.destroy() #Cкрываем надпись приветствия.
        btn.destroy() #Скрываем кнопку "Актуальный прогноз".
        vrbl.destroy() #Скрываем строку пользовательского ввода.
        voice.destroy() #Скрываем кнопку "Воспроизвести".
        show_error() #Выводим всплывающее окно с ошибкой с помощью функции show_error.
        run() #Перезапускаем программу с помощью вызова функции run.

def voice(): #Функция для кнопки "Воспроизвести". Конвертирует текст в речь.
    city = vrbl.get() #С помощью метода "get" присваиваем значение из пользовательского ввода переменной city.
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)  #Ищем текущую погоду в переменной city(тоесть тот населенный пункт, который нам нужен и получаем подробную информацию.
    w = observation.weather
    temperature = w.temperature('celsius') #Выставляем значение температуры в "Цельсиях".
    t1 = temperature['temp'] #Показатели точной температуры.
    t2 = temperature['feels_like'] #Показатели температуры "по ощущениям".
    t3 = w.wind()['speed'] #Скорость ветра.
    t4 = w.pressure['press'] #Влажность.
    t5 = w.humidity #Давление.
    t6 = w.visibility_distance #Видимость.
    engine = pyttsx3.init() #Начало работы библиотеки по конвертации текста в речь.
    engine.say("Температура в пункте " + str(city) + ":" + " " + str(int(t1)) + "Градусов цельсия" + "\nОщущается как: " + str(int(t2)) + "Градусов цельсия" + "\nСкорость ветра: " + str(t3) + " метров в секунду" + "\n" + "Влажность: " + str(t5) + "процентов" + "\n" "Давление: " + str(t4) + "миллиметров ртутного столба" + "\n" + "Видимость: " + str(t6) + "  метров")
    engine.runAndWait() #Блокирует все команды, которые совершаются в данный момент. Делается в целях воспроизведения текста.

welcome=tk.Label(window, text="Введите название населенного пункта, чтобы \nузнать актуальный прогноз.", font=("Bahnschrift_SemiLight_Consedensed 16"), foreground="black", background="white") #Создание приветствия.
btn = tk.Button(text="Актуальный прогноз", command=clicked, font = ("Bahnschrift_SemiLight_Condensed 18"), width=34) #Создаем кнопку для продолжения действия, присвоил функцию для нажатия кнопки, добавил саму кнопку.
voice=tk.Button(text="Воспроизвести", command=voice,font=("Bahnscrift_Semilight_Condensed 18"), width=34) #Создаем кнопку для конвертации текста в речь.

vrbl = tk.Entry(window, width=33) #Создаем окно пользовательского ввода, выставляем размер.
vrbl.configure(font=("Bahnschrift SemiLight Condensed", 26)) #Выставляем шрифт окну пользовательского ввода.
vrbl.focus() #Виджет фокуса ввода.

#Местоположения объектов.
welcome.place(x=20, y=1) #Местоположение приветствия, переменной welcome, тоесть надписи "Введите название населенного пункта, чтобы узнать актуальный прогноз."
vrbl.place(x=1, y=65) #Местоположение пользовательского ввода, переменной vrbl.
btn.place(x=8, y=120) #Местоположение кнопки "Актуальный прогноз", переменной btn.
voice.place(x=8, y=170) #Местоположение кнопки "Воспроизвести", переменной voice.

window.mainloop() #Эта команда создает бесконечный цикл окна, окно будет ждать любого взаимодействия, пока не будет закрыто.

