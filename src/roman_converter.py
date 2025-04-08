def decimal_to_roman(number):
    if not isinstance(number, int):
        raise TypeError("El número debe ser un entero")
        
    if number < 1 or number > 3999999:
        raise ValueError("El número debe estar entre 1 y 3999999")
    
    # Valores y símbolos romanos normales y con línea (multiplicados por 1000)
    val_symbols = [
        (1000000, "M̅"), (900000, "C̅M̅"), (500000, "D̅"), (400000, "C̅D̅"),
        (100000, "C̅"), (90000, "X̅C̅"), (50000, "L̅"), (40000, "X̅L̅"),
        (10000, "X̅"), (9000, "I̅X̅"), (5000, "V̅"), (4000, "I̅V̅"),
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman_numeral = ""
    
    for val, symbol in val_symbols:
        while number >= val:
            roman_numeral += symbol
            number -= val
    
    return roman_numeral

if __name__ == "__main__":
    try:
        entrada = input("Ingrese un número entre 1 y 3999999 para convertir a romano: ")
        numero = int(entrada)
        resultado = decimal_to_roman(numero)
        print(f"El número {numero} en romano es: {resultado}")
        print("Nota: Los símbolos con línea superior (M̅, D̅, C̅, L̅, X̅, V̅, I̅) representan miles.")
    except ValueError as e:
        if "El número debe estar entre" in str(e):
            print(f"Error: {e}")
        else:
            print("Error: Debe ingresar un número entero válido.")
    except TypeError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")
