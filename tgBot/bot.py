import telebot as tb
import config as cfg
import utils as ut
import db

bot = tb.TeleBot(cfg.token)


@bot.message_handler(commands=['start', 'help'])
def start(msg):
    ut.Editor.del_buttons_text(msg)
    text = 'Привет, {0}! 👋\n' \
           'Меня зовут {1} 🤝\n' \
           'Я умею конвертировать валюты 😎\n\n' \
           'Доступные команды:\n' \
           '/start или /help - чтобы снова увидеть это сообщение\n' \
           '/values - чтобы увидеть список валют\n' \
           '/add_value - добавить новую валюту\n' \
           '/get_admin - взять права администратора\n' \
           '/get_logs - посмотреть логи ошибок\n' \
           'Хочешь начать?'.format(msg.from_user.first_name, bot.get_me().first_name)
    bot.send_message(msg.chat.id, text, reply_markup=ut.CreateButtons.start_page())


@bot.message_handler(commands=['values'])
def values(msg):
    ut.Editor.del_buttons_text(msg)
    ut.Values.show_values(msg)


@bot.message_handler(commands=['get_admin'])
def get_admin(msg):
    ut.Editor.del_buttons_text(msg)
    if msg.from_user.id not in cfg.admin_list:
        cfg.admin_list.append(msg.from_user.id)
        bot.send_message(msg.chat.id, "Вам присвоен статус администратора")
    else:
        bot.send_message(msg.chat.id, "Вы уже администратор")


@bot.message_handler(commands=['add_value'])
def write_value(msg):
    ut.Editor.del_buttons_text(msg)
    if db.get_len_info(table='currencies', col='value') >= cfg.max_count_currencies:
        bot.send_message(msg.chat.id, "Достигнуто максимальное количество валют")
    elif msg.from_user.id in cfg.admin_list:
        new_currency = bot.send_message(msg.chat.id, "Введите валюту в формате <Название> <Код>\n"
                                                     "(Например: Биткоин BTC)")
        bot.register_next_step_handler(new_currency, ut.Values.add_value)
    else:
        bot.send_message(msg.chat.id, "У вас нет прав 😔")


@bot.message_handler(commands=['get_logs'])
def get_logs(msg):
    ut.Editor.del_buttons_text(msg)
    if msg.from_user.id in cfg.admin_list:
        bot.send_message(msg.chat.id, ut.Logging.get_logs())
    else:
        bot.send_message(msg.chat.id, "У вас нет прав 😔")


@bot.message_handler(commands=['clear_table'])
def ask_clear(msg):
    ut.Editor.del_buttons_text(msg)
    if msg.from_user.id in cfg.clear_list:
        table = bot.send_message(msg.chat.id, 'Название таблицы(logs, currencies, val_for_convert):')
        bot.register_next_step_handler(table, clear_table)


def clear_table(table):
    db.delete_table(table=table.text, admin=True, msg=table)


@bot.message_handler(content_types=['text', ])
def del_buttons(msg):
    ut.Editor.del_buttons_text(msg)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    currencies_list = []
    for v in db.get_info(col='value', table='currencies'):
        currencies_list.append(*v)

    if call.data == "yes":
        ut.Editor.del_buttons(call)
        db.delete_table(table='val_for_convert')
        bot.send_message(call.message.chat.id, 'Выберите валюту, которую конвертируем: ',
                         reply_markup=ut.CreateButtons.choice_value(currencies_list))
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data in currencies_list:
        ut.Editor.del_buttons(call)
        ut.Editor.edit_text(call)
        db.insert_table(table='val_for_convert', col='currency', value=[call.data])

        if db.get_len_info(col='currency', table='val_for_convert') == 1:
            bot.send_message(call.message.chat.id, 'Выберите валюту, в которую конвертируем: ',
                             reply_markup=ut.CreateButtons.choice_value(currencies_list, call))
            bot.answer_callback_query(callback_query_id=call.id)

        if db.get_len_info(col='currency', table='val_for_convert') > 1:
            bot.answer_callback_query(callback_query_id=call.id)
            count = bot.send_message(call.message.chat.id, 'Введите количество:')
            bot.register_next_step_handler(count, result)


def result(count):
    bot.send_message(count.chat.id, ut.Calculation.Result(count))


bot.polling(none_stop=True)
