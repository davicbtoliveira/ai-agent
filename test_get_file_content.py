from functions.get_file_content import get_file_content

def test():
    print("Result:")
    print(get_file_content("calculator", "main.py"))

    print("Result:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("Result:")
    print(get_file_content("calculator", "/bin/cat"))

    print("Result:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test()
