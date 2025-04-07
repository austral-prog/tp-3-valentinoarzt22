def check_vowels():
    # Código a implementar utilizando input.
nombre = input('Ingresar nombre:' )
    if nombre.find('a') != -1:
        print('contiene a: True')
    else:
        print('Contiene a: False')
    if nombre.find('e') != -1:
        print('contiene e: True')
    else:
        print('Contiene e: False')
    if nombre.find('i') != -1:
        print('contiene i: True')
    else:
        print('Contiene i: False')
    if nombre.find('o') != -1:
        print('contiene o: True')
    else:
        print('Contiene o: False')
    if nombre.find('u') != -1:
        print('contiene u: True')
    else:
        print('Contiene u: False')
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
