# Бот-калькулятор недополученных выгод для рекламного агенства:

Бот запрашивает у клиента его маркетинговые данные.
По авторской формуле агенства считает результаты, которые может получить клиент, воспользовавшись услугами компании.
Информация о пользователях собирается в базе данных users.db и автоматически ипортируется в файл users.xlsx.
Через час после получения результата бот отправляет пользователю напоминание о подписке на телеграмм-канал.

Работает на библиотеке telebot.

### Как запустить бота:

Для начала бота необходимо зарегистрировать и получить его уникальный id, являющийся одновременно и токеном. 
Для этого в Telegram существует специальный бот — @BotFather.

Пишем ему /start и получаем список всех его команд.
Первая и главная — /newbot — отправляем ему и бот просит придумать имя нашему новому боту. Единственное ограничение на имя — оно должно оканчиваться на «bot». В случае успеха BotFather возвращает токен бота и ссылку для быстрого добавления бота в контакты, иначе придется поломать голову над именем.

Клонируем репозитарий:

```
git clone https://github.com/Astapoff/market_bot.git
```

Создаём в корневой директории файл .env с одной переменной:

```
TOKEN=<токен_вашего_бота_полученный_от_BotFather>
```

Устанавливаем библиотеки:

```
pip install pyTelegramBotAPI
```
```
pip install python-dotenv
```
```
pip install pandas
```
```
pip install openpyxl
```


Запустить бота:

```
python3 bot.py
```

Бот работает.


## Автор
Астапов Артём Олегович
Tg: @art_astapoff