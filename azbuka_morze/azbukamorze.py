# Азбука морзе, перевожу текст в азбуку
# и наоборот.

class AzbukaMorze:
    """Вся механика тут."""

    def __init__(self, string):
        self.__string = string

    def set_string(self, string):
        """Установка значения
        в строку."""
        self.__string = string

    def get_string(self):
        """Получения значения из строки."""
        return self.__string

    def dict_az_morze(self):
        """Сохраняю словарь c азбукой."""
        azbuka = {
            'а': '•-', 'б': '-•••', 'в': '•--', 'г': '--•', 'д': '-••',
            'е': '•', 'ж': '•••-', 'з': '--••', 'и': '••', 'й': '•---',
            'к': '-•-', 'л': '•-••', 'м': '--', 'н': '-•', 'о': '---',
            'п': '•--•', 'р': '•-•', 'с': '•••', 'т': '-', 'у': '••-',
            'ф': '••-•', 'х': '••••', 'ц': '-•-•', 'ч': '---•',
            'ш': '----', 'щ': '--•-', 'ъ': '--•--', 'ы': '-•--',
            'ь': '-••-', 'э': '••-••', 'ю': '••--', 'я': '•-•-',
            '0': '-----', '1': '•----', '2': '••---', '3': '•••--',
            '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
            '8': '---••', '9': '----•',
            '.': '••••••', ',': '•-•-•-',
            ':': '---•••', ';': '-•-•-',
            '(': '-•--•-', ')': '-•--•-',
            "'": '•----•', '"': '•-••-•',
            '—': '-••••-', '/': '-••-•',
            '?': '••--••', '!': '--••--',
            '@': '•--•-•', ' ': ' ',
        }

        return azbuka
