from functions.write_file import write_file

def test():
    print(f'Test lorum write: {write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')

    print(f'Test lorum write: {write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')

    print(f'Test lorum write: {write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')


if __name__ == "__main__":
    test()