from functions.get_file_content import get_file_content

def test():
    print(f'Result for main.py is: {get_file_content("calculator", "lorem.txt")}')

    print(f'Result for main.py is: {get_file_content("calculator", "main.py")}')

    print(f'Result for main.py is: {get_file_content("calculator", "pkg/calculator.py")}')

    print(f'Result for main.py is: {get_file_content("calculator", "/bin/cat")}')

    print(f'Result for main.py is: {get_file_content("calculator", "pkg/does_not_exist.py")}')


if __name__ == "__main__":
    test()