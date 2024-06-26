MAIN_MENU = Меню
CHOUSE = Вибирай
CANCELED = Отменено

# register in bot
YOU_ARE_BLOKED = Вы заблокированы
REGISTER_FAIL = Невозможно зарегистрироваться, повторите попытку позже :/
REGISTER_SUCCESS = Вы успешно зарегистрированы!
YOU_NEED_BE_REGISTERED = Чтобы пользоваться этим ботом, нужно запросить доступ у администратора и получить уникальную ссылку

# team access (access list, delete, change status, generate access) ============================
TEAM_HAVENT_ACCESS = У команды нет доступов

WARNING_DELETE_ACCESS = Вы хотите удалить доступ?
SUCCESSFUL_DELETE_ACCESS = Доступ успешно удален.
ERROR_DELETE_ACCESS = Ошибка удаления доступа
    <code>{$error}</code>

CHOICE_NEW_STATUS_ACCESS = Выбор нового статуса доступа
SUCCESSFUL_CHANGE_STATUS_ACCESS = Успешное изменение статуса доступа. новый статус: <b>{$status}</b>
ERROR_CHANGE_STATUS_ACCESS = Ошибка изменения статуса доступа
    <code>{$error}</code>

WARNING_GENERATE_KEY_TEAM = Вы хотите сгенерировать ключ для <b>{$team_name}</b>?
SUCCESSFUL_GENERATE_TEAM = Успешно сгенерирован ключ присоединения для <b>({$team_name})</b>.
    deeplink: <code>{$deeplink}</code>
ERROR_GENERATE_TEAM = Ошибка создания ключа соединения
    <code>{$error}</code>

# team access (activate from user) ===========================================
INPUT_TEAM_KEY = Здравствуйте! Вы не принадлежите ни к одной команде. Администратор должен отправить вам командный ключ!
    Введите командный ключ:
JOIN_KEY_NOT_EXIST = Ключ не существует!
JOIN_KEY_ACTIVATED_BEFORE = Ключ уже был активирован раньше!
JOIN_KEY_FAIL_UPDATE = Какая-то ошибка. Ключ команды не установлен
JOIN_KEY_SUCCESS_UPDATE = Ключ группы успешно установлен!

ACCESS_TEAM_NAME = Доступы ({$team})

# team (create, team list, delete, change status, domain limit) ===========================================================
INPUT_TEAM_NAME = Введите название команды:
TEAM_NAME_TOO_LONG = Название команды слишком длинное. Отправьте сообщение длиной до 255 символов.
ERROR_CREATE_TEAM = Ошибка при создании команды. Повторите попытку.
SUCCESSFUL_CREATE_TEAM = <b>{$team_name}</b> Команда создана!

TEAM_LIST_IS_EMPTY = Список команды пуст
TEAM_MENU = Меню команды

WARNING_DELETE_TEAM = Вы хотите удалить <b>{$team_name}</b>?
    (Действие невозможно отменить!)
SUCCESSFUL_DELETE_TEAM = <b>({$team_name})</b> успешно удалено.
ERROR_DELETE_TEAM = Ошибка удаления команды
    <code>{$error}</code>

CHOICE_NEW_STATUS_TEAM = Выбор нового статуса команды для <b>{$team_name}</b>
SUCCESSFUL_CHANGE_STATUS_TEAM = Успешно изменен статус для <b>({$team_name})</b>. новый статус: <b>{$status}</b>
ERROR_CHANGE_STATUS_TEAM = Ошибка изменения статуса команды
    <code>{$error}</code>

NEW_DOMAIN_LIMIT = Новый лимит доменов для команды:
SET_LIMIT_SUCCESS = Новый дневной лимит ({$limit}) успешно установлен
SET_LIMIT_FAIL = Ошибка при установке нового лимита

# ban system ================================================================================
BANNED_USERS_EMPTY = Пусто
INPUT_USER_BAN_MESSAGE = Введите сообщение о запрете (его могут просматривать только администраторы)
BAN_MESSAGE_TOO_LONG = Сообщение о запрете слишком длинное. Отправьте сообщение длиной до 255 символов.
INPUT_USER_ID_FOR_UNBAN = Введите идентификатор телеграма:
INPUT_USER_ID_OR_USERNAME_FOR_BAN = Введите идентификатор телеграммы или @имя пользователя.
    Например, идентификатор: 1201390139 или имя пользователя: @aoksff (с @ первым):
SUCCESSFUL_BANNED = Пользователь успешно забанен
ERROR_BANNED = Пользователь не забанен правильно
UNBAN_USER_SUCCESSFUL = Пользователь успешно разбанен
ERROR_UNBANNED = Пользователь не разбанен правильно, идентификатор указан правильно? Попробуйте еще раз
SHOW_BANNED_USERS_LIST = <b>Список заблокированных пользователей</b>:
BANNED_USERS_LIST_EMPTY = <b>Нет заблокированных пользователей</b>

