import sys
from helper import check_file_content


def main():
    # Check that file name is existing in returned list
    print("Script name {}".format(sys.argv[0]))
    try:
        name = sys.argv[1]
        if len(sys.argv) > 2:
            print("Too many args")
            sys.exit()
    except(IndexError, UnboundLocalError):
        print("Sorry you provided too less argument")
        sys.exit()

    try:
        print(check_file_content(name, 'error'))
        print(check_file_content(name, 'test'))
        print(check_file_content(name, 'warning'))
        print(check_file_content(name, 'log'))
    except FileNotFoundError as error:
        print("{}".format(error))


# Execution
if __name__ == "__main__":
    main()