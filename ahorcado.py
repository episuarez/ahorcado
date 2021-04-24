import random

class Ahorcardo:
    def __init__(self):
        self.datos = [];
        self.cargar_datos();

        self.dato_elegido = self.seleccionar_datos();

        self.texto_oculto = "_" * len(list(self.dato_elegido.values())[0]);
        self.letras_preguntadas = [];
        self.vidas_restantes = 3;
        self.letras_faltantes = len(self.texto_oculto);

    def seleccionar_datos(self):
        return random.choice(self.datos);

    def puedojugar(self):
        return self.vidas_restantes > 0 and self.texto_oculto.count("_") > 0;

    def guardar_resumen(self, valor):
        fichero = open("historial.csv", "a", encoding="utf-8");

        texto = f"Pregunta: {list(self.dato_elegido.keys())[0]} - Respuesta: {list(self.dato_elegido.values())[0]} - Vidas: {self.vidas_restantes} - Letras preguntadas: {self.letras_preguntadas} - Estado de la adivinación: {self.texto_oculto} - Resultado de la partida: {valor}\n";

        fichero.write(texto);

        fichero.close();

    def mensaje_final(self):
        if self.vidas_restantes < 1:
            self.guardar_resumen("Ha perdido");

            return f"¡Has perdido! La respuesta era {list(self.dato_elegido.values())[0]}";

        if self.texto_oculto.count("_") == 0:
            self.guardar_resumen("Ha ganado");

            return f"¡Has ganado! La respuesta era {list(self.dato_elegido.values())[0]}";

    def intentar_resolver(self, texto):
        acierto = texto == list(self.dato_elegido.values())[0];
        if acierto:
            self.texto_oculto = texto;
            return "¡Es correcto!";
        else:
            self.vidas_restantes -= 1;
            return "¡Has fallado! ¡Has perdido una vida!"; 

    def comprobar_letra(self, letra):
        if len(letra) > 1 and not letra.isalpha():
            self.letras_preguntadas.append(letra);
            self.vidas_restantes -= 1;
            return "¡Has fallado! ¡Has perdido una vida!";
        else:
            if letra in self.letras_preguntadas:
                self.letras_preguntadas.append(letra);
                self.vidas_restantes -= 1;
                return "¡Ya lo has preguntado! ¡Has perdido una vida!";
            else:
                if letra in list(self.dato_elegido.values())[0]:
                    posiciones = self.obtener_posiciones_letra(letra);

                    texto_oculto = list(self.texto_oculto);
                    for posicion in posiciones:
                        texto_oculto[posicion] = letra;
                    self.texto_oculto = "".join(texto_oculto);

                    self.letras_preguntadas.append(letra);
                    return "¡Has acertado la letra!";
                else:
                    self.vidas_restantes -= 1;
                    self.letras_preguntadas.append(letra);
                    return "¡Has fallado! ¡Has perdido una vida!";


    def obtener_posiciones_letra(self, letra):
        respuesta = list(self.dato_elegido.values())[0];
        posiciones = [];

        for posicion in range(0, len(respuesta)):
            if letra == respuesta[posicion]:
                posiciones.append(posicion);

        return posiciones;

    def cargar_datos(self):
        fichero = open("datos.csv", "r", encoding="utf-8");

        linea = fichero.readline();
        while linea != "":
            datos = linea.split(";");
            self.datos.append({datos[0]: datos[1]});

            linea = fichero.readline();

        fichero.close();

    def obtener_turno(self):
        texto = f"Ahorcado - Vidas {self.vidas_restantes} - Faltan: {self.letras_faltantes}\n";
        texto += f"Letras que has preguntado: {self.letras_preguntadas}\n\n";

        texto += f"{list(self.dato_elegido.keys())[0]}\n";
        texto += f"{self.texto_oculto}\n";

        return texto;

