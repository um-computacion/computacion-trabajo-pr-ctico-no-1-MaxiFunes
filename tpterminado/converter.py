def decimal_to_roman(number):
    """
    Convierte un número decimal a su representación en números romanos.
    
    Args:
        number (int): Número entero entre 1 y 3999
        python3 -m unittest tests/test_roman_converter.py
        python3 src/roman_converter.py

    Returns:
        str: Representación en números romanos del número decimal
    """
    if not isinstance(number, int):
        raise TypeError("El número debe ser un entero")
        
    if number < 1 or number > 3999:
        raise ValueError("El número debe estar entre 1 y 3999")
    
    # Diccionario de valores y símbolos romanos (ordenados de mayor a menor)
    val_symbols = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman_numeral = ""
    
    # Convertir el número a romano
    for val, symbol in val_symbols:
        while number >= val:
            roman_numeral += symbol
            number -= val
    
    return roman_numeral

if __name__ == "__main__":
    try:
        entrada = input("Ingrese un número entre 1 y 3999 para convertir a romano: ")
        numero = int(entrada)
        resultado = decimal_to_roman(numero)
        print(f"El número {numero} en romano es: {resultado}")
    except ValueError as e:
        if "El número debe estar entre 1 y 3999" in str(e):
            print(f"Error: {e}")
        else:
            print("Error: Debe ingresar un número entero válido.")
    except TypeError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")
