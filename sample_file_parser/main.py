import os
from helper import check_file_content


def main():
    # Check that file name is existing in returned list
    name = "messages.log"
    if name in os.listdir():
        print("Existing!")

    check_file_content(name, 'error')


if __name__ == "__main__":
    main()
