#СТАРТ И РЕГИСТРАЦИЯ
startMessage_1 = "Привет! Я политехник - неофициальный бот Политехнического университета." \
                 "\n\nВокруг мессенджеров сейчас строится наибольшая часть взаимодействия между людьми, " \
                 "поэтому было бы удобно пользоваться всем, не выходя из Телеграмма." \
                 "\n\nЭтот бот - аналог приложений PolyNavi и подобных, но его отличие в том, что он универсален " \
                 "абсолютно для всех устройств вне зависимости от их платформы и везде выглядит одинаково. " \
                 "\n\nТак-с, что-то мы слишком много говорим, пора идти дальше, нажимай на кнопку под сообщением!"
startMessage_2 = "Итак, вот что я умею:" \
                 "\n- показывать расписание твоей группы (или любой другой, которая тебе понадобится)" \
                 "\n- строить маршруты между корпусами Политеха" \
                 "\n- показывать собачек и котиков" \
                 "\n- искать контактные данные преподавателя или представителя администрации университета" \
                 "\n\nЧтобы использовать команду, напиши косую черту (/) и выбери из списка нужную команду" \
                 "\n\nпару слов о том, как работает расписание" \
                 "\nПри команде /schedule бот выдаёт расписание на текущий день, около каждого занятия есть кружок " \
                 "(зелёный - занятие идёт, оранжевый - ещё не началось, красный - закончено). Если на текущий день " \
                 "пары закончились, то бот выдаст расписание на следующий день. Совсем скоро ты сможешь посмотреть " \
                 "расписание на любой день."
regMessage_1 = "Чтобы нам было проще общаться, напиши, как тебя зовут (просто напиши своё имя в сообщении " \
               "*без лишних символов*)"

#-----------------------------------------------------------------------------------------

#ОШИБКИ
errorMessage_1 = "*Твоё имя должно состоять не более чем из 25 символов, придумай новое и отправь его снова*"
errorMessage_2 = "Я пока не знаю, в какой группе ты обучаешься. " \
                 "Чтобы это исправить, сделай следующее:" \
                 "\n1. Перейди на сайт https://ruz.spbstu.ru, выбери свой университет и группу" \
                 "\n2. Скопируй ссылку на эту страницу и отправь её мне"
errorMessage_3 = "*{0}, этой командой могут пользоваться только те, кто ещё не зарегистрирован в боте*"
errorMessage_4 = "*Введённые тобой данные неверны, проверь их и отправь ещё раз*"
errorMessage_5 = "*Для использования этой команды тебе сначала необходимо зарегистрироваться, используй /start*"
errorMessage_6 = "*Я ещё не научился отвечать на вопросы из беседы, поэтому пока ты можешь сделать это только через личные сообщения*"
errorMessage_7 = "*Твоё имя должно состоять не менее чем из 2 символов, придумай новое и отправь его снова*"
kbfyerrorMessage_8 = "*Ты используешь недопустимые символы, имя должно состоять только из русских или английских букв, придумай новое и отправь его снова*"
errorMessage_9 = "*Я вижу тут больше, чем одно слово, придумай новое имя и отправь его снова*"
#-----------------------------------------------------------------------------------------

#ОТВЕТЫ
replyMessage_1 = "*Приятно познакомиться, {0}!*"
replyMessage_2 = "*Жду от тебя ссылку 👀*"
replyMessage_3 = "*Твоё расписание добавлено! Теперь можешь использовать команду /schedule*"
replyMessage_4 = "*Действие отменено*"
replyMessage_5 = "*Куда ты хочешь попасть?*"
replyMessage_6 = "*Локация: {0}\n\nОткрывай с помощью любых карт на твоём телефоне и в путь!*"
replyMessage_7 = "*НАСТРОЙКИ*"
replyMessage_8 = "*{}, твоё имя обновлено!*"
replyMessage_9 = "*Расписание обновлено! Проверяй через /schedule*"

#-----------------------------------------------------------------------------------------

#РАСПИСАНИЕ
scheduleMessage_1 = "*Расписание на {0}.{1}.{2}\n*"
scheduleMessage_2 = "*Расписание на {0}.{1}.{2} отсутствует*"
scheduleMessage_3 = "_{0}{1}_\n📖 *{2}*\n🏢 *{3}*\n👨 *{4}*"

#-----------------------------------------------------------------------------------------

#СЕРВИСНЫЕ
serviceMessage_1 = "Система перезагружена" \
                   "\nДата: {0}" \
                   "\nВремя: {1}"

serviceMessage_2 = "*Напишите текст сообщения для массовой рассылки*"
serviceMessage_3 = "*Проверьте текст и выберите действие*\n\n{0}"
serviceMessage_4 = "*Рассылка окончена*"
serviceMessage_5 = "*Пользователь с tID {0} заблокировал бота, удаление из базы данных*"
#-----------------------------------------------------------------------------------------

#СНАСТРОЙКИ
settingsMessage_1 = "Твоё текущее имя в системе: *{0}*\nВведи новое имя (без лишних символов и пробелов)"
settingsMessage_2 = "Для того, чтобы изменить номер группы, сделай следующее:" \
                    "\n1. Перейди на сайт https://ruz.spbstu.ru, выбери свой университет и группу" \
                    "\n2. Скопируй ссылку на эту страницу и отправь её мне"
settingsMessage_3 = "В скором времени здесь будет доступна форма для вопросов, а пока по всем вопросам пиши @lrrrtm"
settingsMessage_4 = "Я политехник - неофициальный бот Политехнического университета." \
                 "\n\nВокруг мессенджеров сейчас строится наибольшая часть взаимодействия между людьми, " \
                 "поэтому было бы удобно пользоваться всем, не выходя из Телеграмма." \
                 "\n\nЭтот бот - аналог приложений PolyNavi и подобных, но его отличие в том, что он универсален " \
                 "абсолютно для всех устройств вне зависимости от их платформы и везде выглядит одинаково. " \
                    "\n\nДоступные функции:" \
                    "\n-доступ к расписанию (/schedule)" \
                    "\n-построение маршрутов (/routes)" \
                    "\n-поиск данных преподавателей и администрации (/find)" \
                    "\n-собачки и котики для снятия морального напряжения (/dogs и /cats)"
