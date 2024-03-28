# «Холодильник»

Опишите функции add(), add_by_note(), find(), amount() и expire().    
С чего начать    
Не пытайтесь выполнить всю работу одновременно: делайте работу по шагам.     

Объявите словарь goods, добавьте в него пару продуктов — их можно скопировать из приведённых примеров.     

Займитесь функцией add() — научите её добавлять продукты в словарь. Протестируйте работу этой функции и переходите к следующей. На каждом этапе перечитывайте     подсказки и описания, относящиеся к функции, над которой вы работаете.    

Каждую готовую функцию вызовите несколько раз с разными аргументами: с необязательными аргументами и без них, со вчерашней и завтрашней датой (через сто лет — тоже  попробуйте), передавайте в add() и add_by_note() новые продукты и те, что уже есть в словаре goods. 

Тестирование программы — значительная и обязательная часть работы, не пренебрегайте ей.    

Подсказки

    Формат даты можно определить константой DATE_FORMAT = '%Y-%m-%d'.
    
    Функция add(). 
        Проверить, есть ли продукт (title) в словаре items.
        Преобразовать строку в дату с помощью модуля datetime.
        Применить append для добавления словаря с ключами 'amount' и 'expiration_date' в список для конкретного title.
        
    Функция add_by_note(). 
        Разделить строку на части с помощью str.split.
        Определить, является ли последняя часть строки датой.
        Нужную часть строки конвертировать в число типа Decimal
        Оставшуюся часть строки объединить, чтобы получить название продукта: если название состояло из нескольких слов — функция str.split разобъёт его на части.
        Вызвать функцию add(), передав в неё получившиеся данные — название, количество и срок хранения.
    
    Функция find(). 
        Перебрать ключи словаря.
        Применить функцию lower, чтобы провести поиск без учёта регистра.
        Добавить найденные заголовки в результат поиска с помощью функции append.
    
    Функция amount(). 
        Применить функцию find() для получения списка подходящих товаров.
        Суммировать значения amount для вычисления количества каждого найденного товара.
        
    Функция expire().
        Получить текущую дату с помощью datetime.date.today().
        Добавить определённое количество дней к текущей дате.
        Проверить, истекает ли срок годности товара: сравнить его с текущей датой и с датой истечения срока годности.
