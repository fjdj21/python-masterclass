from z_debuggers import print_ruler

def banner_text(text: str = " ", width: int = 80):
    """
    Display a centered banner message, wrapped with asterisks on either
    side for formatting.

    :param text: The message to display. If set to '*', a full-width
        line of asterisks will be printed instead.
    :param width: Total width of the banner including the '**' border.
        Default is 80.
    :return: None. The function prints banner directly
    :raises ValueError: If the length of `text` exceeds `width -4`,
        meaning it cannot fit between the asterisk borders.
    """
    if len(text) > width - 4:
        raise ValueError(f"String '{text}' is larger than "
                         f"specified width '{width}'", 60)

    if text == "*":
        print("*" * width)
    else:
        output_string = f"**{text.center(width - 4)}**"
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten, ", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(width=60)
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps, ", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)
banner_text()
