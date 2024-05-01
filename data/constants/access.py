ADMIN = "admin"
USER = "user"

# states for teams
Trial_TEAM = "Trial"
Basic_TEAM = "Basic"
Standard_TEAM = "Standard"
Premium_TEAM = "Premium"
Ultimate_TEAM = "Ultimate"

TEAM_STATUS_LIST = (Trial_TEAM, Basic_TEAM, Standard_TEAM, Premium_TEAM, Ultimate_TEAM)

Byer_ACCESS = "Buyer"
TeamLead_ACCESS = "TeamLead"

ACCESS_STATUS_LIST = (Byer_ACCESS, TeamLead_ACCESS)

# states for apps
DRAFT_APP_STATUS = "Draft"
ACTIVE_APP_STATUS = "Active"
BANNED_APP_STATUS = "Banned"

APP_STATUS_LIST = (ACTIVE_APP_STATUS, BANNED_APP_STATUS)

MACROS = "{subid}"


def validate_user_link(link: str) -> bool:
    return link.startswith("https://") and link.__contains__(MACROS)


# source app
ONELINK = "onelink"

# desc localization
DEFAULT_DESC = "default"


