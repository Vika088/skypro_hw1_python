from smartphone import Smartphone

sp1 = Smartphone('Apple iPhone', '15 Pro Max', '+79990001122')
sp2 = Smartphone('Samsung', 'Galaxy S24+', '+79991112233')
sp3 = Smartphone('Xiaomi', '14', '+79992223344')
sp4 = Smartphone('Infinix', 'ZERO 30', '+79993334455')
sp5 = Smartphone('HONOR', '90 series', '+79994445566')

catalog = [sp1, sp2, sp3, sp4, sp5]

for phone in catalog:
    phone.smartphone()
