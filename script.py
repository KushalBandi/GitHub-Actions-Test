import os
import sys

EXPECTED_PARAM_1 = "Hello"
EXPECTED_PARAM_2 = "World"
EXPECTED_PARAM_3 = "!"


def check_secret(name, actual, expected):
    if actual == expected:
        print(f"{name} is correct.")
    else:
        print(f"{name} is incorrect.")
        sys.exit(1)


def main():
    test_param_1 = os.environ.get("TEST_PARAM_1")
    test_param_2 = os.environ.get("TEST_PARAM_2")
    test_param_3 = os.environ.get("TEST_PARAM_3")

    check_secret("TEST_PARAM_1", test_param_1, EXPECTED_PARAM_1)
    check_secret("TEST_PARAM_2", test_param_2, EXPECTED_PARAM_2)
    check_secret("TEST_PARAM_3", test_param_3, EXPECTED_PARAM_3)

    print("All secrets validated successfully.")


if __name__ == "__main__":
    main()
