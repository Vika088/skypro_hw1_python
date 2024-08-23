class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def smartphone(self):
        print(f'марка: {self.brand} - модель: {self.model}. номер телефона: '
              f'{self.number}')

    def addSp(self, catalog):
        self.sp = catalog

    def getCatalog(self):
        return self.smartphone()
