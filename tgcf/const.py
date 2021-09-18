"""Declare all global constants."""

COMMANDS = {
    "start": "Check whether I am alive",
    "forward": "Settings for Bot",
    "remove": "Update the bot",
    "help": "Contact @Gamer_4560",
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.yml"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"


class BotMessages:
    """Messages given by the bot to users."""

    # pylint: disable=too-few-public-methods
    start = "Hi! I am alive"
    bot_help = "Buy Your Own Bot @Gamer_4560"
