from collections import deque


def is_palindrome(s: str) -> bool:
    char_deque = deque("".join(s.casefold().split()))

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


def main():
    test_strings = ["Tenet", "mom", "racecar", "  dad   ", "a", "hello", "World", "a a"]

    for s in test_strings:
        res = is_palindrome(s)
        print(f"Is '{s}' palindrome: {res}")


if __name__ == "__main__":
    main()