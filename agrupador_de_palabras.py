ids = []
palabras = []
categorias = []
idiomas = []
cantidades_letras = []
fechas = []
descripciones = []
while True:
    print("menu principal agrupador de palabras")
    print("1) crear palabra")
    print("2) editar palabra")
    print("3) eliminar palabra")
    print("4) buscar palabra")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-------------------#
    #--|crear_palabra|--#
    #-------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_palabra = 1
        else:
            id_palabra = ids[-1] + 1
        palabra = input("palabra: ")
        categoria = input("categoría: ")
        idioma = input("idioma: ")
        cantidad_letras = int(input("cantidad de letras: "))
        fecha = input("fecha: ")
        descripcion = input("descripción: ")
        ids.append(id_palabra)
        palabras.append(palabra)
        categorias.append(categoria)
        idiomas.append(idioma)
        cantidades_letras.append(cantidad_letras)
        fechas.append(fecha)
        descripciones.append(descripcion)
        print("palabra registrada correctamente.")
        print("id:", id_palabra)
    #--------------------#
    #--|editar_palabra|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar palabra")
            for i in range(len(ids)):
                print(f"{ids[i]} | {palabras[i]} | {categorias[i]} | {idiomas[i]} | {cantidades_letras[i]} | {fechas[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {palabras[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {cantidades_letras[posicion]} | {fechas[posicion]} | {descripciones[posicion]}")
                palabras[posicion] = input("nueva palabra: ")
                categorias[posicion] = input("nueva categoría: ")
                idiomas[posicion] = input("nuevo idioma: ")
                cantidades_letras[posicion] = int(input("nueva cantidad de letras: "))
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_palabra|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar palabra")
            for i in range(len(ids)):
                print(f"{ids[i]} | {palabras[i]} | {categorias[i]} | {idiomas[i]} | {cantidades_letras[i]} | {fechas[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {palabras[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {cantidades_letras[posicion]} | {fechas[posicion]} | {descripciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    palabras.pop(posicion)
                    categorias.pop(posicion)
                    idiomas.pop(posicion)
                    cantidades_letras.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_palabra|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar palabra")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {palabras[posicion]} | {categorias[posicion]} | {idiomas[posicion]} | {cantidades_letras[posicion]} | {fechas[posicion]} | {descripciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = cantidades_letras[0]
            menor = cantidades_letras[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {palabras[i]} | {categorias[i]} | {idiomas[i]} | {cantidades_letras[i]} | {fechas[i]} | {descripciones[i]}")
                suma += cantidades_letras[i]
                if cantidades_letras[i] > mayor:
                    mayor = cantidades_letras[i]
                if cantidades_letras[i] < menor:
                    menor = cantidades_letras[i]
            promedio = suma / len(ids)
            print("estadísticas agrupador de palabras")
            print("cantidad de palabras:", len(ids))
            print("total de letras:", suma)
            print("promedio de letras:", round(promedio, 2))
            print("palabra con más letras:", mayor)
            print("palabra con menos letras:", menor)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el agrupador de palabras.")
        break
    else:
        print("opción no válida.")