# settings (locale)
CHOICE_LANG = Выбор языка
SUCCESSFUL_CHANGE_LANG = Язык успешно изменен на <b>{$lang}</b>
FAIL_CHANGE_LANG = Ошибка изменения языка (возможно, вы пытаетесь изменить язык на тот, который установлен сейчас)

# applications (add, preview template, publish, show)
APP-SET_PLATFORM = Под какую платформу приложение?
APP-SET_NAME = Имя приложения:
APP-SET_BUNDLE = Укажи bundle приложения (IOS=1451177077, Android=com.af.smart):
APP-SET_IMAGE = Пришли картинку для приложения (не файлом):
APP-SET_GEO = Укажи открытые гео, например (UA, AL, BR):
APP-SET_SOURCE = Укажи под какой источник направлено приложение:
APP-SET_DESC = Ваш комментарий\описание:
APP-DEFAULT_DESC = Чтобы открыть ГEО, свяжитесь с сапортом
APP-PREVIEW = Предварительный просмотр, посмотри все ли правильно и публикуй Draft или возвращайся к началу. ⚠️⚠️⚠️
APP-ALREADY_ADDED = Это приложение было добавлено ранее, просмотрите в существующих или в базе

APP-SUCCESS_PUBLISHED = Вы успешно создали приложение со статусом (Draft), чтобы его увидели другие пользователи, вам нужно активировать его (изменить статус на Active).

    Masons Link: <code>{$masons}</code>

    <b>Также вот органическая кампания под это приложение</b>
    ID: <code>{$id}</code>
    Name: <code>{$name}</code>
    Link in Keitaro: <code>{$link}</code>
APP-FAIL_PUBLISHED = Не удалось создать приложение, нужно срочно посмотреть логи, пока они не потерялись ({$error})

APP-CHOICE_PLATFORM = Выберите платформу
APP-APP_LIST_EMPTY = Приложений под данную платформу нет
APP-IOS_APPS = IOS Приложения:
APP-DESC_TEMPLATE = Имя: <b>{$name_url}</b>

     ID: {$id}

     Платформа: <b>{$platform}</b>
     Источник: <b>{$source}</b>

     ГЕО: {$geo}

     Статус: <b>{$status}</b>

     {$desc}

APP-GEO_EDIT_SUCCESSFUL = Гео успешно отредактировано
APP-GEO_EDIT_FAIL = Ошибка при редактировании гео

APP-SET_STATUS = Укажите новый статус приложения <b>{$name}</b>
APP-STATUS_EDIT_SUCCESS=Статус приложения успешно изменен
APP-STATUS_EDIT_FAIL = Ошибка при изменении статуса приложения, возможно вы пытаетесь изменить на тот же статус
APP-STATUS_NOTIFY_NEW_STATUS = Отправить пользователям уведомление о новом статусе приложения ({$status})?

APP-DELETE_WARNING = Вы точно хотите удалить приложение <b>{$name}</b>? (из базы данных он не удаляется)
APP-DELETE_SUCCESS = Приложение <b>{$name}</b> успешно удалено, его можно установить напрямую через базу данных
APP-DELETE_FAIL = Ошибка при удалении приложения <b>{$name}</b>

# user (apps)
USER-CHOICE_PLATFORM_APP = Выберите платформу приложений
USER-IOS_APPS = Доступные IOS Приложения:
USER-DESC_TEMPLATE = Имя: <b>{$name_url}</b>

     Платформа: <b>{$platform}</b>
     Источник: <b>{$source}</b>

     ГЕО: {$geo}

     {$desc}

# user (add pixel, show my pixel, delete pixel)
USER-ADD_PIXEL_ID = Отправьте Pixel ID:
USER-ADD_TOKEN_EAAG = Отправьте Token EAAG:
USER-SUCCESS_ADD_PIXEL=Пиксель успешно добавлен
USER-FAIL_ADD_PIXEL = Не удалось добавить пикесль

USER-HAVENT_ANY_PIXEL = У вас нет созданных пикселей
USER-YOUR_PIXELS = Ваши пиксели:
USER-PIXEL_INFO = Pixel ID: <code>{$pixel_id}</code>

     Token EAAG: <code>{$token}</code>

     Пиксель создан: <b>{$date}</b>

USER-SUCCESS_DELETE_PIXEL = Pixel успешно удален из библиотеки
USER-FAIL_DELETE_PIXEL = Не удалось удалить pixel

# flow user (create, show, edit)
FLOW-SELECT_PIXEL_FB = Выберите пиксель для потока:
FLOW-HAVENT_PIXEL_FB = У вас нет созданных пикселей, хотите создать?
FLOW-COMMENT = Добавить комментарий к потоку
FLOW-OFFER_LINK = Отправьте свою ссылку
FLOW-OFFER_LINK_ERROR = Внимание!

    1) Ссылка должна быть с обязательным макросом 'ваш_параметр={$subid}'
    2) Начинаться с 'https://'
    3) НЕ заканчиваться '/' символом

    Например https://example.site/test?asdpg={$subid} – это минимальный пример!
FLOW-FLOW_SUCCESS_CREATED=Поток успешно создан, желаем качественного трафика!
     <code>{$flow}</code>
