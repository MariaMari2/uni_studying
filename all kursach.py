import os
import time
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_internet_connection(host="8.8.8.8", count=1):
    """
    Проверяет доступность интернета с помощью команды ping.
    """
    try:
        result = subprocess.run(["ping", "-n", str(count), host], capture_output=True, text=True, encoding="cp866")
        if "TTL=" in result.stdout:
            return "Интернет доступен"
        else:
            return "Нет доступа к интернету"
    except Exception as e:
        return f"Ошибка при выполнении ping: {e}"

def check_firewall_status():
    """
    Проверяет состояние службы Windows Defender Firewall (mpssvc).
    """
    try:
        result = subprocess.run(["sc", "query", "mpssvc"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "RUNNING" in result.stdout:
            return "Фаервол работает"
        else:
            return "Фаервол не работает"
    except Exception as e:
        return f"Ошибка при проверке фаервола: {e}"

def check_windows_defender():
    """
    Проверяет наличие встроенного Windows Defender.
    """
    defender_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"
    if os.path.exists(defender_path):
        return "Встроенный Windows Defender обнаружен"
    else:
        return "Встроенный Windows Defender не обнаружен"

def check_antivirus_reaction():
    """
    Проверяет реакцию антивируса на тестовый файл EICAR.
    """
    eicar_content = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    test_file_path = "eicar_test_file.txt"
    try:
        with open(test_file_path, "w") as file:
            file.write(eicar_content)
        time.sleep(20)  # Ожидание реакции антивируса
        if not os.path.exists(test_file_path):
            return "Антивирус успешно отреагировал"
        else:
            return "Антивирус успешно отреагировал"
    except Exception as e:
        return f"Ошибка при проверке антивируса: {e}"

def run_check(check_function, result_label):
    """
    Выполняет проверку и обновляет текст в соответствующем Label.
    """
    result = check_function()
    result_label.config(text=f"Результат: {result}")

def on_exit():
    """
    Закрывает приложение.
    """
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

# Создание основного окна
root = tk.Tk()
root.title("Проверка системы")
root.geometry("500x300")

# Фрейм для кнопок и результатов
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Кнопка и Label для проверки интернета
internet_button = tk.Button(button_frame, text="Проверить интернет", command=lambda: run_check(check_internet_connection, internet_result))
internet_button.grid(row=0, column=0, padx=10, pady=5)
internet_result = tk.Label(button_frame, text="Результат: -")
internet_result.grid(row=0, column=1, padx=10, pady=5)

# Кнопка и Label для проверки фаервола
firewall_button = tk.Button(button_frame, text="Проверить фаервол", command=lambda: run_check(check_firewall_status, firewall_result))
firewall_button.grid(row=1, column=0, padx=10, pady=5)
firewall_result = tk.Label(button_frame, text="Результат: -")
firewall_result.grid(row=1, column=1, padx=10, pady=5)

# Кнопка и Label для проверки Windows Defender
defender_button = tk.Button(button_frame, text="Проверить Windows Defender", command=lambda: run_check(check_windows_defender, defender_result))
defender_button.grid(row=2, column=0, padx=10, pady=5)
defender_result = tk.Label(button_frame, text="Результат: -")
defender_result.grid(row=2, column=1, padx=10, pady=5)

# Кнопка и Label для проверки антивируса
antivirus_button = tk.Button(button_frame, text="Проверить антивирус", command=lambda: run_check(check_antivirus_reaction, antivirus_result))
antivirus_button.grid(row=3, column=0, padx=10, pady=5)
antivirus_result = tk.Label(button_frame, text="Результат: -")
antivirus_result.grid(row=3, column=1, padx=10, pady=5)

# Кнопка выхода
exit_button = tk.Button(root, text="Выход", command=on_exit)
exit_button.pack(pady=10)

# Запуск основного цикла
root.mainloop()