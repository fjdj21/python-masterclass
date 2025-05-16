def is_anagram(string1: str, string2: str) -> bool:
    def cleanstring(s):
        return ''.join([c.lower() for c in s if c.isalpha()])

    return sorted(cleanstring(string1)) == sorted(cleanstring(string2))

is_anagram("Astronomer", "Moon starer")  # → True
is_anagram("Hello", "Olelh")            # → True
is_anagram("Hi there", "Bye there")     # → False