FLOW-FLOW_FAIL_CREATED = Не удалось создать поток ({$error}), перешлите админу это сообщение

FLOW-MY_FLOWS = Мои потоки
FLOW-DETAIL_FLOW = <b>Ваша рабочая ссылка:</b>
     <code>{$link_keitaro}</code>

     =====================================
     <b>ID:</b> {$id}
     <b>Дата создания: </b> {$date}

     <b>Приложение:</b> {$app_name}
     <b>Платформа:</b> {$platform}
     <b>Источник:</b> {$source}
     <b>Статус приложения:</b> {$status}

     <b>Домен:</b> <code>{$domain}</code>
     <b>Ваш оффер\трекер:</b> <code>{$link_user}</code>

     <b>Pixel ID:</b> {$pixel}
     <b>Token:</b> {$token}

     <b>ГЕО:</b> {$geo}

     <b>Коментарий:</b> {$comment}

     ⚠️Чтобы открыть ГЕО, свяжитесь с сапортом⚠️
FLOW-HAVNT_FREE_DOMAINS=Нет свободных доменов, админу отправлено сообщение, скоро их пополнят!
FLOW-DOMAIN_LIMIT_OVER = Превышен дневной лимит доменов на вашу команду ({$limit})
     Чтобы увеличить дневной предел, напишите в поддержку

# COMMENT
FLOW-EDIT-NEW_COMMENT = Введите новый комментарий к потоку:
FLOW-EDIT-NEW_COMMENT_SUCCESS = Комментарий к потоку успешно обновлен!
FLOW-EDIT-NEW_COMMENT_FAIL = Не удалось обновить комментарий, напишите в поддержку
# PIXEL
FLOW-EDIT-NEW_PIXEL = Выберите новый PIXEL
FLOW-EDIT-NEW_PIXEL_SUCCESS = Новый PIXEL успешно установлен
FLOW-EDIT-NEW_PIXEL_FAIL = Не удалось заменить ваш PIXEL ({$error}), попробуйте еще раз или напишите в поддержку, вам обязательно помогут!
#OFFER
FLOW-EDIT-NEW_OFFER = Введите новую ссылку на оффер/трекер:
FLOW-EDIT-NEW_OFFER_SUCCESS = Ваша ссылка обновлена!
FLOW-EDIT-NEW_OFFER_FAIL = Не удалось обновить вашу ссылку ({$error}), попробуйте еще раз или напишите в поддержку, вам обязательно помогут!
# APPS
FLOW-EDIT-NEW_APP = Выберите новое приложение:
FLOW-EDIT-NEW_APP_SUCCESS = Ваше приложение заменено!
FLOW-EDIT-NEW_APP_FAIL = Не удалось заменить ваше приложение ({$error}), попробуйте еще раз или напишите в поддержку, вам обязательно помогут!

# notification
NOTIFY-CATEGORY = Выберите категорию рассылки
NOTIFY-MESSAGE = Введите текст рассылки:
NOTIFY-MEDIA = Отправьте фото\гифку\видео в сжатом формате (не файлом)
NOTIFY-BUTTON_URL = Введите ссылку для кнопки:
NOTIFY-BUTTON_URL_VALIDATION = Ссылка должна начинаться с https://
NOTIFY-BUTTON_TEXT = Введите текст для кнопки (до 50 символов):
NOTIFY-BUTTON_TEXT_LIMIT = до 50 символов:
NOTIFY-PREVIEW = Если все правильно, межете отправлять пользователям, они получат точно такое же сообщение
NOTIFY-RESULT = <b>=== Результат рассылки ===</b>

    <b>{$get}\{$users}</b> - получили свои сообщения
    ======================
    Заблокировали бота: <b>{$block}</b>
    Другое: <b>{$other}</b>

# ban, active notification
NOYIFY-APP_STATUS_BAN = Приложение <b>{$app_name}</b> было заблокировано‼️

    Остановите трафик!
NOYIFY-APP_STATUS_ACTIVE = Приложение <b>{$app_name}</b> активно! ✅
NOYIFY-APP_STATUS_DRAFT = Приложение <b>{$app_name}</b> временно будет не доступно для новых потоков, но можете не останавливать старые, с приложением все хорошо!
# admin notification
ADMIN-NOTIFICATION-HAVENT_DOMAIN = 🆘 Домены закончились 🆘
    Срочно пополните домены в кейтаро, чтобы пользователи смогли создавать ссылки Onelink!!!
ADMIN-NOTIFICATION-DOMAIN_LIMIT_WAS_OVER = Команда ({$team}) достигла своего дневного лимита по доменам и хочет создать новую ссылку 🤷‍♂️
ADMIN-NOTIFICATION-NEW_USER = Новый пользователь {$username} запустил бота!

    Подробно:
    <b>telegram id:</b> {$id}
    <b>username:</b> {$username}
    <b>first name:</b> {$firstname}
    <b>last name:</b> {$lastname}
    <b>lang:</b> {$lang}
    <b>start time:</b> {$time}