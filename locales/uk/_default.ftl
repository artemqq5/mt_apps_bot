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

ACCESS_TEAM_NAME = Доступи ({$team})

# team (create, team list, delete, change status, domain limit) ===========================================================
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

NEW_DOMAIN_LIMIT = Новий ліміт доменів для команди:
SET_LIMIT_SUCCESS = Новий денний ліміт ({$limit}) успішно встановленно
SET_LIMIT_FAIL = Помилка при встановленні нового ліміту

# ban system ================================================================================
BANNED_USERS_EMPTY = Порожньо
INPUT_USER_BAN_MESSAGE = Повідомлення про заборону введення (тільки адміністратори можуть переглядати його)
BAN_MESSAGE_TOO_LONG = Повідомлення про заборону занадто довге. Надіслати повідомлення до 255 символів
INPUT_USER_ID_FOR_UNBAN = Введіть ідентифікатор телеграма:
INPUT_USER_ID_OR_USERNAME_FOR_BAN = Введіть ідентифікатор телеграми або @username.
    Наприклад, id: 1201390139 або ім’я користувача: @aoksff (з першим @):
SUCCESSFUL_BANNED = Користувача успішно забанено
ERROR_BANNED = Користувача заблоковано неправильно
UNBAN_USER_SUCCESSFUL = Користувача успішно розблоковано
ERROR_UNBANNED = Користувач не був розблокований правильно, ID правильний? Спробуйте знову
SHOW_BANNED_USERS_LIST = <b>Список заблокованих користувачів</b>:
BANNED_USERS_LIST_EMPTY = <b>Немає заблокованих користувачів</b>


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
APP-SET_SOURCE = Вкажи під яке джерело націлений додаток:
APP-SET_DESC = Твій коментар\опис:
APP-DEFAULT_DESC = Щоб відкрити ГЕО зв'яжіться з сапортом
APP-PREVIEW = Попередній перегляд, подивись чи все правильно і публікуй Draft або повертайся на початок. ⚠️⚠️⚠️
APP-ALREADY_ADDED = Цей додаток було додано раніше, перегляньте у наявних або у базі

APP-SUCCESS_PUBLISHED = Ви успішно створили додаток зі статусом (Draft), щоб його побачили інші користувачі вам потрібно активувати його (змінити статус на Active).

    Masons Link: <code>{$masons}</code>

    <b>Також ось органічна кампанія під цей додаток</b>
    ID: <code>{$id}</code>
    Name: <code>{$name}</code>
    Link in Keitaro: <code>{$link}</code>
APP-FAIL_PUBLISHED = Не вдалося створити додаток, потрібно терміново подивитись логи поки вони не загубились ({$error})

APP-CHOICE_PLATFORM = Оберіть платформу
APP-APP_LIST_EMPTY = Додатків під дану платформу немає
APP-IOS_APPS = IOS Додатки:
APP-DESC_TEMPLATE = Назва: <b>{$name_url}</b>

    ID: {$id}

    Платформа: <b>{$platform}</b>
    Джерело: <b>{$source}</b>

    ГЕО: {$geo}

    Статус: <b>{$status}</b>

    {$desc}
APP-GEO_EDIT_SUCCESSFUL = Гео успішно відредаговані
APP-GEO_EDIT_FAIL = Помилка при редагуванні гео

APP-SET_STATUS = Вкажіть новий статус додатка <b>{$name}</b>
APP-STATUS_EDIT_SUCCESS = Cтатус додатка успішно змінено
APP-STATUS_EDIT_FAIL = Помилка при зміні статусу додатка, можливо ви намагаєтеся змінити на той самий статус
APP-STATUS_NOTIFY_NEW_STATUS = Відправити користувачам повідомленням про новий статус додатка ({$status})?

APP-DELETE_WARNING = Ви точно хочете видалити додаток <b>{$name}</b>? (з бази даних він не видаляється)
APP-DELETE_SUCCESS = Додаток <b>{$name}</b> успішно видалено, його можна востановити напряму через базу даних
APP-DELETE_FAIL = Помилка при видаленні додатку <b>{$name}</b>

# user (apps)
USER-CHOICE_PLATFORM_APP = Оберіть платформу додатків
USER-IOS_APPS = Доступні IOS Додатки:
USER-DESC_TEMPLATE = Назва: <b>{$name_url}</b>

    Платформа: <b>{$platform}</b>
    Джерело: <b>{$source}</b>

    ГЕО: {$geo}

    {$desc}

# user (add pixel, show my pixel, delete pixel)
USER-ADD_PIXEL_ID = Надішліть Pixel ID:
USER-ADD_TOKEN_EAAG = Надішліть Token EAAG:
USER-SUCCESS_ADD_PIXEL = Pixel успішно додано
USER-FAIL_ADD_PIXEL = Не вдалося додати pixel

USER-HAVENT_ANY_PIXEL = Ви не маєте створених пікселів
USER-YOUR_PIXELS = Ваші пікселі:
USER-PIXEL_INFO = Pixel ID: <code>{$pixel_id}</code>

    Token EAAG: <code>{$token}</code>

    Піксель створено: <b>{$date}</b>

USER-SUCCESS_DELETE_PIXEL = Pixel успішно видалено з бібліотеки
USER-FAIL_DELETE_PIXEL = Не вдалося видалити pixel

