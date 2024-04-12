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

# team (create, team list, delete, change status) ===========================================================
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
    {$list}

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
APP-SET_SOURCE = Specify under which sources, for example (Facebook deeplink or onelink):
APP-SET_DESC = Your comment\description:
APP-PREVIEW = Preview, see if everything is correct and publish Draft or go back to the beginning. ⚠️⚠️⚠️

APP-SUCCESS_PUBLISHED = You have successfully created an app with the status (Draft), so that it can be seen by other users, you need to activate it (change the status to Active)
APP-FAIL_PUBLISHED = Failed to create the application, urgently need to look at the logs before they are lost ({$error})

APP-CHOICE_PLATFORM = Choose a platform
APP-APP_LIST_EMPTY = There are no applications for this platform
APP-IOS_APPS = IOS Apps:
APP-DESC_TEMPLATE = Name: <b>{$name_url}</b>

     Platform: <b>{$platform}</b>
     Sources: <b>{$source}</b>

     GEO: {$geo}

     Status: <b>{$status}</b>

     {$desc}

APP-GEO_EDIT_SUCCESSFUL = Geo successfully edited
APP-GEO_EDIT_FAIL = Error editing geo

APP-SET_STATUS = Specify new application status <b>{$name}</b>
APP-STATUS_EDIT_SUCCESS = The status of the application has been changed successfully
APP-STATUS_EDIT_FAIL = Error editing app status, you may be trying to change to the same status

APP-DELETE_WARNING = Are you sure you want to delete the app <b>{$name}</b>? (it is not deleted from the database)
APP-DELETE_SUCCESS = App <b>{$name}</b> was successfully deleted and can be reinstalled directly from the database
APP-DELETE_FAIL = Error deleting application <b>{$name}</b>

#user(apps)
USER-CHOICE_PLATFORM_APP = Choose an app platform
USER-IOS_APPS = Available IOS Apps:
USER-DESC_TEMPLATE = Name: <b>{$name_url}</b>

     Platform: <b>{$platform}</b>
     Sources: <b>{$source}</b>

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