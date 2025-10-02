from interface import CipherApp
import tkinter as tk

def main():
    """
    Основная функция приложения.
    Создает главное окно и запускает приложение для дешифровки текста.
    """
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
