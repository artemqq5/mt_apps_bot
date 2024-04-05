MAIN_MENU = Меню
CHOUSE = Вибирай
CANCELED = Отменено

# register in bot
YOU_ARE_BLOKED = Вы заблокированы
REGISTER_FAIL = Невозможно зарегистрироваться, повторите попытку позже :/
REGISTER_SUCCESS = Вы успешно зарегистрированы!
SEND_REQUEST_TO_ADMIN = Запрос на получение доступа отправлен администратору! Администратор даст вам ключ доступа для использования этого бота.

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

# team (create, team list, delete, change status) ===========================================================
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

# ban system ================================================================================
BANNED_USERS_EMPTY = Пусто
INPUT_USER_BAN_MESSAGE = Введите сообщение о запрете (его могут просматривать только администраторы)
BAN_MESSAGE_TOO_LONG = Сообщение о запрете слишком длинное. Отправьте сообщение длиной до 255 символов.
INPUT_USER_ID_FOR_UNBAN = Введите идентификатор телеграммы:
INPUT_USER_ID_OR_USERNAME_FOR_BAN = Введите идентификатор телеграммы или @имя пользователя.
    Например, идентификатор: 1201390139 или имя пользователя: @aoksff (с @ первым):
SUCCESSFUL_BANNED = Пользователь успешно забанен
ERROR_BANNED = Пользователь не забанен правильно
UNBAN_USER_SUCCESSFUL = Пользователь успешно разбанен
ERROR_UNBANNED = Пользователь не разбанен правильно, идентификатор указан правильно? Попробуйте еще раз
SHOW_BANNED_USERS_LIST = <b>Список забаненных пользователей</b>:
    {$list}

# settings (locale)
CHOICE_LANG = Выбор языка
SUCCESSFUL_CHANGE_LANG = Язык успешно изменен на <b>{$lang}</b>
FAIL_CHANGE_LANG = Ошибка изменения языка (возможно, вы пытаетесь изменить язык на тот, который установлен сейчас)