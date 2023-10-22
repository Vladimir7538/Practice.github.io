< !DOCTYPE
html >
< html >
< body >
< h1 >

import telebot
from telebot import types  # для указание типов

api_token = '6506210150:AAEOs6uiM7ejODQuCIw4O10UtRZ_GM1WlkE'
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    sent = bot.send_message(message.chat.id, text="Привет {first}, ты проходищь практику у нас?"
                            .format(first=message.from_user.first_name),
                            reply_markup=markup)
    bot.register_next_step_handler(sent, func2)


def func2(message):
    if message.text == "Да":
        deli = telebot.types.ReplyKeyboardRemove()
        sent = bot.send_message(message.chat.id, text="Отлично вводи пароль и начнем", reply_markup=deli)
        bot.register_next_step_handler(sent, func3)

    elif message.text == "Нет":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад")
        btn2 = types.KeyboardButton("Узнать о стажировках")
        markup1.add(btn1, btn2)

        sent = bot.send_message(message.chat.id, text="Информацию о стажировках ты сможешь найти по кнопке помощь",
                                reply_markup=markup1)
        bot.register_next_step_handler(sent, func3)

    elif message.text == "/start":
        start(message)

    else:
        bot.send_message(message.chat.id, text="используй кнопки")
        start(message)


def func3(message):
    if message.text == "Узнать о стажировках":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Кнопка1", url="https://eog.gazprom.ru/")
        btn2 = types.InlineKeyboardButton("Кнопка2", url="https://www.gazprom.ru/")
        markup.add(btn1, btn2)
        sent = bot.send_message(message.chat.id, text="Информацию о стажировках ты сможешь найти по кнопкам ниже",
                                reply_markup=markup)
        bot.register_next_step_handler(sent, func3)

    elif message.text == "Назад":
        start(message)

    elif message.text == "/start":
        start(message)

    elif message.text == "1234":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Поехали")
        markup.add(btn1)
        sent = bot.send_message(message.chat.id, text="Отлично давай начнем", reply_markup=markup)
        bot.register_next_step_handler(sent, func4)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func3)


def func4(message):
    if message.text == "Поехали":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Производственная практика")
        btn2 = types.KeyboardButton("Ознакомительная практика")
        btn3 = types.KeyboardButton("Преддипломная практика")
        btn4 = types.KeyboardButton("Вернуться в начало")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какую практику вы проходите?", reply_markup=markup)
        bot.register_next_step_handler(sent, func5)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func4)


def func5(message):
    if message.text == "Производственная практика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Предстоящие мероприятия")
        btn2 = types.KeyboardButton("Работа на преприятии")
        btn3 = types.KeyboardButton("Контакты руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2, btn3)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func6)

    elif message.text == "Ознакомительная практика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Предстоящие мероприятия")
        btn2 = types.KeyboardButton("Работа на преприятии")
        btn3 = types.KeyboardButton("Контакты руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2, btn3)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func7)

    elif message.text == "Преддипломная практика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Список возможных тем для дипломных работ")
        btn2 = types.KeyboardButton("Контакты научных руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2)

        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func8)

    elif message.text == "Вернуться в начало":
        start(message)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func5)


def func6(message):
    if message.text == "Предстоящие мероприятия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Лекции и семинары")
        btn3 = types.KeyboardButton("Конференции и хакатоны")
        btn4 = types.KeyboardButton("Олимпиады и кейс-чемпионаты")
        btn5 = types.KeyboardButton("Назад")
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        sent = bot.send_message(message.chat.id, text="Какие мероприятия вас интересуют?", reply_markup=markup)
        bot.register_next_step_handler(sent, func9)

    elif message.text == "Работа на преприятии":
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с тем, на каких предприятиях и в течение каких сроков вы сможете поработать в рамках практики")
        bot.register_next_step_handler(sent, func6)

    elif message.text == "Контакты руководителей":
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с контактами руководителей вашей практики")
        bot.register_next_step_handler(sent, func6)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Производственная практика")
        btn2 = types.KeyboardButton("Ознакомительная практика")
        btn3 = types.KeyboardButton("Преддипломная практика")
        btn4 = types.KeyboardButton("Вернуться в начало")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какой вид практики вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func5)

    elif message.text == "Помощь":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Кнопка1", url="https://eog.gazprom.ru/")
        btn2 = types.InlineKeyboardButton("Кнопка2", url="https://www.gazprom.ru/")
        markup.add(btn1, btn2)
        sent = bot.send_message(message.chat.id, text="Информацию о стажировках ты сможешь найти тут",
                                reply_markup=markup)
        bot.register_next_step_handler(sent, func6)

    elif message.text == "FAQ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        btn5 = types.KeyboardButton("5")
        btn6 = types.KeyboardButton("6")
        btn7 = types.KeyboardButton("7")
        btn8 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4)
        markup.add(btn5, btn6, btn7)
        markup.add(btn8)
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с ответами на наиболее часто задаваемые вопросы по практике",
                                reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="1)Кто может поступить на стажировку?\n"
                              "2)Что писать в резюме, если у меня нет опыта работы?\n"
                              "3)Смогу ли я совмещать стажировку с основной учебой?\n"
                              "4)Могу ли я остаться работать в компании после окончания стажировки?\n"
                              "5)Когда начинается практика?\n"
                              "6)Где можно узнать своего руководителя практики от академии?\n"
                              "7)Какие обязанности должен выполнять руководитель практики?\n")
        bot.register_next_step_handler(sent, func9)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func6)


