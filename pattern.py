import sys


def build_pattern(n):
    return "\n".join("a" * count for count in range(1, n + 1))


def main():
    data = sys.stdin.read().strip()
    if not data:
        return

    n = int(data)
    pattern = build_pattern(n)
    if pattern:
        print(pattern)
