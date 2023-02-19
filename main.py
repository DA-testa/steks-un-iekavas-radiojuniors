# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            if opening_brackets_stack == [] or are_matching(opening_brackets_stack[-1].char, next) == False:
                return i+1
            else:
                opening_brackets_stack.pop()
                pass

    if opening_brackets_stack == []:
        return "Success"
    else:
        return opening_brackets_stack[-1].position + 1


def main():
    inp = input()
    if inp.capitalize() == "I":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)


if __name__ == "__main__":
    main()
