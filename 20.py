# s = "()"
# s = "()[]{}"
# s = "(]"
s = "{[]}"


# def is_valid(self, s: str) -> bool:
def is_valid(s: str) -> bool:

    parentheses = [
        {"open": "(", "close": ")"},
        {"open": "[", "close": "]"},
        {"open": "{", "close": "}"}
    ]

    i = 0

    while i < len(s):
        current_symbol = s[i]

        if i < len(s) - 1:
            next_symbol = s[i+1]
        else:
            return False

        for p in range(len(parentheses)):
            if current_symbol == parentheses[p]["open"]:
                if next_symbol == parentheses[p]["close"]:
                    i += 2
                else:
                    return False

    return True

    # parentheses = {
    #     "open": ["(", "[", "{"],
    #     "close": [")", "]", "}"]
    # }


print(is_valid(s))
