import os
import platform


# print("Name of OS {}".format(os.name))
# print("System is {}".format(platform.system()))
# print("Relese is {}".format(platform.release()))
# print("platform is {}".format(platform.platform()))
# print("proces is {}".format(platform.processor()))
# print("Architecture is {}".format(platform.machine()))


def os_param():
    os_values_dict = {'system': platform.system(),
                      'name': os.name,
                      'release': platform.release(),
                      'uname': platform.uname(),
                      'cpu': platform.processor(),
                      'architecture': platform.machine()
                      }
    for k, v in os_values_dict.items():
        print("{}: {}".format(k, v))


def main():
    print(os_param())


if __name__ == "__main__":
    main()