def func7(message):
    if message.text == "Предстоящие мероприятия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Лекции и семинары")
        btn3 = types.KeyboardButton("Конференции и хакатоны")
        btn4 = types.KeyboardButton("Олимпиады и кейс-чемпионаты")
        btn5 = types.KeyboardButton("Назад")
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        sent = bot.send_message(message.chat.id, text="Какие мероприятия вас интересуют?", reply_markup=markup)
        bot.register_next_step_handler(sent, func10)

    elif message.text == "Работа на преприятии":
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с тем, на каких предприятиях и в течение каких сроков вы сможете поработать в рамках практики")
        bot.register_next_step_handler(sent, func7)

    elif message.text == "Контакты руководителей":
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с контактами руководителей вашей практики")
        bot.register_next_step_handler(sent, func7)

    elif message.text == "FAQ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        btn5 = types.KeyboardButton("5")
        btn6 = types.KeyboardButton("6")
        btn7 = types.KeyboardButton("7")
        btn8 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4)
        markup.add(btn5, btn6, btn7)
        markup.add(btn8)
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с ответами на наиболее часто задаваемые вопросы по практике",
                                reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="1)Кто может поступить на стажировку?\n"
                              "2)Что писать в резюме, если у меня нет опыта работы?\n"
                              "3)Смогу ли я совмещать стажировку с основной учебой?\n"
                              "4)Могу ли я остаться работать в компании после окончания стажировки?\n"
                              "5)Когда начинается практика?\n"
                              "6)Где можно узнать своего руководителя практики от академии?\n"
                              "7)Какие обязанности должен выполнять руководитель практики?\n")
        bot.register_next_step_handler(sent, func10)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Производственная практика")
        btn2 = types.KeyboardButton("Ознакомительная практика")
        btn3 = types.KeyboardButton("Преддипломная практика")
        btn4 = types.KeyboardButton("Вернуться в начало")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какой вид практики вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func5)

    elif message.text == "Помощь":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Кнопка1", url="https://eog.gazprom.ru/")
        btn2 = types.InlineKeyboardButton("Кнопка2", url="https://www.gazprom.ru/")
        markup.add(btn1, btn2)
        sent = bot.send_message(message.chat.id, text="Информацию о стажировках ты сможешь найти тут",
                                reply_markup=markup)
        bot.register_next_step_handler(sent, func7)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func7)


def func8(message):
    if message.text == "Список возможных тем для дипломных работ":
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться со списком возможных тем для дипломных работ, а также узнать, кто из научных руководителей занимается каждой из этих тем")
        bot.register_next_step_handler(sent, func8)

    elif message.text == "Контакты научных руководителей":
        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с контактами руководителей вашей практики")
        bot.register_next_step_handler(sent, func8)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Производственная практика")
        btn2 = types.KeyboardButton("Ознакомительная практика")
        btn3 = types.KeyboardButton("Преддипломная практика")
        btn4 = types.KeyboardButton("Вернуться в начало")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какой вид практики вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func5)

    elif message.text == "Помощь":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Кнопка1", url="https://eog.gazprom.ru/")
        btn2 = types.InlineKeyboardButton("Кнопка2", url="https://www.gazprom.ru/")
        markup.add(btn1, btn2)
        sent = bot.send_message(message.chat.id, text="Информацию о стажировках ты сможешь найти тут",
                                reply_markup=markup)
        bot.register_next_step_handler(sent, func8)

    elif message.text == "FAQ":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        btn5 = types.KeyboardButton("5")
        btn6 = types.KeyboardButton("6")
        btn7 = types.KeyboardButton("7")
        btn8 = types.KeyboardButton("8")
        btn9 = types.KeyboardButton("9")
        btn10 = types.KeyboardButton("10")
        btn11 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        markup.add(btn11)

        sent = bot.send_message(message.chat.id,
                                text="Здесь вы сможете ознакомиться с ответами на наиболее часто задаваемые вопросы по практике",
                                reply_markup=markup)

        bot.send_message(message.chat.id,

                         text="1)Кто может поступить на стажировку?\n"

                              "2)Что писать в резюме, если у меня нет опыта работы?\n"

                              "3)Смогу ли я совмещать стажировку с основной учебой?\n"

                              "4)Могу ли я остаться работать в компании после окончания стажировки?\n"

                              "5)Когда начинается практика?\n"

                              "6)Где можно узнать своего руководителя практики от академии?\n"

                              "7)Какие обязанности должен выполнять руководитель практики?\n"

                              "8)Кто осуществляет руководство преддипломной практики?\n"

                              "9)Какие формы отчетности по преддипломной практике необходимы для успешной защиты?\n"

                              "10)Как проходит защита преддипломной практики?")

        bot.register_next_step_handler(sent, func10_5)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func8)


