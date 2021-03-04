import math


class RandomNumberGenerator:
    def __init__(self, seedValue=None):
        self.__seed = seedValue

    def nextInt(self, low, high):
        m = 2147483647
        a = 16807
        b = 127773
        c = 2836
        k = int(self.__seed / b)
        self.__seed = a * (self.__seed % b) - k * c
        if self.__seed < 0:
            self.__seed = self.__seed + m
        value_0_1 = self.__seed
        value_0_1 = value_0_1 / m
        return low + int(math.floor(value_0_1 * (high - low + 1)))

    def nextFloat(self, low, high):
        low *= 100000
        high *= 100000
        val = self.nextInt(low, high) / 100000.0
        return val


def main():
    seed = int(input("Enter Z number: "))
    generator = RandomNumberGenerator(seed)
    task_number = int(input("Enter tasks number: "))
    tasks = range(1, task_number + 1)
    rj = []
    pj = []

    for _ in tasks:
        pj.append(generator.nextInt(1, 29))

    sum = 0

    for num in pj:
        sum += num

    for _ in tasks:
        rj.append(generator.nextInt(1, sum))

    print("Rj: {} \nPj: {}".format(rj, pj))

    rj.sort()
    pj.sort()

    print("\nSorted\nRj: {} \nPj: {}".format(rj, pj))

if __name__ == "__main__":
    main()


