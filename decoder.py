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

    def get_decrypted_char(self, char, substitutions):
        """
        Возвращает расшифрованный символ или подчеркивание, если замена не определена.

        Args:
            char (str): Символ для дешифровки
            substitutions (dict): Словарь подстановок символов

        Returns:
            str: Расшифрованный символ или '_', если замена не определена
        """
        if char == ' ':
            return ' '
        return substitutions.get(char.upper(), '_')

    def get_original_char(self, char, substitutions):
        """
        Возвращает оригинальный символ или пробел для уже расшифрованных символов.

        Args:
            char (str): Символ для проверки
            substitutions (dict): Словарь подстановок символов

        Returns:
            str: Оригинальный символ или пробел, если символ уже расшифрован
        """
        if char == ' ':
            return ' '
        return ' ' if char.upper() in substitutions else char

    def get_encrypted_letters(self):
        """
        Извлекает уникальные зашифрованные буквы из текста.

        Returns:
            list: Отсортированный список уникальных букв, присутствующих в тексте
        """
        letters = set()
        for char in self.encrypted_text:
            if char in self.RUSSIAN_LETTERS:
                letters.add(char)
        return sorted(list(letters))

    def get_decrypted_display(self, substitutions):
        """
        Формирует отформатированное отображение дешифрованного текста.

        Args:
            substitutions (dict): Словарь подстановок символов

        Returns:
            str: Отформатированный текст с дешифрованными и оригинальными символами
        """
        lines = self.get_text_lines()
        if not lines:
            return "Введите зашифрованный текст для отображения"
        result = []
        for line in lines:
            groups = self.get_char_groups(line)

            # Строка с расшифрованными символами
            decrypted_line = []
            for group in groups:
                decrypted_group = ''.join([self.get_decrypted_char(char, substitutions) for char in group])
                decrypted_line.append(decrypted_group)
            result.append(' '.join(decrypted_line))

            # Строка с оригинальными символами
            original_line = []
            for group in groups:
                original_group = ''.join([self.get_original_char(char, substitutions) for char in group])
                original_line.append(original_group)
            result.append(' '.join(original_line))
        return '\n'.join(result)
