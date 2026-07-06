import os

def main():
    param_1 = os.environ.get("PARAM_1")
    param_2 = os.environ.get("PARAM_2")
    param_3 = os.environ.get("PARAM_3")

    print(f"param_1: {param_1}")
    print(f"param_2: {param_2}")
    print(f"param_3: {param_3}")

if __name__ == "__main__":
    main()
