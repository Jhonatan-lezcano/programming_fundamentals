def col_a_indice(col):
    return ord(col.upper()) - ord('A')

def indice_a_col(indice):
    return chr(ord('A') + indice)

def parsear_celda(ref_celda):
    col = col_a_indice(ref_celda[0])
    fila = int(ref_celda[1:]) - 1
    return fila, col

def imprimir_hoja(hoja, F, C):
    encabezados = [indice_a_col(i) for i in range(C)]
    print("\t" + "\t".join(encabezados))
    
    max_fila_con_datos = -1
    for i in range(F):
        for j in range(C):
            if hoja[i][j] is not None:
                max_fila_con_datos = max(max_fila_con_datos, i)
    
    for i in range(max_fila_con_datos + 1):
        max_col_con_datos = -1
        for j in range(C):
            if hoja[i][j] is not None:
                max_col_con_datos = max(max_col_con_datos, j)
        
        if max_col_con_datos == -1:
            print(f"{i+1}")
        else:
            valores_fila = []
            for j in range(max_col_con_datos + 1):
                if hoja[i][j] is not None:
                    valores_fila.append(str(hoja[i][j]))
                else:
                    valores_fila.append("")
            print(f"{i+1}\t" + "\t".join(valores_fila))

casos = int(input())
for _ in range(casos):
    F = int(input())
    C = int(input())
    hoja = [[None for _ in range(C)] for _ in range(F)]
    
    lineas = []
    while True:
        linea = input().strip()
        if linea == ".":
            break
        lineas.append(linea)
    
    for linea in lineas:
        if "=SUMA(" not in linea:
            if ":" in linea.split("=")[0]:
                coordenadas, valor = linea.split("=")
                celda_inicio, celda_fin = coordenadas.split(":")
                valor = int(valor)
                
                fila_inicio, col_inicio = parsear_celda(celda_inicio)
                fila_fin, col_fin = parsear_celda(celda_fin)
                
                if fila_inicio == fila_fin:
                    for j in range(col_inicio, col_fin + 1):
                        hoja[fila_inicio][j] = valor
                elif col_inicio == col_fin:
                    for i in range(fila_inicio, fila_fin + 1):
                        hoja[i][col_inicio] = valor
            else:
                coordenada, valor = linea.split("=")
                fila, col = parsear_celda(coordenada)
                hoja[fila][col] = int(valor)
    
    cambio = True
    while cambio:
        cambio = False
        for linea in lineas:
            if "=SUMA(" in linea:
                objetivo, expresion = linea.split("=")
                fila_objetivo, col_objetivo = parsear_celda(objetivo)
                
                if hoja[fila_objetivo][col_objetivo] is not None:
                    continue
                
                contenido_suma = expresion[5:-1]
                partes = contenido_suma.split(";")
                total = 0
                puede_evaluar = True
                
                for parte in partes:
                    if ":" in parte:
                        celda_inicio, celda_fin = parte.split(":")
                        fila_inicio, col_inicio = parsear_celda(celda_inicio)
                        fila_fin, col_fin = parsear_celda(celda_fin)
                        
                        if fila_inicio == fila_fin:
                            for j in range(col_inicio, col_fin + 1):
                                if hoja[fila_inicio][j] is not None:
                                    total += hoja[fila_inicio][j]
                        elif col_inicio == col_fin:
                            for i in range(fila_inicio, fila_fin + 1):
                                if hoja[i][col_inicio] is not None:
                                    total += hoja[i][col_inicio]
                    else:
                        fila_ref, col_ref = parsear_celda(parte)
                        if hoja[fila_ref][col_ref] is not None:
                            total += hoja[fila_ref][col_ref]
                
                if puede_evaluar:
                    hoja[fila_objetivo][col_objetivo] = total
                    cambio = True
    
    imprimir_hoja(hoja, F, C)