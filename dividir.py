def dividir(a, b):
    """
    Divide dos números.
    Maneja el caso de división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b
