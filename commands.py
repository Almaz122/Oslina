akinator_list = ["Однозначно - да", "Скорее всего", "хз", "Скорее - нет", "Однозначно - нет"]
token = ''
count = "counter.txt"


def count_add():
    count_r = open('counter.txt', 'r')
    count_am = count_r.read()
    count_am = int(count_am)
    count_am = count_am + 1
    count_am = str(count_am)
    count_w = open('counter.txt', 'w+')
    count_w.write(count_am)

def count_msg_add():
    count_r = open('counter_msg.txt', 'r')
    count_am = count_r.read()
    count_am = int(count_am)
    count_am = count_am + 1
    count_am = str(count_am)
    count_w = open('counter_msg.txt', 'w+')
    count_w.write(count_am)

start = ('Мои команды:\n'
        '/start ; /help - список команд\n'
        '/chat - ссылка на чат\n'
        '/future - предсказание\n'
        '/dima - рандомное фото димаса\n'
        '/count - статистика бота\n'
        '/penis - размер валыны\n'
        '/iq - количество IQ\n'
        '====================================\n'
        'Создатель бота: Almaz')    


rules = '3 правила:\n1. Без женщин\n2. Пез патокина\n3. 2 админа и 1 модер'
chat = (
    'Наш чат - https://t.me/+opyxxiHP0AxkYjYy'
)

error = (
    "Произошли технические шоколадки, скоро все исправим"
)

oslina = [
    'ослина',
    'Ослина'
]
future = [
    "Скорее всего",
    "Наверняка",
    "Не знаю",
    "Скорее всего нет"
]
