import tkinter as tk
from tkinter import ttk
import os
import sys
from decoder import RussianSubstitutionCipher


def resource_path(relative_path):
    """
    Определяет абсолютный путь к ресурсу для работы как в режиме разработки, так и в собранном приложении.

    Args:
        relative_path (str): Относительный путь к ресурсу

    Returns:
        str: Абсолютный путь к ресурсу
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, relative_path)
    if not os.path.exists(path) and hasattr(sys, '_MEIPASS'):
        alt_path = os.path.join(base_path, 'public', os.path.basename(relative_path))
        if os.path.exists(alt_path):
            return alt_path
    return path


class CipherApp:
    """
    Основной класс приложения для дешифровки текста методом простой замены.
    Содержит весь пользовательский интерфейс и логику взаимодействия.
    """

    def __init__(self, root):
        """
        Инициализирует приложение и создает пользовательский интерфейс.

        Args:
            root (tk.Tk): Корневое окно приложения
        """
        self.root = root
        self.root.title("Дешифровка текста методом простой замены")
        self.root.geometry("750x700")
        self.root.resizable(False, False)
        self.set_icon()
        self.cipher = RussianSubstitutionCipher()
        self.substitutions = {}
        self.create_widgets()

    def set_icon(self):
        """Устанавливает иконку приложения из PNG файла."""
        try:
            possible_paths = [
                "./public/icon.png",
                "public/icon.png",
                "icon.png",
                os.path.join(os.path.dirname(__file__), "public", "icon.png"),
                os.path.join(os.path.dirname(__file__), "icon.png"),
            ]
            icon_path = None
            for path in possible_paths:
                full_path = resource_path(path)
                if os.path.exists(full_path):
                    icon_path = full_path
                    break
            if icon_path:
                icon = tk.PhotoImage(file=icon_path)
                self.root.iconphoto(False, icon)
                self.app_icon = icon
                print(f"Иконка установлена: {icon_path}")
            else:
                print("Иконка не найдена ни по одному из путей:")
                for path in possible_paths:
                    full_path = resource_path(path)
                    print(f"  {full_path} - {'существует' if os.path.exists(full_path) else 'не существует'}")
        except Exception as e:
            print(f"Ошибка при установке иконки: {e}")

    def create_widgets(self):
        """Создает и размещает все элементы пользовательского интерфейса."""
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Настройка весов строк и столбцов для растягивания
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=0)  # Поле ввода
        main_frame.grid_rowconfigure(1, weight=3)  # Область дешифровки
        main_frame.grid_rowconfigure(2, weight=1)  # Таблица замен
        main_frame.grid_columnconfigure(0, weight=1)

        # Поле ввода зашифрованного текста
        input_frame = ttk.LabelFrame(main_frame, text="Зашифрованный текст:", padding="5")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        input_frame.grid_columnconfigure(0, weight=1)
        self.text_input = tk.Text(input_frame, height=6, width=90, wrap=tk.WORD)
        self.text_input.pack(fill=tk.BOTH, expand=True)

        # Область отображения дешифрованного текста
        output_frame = ttk.LabelFrame(main_frame, text="Текст для дешифровки:", padding="5")
        output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        output_frame.grid_columnconfigure(0, weight=1)
        self.text_output = tk.Text(output_frame, height=20, width=90, wrap=tk.WORD,
                                   font=("Courier", 10), state=tk.DISABLED)
        self.text_output.pack(fill=tk.BOTH, expand=True)

        # Таблица замен
        substitution_frame = ttk.LabelFrame(main_frame, text="Таблица замен:", padding="5")
        substitution_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        substitution_frame.grid_columnconfigure(0, weight=1)
