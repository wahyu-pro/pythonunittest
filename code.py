class PythonUnitTest:
    @staticmethod
    def count(arg):
        str = arg
        total = 0

        for i in str:
            total = total + 1
        return total

    @staticmethod
    def grade(arg):
        number = arg
        if number >= 90:
            return "A"
        elif (number >= 80) and (number <= 89):
            return "B"
        elif (number >= 70) and (number <= 79):
            return "C"
        elif (number >= 60) and (number <= 69):
            return "D"
        elif number <= 59:
            return "E"

    @staticmethod
    def oddoreven(arg):
        num = arg
        if (num % 2) == 0:
            return "Genap"
        elif(num % 2) == 1:
            return "Ganjil"

    @staticmethod
    def kabisat(arg):
        tahun = arg
        if (tahun % 4) == 0:
            if (tahun % 100) == 0:
                if (tahun % 400) == 0:
                    return "Tahun Kabisat"
                else:
                    return "Bukan Tahun Kabisat"
            else:
                return "Tahun Kabisat"
        else:
            return "Bukan Tahun Kabisat"

    @staticmethod
    def filmRate(arg):
        rateFilm = arg
        if rateFilm >= 21:
            return "Dewasa"
        elif rateFilm >= 13:
            return "Remaja"
        elif rateFilm >= 9:
            return "BIMBINGAN ORANG TUA"
        elif rateFilm < 9:
            return "SEMUA USIA"

    @staticmethod
    def loop_with_range(arg1, arg2):
        bil = []
        inp1 = arg1
        inp2 = arg2
        inp3 = inp2+1
        rentangAngka = range(inp1, inp3)

        for i in rentangAngka:
            bil.append(i)
        return bil

    @staticmethod
    def even1_100():
        prime = list()
        for x in range(1, 100):
            if  x % 2 == 1:
                prime.append(x)
            else:
                pass
        return prime

    @staticmethod
    def odd_even_multiples():
        for i in range(1, 1001):
            if (i % 2) == 1:
                if (i % 5) == 0:
                    if __name__ == "__main__":
                        print(i, "Ganjil kelipatan 5")
                else:
                    if __name__ == "__main__":
                        print(i, "Ganjil")
            elif (i % 2) == 0:
                if (i % 5) == 0:
                    if (i % 100) == 0:
                        if __name__ == "__main__":
                            print(i, "kelipatan 100")
                    else:
                        if __name__ == "__main__":
                            print(i, "Genap kelipatan 5")
                else:
                    if __name__ == "__main__":
                        print(i, "Genap")

    @staticmethod
    def reverseword(arg):
        text = arg
        pish = text.split()
        rev = " ".join(reversed(pish))
        return rev

    @staticmethod
    def addtoarray():
        stuff = ['Meja', 'Buku', 'Topi', 'Baju', 'Kayu']
        stuff.insert(0, 'Handuk')
        stuff.append('celana')
        return stuff