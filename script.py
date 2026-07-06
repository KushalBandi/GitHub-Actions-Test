import os
import sys


def check_secret_exists(name):
    value = os.environ.get(name)

    if value:
        print(f"{name} exists.")
    else:
        print(f"{name} is missing or empty.")
        sys.exit(1)


def main():
    check_secret_exists("TEST_PARAM_1")
    check_secret_exists("TEST_PARAM_2")
    check_secret_exists("TEST_PARAM_3")

    print("All required secrets are present.")


if __name__ == "__main__":
    main()
