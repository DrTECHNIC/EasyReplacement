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
