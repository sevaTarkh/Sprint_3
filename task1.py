# import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name(self):
        return self.__name_items
    
    @property
    def number(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if  len(name) == 0 and len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif not name in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    
    def delete_item_from_check(self, name):
        if not name in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        if self.__number_items > 10:
            return sum(total) * 0.9
        return sum(total)
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for i in self.__name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)
                total.append(self.__item_price[i])
        if self.__number_items > 10:
            return sum(total) * 0.2 * 0.9
        return sum(total) * 0.2
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for i in self.__name_items:
            if self.__tax_rate[i] == 10:
                ten_percent_tax.append(i)
                total.append(self.__item_price[i])
        if self.__number_items > 10:
            return sum(total) * 0.1 * 0.9
        return sum(total) * 0.1
    
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) != int:
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        if len(str(telephone_number)) == 10:
            return f'+7({str(telephone_number)[:3]}){str(telephone_number)[3:6]}-{str(telephone_number)[6:8]}-{str(telephone_number)[8:10]}'
        else:
             return f'+7({str(telephone_number)}'

YO = OnlineSalesRegisterCollector()
YO.add_item_to_cheque('чипсы')
YO.add_item_to_cheque('чипсы')
YO.add_item_to_cheque('молоко')
YO.add_item_to_cheque('кола')
YO.delete_item_from_check('чипсы')

print(YO.name)
print(YO.check_amount())
print(YO.total_tax())
print(YO.get_telephone_number(9852223456))