class Contador:
    def __init__(self,archivo):
        self.archivo = archivo
    
    def ordenar_palabras(self):
        coleccion_palabras = dict()
        archivo = open(self.archivo, 'r')
        lista_palabras = archivo.read().strip().replace('\n', ' ').split(' ')
        for palabra in lista_palabras:
            coleccion_palabras[palabra] = coleccion_palabras.get(palabra, 0) + 1        
        return sorted([(v,k) for k,v in coleccion_palabras.items()])

    def obtener_palabras_mas_frecuentes(self):
        palabras_ordenadas = self.ordenar_palabras()
        for palabra in palabras_ordenadas[-1:-11:-1]:
            print('palabra: "'+palabra[1]+'" valor: '+str(palabra[0]))
            
contador_1 = Contador('Wuthering_Heights.txt')
contador_1.obtener_palabras_mas_frecuentes()
        
        