# flow user (create, show, edit)
FLOW-SELECT_PIXEL_FB = Оберіть ваш піксель для потоку:
FLOW-HAVENT_PIXEL_FB = У вас немає створених пікселів, бажаєте створити?
FLOW-COMMENT = Додайте коментар до потоку
FLOW-OFFER_LINK = Пришліть свою лінку
FLOW-OFFER_LINK_ERROR = Увага! Лінка повина бути з обов'язковим макросом ={$subid} та починатися з https://
    Наприклад https://example.site/test?asdpg={$subid} - це мінімальний приклад!
FLOW-FLOW_SUCCESS_CREATED = Поток успішно створено, бажаємо якісного трафіку!
    <code>{$flow}</code>
FLOW-FLOW_FAIL_CREATED = Не вийшло створити поток ({$error}), перешліть адміну це повідомлення

FLOW-MY_FLOWS = Мої потоки
FLOW-DETAIL_FLOW = <b>Ваша робоча лінка:</b>
    <code>{$link_keitaro}</code>

    =====================================
    <b>ID:</b> {$id}
    <b>Дата створення: </b> {$date}

    <b>Додаток:</b> {$app_name}
    <b>Платформа:</b> {$platform}
    <b>Джерело:</b> {$source}
    <b>Статус додатка:</b> {$status}

    <b>Домен:</b> <code>{$domain}</code>
    <b>Ваш оффер\трекер:</b> <code>{$link_user}</code>

    <b>Pixel ID:</b> {$pixel}
    <b>Token:</b> {$token}

    <b>ГЕО:</b> {$geo}

    <b>Коментар:</b> {$comment}

     ⚠️ Щоб відкрити ГЕО зв'яжіться з сапортом ⚠️
FLOW-HAVNT_FREE_DOMAINS = Немає вільних доменів, адміну відправлено повідомлення, скоро їх поповнять!
FLOW-DOMAIN_LIMIT_OVER = Перевищено денний ліміт доменів на вашу команду ({$limit})
    Щоб збільшити денний ліміт, напишіть у підтримку

# COMMENT
FLOW-EDIT-NEW_COMMENT = Введіть новий коментар до потоку:
FLOW-EDIT-NEW_COMMENT_SUCCESS = Комент до потоку успішно оновлено!
FLOW-EDIT-NEW_COMMENT_FAIL = Не вийшло оновити комент, напишіть у підтримку
# PIXEL
FLOW-EDIT-NEW_PIXEL = Оберіть новий PIXEL
FLOW-EDIT-NEW_PIXEL_SUCCESS = Новий PIXEL успішно встановлено
FLOW-EDIT-NEW_PIXEL_FAIL = Не вийшло замінити ваш PIXEL ({$error}), спробуйте ще раз або напишіть у підтримку, вам обовґязково допоможуть!
# OFFER
FLOW-EDIT-NEW_OFFER = Введіть нове посилання на оффер/трекер:
FLOW-EDIT-NEW_OFFER_SUCCESS = Ваше посилання оновлено!
FLOW-EDIT-NEW_OFFER_FAIL = Не вийшло оновити ваше посилання ({$error}), спробуйте ще раз або напишіть у підтримку, вам обовґязково допоможуть!
# APPS
FLOW-EDIT-NEW_APP = Оберіть новий додаток:
FLOW-EDIT-NEW_APP_SUCCESS = Ваш додаток замінено!
FLOW-EDIT-NEW_APP_FAIL = Не вийшло замінити ваш додаток ({$error}), спробуйте ще раз або напишіть у підтримку, вам обовґязково допоможуть!

# notification
NOTIFY-CATEGORY = Оберіть категорію для розсилки
NOTIFY-MESSAGE = Введіть текст розсилки:
NOTIFY-MEDIA = Надішліть фото\гіфку\відео в зжатому форматі (не файлом)
NOTIFY-BUTTON_URL = Введіть посилання для кнопки:
NOTIFY-BUTTON_URL_VALIDATION = Посилання має починатися з https://
NOTIFY-BUTTON_TEXT = Введіть текст для кнопки (до 50 символів):
NOTIFY-BUTTON_TEXT_LIMIT = до 50 символів:
NOTIFY-PREVIEW = Якщо все правильно, можете надсилати користувачам, вони отримають точно таке ж повідомлення
NOTIFY-RESULT = <b>=== Результат розсилки ===</b>

    <b>{$get}\{$users}</b> - отримали свої повідомлення
    ======================
    Заблокувули бота: <b>{$block}</b>
    Інше: <b>{$other}</b>

# ban, active notification
NOYIFY-APP_STATUS_BAN = Додаток <b>{$app_name}</b> було заблоковано‼️

    Зупиніть трафік!
NOYIFY-APP_STATUS_ACTIVE = Додаток <b>{$app_name}</b> активний! ✅
NOYIFY-APP_STATUS_DRAFT = Додаток <b>{$app_name}</b> тимчасово буде не доступний для нових потоків, але можете не зупиняти старі, з додатком все добре!

# admin notification message
ADMIN-NOTIFICATION-HAVENT_DOMAIN = 🆘 Домени закінчились 🆘
    Терміново поповніть домени в кейтаро, щоб користувачі змогли створювати посилання Onelink!!!
ADMIN-NOTIFICATION-DOMAIN_LIMIT_WAS_OVER = Команда ({$team}) досягла свого денного ліміту по доменам і хоче створити нове посилання 🤷‍♂️