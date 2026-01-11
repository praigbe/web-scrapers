import tkinter as tk
import requests

running = True

def get_weather():
    global running
    city = city_entry.get()
    if city.lower() == "quit":
        running = False
        result_label.config(text="Goodbye!")
        return
    weather = requests.get(f"https://wttr.in/{city}?format=3")
    if weather.status_code == 200:
        result_label.config(text=weather.text)
    else:
        result_label.config(text="failed")

root = tk.Tk()
root.title("Weather Checker")
root.geometry("400x150")

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=20)
city_entry.insert(0, "")

check_btn = tk.Button(root, text="Check Weather", command=get_weather)
check_btn.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

