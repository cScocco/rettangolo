# rettangolo.py: area del rettangolo
class Rettangolo(object):
    __base: float = 0.0
    __altezza: float = 0.0

    def __init__(self, b: float, h: float):
        """

        :type b: object
        :type h: float
        """
        self.__base = b
        self.__altezza = h

    def assegna(self, b: float, h: float):
        """

        :type h: float
        :type b: float
        """
        self.__base = b
        self.__altezza = h

    def area(self):
        """

        :rtype: float
        """
        return self.__base * self.__altezza


def main():
    tovaglia = Rettangolo(2, 1)
    tovaglia.assegna(2, 3)
    print("Area =", tovaglia.area())


# funzione principale
if __name__ == '__main__':
    main()
