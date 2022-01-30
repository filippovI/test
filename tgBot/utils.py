import telebot as tb
import db
import config as cfg
import requests as rq
from datetime import datetime as dt

bot = tb.TeleBot(cfg.token)


class ConvertionException(Exception):
    pass


# Класс для изменний структры сообщений (Удаление кнопок, редактирования)
class Editor:

    # Удаление кнопок у сообщения выше при написании текста
    @staticmethod
    def del_buttons_text(msg):
        try:
            bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=msg.message_id - 1,
                                          reply_markup=None)
        except Exception:
            pass

    # Удаление кнопок у сообщения выше при нажатии на кнопку
    @staticmethod
    def del_buttons(call):
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=None)

    # Редактирование сообщения
    @staticmethod
    def edit_text(call):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text + " " + call.data)


# Класс для создания кнопок
class CreateButtons:

    # Создание кнопок на стартовом сообщении
    @staticmethod
    def start_page():
        buttons = tb.types.InlineKeyboardMarkup()
        item_yes = tb.types.InlineKeyboardButton(text='✅', callback_data='yes')
        item_no = tb.types.InlineKeyboardButton(text='❌', callback_data='No')
        buttons.add(item_yes, item_no)
        return buttons

    # Создание кнопок у сообщений с выбором валюты
    @staticmethod
    def choice_value(currencies_list, call=None):
        if call:
            currencies_list.remove(call.data)
        buttons = tb.types.InlineKeyboardMarkup()
        button_list = [tb.types.InlineKeyboardButton(text=x, callback_data=x) for x in currencies_list]
        buttons.add(*button_list)
        return buttons


# Класс для расчетов
class Calculation:

    # Результирующий расчет курса
    @staticmethod
    def Result(count):
        try:
            if float(count.text) < 0:
                raise ValueError
        except ValueError as err:
            Logging.write_log(count, 'Неверное значение: {0}'.format(str(count.text)), err)
            return "Неверное значение"
        except Exception as err:
            Logging.write_log(count, 'Неизвестная ошибка', err)
            return "Неизвестная ошибка"
        else:
            url = 'https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms={1}'
            end_value_sheet = []
            for v in db.get_info(table='val_for_convert', col='currency'):
                end_value_sheet.append(*v)
            request = rq.get(url.format(end_value_sheet[0], end_value_sheet[1]))
            request_json = request.json()
            result = "{0} {1} = {2} {3}".format(count.text, end_value_sheet[0],
                                                request_json[end_value_sheet[1]] * float(count.text),
                                                end_value_sheet[1])
            return result


# Класс для работы со списком валют
class Values:

    # Добавление новой валюты
    @staticmethod
    def add_value(msg):
        try:
            new_cur_rub, new_cur_eng = msg.text.split(' ')
        except ValueError:
            bot.send_message(msg.chat.id, 'Неверное значение')
        else:
            db.insert_table(table='currencies', col='rus_value, value', value=[new_cur_rub, new_cur_eng])
            bot.send_message(msg.chat.id, 'Новая валюта добавлена 👍')

    # Вывод списка доступных валют
    @staticmethod
    def show_values(msg):
        text = 'Доступные валюты: \n'
        for v, rv in db.get_info(table='currencies', col='value, rus_value'):
            text = '\n'.join((text, '{0} - {1}'.format(rv, v)))
        bot.reply_to(msg, text)


# Класс для логирования событий
class Logging:

    # Запись логов в БД
    @staticmethod
    def write_log(count, text, err):
        format_time = dt.now()
        db.insert_table(table='logs',
                        col='time,error_handled,error,user',
                        value=[str(format_time.strftime('%d/%m/%Y, %H:%M')),
                               text, str(err), count.from_user.username])

    # Запись логов из БД в text
    @staticmethod
    def get_logs():
        text = ''
        for i in db.get_info(table='logs', col='time,user,error_handled'):
            for v in i:
                text = ''.join((text, str(v) + ' | '))
            text += '\n\n'
        return text
