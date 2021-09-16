import lh1al.test_one
from lh1al.test_one import var1 as variable
from lh1al.test_one import resolve_equation as function


def main():
    print("Hello World!")
    print(lh1al.test_one.var1)
    print(lh1al.test_one.var2)
    print(variable)
    x = lh1al.test_one.resolve_equation(2, 3, "*")
    print(x)
    y = function(2, 8, "*")
    print(y)


if __name__ == "__main__":
    main()
