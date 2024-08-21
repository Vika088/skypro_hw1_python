from smartphone import Smartphone

sp1 = Smartphone('Apple iPhone', '15 Pro Max', '+79990001122')
sp2 = Smartphone('Samsung', 'Galaxy S24+', '+79991112233')
sp3 = Smartphone('Xiaomi', '14', '+79992223344')
sp4 = Smartphone('Infinix', 'ZERO 30', '+79993334455')
sp5 = Smartphone('HONOR', '90 series', '+79994445566')

catalog = [sp1, sp2, sp3, sp4, sp5]

sp1.addSp(sp1)
sp1.getCatalog()
sp2.addSp(sp2)
sp2.getCatalog()
sp3.addSp(sp3)
sp3.getCatalog()
sp4.addSp(sp4)
sp4.getCatalog()
sp5.addSp(sp5)
sp5.getCatalog()
