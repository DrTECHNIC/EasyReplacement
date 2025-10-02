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
        self.cipher = RussianSubstitutionCipher()
        self.substitutions = {}