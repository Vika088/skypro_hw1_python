from address import Address
from mailing import Mailing

adr_to = Address('170100', 'Tver', 'Svobodniy alley', '7', 'placement')
adr_from = Address('170100', 'Tver', 'Tverskoy avenue', '18', 'office')

mail1 = Mailing(adr_to, adr_from, 666, '456123')
print(mail1)
