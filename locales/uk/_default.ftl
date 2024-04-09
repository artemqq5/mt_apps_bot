MAIN_MENU = Меню
CHOUSE = Вибирай
CANCELED = Скасовано

# реєстрація в боті
YOU_ARE_BLOKED = Ви заблоковані
REGISTER_FAIL = Не вдається зареєструватися, спробуйте пізніше :/
REGISTER_SUCCESS = Ви успішно зареєстровані!
YOU_NEED_BE_REGISTERED = Щоб користуватися цим ботом, потрібно запросити доступ у адміністратора і отримати унікальне посилання

# доступ команди (список доступу, видалення, зміна статусу, створення доступу) =============================
TEAM_HAVENT_ACCESS = Команда не має доступів

WARNING_DELETE_ACCESS = Ви бажаєте видалити доступ?
SUCCESSFUL_DELETE_ACCESS = Доступ успішно видалено
ERROR_DELETE_ACCESS = Помилка видалення доступу
    <code>{$error}</code>

CHOICE_NEW_STATUS_ACCESS = Виберіть новий статус доступу
SUCCESSFUL_CHANGE_STATUS_ACCESS = Успішно змінено статус доступу. новий статус: <b>{$status}</b>
ERROR_CHANGE_STATUS_ACCESS = Помилка зміни статусу доступу
    <code>{$error}</code>

WARNING_GENERATE_KEY_TEAM = Ви хочете створити ключ для <b>{$team_name}</b>?
SUCCESSFUL_GENERATE_TEAM = Успішно створено ключ приєднання для <b>({$team_name})</b>.
    Глибоке посилання: <code>{$deeplink}</code>
ERROR_GENERATE_TEAM = Помилка створення ключа приєднання
    <code>{$error}</code>

# team access (activate from user) ===========================================
INPUT_TEAM_KEY = Привіт! Ви не пов'язані з жодною командою. Адміністратор має надіслати вам ключ команди!
    Введіть ключ команди:
JOIN_KEY_NOT_EXIST = Ключ не існує!
JOIN_KEY_ACTIVATED_BEFORE = Ключ був активований раніше!
JOIN_KEY_FAIL_UPDATE = Якась помилка. Ключ команди не встановлено
JOIN_KEY_SUCCESS_UPDATE = Ключ команди встановлено успішно!

# team (create, team list, delete, change status) ===========================================================
INPUT_TEAM_NAME = Введіть назву команди:
TEAM_NAME_TOO_LONG = Назва команди занадто довга. Надіслати повідомлення до 255 символів
ERROR_CREATE_TEAM = Якась помилка під час спроби створити команду, повторіть спробу
SUCCESSFUL_CREATE_TEAM = Команда <b>{$team_name}</b> створена!

TEAM_LIST_IS_EMPTY = Список команд порожній
TEAM_MENU = Командне меню

WARNING_DELETE_TEAM = Ви хочете видалити <b>{$team_name}</b>?
    (Дію неможливо скасувати!)
SUCCESSFUL_DELETE_TEAM = Успішно видалено <b>({$team_name})</b>
ERROR_DELETE_TEAM = Помилка видалення команди
    <code>{$error}</code>

CHOICE_NEW_STATUS_TEAM = Виберіть новий статус команди для <b>{$team_name}</b>
SUCCESSFUL_CHANGE_STATUS_TEAM = Успішно змінено статус <b>({$team_name})</b>. новий статус: <b>{$status}</b>
ERROR_CHANGE_STATUS_TEAM = Помилка зміни статусу команди
    <code>{$error}</code>

# ban system ================================================================================
BANNED_USERS_EMPTY = Порожньо
INPUT_USER_BAN_MESSAGE = Повідомлення про заборону введення (тільки адміністратори можуть переглядати його)
BAN_MESSAGE_TOO_LONG = Повідомлення про заборону занадто довге. Надіслати повідомлення до 255 символів
INPUT_USER_ID_FOR_UNBAN = Введіть ідентифікатор телеграми:
INPUT_USER_ID_OR_USERNAME_FOR_BAN = Введіть ідентифікатор телеграми або @username.
    Наприклад, id: 1201390139 або ім’я користувача: @aoksff (з першим @):
SUCCESSFUL_BANNED = Користувача успішно забанено
ERROR_BANNED = Користувача заблоковано неправильно
UNBAN_USER_SUCCESSFUL = Користувача успішно розблоковано
ERROR_UNBANNED = Користувач не був розблокований правильно, ID правильний? Спробуйте знову
SHOW_BANNED_USERS_LIST = <b>Список забанених користувачів</b>:
    {$list}

# settings (locale)
CHOICE_LANG = Вибір мови
SUCCESSFUL_CHANGE_LANG = Мову успішно змінено на <b>{$lang}</b>
FAIL_CHANGE_LANG = Помилка зміни мови (можливо ви намагаєтесь змінити мову на ту що встановлено зараз)

# applications (add, preview template, publish, show, manage)
APP-SET_PLATFORM = Під яку платформу додаток?
APP-SET_NAME = Назва додатку:
APP-SET_BUNDLE = Вкажи bundle додатку (IOS=1451177077, Android=com.af.smart):
APP-SET_IMAGE = Надішли картинку для додатку (не файлом):
APP-SET_GEO = Вкажи відкриті гео, наприклад (UA, AL, BR):
APP-SET_SOURCE = Вкажи під які джерела, наприклад (Facebook deeplink або onelink):
APP-SET_DESC = Твій коментар\опис:
APP-PREVIEW = Попередній перегляд, подивись чи все правильно і публікуй Draft або повертайся на початок. ⚠️⚠️⚠️

APP-SUCCESS_PUBLISHED = Ви успішно створили додаток зі статусом (Draft), щоб його побачили інші користувачі вам потрібно активувати його (змінити статус на Active)
APP-FAIL_PUBLISHED = Не вдалося створити додаток, потрібно терміново подивитись логи поки вони не загубились

APP-CHOICE_PLATFORM = Оберіть платформу
APP-APP_LIST_EMPTY = Додатків під дану платформу немає
APP-IOS_APPS = IOS Додатки:
APP-DESC_TEMPLATE = Назва: <b>{$name_url}</b>

    Платформа: <b>{$platform}</b>
    Джерела: <b>{$source}</b>

    ГЕО: {$geo}

    Статус: <b>{$status}</b>

    {$desc}
APP-GEO_EDIT_SUCCESSFUL = Гео успішно відредаговані
APP-GEO_EDIT_FAIL = Помилка при редагуванні гео

APP-SET_STATUS = Вкажіть новий статус додатка <b>{$name}</b>
APP-STATUS_EDIT_SUCCESS = Cтатус додатка успішно змінено
APP-STATUS_EDIT_FAIL = Помилка при зміні статусу додатка, можливо ви намагаєтеся змінити на той самий статус

APP-DELETE_WARNING = Ви точно хочете видалити додаток <b>{$name}</b>? (з бази даних він не видаляється)
APP-DELETE_SUCCESS = Додаток <b>{$name}</b> успішно видалено, його можна востановити напряму через базу даних
APP-DELETE_FAIL = Помилка при видаленні додатку <b>{$name}</b>

# user (apps)
USER-CHOICE_PLATFORM_APP = Оберіть платформу додатків
USER-IOS_APPS = Доступні IOS Додатки:
USER-DESC_TEMPLATE = Назва: <b>{$name_url}</b>

    Платформа: <b>{$platform}</b>
    Джерела: <b>{$source}</b>

    ГЕО: {$geo}

    {$desc}