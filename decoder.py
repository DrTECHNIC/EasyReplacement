class RussianSubstitutionCipher:
    """
    Класс для дешифровки текста методом простой замены символов.
    Обеспечивает функциональность для работы с русским алфавитом без букв Ё, Й, Ъ.
    """

    def __init__(self):
        """Инициализирует класс с русским алфавитом без букв Ё, Й, Ъ"""
        self.RUSSIAN_LETTERS = list('АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ')
        self.encrypted_text = ''

    def set_encrypted_text(self, text):
        """
        Устанавливает зашифрованный текст для дешифровки.

        Args:
            text (str): Зашифрованный текст, который нужно дешифровать
        """
        self.encrypted_text = text.upper()

    def get_text_lines(self):
        """
        Разбивает текст на строки по 75 символов для удобного отображения.

        Returns:
            list: Список строк по 75 символов каждая
        """
        if not self.encrypted_text:
            return []
        lines = []
        for i in range(0, len(self.encrypted_text), 75):
            lines.append(self.encrypted_text[i:i + 75])
        return lines

    def get_char_groups(self, line):
        """
        Разбивает строку на группы по 5 символов для удобного отображения.

        Args:
            line (str): Строка для разбиения на группы

        Returns:
            list: Список групп по 5 символов каждая
        """
        groups = []
        for i in range(0, len(line), 5):
            groups.append(line[i:i + 5])
        return groups
