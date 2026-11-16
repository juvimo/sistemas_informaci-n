def codificacion_hamming():
    print("Mensaje Original Ingreso")
    print("Ingresa los 4 bits de datos:")

    p3 = int(input("Bit para P3: "))
    
    p5 = int(input("Bit para P5: "))
    p6 = int(input("Bit para P6: "))
    p7 = int(input("Bit para P7: "))
    

    
    p1 = (p3 + p5 + p7) % 2
    p2 = (p3 + p6 + p7) % 2
    p4 = (p5 + p6 + p7) % 2

    mensaje_codificado = [p1, p2, p3, p4, p5, p6, p7]

    print(f"Paridades calculadas -> P1:{p1}, P2s:{p2}, P4:{p4}")
    print(f"MENSAJE CODIFICADO GENERADO: {mensaje_codificado}")

    print("Mensaje Recibido: ")
    print("Ingresa nuevamente los 4 bits:")

    rec_p3 = int(input("Bit recibido para P3: "))
    rec_p5 = int(input("Bit recibido para P5: "))
    rec_p6 = int(input("Bit recibido para P6: "))
    rec_p7 = int(input("Bit recibido para P7: "))

    mensaje_recibido = [p1, p2, rec_p3, p4, rec_p5, rec_p6, rec_p7]

    r = mensaje_recibido
    
    c1 = (r[0] + r[2] + r[4] + r[6]) % 2  
    c2 = (r[1] + r[2] + r[5] + r[6]) % 2  
    c4 = (r[3] + r[4] + r[5] + r[6]) % 2  

    posicion_error = (c4 * 4) + (c2 * 2) + (c1 * 1)

    print("Resultado Total")
    print(f"Mensaje enviado  : {mensaje_codificado}")
    print(f"Mensaje recibido : {mensaje_recibido}")

    if posicion_error == 0:
        print("RESULTADO: El mensaje recibido es CORRECTO.")
    else:
        print("RESULTADO: El mensaje recibido es INCORRECTO.")
        print(f"Se detectó el error en la posición: P{posicion_error}")

        idx = posicion_error - 1
        mensaje_recibido[idx] = 1 - mensaje_recibido[idx]
        print(f" Mensaje CORREGIDO automáticamente: {mensaje_recibido}")


if __name__ == "__main__":
    codificacion_hamming()