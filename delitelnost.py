
def jeDelitelneTremi(number):
    if number % 3 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    number = input("Zadejte cislo: ")
    number = int(number)
    if jeDelitelneTremi(number):
        print(f"Cislo {number} je delitelne 3.")
    else:
        print(f"Cislo {number} neni delitelne 3.")