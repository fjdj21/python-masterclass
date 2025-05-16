import inspect

def print_ruler(with_line_number=True):
    ruler = "--" * 30
    if with_line_number:
        print(ruler, f"(line {inspect.currentframe().f_back.f_lineno})")
    else:
        print(ruler)

def ruler(char="-", width=80, default=False):
    """
    Print a horizontal ruler line using a specified character and width.

    if `default` is True, also prints the caller's line number.

    :param default: If true, include the caller's line number
        in the output.
    :param char: The character to use for the ruler line.
        Defaults to "*".
    :param width: The total width of the ruler line. Defaults to 80
    :return: None
    """
    if default:
        print(char * width, f"(line {inspect.currentframe().f_back.f_lineno})")
    else:
        print(char * width)

def banner(text=" ", fill_char='-', width=80):
    """
    Prints a formatted banner message, centered and optionally
    fill character.

    :param text: Message to display. Defaults to single space
    :param width: Total width of the banner, including fill characters.
        Defaults to 80.
    :param fill_char: character used to fill the empty space around
        the text. Defaults to '-'.
    :raises ValueError: If the length exceeds (width - 4).
    """
    if len(text) > width - 4:
        raise ValueError(f"String '{text}' is larger than "
                         f"specified width '{width}'", 60)

    if text == "*":
        print("*" * width)
    else:
        output_string = f"{text.center(width, fill_char)}"
        print(output_string.upper())


"""-------Some ANSI escape sequences for colours and effects---------"""
# ANSI escape sequences for colours and effects
COLORS = {
    "BLACK": '\u001b[30m',
    "RED": '\u001b[31m',
    "GREEN": '\u001b[32m',
    "YELLOW": '\u001b[33m',
    "BLUE": '\u001b[34m',
    "MAGENTA": '\u001b[35m',
    "CYAN": '\u001b[36m',
    "WHITE": '\u001b[37m',
    "RESET": '\u001b[0m',
    "BOLD": '\u001b[1m',
    "UNDERLINE": '\u001b[4m',
    "REVERSE": '\u001b[7m',
}
# Extract constants from the dictionary for direct use
BLACK = COLORS["BLACK"]
RED = COLORS["RED"]
GREEN = COLORS["GREEN"]
YELLOW = COLORS["YELLOW"]
BLUE = COLORS["BLUE"]
MAGENTA = COLORS["MAGENTA"]
CYAN = COLORS["CYAN"]
WHITE = COLORS["WHITE"]
RESET = COLORS["RESET"]
BOLD = COLORS["BOLD"]
UNDERLINE = COLORS["UNDERLINE"]
REVERSE = COLORS["REVERSE"]


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using ANSI escape sequences to apply color
    and styling effects.

    :param text: Text to print.
    :param effects: One or more ANSI escape code constants
        (like RED, BOLD, REVERSE) used to style the text.
        These should be defined constants.
    """
    effect_string = "".join(effects)
    output_string = f"{effect_string}{text}{RESET}"
    print(output_string)
