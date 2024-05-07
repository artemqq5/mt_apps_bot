MAIN_MENU = Menu
CHOUSE = Choice
CANCELED = Canceled

# register in bot
YOU_ARE_BLOKED = You are blocked
REGISTER_FAIL = Can`t register, try again later :/
REGISTER_SUCCESS = You are successfully registered!
YOU_NEED_BE_REGISTERED = To use this bot, you need to request access from the administrator and get a unique link

# team access (access list, delete, change status, generate access) ============================
TEAM_HAVENT_ACCESS = Team haven't access

WARNING_DELETE_ACCESS = Do you want to delete access?
SUCCESSFUL_DELETE_ACCESS = Successfully deleted access
ERROR_DELETE_ACCESS = Error delete access
    <code>{$error}</code>

CHOICE_NEW_STATUS_ACCESS = Choice new access status
SUCCESSFUL_CHANGE_STATUS_ACCESS = Successfully change access status. new status: <b>{$status}</b>
ERROR_CHANGE_STATUS_ACCESS = Error change access status
    <code>{$error}</code>

WARNING_GENERATE_KEY_TEAM = Do you want to generate key for <b>{$team_name}</b>?
SUCCESSFUL_GENERATE_TEAM = Successfully generate join key for <b>({$team_name})</b>.
    deeplink: <code>{$deeplink}</code>
ERROR_GENERATE_TEAM = Error generate join key
    <code>{$error}</code>

# team access (activate from user) ===========================================
INPUT_TEAM_KEY = Hello! You are not affiliated with any team. An administrator should send you your command key!
    Enter your command key:
JOIN_KEY_NOT_EXIST = Key not exist!
JOIN_KEY_ACTIVATED_BEFORE = Key had activated before!
JOIN_KEY_FAIL_UPDATE = Some error. Team key was not set
JOIN_KEY_SUCCESS_UPDATE = Team key was set successfully!

ACCESS_TEAM_NAME = Access({$team})

# team (create, team list, delete, change status, domain limit) ===========================================================
INPUT_TEAM_NAME = Enter a team name:
TEAM_NAME_TOO_LONG = Team name is too long. Send message up to 255 symbols
ERROR_CREATE_TEAM = Some error when try create team, try again
SUCCESSFUL_CREATE_TEAM = <b>{$team_name}</b> Team was created!

TEAM_LIST_IS_EMPTY = Team list is empty
TEAM_MENU = Team menu

WARNING_DELETE_TEAM = Do you want to delete <b>{$team_name}</b>?
    (The action cannot be undone!)
SUCCESSFUL_DELETE_TEAM = Successfully deleted <b>({$team_name})</b>
ERROR_DELETE_TEAM = Error delete team
    <code>{$error}</code>

CHOICE_NEW_STATUS_TEAM = Choice new team status for <b>{$team_name}</b>
SUCCESSFUL_CHANGE_STATUS_TEAM = Successfully change status for <b>({$team_name})</b>. new status: <b>{$status}</b>
ERROR_CHANGE_STATUS_TEAM = Error change team status
    <code>{$error}</code>

NEW_DOMAIN_LIMIT = New domain limit for team:
SET_LIMIT_SUCCESS = New daily limit ({$limit}) successfully set
SET_LIMIT_FAIL = Error setting new limit

# ban system ================================================================================
BANNED_USERS_EMPTY = Empty
INPUT_USER_BAN_MESSAGE = Input ban message (only admins can view it)
BAN_MESSAGE_TOO_LONG = Ban message is too long. Send message up to 255 symbols
INPUT_USER_ID_FOR_UNBAN = Enter telegram id:
INPUT_USER_ID_OR_USERNAME_FOR_BAN = (Enter telegram id or @username.
    For example id: 1201390139 or username: @aoksff (with @ first))
SUCCESSFUL_BANNED = User banned successfully
ERROR_BANNED = User not banned correctly
UNBAN_USER_SUCCESSFUL = User unbanned successfully
ERROR_UNBANNED = User not unbanned correctly, ID is correctly? Try again
SHOW_BANNED_USERS_LIST = <b>List of banned users</b>:
BANNED_USERS_LIST_EMPTY = <b>No banned users</b>

# settings (locale)
CHOICE_LANG = Choice lang
SUCCESSFUL_CHANGE_LANG = Successfully changed language to <b>{$lang}</b>
FAIL_CHANGE_LANG = Error language change (maybe you are trying to change the language to the one currently installed)

# applications (add, preview template, publish, show)
APP-SET_PLATFORM = What platform is the app for?
APP-SET_NAME = App Name:
APP-SET_BUNDLE = Specify the application bundle (IOS=1451177077, Android=com.af.smart):
APP-SET_IMAGE = An image for the application has been sent (not a file):
APP-SET_GEO = Specify open geo, for example (UA, AL, BR):
APP-SET_SOURCE = Specify which source the application is targeting:
APP-SET_DESC = Your comment\description:
APP-DEFAULT_DESC = To open GEO, contact support
APP-PREVIEW = Preview, see if everything is correct and publish Draft or go back to the beginning. ⚠️⚠️⚠️
APP-ALREADY_ADDED = This app has already been added, check in existing or database

APP-SUCCESS_PUBLISHED = You have successfully created an app with the status (Draft) to be seen by other users you need to activate it (change the status to Active).

    Masons Link: <code>{$masons}</code>

    <b>Also here is an organic campaign for this app</b>
    ID: <code>{$id}</code>
    Name: <code>{$name}</code>
    Link in Keitaro: <code>{$link}</code>
APP-FAIL_PUBLISHED = Failed to create the application, urgently need to look at the logs before they are lost ({$error})

APP-CHOICE_PLATFORM = Choose a platform
APP-APP_LIST_EMPTY = There are no applications for this platform
APP-IOS_APPS = IOS Apps:
APP-DESC_TEMPLATE = Name: <b>{$name_url}</b>

     ID: {$id}

     Platform: <b>{$platform}</b>
     Source: <b>{$source}</b>

     GEO: {$geo}

     Status: <b>{$status}</b>

     {$desc}

APP-GEO_EDIT_SUCCESSFUL = Geo successfully edited
APP-GEO_EDIT_FAIL = Error editing geo

APP-SET_STATUS = Specify new application status <b>{$name}</b>
APP-STATUS_EDIT_SUCCESS = The status of the application has been changed successfully
APP-STATUS_EDIT_FAIL = Error editing app status, you may be trying to change to the same status
APP-STATUS_NOTIFY_NEW_STATUS = Notify users about new app status ({$status})?

APP-DELETE_WARNING = Are you sure you want to delete the app <b>{$name}</b>? (it is not deleted from the database)
APP-DELETE_SUCCESS = App <b>{$name}</b> was successfully deleted and can be reinstalled directly from the database
APP-DELETE_FAIL = Error deleting application <b>{$name}</b>

#user(apps)
USER-CHOICE_PLATFORM_APP = Choose an app platform
USER-IOS_APPS = Available IOS Apps:
USER-DESC_TEMPLATE = Name: <b>{$name_url}</b>

     Platform: <b>{$platform}</b>
     Source: <b>{$source}</b>

     GEO: {$geo}

     {$desc}

# user (add pixel, show my pixel, delete pixel)
USER-ADD_PIXEL_ID = Submit Pixel ID:
USER-ADD_TOKEN_EAAG = Send Token EAAG:
USER-SUCCESS_ADD_PIXEL = Pixel added successfully
USER-FAIL_ADD_PIXEL = Failed to add pixel

USER-HAVENT_ANY_PIXEL = You have no pixels created
USER-YOUR_PIXELS = Your Pixels:
USER-PIXEL_INFO = Pixel ID: <code>{$pixel_id}</code>

     EAAG token: <code>{$token}</code>

     Pixel created: <b>{$date}</b>

USER-SUCCESS_DELETE_PIXEL = Pixel successfully deleted from library
USER-FAIL_DELETE_PIXEL = Failed to delete pixel

# flow user (create, show, edit)
FLOW-SELECT_PIXEL_FB = Select your pixel for flow:
FLOW-HAVENT_PIXEL_FB = You have no created pixels, want to create one?
FLOW-COMMENT = Add a comment to the flow
FLOW-OFFER_LINK = Send your link
FLOW-OFFER_LINK_ERROR = Attention! The link must have the mandatory macro ={$subid} and start with https://
     For example https://example.site/test?asdpg={$subid} - is a minimal example!
FLOW-FLOW_SUCCESS_CREATED = Flow successfully created, we wish you quality traffic!
     <code>{$flow}</code>
FLOW-FLOW_FAIL_CREATED = Failed to create flow ({$error}), forward this message to admin

FLOW-MY_FLOWS = My Flows
FLOW-DETAIL_FLOW = <b>Your working link:</b>
     <code>{$link_keitaro}</code>

     ====================================
     <b>ID:</b> {$id}
     <b>Created date: </b> {$date}

     <b>App:</b> {$app_name}
     <b>Platform:</b> {$platform}
     <b>Source:</b> {$source}
     <b>App Status:</b> {$status}

     <b>Domain:</b> <code>{$domain}</code>
     <b>Your offer\tracker:</b> <code>{$link_user}</code>

     <b>Pixel ID:</b> {$pixel}
     <b>Token:</b> {$token}

     <b>GEO:</b> {$geo}

     <b>Comment:</b> {$comment}

     ⚠️ To open GEO, contact support ⚠️
FLOW-HAVNT_FREE_DOMAINS = There are no free domains, a message has been sent to the admin, they will be replenished soon!
FLOW-DOMAIN_LIMIT_OVER = Daily domain limit for your team exceeded ({$limit})
     To increase the daily limit, write to support

# COMMENT
FLOW-EDIT-NEW_COMMENT = Enter a new comment for the flow:
FLOW-EDIT-NEW_COMMENT_SUCCESS = Flow comment successfully updated!
FLOW-EDIT-NEW_COMMENT_FAIL = Failed to update comment, write to support
# PIXEL
FLOW-EDIT-NEW_PIXEL = Select new PIXEL
FLOW-EDIT-NEW_PIXEL_SUCCESS = New PIXEL installed successfully
FLOW-EDIT-NEW_PIXEL_FAIL = Failed to replace your PIXEL ({$error}), try again or write to support, they will help you!
# OFFER
FLOW-EDIT-NEW_OFFER = Enter new offer/tracker link:
FLOW-EDIT-NEW_OFFER_SUCCESS = Your link has been updated!
FLOW-EDIT-NEW_OFFER_FAIL = Failed to update your link ({$error}), please try again or contact support, they will help you!
# APPS
FLOW-EDIT-NEW_APP = Select new app:
FLOW-EDIT-NEW_APP_SUCCESS = Your app has been replaced!
FLOW-EDIT-NEW_APP_FAIL = Failed to replace your app ({$error}), try again or write to support, they will help you!

# notification
NOTIFY-CATEGORY = Select a category for notification
NOTIFY-MESSAGE = Enter the message text:
NOTIFY-MEDIA = Send photo\gif\video in compressed format (not file)
NOTIFY-BUTTON_URL = Enter the URL for the button:
NOTIFY-BUTTON_URL_VALIDATION = Link must start with https://
NOTIFY-BUTTON_TEXT = Enter the text for the button (up to 50 characters):
NOTIFY-BUTTON_TEXT_LIMIT = up to 50 characters:
NOTIFY-PREVIEW = If everything is correct, send to users, they will receive exactly the same message
NOTIFY-RESULT = <b>=== Notification result ===</b>

    <b>{$get}\{$users}</b> - received your messages
    ======================
    Bot blocked: <b>{$block}</b>
    Other: <b>{$other}</b>

# ban, active notification
NOYIFY-APP_STATUS_BAN = App <b>{$app_name}</b> has been banned‼️

    Stop traffic!
NOYIFY-APP_STATUS_ACTIVE = App <b>{$app_name}</b> is active! ✅
NOYIFY-APP_STATUS_DRAFT = App <b>{$app_name}</b> will be temporarily unavailable for new threads, but feel free to stop old ones, the app is fine!

#admin notification
ADMIN-NOTIFICATION-HAVENT_DOMAIN = 🆘 Domains have run out 🆘
    Urgently replenish the domains in keitaro so that users can create links Onelink!!!
ADMIN-NOTIFICATION-DOMAIN_LIMIT_WAS_OVER = Team ({$team}) has reached its daily domain limit and wants to create a new link 🤷‍♂️
