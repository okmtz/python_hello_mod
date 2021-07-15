import numpy as np

def main():
    rand_int = np.random.randint(1, 10)
    if 0 <= rand_int < 3:
        print("hello world")
    elif 3 <= rand_int < 6:
        print("ハローワールド")
    elif 6 <= rand_int < 8:
        print("はろーわーるど")
    else:
        print("Hello World!!!")

if __name__ == "__main__":
    main()
