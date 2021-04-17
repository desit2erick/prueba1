from math import floor, log
import re

espacioZ = (11.3, 12.4, 13.5, 14.7, 15.8, 17, 18.1, 19.3, 20.4, 21.5, 22.7, 23.8, 24.9, 26, 27.2, 28.3,
            29.4, 30.5, 31.7, 32.8, 34, 35.1, 36.2, 37.3, 38.5, 39.6, 40.7, 41.8, 43, 44.1, 45.2, 46.4, 47.5, 48.6,
            49.8, 50.9, 52, 53.2, 54.3, 55.4, 56.5, 57.7, 58.8, 60, 61.1, 62.2, 63.3, 64.5, 65.6, 66.7, 67.9, 69,
            70.1, 71.2, 72.4, 73.5, 74.7, 75.8, 76.9, 78, 79.2, 80.3, 81.4, 82.5, 83.7, 84.8, 86, 87.1, 88.2, 89.4,
            90.5, 91.6, 92.8, 93.9, 95.1, 96.2, 97.3, 98.4, 99.6, 100.7)
espacioV = (25.8, 27.3, 28.9, 30.2, 31.6, 33.1, 34.5, 36, 37.5, 38.9, 40.1, 50.1, 41.6, 43.1, 44.5, 45.9,
            47.5, 48.8, 51.6, 53.1, 54.5, 56.1, 57.4, 58.7, 60.1, 61.7, 63.1, 64.5, 65.9, 67.4, 68.8, 70.2, 71.6, 73.1,
            74.4, 76.1, 77.5, 78.9, 80.4, 81.8, 83.3, 84.9, 86, 87.6, 88.9, 90.2, 91.6, 93, 94.5, 96, 97.5, 98.9, 100.4,
            101.8, 103.8, 105.2, 106.6, 108.1)


def splitRef(cad):
    try:
        refSearch = re.search(r'[VZCHEvzche][0-9]+[AL]?[\s\-]{1,3}[0-9]*', cad)
        if refSearch == None:
            return None
        ref = refSearch.group()
        listTipo = re.findall(r'[a-zA-Z]+', ref)
        tipo = ''.join(listTipo)
        filas, dim = tuple(re.findall(r'[0-9]+', ref))
        if len(dim) < 2:
            return None
        if len(dim) % 2 == 0:
            alto, ancho = dim[:len(dim)//2], dim[len(dim)//2:]
        else:
            alto1, ancho1 = int(dim[:len(dim)//2]), int(dim[len(dim)//2:])
            alto2, ancho2 = int(dim[:len(dim)//2+1]), int(dim[len(dim)//2+1:])
            alto, ancho = (str(alto1), str(ancho1)) if abs(
                alto1-ancho1) < abs(alto2-ancho2) and dim[2] != '0' else (str(alto2), str(ancho2))
        return ','.join([ref, tipo, filas, alto, ancho])
    except:
        return None


class medidasPanal():

    grosorTubo = 0.24
    anchoFinsVZ = (3.2, 5.1, 6.7, 8.2, 0)
    anchoFinsCH = (3.7, 5.1, 6.4, 7.7, 9.3, 10.5, 12, 15.3, 0)

    medidas = {}

    medidas = {}

    def __init__(self, tipo, filas, alto, ancho, soporte=None) -> None:
        self.tipo = tipo
        self.filas = filas
        self.alto = alto
        self.ancho = ancho
        self.soporte = soporte
        super(medidasPanal).__init__()

    def largoPlatina(self):
        return self.ancho + 8

    def largoTubos(self):
        return self.alto + (1.1 if (self.alto < 60) else 1.5)

    def tubosPorHilera(self):
        return self.totalFins() - 1

    def totalTubos(self):
        return self.tubosPorHilera() * self.filas + (0 if self.soporte == 'Abrazados' else 4)

    def grosorFins(self):
        if self.tipo.upper() == 'V':
            return 1.2
        elif self.tipo.upper() == 'Z':
            return 0.9
        return self.tubosPorHilera() * self.filas

    def anchoFins(self):
        if self.tipo.upper() in ['V', 'Z']:
            index = self.filas-2 if self.filas-2<4 else len(self.anchoFinsVZ)-1

            return self.anchoFinsVZ[index] if self.tipo.upper() in ['V', 'Z'] else self.anchoFinsCH[index]
        else:
            index = self.filas-2 if self.filas-2<8 else len(self.anchoFinsCH)-1
            return self.anchoFinsCH[index]

    def largoFins(self):
        return round(self.alto)

    def totalFins(self):
        W, gF, gT = self.ancho, self.grosorFins(), self.grosorTubo
        return floor((W+gT)/(gF+gT))

    def espacio(self):
        # Utilizando tuplas
        if self.tipo.upper() == 'V':
            if self.totalFins()-20 < len(espacioV) and self.totalFins()-20 > 0:
                return espacioV[self.totalFins()-20]
            else:
                return None
        elif self.tipo.upper() == 'Z':
            if self.totalFins()-12 < len(espacioZ) and self.totalFins()-12 > 0:
                return espacioZ[self.totalFins()-12]
            else:
                return None

    def getMeasures(self):
        self.medidas['U_Largo'] = self.largoTubos()
        self.medidas['U_TubosXH'] = self.tubosPorHilera()
        self.medidas['U_Tubos'] = self.totalTubos()
        self.medidas['U_Grosor'] = self.anchoFins()
        self.medidas['U_FinsL'] = self.largoFins()
        self.medidas['U_Fins'] = self.totalFins()
        self.medidas['U_Espacio'] = self.espacio()
        return self.medidas
