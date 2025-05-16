from z_debuggers import ruler, banner

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

banner("my code")
print(f"This is how to use to {RED}color{RESET} specific text")
print(RED, "This will be in red", RESET)
print(f"test")
ruler('-')


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

colour_print("Hello, Red", RED)
colour_print("Hello, Red", RED, BOLD)
# test that the colour was reset
print("This should be in the default terminal colour.")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Blue reversed", BLUE, REVERSE)
colour_print("Hello, Blue reversed and underlined", BLUE, REVERSE, UNDERLINE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Yellow bold", YELLOW, BOLD)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
ruler()
