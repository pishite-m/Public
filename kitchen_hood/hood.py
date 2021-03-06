class Hood():
    """Обсновной класс с параметрами вытяжки"""

    def __init__(self):
        """Инициалаизирую параметры"""
        self.ventilation = 12             # Оптимальный воздухообмен за час
        self.reserve_power_factor = 1.6   # коэффициент резервной мощности

    def show_menu(self):
        """Показывает меню для выбора нужной операции."""
        print("\nКалькулятор расчитаывает необходимую куб. кухонной вытяжки.")
        choice = None
        while choice != "0":
            print(
                """
                Меню:
                0 - Выход.
                1 - Площадь известна?
                2 - Посчитать площадь?
                """
            )
            choice = input("Ваш выбор - ")
            if choice == "0":
                print("Спасибо за использование моей программы.")
            elif choice == "1":
                self.result_one()
            elif choice == "2":
                self.result_two()
            else:
                print(f"Простите, но пункта '{choice}' нет в меню.")


    def m_height(self):
        """Высота"""
        try:
            m_height = input('Высота: ')
            m_height = float(m_height)
        except ValueError:
            print("Нельзя вводить буквы, давайте попробуем с начала...")
        else:
            return m_height

    def yes_m2(self):
        """Если известна площадь кухни"""
        try:
            m_m2 = input('Введите сколько квадратов кухня: ')
            m_m2 = float(m_m2)
        except ValueError:
            print("Нельзя вводить буквы, давайте попробуем с начала...")
        else:
            return m_m2

    def no_m2(self):
        """Если не известна квадратура кухни, нужно её высчитать."""
        try:
            m_width = input("Ширина: ")
            m_width = float(m_width)
            m_length = input("Длина: ")
            m_length = float(m_length)
            area_m2 = m_width * m_length
        except ValueError:
            print("Нельзя вводить буквы, давайте попробуем с начала...")
        else:
            return area_m2

    def result_one(self):
        """Итоговый результат, если известна площадь кухни"""
        mresult = self.yes_m2() * self.m_height()\
                      * self.ventilation * self.reserve_power_factor
        print(f"\nНеобходимая мощность мотора в кубах - {mresult}\n")

    def result_two(self):
        """Итоговый результат, при котором не известна площадь кухни."""
        result = self.no_m2() * self.m_height()\
                      * self.ventilation * self.reserve_power_factor
        print(f"\nНеобходимая мощность мотора в кубах - {result}\n")


my = Hood()
my.show_menu()
