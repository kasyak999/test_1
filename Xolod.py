import datetime as dt
from decimal import Decimal

def add(items, title, amount, expiration_date=None):
    if expiration_date != None:
        expiration_date = dt.datetime.strptime(expiration_date, '%Y-%m-%d')
        expiration_date = expiration_date.date()
    if title in items:
        add = { 'amount': amount, 'expiration_date': expiration_date}
        list.append(items[title], add)
    else:
        items[title] = [{ 'amount': amount, 'expiration_date': expiration_date}]

def add_by_note(items, note):
    qwe = str.split(note)
    if str.find(qwe[-1], '-') != -1:
        expiration_date = list.pop(qwe, -1)
    else:
        expiration_date = None
    amount = Decimal(list.pop(qwe, -1))
    title = ' '.join(qwe)
    add(items, title, amount, expiration_date)

def find(items, needle):
    search = list()
    for value in items:
        if str.lower(needle) in str.lower(value):
            list.append(search, value)
    return search

def amount(items, needle):
    qwe = find(items, needle)
    count = 0
    for i in qwe:
        count += sum([ii['amount'] for ii in items[i]])
        print(i)
    return Decimal(count)


def expire(items, in_advance_days=0):
    tec_data = dt.date.today() + dt.timedelta(days=in_advance_days)
    spis = list()
    for key, value in items.items():
        sum = 0
        for i in value:
            if i['expiration_date'] != None:
                if tec_data >= i['expiration_date']:
                    sum += i['amount']
        if sum != 0:
            list.append(spis, (key, sum))
    return spis


goods = dict()

add(goods, 'Хлеб', Decimal('10'), '2024-3-30')
add(goods, 'Хлеб', Decimal('10'), '2024-3-30')
add(goods, 'Хлеб', Decimal('2.5'))
add_by_note(goods, 'Яйца 4 2024-03-15')
add_by_note(goods, 'Вода 4')
# print(find(goods, 'яй'))
print(amount(goods, 'х'))
print(expire(goods, 2))
print(goods)