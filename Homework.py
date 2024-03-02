import requests
import sqlite3
from datetime import datetime


def get_temperature():
    url = 'https://ua.sinoptik.ua'
    response = requests.get(url)
    if response.status_code == 200:
        temperature = response.text.strip()
        return temperature
    else:
        return 'Немає даних'


try:
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    temperature = get_temperature()

    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS weather
                 (date_time TEXT, temperature TEXT)''')

    c.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (date_time, temperature))

    conn.commit()
    conn.close()

    print("Дані успішно додані до бази даних.")
except Exception as e:
    print("Виникла помилка:", e)
