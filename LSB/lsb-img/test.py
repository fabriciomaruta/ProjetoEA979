import random

def randomizeOne():
    random.seed(9001)
    listOne = random.sample(range(20), 10)
    for i in range(10):
        print(listOne[i])

def randomizeTwo():
    random.seed(9001)
    listTwo = random.sample(range(20), 10)
    for i in range(10):
        print(listTwo[i])

def main():
    randomizeOne()
    print("-----")
    randomizeTwo()


if __name__ == "__main__":
    main()