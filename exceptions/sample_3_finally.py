if __name__ == '__main__':
    try:
        file = open("temp.txt")
        file.write("Ala ma kota")
    except IOError:
        print("Wystąpił błąd podczas przetwarzania pliku!")
    finally:
        file.close()
