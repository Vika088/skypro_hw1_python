class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def smartphone(self):
        print('марка', self.brand, '-', 'модель', self.model, '.',
              'номер телефона: ', self.number)

    def addSp(self, catalog):
        self.sp = catalog

    def getCatalog(self):
        return self.smartphone()
