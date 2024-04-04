MAIN_MENU = Menu

# register in bot
YOU_ARE_BLOKED = You are blocked
REGISTER_FAIL = Can`t register, try again later :/
REGISTER_SUCCESS = You are successfully registered!
SEND_REQUEST_TO_ADMIN = Request to get access has sent to admin! Admin will give you pass key to use this bot

# team access (access list, delete, change status, generate access) ============================
TEAM_HAVENT_ACCESS = Team haven't access

WARNING_DELETE_ACCESS = Do you want to delete access?
SUCCESSFUL_DELETE_ACCESS = Successfully deleted access
ERROR_DELETE_ACCESS = Error delete access {"\n"}<code>{$error}</code>

CHOICE_NEW_STATUS_ACCESS = Choice new access status
SUCCESSFUL_CHANGE_STATUS_ACCESS = Successfully change access status. new status: <b>{$status}</b>
ERROR_CHANGE_STATUS_ACCESS = Error change access status {"\n"}<code>{$error}</code>

WARNING_GENERATE_KEY_TEAM = Do you want to generate key for <b>{$team_name}</b>?
SUCCESSFUL_GENERATE_TEAM = Successfully generate join key for <b>({$team_name})</b>.{"\n"}{"\n"} deeplink: <code>{$deeplink}</code>
ERROR_GENERATE_TEAM = Error generate join key {"\n"}<code>{$error}</code>

# team access (activate from user) ===========================================
INPUT_TEAM_KEY = Hello! You are not affiliated with any team. An administrator should send you your command key!{"\n"}{"\n"}Enter your command key:
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

WARNING_DELETE_TEAM = Do you want to delete <b>{$team_name}</b>? {"\n"}{"\n"}(The action cannot be undone!)
SUCCESSFUL_DELETE_TEAM = Successfully deleted <b>({$team_name})</b>
ERROR_DELETE_TEAM = Error delete team {"\n"}<code>{$error}</code>

CHOICE_NEW_STATUS_TEAM = Choice new team status for <b>{$team_name}</b>
SUCCESSFUL_CHANGE_STATUS_TEAM = Successfully change status for <b>({$team_name})</b>. new status: <b>{$status}</b>
ERROR_CHANGE_STATUS_TEAM = Error change team status {"\n"}<code>{$error}</code>

# ban system ================================================================================
BANNED_USERS_EMPTY = Empty
INPUT_USER_BAN_MESSAGE = Input ban message (only admins can view it)
BAN_MESSAGE_TOO_LONG = Ban message is too long. Send message up to 255 symbols
INPUT_USER_ID_FOR_UNBAN = Enter telegram id:
INPUT_USER_ID_OR_USERNAME_FOR_BAN = (Enter telegram id or @username.{"\n"}
                                     For example id: 1201390139 or username: @aoksff (with @ first))
SUCCESSFUL_BANNED = User banned successfully
ERROR_BANNED = User not banned correctly
UNBAN_USER_SUCCESSFUL = User unbanned successfully
ERROR_UNBANNED = User not unbanned correctly, ID is correctly? Try again
