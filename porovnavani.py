def jeVetsiNezTri(value, constantValue):
    if value > 3:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    value = input("Zadej cislo: ")
    value = int(value)
    constantValue = input("Zadej cislo na porovnani: ")
    constantValue = int(constantValue)
    if jeVetsiNezTri(value, constantValue):
        print(f"Cislo {value} je vetsi nez {constantValue}.")
    else:
        print(f"Cislo {value} je mensi nez {constantValue}.")