def func9(message):
    if message.text == "Лекции и семинары":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Марафон лекций от экспертов «Газпром нефти»")
        btn2 = types.KeyboardButton("Газпром нефть канал на ютубе")
        btn3 = types.KeyboardButton("Научно-Технический Центр канал на ютубе")
        btn4 = types.KeyboardButton("Газпром образование")
        btn5 = types.KeyboardButton("Газпром молодым специалистам")
        btn7 = types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(btn7)
        sent = bot.send_message(message.chat.id, text="Выбери олимпиаду которая тебя интересует", reply_markup=markup)
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Конференции и хакатоны":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("X Молодежная международная научно-практическая конференция")
        btn2 = types.KeyboardButton("Волонтерский корпус Петербургского международного газового форума")
        btn3 = types.KeyboardButton("Форсайт-игра Дирекции по газу и энергетике")
        btn4 = types.KeyboardButton("Российские студенческие отряды")
        btn7 = types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn7)
        sent = bot.send_message(message.chat.id, text="Выбери олимпиаду которая тебя интересует", reply_markup=markup)
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Олимпиады и кейс-чемпионаты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("IT-чемпионат нефтяной отрасли")
        btn2 = types.KeyboardButton("Международный инженерный чемпионат «CASE-IN»")
        btn3 = types.KeyboardButton("GPN Intelligence cup")
        btn4 = types.KeyboardButton("Стажировка “ИТ-старт”")
        btn5 = types.KeyboardButton('Кейс-чемпионат "Pro нефть"')
        btn6 = types.KeyboardButton("Студенческая олимпиада «Газпром»")
        btn7 = types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn7)
        sent = bot.send_message(message.chat.id, text="Выбери олимпиаду которая тебя интересует", reply_markup=markup)
        bot.register_next_step_handler(sent, func11)

    elif message.text == "1":
        sent = bot.send_message(message.chat.id,
                                text="Студент 4 курса бакалавриата, 4-5 курса специалитета или 1-2 курса магистратуры, который имеет средний балл диплома (GPA) не ниже 4 и готов к переезду.\n"
                                     "Знание английского на уровне B1 и выше, уверенное владение Excel и Power Point будет вашим преимуществом.")
        bot.register_next_step_handler(sent, func9)
    elif message.text == "2":
        sent = bot.send_message(message.chat.id,
                                text="Ты можешь указать практики и стажировки, учебные проекты, рассказать об участии в научных конференциях и форумах, кейс-чемпионатах, волонтерских проектах, обучении на дополнительных курсах и т.д. Нам важно оценить уровень твоих теоретических знаний, а также понять, какими навыками, умениями и личностными чертами ты обладаешь и насколько они релевантные для нас. Помни, кроме опыта для работодателя очень важна мотивация! ")
        bot.register_next_step_handler(sent, func9)
    elif message.text == "3":
        sent = bot.send_message(message.chat.id, text="Да, как правило, такая возможность есть.")
        bot.register_next_step_handler(sent, func9)
    elif message.text == "4":
        sent = bot.send_message(message.chat.id,
                                text="Зарекомендовавшим себя стажерам «компания» будет рада предложить поучаствовать в конкурсе на открывающиеся стартовые вакансии.")
        bot.register_next_step_handler(sent, func9)
    elif message.text == "5":
        sent = bot.send_message(message.chat.id,
                                text="Набор на стажировки, как и старт стажировок, происходит в течение всего года.")
        bot.register_next_step_handler(sent, func9)
    elif message.text == "6":
        sent = bot.send_message(message.chat.id,
                                text="Наставник назначается в момент издания приказа о назначении практики, заранее узнать кто именно наставник студента(-ов) невозможно.")
        bot.register_next_step_handler(sent, func9)
    elif message.text == "7":
        sent = bot.send_message(message.chat.id,
                                text="Согласовывает индивидуальные задания для обучающихся, выполняемые в период практики, определяет содержание и планируемые результаты практики;\n"
                                     "Организует участие обучающихся в выполнении определенных видов работ, связанных с будущей профессиональной деятельностью\n"
                                     "Обеспечивает обучающимся безопасные условия прохождения практики, отвечающие санитарным правилам и требованиям охраны труда;\n"
                                     "Проводит инструктаж обучающихся по ознакомлению с требованиями охраны труда, техники безопасности, пожарной безопасности, а также правилами внутреннего трудового распорядка;\n"
                                     "Составляет подробную характеристику на практиканта по окончании практики.")
        bot.register_next_step_handler(sent, func9)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Предстоящие мероприятия")
        btn2 = types.KeyboardButton("Работа на преприятии")
        btn3 = types.KeyboardButton("Контакты руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2, btn3)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func6)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func9)


def func10(message):
    if message.text == "Лекции и семинары":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("Марафон лекций от экспертов «Газпром нефти»")

        btn2 = types.KeyboardButton("Газпром нефть канал на ютубе")

        btn3 = types.KeyboardButton("Научно-Технический Центр канал на ютубе")

        btn4 = types.KeyboardButton("Газпром образование")

        btn5 = types.KeyboardButton("Газпром молодым специалистам")

        btn7 = types.KeyboardButton("Назад")

        markup.add(btn1)

        markup.add(btn2)

        markup.add(btn3)

        markup.add(btn4)

        markup.add(btn5)

        markup.add(btn7)

        sent = bot.send_message(message.chat.id, text="Выбери что тебя интересует", reply_markup=markup)

        bot.register_next_step_handler(sent, func12)

    elif message.text == "Конференции и хакатоны":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("X Молодежная международная научно-практическая конференция")

        btn2 = types.KeyboardButton("Волонтерский корпус Петербургского международного газового форума")

        btn3 = types.KeyboardButton("Форсайт-игра Дирекции по газу и энергетике")

        btn4 = types.KeyboardButton("Российские студенческие отряды")

        btn7 = types.KeyboardButton("Назад")

        markup.add(btn1)

        markup.add(btn2)

        markup.add(btn3)

        markup.add(btn4)

        markup.add(btn7)

        sent = bot.send_message(message.chat.id, text="Выбери что тебя интересует", reply_markup=markup)

        bot.register_next_step_handler(sent, func12)


    elif message.text == "Олимпиады и кейс-чемпионаты":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("IT-чемпионат нефтяной отрасли")

        btn2 = types.KeyboardButton("Международный инженерный чемпионат «CASE-IN»")

        btn3 = types.KeyboardButton("GPN Intelligence cup")

        btn4 = types.KeyboardButton("Стажировка “ИТ-старт”")

        btn5 = types.KeyboardButton('Кейс-чемпионат "Pro нефть"')

        btn6 = types.KeyboardButton("Студенческая олимпиада «Газпром»")

        btn7 = types.KeyboardButton("Назад")

        markup.add(btn1)

        markup.add(btn2)

        markup.add(btn3)

        markup.add(btn4)

        markup.add(btn5)

        markup.add(btn6)

        markup.add(btn7)

        sent = bot.send_message(message.chat.id, text="Выбери что тебя интересует", reply_markup=markup)

        bot.register_next_step_handler(sent, func12)

    elif message.text == "1":
        sent = bot.send_message(message.chat.id,
                                text="Студент 4 курса бакалавриата, 4-5 курса специалитета или 1-2 курса магистратуры, который имеет средний балл диплома (GPA) не ниже 4 и готов к переезду.\n"
                                     "Знание английского на уровне B1 и выше, уверенное владение Excel и Power Point будет вашим преимуществом.")
        bot.register_next_step_handler(sent, func10)
    elif message.text == "2":
        sent = bot.send_message(message.chat.id,
                                text="Ты можешь указать практики и стажировки, учебные проекты, рассказать об участии в научных конференциях и форумах, кейс-чемпионатах, волонтерских проектах, обучении на дополнительных курсах и т.д. Нам важно оценить уровень твоих теоретических знаний, а также понять, какими навыками, умениями и личностными чертами ты обладаешь и насколько они релевантные для нас. Помни, кроме опыта для работодателя очень важна мотивация! ")
        bot.register_next_step_handler(sent, func10)
    elif message.text == "3":
        sent = bot.send_message(message.chat.id, text="Да, как правило, такая возможность есть.")
        bot.register_next_step_handler(sent, func10)
    elif message.text == "4":
        sent = bot.send_message(message.chat.id,
                                text="Зарекомендовавшим себя стажерам «компания» будет рада предложить поучаствовать в конкурсе на открывающиеся стартовые вакансии.")
        bot.register_next_step_handler(sent, func10)
    elif message.text == "5":
        sent = bot.send_message(message.chat.id,
                                text="Набор на стажировки, как и старт стажировок, происходит в течение всего года.")
        bot.register_next_step_handler(sent, func10)
    elif message.text == "6":
        sent = bot.send_message(message.chat.id,
                                text="Наставник назначается в момент издания приказа о назначении практики, заранее узнать кто именно наставник студента(-ов) невозможно.")
        bot.register_next_step_handler(sent, func10)
    elif message.text == "7":
        sent = bot.send_message(message.chat.id,
                                text="Согласовывает индивидуальные задания для обучающихся, выполняемые в период практики, определяет содержание и планируемые результаты практики;\n"
                                     "Организует участие обучающихся в выполнении определенных видов работ, связанных с будущей профессиональной деятельностью\n"
                                     "Обеспечивает обучающимся безопасные условия прохождения практики, отвечающие санитарным правилам и требованиям охраны труда;\n"
                                     "Проводит инструктаж обучающихся по ознакомлению с требованиями охраны труда, техники безопасности, пожарной безопасности, а также правилами внутреннего трудового распорядка;\n"
                                     "Составляет подробную характеристику на практиканта по окончании практики.")
        bot.register_next_step_handler(sent, func10)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Предстоящие мероприятия")
        btn2 = types.KeyboardButton("Работа на преприятии")
        btn3 = types.KeyboardButton("Контакты руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2, btn3)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func7)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func10)


def func10_5(message):
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Список возможных тем для дипломных работ")
        btn2 = types.KeyboardButton("Контакты научных руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2)

        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func8)

    elif message.text == "1":
        sent = bot.send_message(message.chat.id,
                                text="Студент 4 курса бакалавриата, 4-5 курса специалитета или 1-2 курса магистратуры, который имеет средний балл диплома (GPA) не ниже 4 и готов к переезду.\n"
                                     "Знание английского на уровне B1 и выше, уверенное владение Excel и Power Point будет вашим преимуществом.")
        bot.register_next_step_handler(sent, func10_5)
    elif message.text == "2":
        sent = bot.send_message(message.chat.id,
                                text="Ты можешь указать практики и стажировки, учебные проекты, рассказать об участии в научных конференциях и форумах, кейс-чемпионатах, волонтерских проектах, обучении на дополнительных курсах и т.д. Нам важно оценить уровень твоих теоретических знаний, а также понять, какими навыками, умениями и личностными чертами ты обладаешь и насколько они релевантные для нас. Помни, кроме опыта для работодателя очень важна мотивация! ")
        bot.register_next_step_handler(sent, func10_5)
    elif message.text == "3":
        sent = bot.send_message(message.chat.id, text="Да, как правило, такая возможность есть.")
        bot.register_next_step_handler(sent, func10_5)
    elif message.text == "4":
        sent = bot.send_message(message.chat.id,
                                text="Зарекомендовавшим себя стажерам «компания» будет рада предложить поучаствовать в конкурсе на открывающиеся стартовые вакансии.")
        bot.register_next_step_handler(sent, func10_5)
    elif message.text == "5":
        sent = bot.send_message(message.chat.id,
                                text="Набор на стажировки, как и старт стажировок, происходит в течение всего года.")
        bot.register_next_step_handler(sent, func10_5)
    elif message.text == "6":
        sent = bot.send_message(message.chat.id,
                                text="Наставник назначается в момент издания приказа о назначении практики, заранее узнать кто именно наставник студента(-ов) невозможно.")
        bot.register_next_step_handler(sent, func10_5)
    elif message.text == "7":
        sent = bot.send_message(message.chat.id,
                                text="Согласовывает индивидуальные задания для обучающихся, выполняемые в период практики, определяет содержание и планируемые результаты практики;\n"
                                     "Организует участие обучающихся в выполнении определенных видов работ, связанных с будущей профессиональной деятельностью\n"
                                     "Обеспечивает обучающимся безопасные условия прохождения практики, отвечающие санитарным правилам и требованиям охраны труда;\n"
                                     "Проводит инструктаж обучающихся по ознакомлению с требованиями охраны труда, техники безопасности, пожарной безопасности, а также правилами внутреннего трудового распорядка;\n"
                                     "Составляет подробную характеристику на практиканта по окончании практики.")
        bot.register_next_step_handler(sent, func10_5)

    elif message.text == "8":
        sent = bot.send_message(message.chat.id,
                                text="Руководителем практики от Академии является научный руководитель преддипломной практики, который назначается из числа профессоров, доцентов выпускающей кафедры. Решение об утверждении научного руководителя фиксируется в протоколе заседания кафедры.\n"
                                     "При назначении научного руководителя практики учитываются пожелания обучающихся, они могут присутствовать на заседании кафедры при назначении научных руководителей.\n"
                                     "Научный руководитель преддипломной практики:\n"
                                     "•	разрабатывает индивидуальные задания для обучающихся, выполняемые в период практики;\n"
                                     "•	оказывает методическую помощь при выполнении индивидуальных заданий, а также при сборе материалов к выпускной квалификационной работе в ходе преддипломной практики;\n"
                                     "•	осуществляет сбор материалов практики от обучающихся и их проверку на соответствие требованиям программы практики;\n"
                                     "•	оценивает результаты прохождения практики обучающимися.")
        bot.register_next_step_handler(sent, func10_5)

    elif message.text == "9":
        sent = bot.send_message(message.chat.id,
                                text="По окончании преддипломной практики обучающийся составляет отчет о работе, проведенной в период практики, который отражает обстоятельные выводы практиканта о проделанной работе.")
        bot.register_next_step_handler(sent, func10_5)

    elif message.text == "10":
        sent = bot.send_message(message.chat.id,
                                text="В ходе защиты учитывается качество и полнота представленных материалов, содержание представленного отчета. Оценка учитывает качество представленных отчетных материалов и отзывы научного руководителя.\n"
                                     "Обучающиеся, не выполнившие программу преддипломной практики, не допускаются к государственной итоговой аттестации.")
        bot.register_next_step_handler(sent, func10_5)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func10_5)


def func11(message):
    if message.text == "IT-чемпионат нефтяной отрасли":
        sent = bot.send_message(message.chat.id,
                                text="IT-чемпионат нефтяной отрасли – командное соревнование для сотрудников компаний нефтяной и иных отраслей Российской Федерации и зарубежных стран, а также для студентов образовательных организаций высшего образования, обучающихся по профильным направлениям. (https://career.gazprom-neft.ru/about/prof-events/it-championship-of-the-oil-industry/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Международный инженерный чемпионат «CASE-IN»":
        sent = bot.send_message(message.chat.id,
                                text="Инженерный чемпионат «CASE-IN» – это международная система соревнований по решению инженерных кейсов для школьников, студентов и молодых специалистов.Чемпионат проходит с 2013 года и посвящен темам топливно-энергетического и минерально-сырьевого комплексов и смежных отраслей. Тема XI сезона чемпионата - «Технологическое лидерство».  (https://career.gazprom-neft.ru/about/prof-events/mejdunarodni-injenerni-chempionat-case-in/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "GPN Intelligence cup":
        sent = bot.send_message(message.chat.id,
                                text="Участникам предстоит выполнить индивидуальные кейсы по разработке и аналитике. Принять участие в интеллектуальном турнире смогут студенты старших курсов и магистранты из вузов России. Победители чемпионата получат возможность пройти оплачиваемую стажировку в «Газпром нефти», где наставниками выступят опытные специалисты и эксперты компании. (https://career.gazprom-neft.ru/about/prof-events/gpn-intelligence-cup/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Стажировка “ИТ-старт”":
        sent = bot.send_message(message.chat.id,
                                text="Компания «Газпром нефть» зимой откроет регистрацию на программу стажировки «ИТ-старт». Стажировка в IT-отделе компании – это отличная возможность прокачать свои навыки на практике, получить опыт работы в конкретной сфере и сделать первые карьерные шаги. Принять участие смогут студенты старших курсов вузов России и молодые специалисты до 25 лет включительно. Кандидаты должен владеть языками программирования, быть готовым работать full-time (40 часов в неделю) и быть заинтересованным в трудоустройстве после окончания стажировки. (https://career.gazprom-neft.ru/about/prof-events/start-it-start/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == 'Кейс-чемпионат "Pro нефть"':
        sent = bot.send_message(message.chat.id,
                                text='Конкурсное мероприятие состоящее из 3-х раундов. Кроссфункциональные команды - студенты 3-х курсов направлений обучения Химическая технология, Технологические машины и оборудование, Автоматизация, Экономика, Теплоэнергетика. Цель мероприятия: сформировать внешний кадровый резерв из числа студентов-победителей, формировать и поддерживать культуру открытого диалога "работодатель-студент". (https://career.gazprom-neft.ru/about/prof-events/case-chemp-pro-oil/)')
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Студенческая олимпиада «Газпром»":
        sent = bot.send_message(message.chat.id,
                                text="Студенческая олимпиада «Газпром» - это олимпиада для студентов разных направлений подготовки, ориентированных на инженерно-технические специальности, способных к техническому творчеству и инновационному мышлению и планирующих свою профессиональную деятельность в нефтегазовой отрасли. (https://studolymp.gazprom.ru)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Марафон лекций от экспертов «Газпром нефти»":
        sent = bot.send_message(message.chat.id,
                                text="Станьте участником масштабной серии открытых образовательных мероприятий о геологии и разработке месторождений нефти и газа  (https://hwtpu.ru/events/gpn/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Газпром нефть канал на ютубе":
        sent = bot.send_message(message.chat.id, text="https://www.youtube.com/@GAZPROMNEFT/featured")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Научно-Технический Центр канал на ютубе":
        sent = bot.send_message(message.chat.id, text="https://www.youtube.com/@user-gp9eo6jw2q/featured")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Газпром образование":
        sent = bot.send_message(message.chat.id, text="https://www.gazprom.ru/sustainability/people/education/")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Газпром молодым специалистам":
        sent = bot.send_message(message.chat.id, text="https://career.gazprom-neft.ru/graduates/")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "X Молодежная международная научно-практическая конференция":
        sent = bot.send_message(message.chat.id,
                                text="https://vniigaz.gazprom.ru/events/2022/x-youth-international-scientific-practical-conference/")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Волонтерский корпус Петербургского международного газового форума":
        sent = bot.send_message(message.chat.id, text="https://gas-forum-volunteer.ru")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Форсайт-игра Дирекции по газу и энергетике":
        sent = bot.send_message(message.chat.id,
                                text="«Газпром нефть» проводит форсайт-игру для студентов экономических, инженерно-технических и нефтегазовых направлений партнерских вузов. Форсайт-игра позволит участникам заглянуть в будущее нефтегазовой отрасли и разработать уникальную стратегию развития компании. (https://career.gazprom-neft.ru/about/prof-events/forsite-game-dpgeng/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Российские студенческие отряды":
        sent = bot.send_message(message.chat.id,
                                text="17 июня 2022 на 25-ом Петербургском международном экономическом форуме было подписано Соглашение о стратегическом партнерстве между ПАО «Газпром», МООО «РСО» и АО «Газстройпром». (https://www.gazprom.ru/sustainability/people/education/student/rso/)")
        bot.register_next_step_handler(sent, func11)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Предстоящие мероприятия")
        btn2 = types.KeyboardButton("Работа на преприятии")
        btn3 = types.KeyboardButton("Контакты руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2, btn3)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func6)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func11)


def func12(message):
    if message.text == "IT-чемпионат нефтяной отрасли":
        sent = bot.send_message(message.chat.id,
                                text="IT-чемпионат нефтяной отрасли – командное соревнование для сотрудников компаний нефтяной и иных отраслей Российской Федерации и зарубежных стран, а также для студентов образовательных организаций высшего образования, обучающихся по профильным направлениям. (https://career.gazprom-neft.ru/about/prof-events/it-championship-of-the-oil-industry/)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Международный инженерный чемпионат «CASE-IN»":
        sent = bot.send_message(message.chat.id,
                                text="Инженерный чемпионат «CASE-IN» – это международная система соревнований по решению инженерных кейсов для школьников, студентов и молодых специалистов.Чемпионат проходит с 2013 года и посвящен темам топливно-энергетического и минерально-сырьевого комплексов и смежных отраслей. Тема XI сезона чемпионата - «Технологическое лидерство».  (https://career.gazprom-neft.ru/about/prof-events/mejdunarodni-injenerni-chempionat-case-in/)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "GPN Intelligence cup":
        sent = bot.send_message(message.chat.id,
                                text="Участникам предстоит выполнить индивидуальные кейсы по разработке и аналитике. Принять участие в интеллектуальном турнире смогут студенты старших курсов и магистранты из вузов России. Победители чемпионата получат возможность пройти оплачиваемую стажировку в «Газпром нефти», где наставниками выступят опытные специалисты и эксперты компании. (https://career.gazprom-neft.ru/about/prof-events/gpn-intelligence-cup/)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Стажировка “ИТ-старт”":
        sent = bot.send_message(message.chat.id,
                                text="Компания «Газпром нефть» зимой откроет регистрацию на программу стажировки «ИТ-старт». Стажировка в IT-отделе компании – это отличная возможность прокачать свои навыки на практике, получить опыт работы в конкретной сфере и сделать первые карьерные шаги. Принять участие смогут студенты старших курсов вузов России и молодые специалисты до 25 лет включительно. Кандидаты должен владеть языками программирования, быть готовым работать full-time (40 часов в неделю) и быть заинтересованным в трудоустройстве после окончания стажировки. (https://career.gazprom-neft.ru/about/prof-events/start-it-start/)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == 'Кейс-чемпионат "Pro нефть"':
        sent = bot.send_message(message.chat.id,
                                text='Конкурсное мероприятие состоящее из 3-х раундов. Кроссфункциональные команды - студенты 3-х курсов направлений обучения Химическая технология, Технологические машины и оборудование, Автоматизация, Экономика, Теплоэнергетика. Цель мероприятия: сформировать внешний кадровый резерв из числа студентов-победителей, формировать и поддерживать культуру открытого диалога "работодатель-студент". (https://career.gazprom-neft.ru/about/prof-events/case-chemp-pro-oil/)')
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Студенческая олимпиада «Газпром»":
        sent = bot.send_message(message.chat.id,
                                text="Студенческая олимпиада «Газпром» - это олимпиада для студентов разных направлений подготовки, ориентированных на инженерно-технические специальности, способных к техническому творчеству и инновационному мышлению и планирующих свою профессиональную деятельность в нефтегазовой отрасли. (https://studolymp.gazprom.ru)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Марафон лекций от экспертов «Газпром нефти»":
        sent = bot.send_message(message.chat.id,
                                text="Станьте участником масштабной серии открытых образовательных мероприятий о геологии и разработке месторождений нефти и газа  (https://hwtpu.ru/events/gpn/)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Газпром нефть канал на ютубе":
        sent = bot.send_message(message.chat.id, text="https://www.youtube.com/@GAZPROMNEFT/featured")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Научно-Технический Центр канал на ютубе":
        sent = bot.send_message(message.chat.id, text="https://www.youtube.com/@user-gp9eo6jw2q/featured")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Газпром образование":
        sent = bot.send_message(message.chat.id, text="https://www.gazprom.ru/sustainability/people/education/")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Газпром молодым специалистам":
        sent = bot.send_message(message.chat.id, text="https://career.gazprom-neft.ru/graduates/")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "X Молодежная международная научно-практическая конференция":
        sent = bot.send_message(message.chat.id,
                                text="https://vniigaz.gazprom.ru/events/2022/x-youth-international-scientific-practical-conference/")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Волонтерский корпус Петербургского международного газового форума":
        sent = bot.send_message(message.chat.id, text="https://gas-forum-volunteer.ru")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Форсайт-игра Дирекции по газу и энергетике":
        sent = bot.send_message(message.chat.id,
                                text="«Газпром нефть» проводит форсайт-игру для студентов экономических, инженерно-технических и нефтегазовых направлений партнерских вузов. Форсайт-игра позволит участникам заглянуть в будущее нефтегазовой отрасли и разработать уникальную стратегию развития компании. (https://career.gazprom-neft.ru/about/prof-events/forsite-game-dpgeng/)")
        bot.register_next_step_handler(sent, func12)

    elif message.text == "Российские студенческие отряды":
        sent = bot.send_message(message.chat.id,
                                text="17 июня 2022 на 25-ом Петербургском международном экономическом форуме было подписано Соглашение о стратегическом партнерстве между ПАО «Газпром», МООО «РСО» и АО «Газстройпром». (https://www.gazprom.ru/sustainability/people/education/student/rso/)")
        bot.register_next_step_handler(sent, func12)


    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Предстоящие мероприятия")
        btn2 = types.KeyboardButton("Работа на преприятии")
        btn3 = types.KeyboardButton("Контакты руководителей")
        btn4 = types.KeyboardButton("Назад")
        btn5 = types.KeyboardButton("Помощь")
        btn6 = types.KeyboardButton("FAQ")
        markup.add(btn1, btn2, btn3)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn4)
        sent = bot.send_message(message.chat.id, text="Какая информация вас интересует?", reply_markup=markup)
        bot.register_next_step_handler(sent, func7)

    elif message.text == "/start":
        start(message)

    else:
        sent = bot.send_message(message.chat.id, text="Что-то пошло не так, попробуй снова")
        bot.register_next_step_handler(sent, func12)


@bot.message_handler(content_types=['text', 'photo'])
def reply(message):
    bot.send_message(message.chat.id, text="Нажми /start чтобы начать")


bot.infinity_polling()

< / h1 >
< p > I
'm hosted with GitHub Pages.</p>
< / body >
< / html >