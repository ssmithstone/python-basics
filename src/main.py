from sys import stdin


def main():
    print("Learning Python")
    print("basics")
    print("Enter line of text")
    line = stdin.readline().strip()
    print(f"User input {line}")
    print("User input %s" % line)
    print("User input {}".format(line))


if __name__ == "__main__":
    main()
