from prettytable import PrettyTable

from data import dt

x = PrettyTable()

x.field_names = ['Товар', 'Ринок', 'Ціна в 2007', 'Ціна в 2008',
                 'Ціна в 2011', 'Ціна в 2017', 'зміна за рік']

for i in range (0, len(dt)):

    x.add_rows(
    [
        dt[i]
    ]
    )

def opentabble():
    print('\nАНАЛІЗ ЗМІНИ ЦІН')
    print(x)