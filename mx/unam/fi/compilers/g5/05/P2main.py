# importamos la biblioteca para el uso de expresiones regulares
import re


def testRE(codigo, solucion, match, nmatch):
    print("Probando ejercicio " + str(codigo) + ":\n")
    re = solucion
    count = 0
    mismatches = 0
    for cadena in match:
        count += 1
        output = re.fullmatch(cadena)  # verificamos que la cadena de prueba hace match con la ER correspondiente
        mensaje = "correcto"
        if output:
            print("\t Acierto: la cadena '{}' coincide con la ER '{}' como se esperaba".format(cadena.strip(),
                                                                                               re.pattern))
        elif not output:
            print("\t\033[92m Error  \033[0m: la cadena '{}' debería coincidir con la ER '{}'".format(cadena.strip(),
                                                                                                      re.pattern))
            mismatches += 1
    print("\n")
    for cadena in nmatch:
        count += 1
        output = re.fullmatch(cadena)  # verificamos que la cadena de prueba hace match con la ER correspondiente
        mensaje = "correcto"
        if not output:
            print("\t Acierto: la cadena '{}' no coincide con la ER '{}' como se esperaba".format(cadena.strip(),
                                                                                                  re.pattern))
        elif output:
            print("\t Error  : la cadena '{}' no debería coincidir con la ER '{}'".format(cadena.strip(), re.pattern))
            mismatches += 1
    if count == 0:
        print("ALERTA:No hay cadenas de prueba para el ejercicio " + str(codigo))
    elif count < 10:
        print("\nALERTA: No hay suficientes cadenas de prueba para el ejercicio " + str(
            codigo) + ", se sugiere probar con al menos 5 cadenas en el lenguaje y 5 cadenas que no pertenecen al "
                      "lenguaje.")
    elif mismatches != 0:
        print("\nALERTA: La solución para el ejercicio " + str(
            codigo) + " no parece no ser la respuesta correcta, ya que no pasó " + str(mismatches) + " de las pruebas")
    else:
        print("\nEjercicio " + str(
            codigo) + ": CORRECTO (La solución parece ser la respuesta correcta, ya que pasó todas las pruebas)")


with open("./expresiones.py") as f:
    exec(f.read())
    for codigo in ejercicios:
        testRE(codigo, ejercicios[codigo], pruebas_match[codigo], pruebas_nmatch[codigo])
        print("")
