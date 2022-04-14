import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
  
        for key, value in kwargs.items():

            for i in range(value):
                self.contents.append(f'{key}')
        
    def draw(self, draw):
        if draw > len(self.contents):
            return self.contents
        
        else:
            pelotas_sacadas = []

            for i in range(draw):
                indice_a_sacar = random.randint(0, len(self.contents) - 1)
                pelota_sacada = self.contents.pop(indice_a_sacar)
                pelotas_sacadas.append(pelota_sacada)

            return pelotas_sacadas




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pelotas = copy.deepcopy(hat.contents)

    satisfactorios = 0
    for i in range(num_experiments):
        pelotas_sacadas = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(pelotas)

        fue_satisfactorio_el_experimento = True

        for nombre_pelota, cantidad_esperada in expected_balls.items():
            cantidad_obtenida = pelotas_sacadas.count(nombre_pelota)

            if cantidad_obtenida < cantidad_esperada:
                fue_satisfactorio_el_experimento = False
                break
        
        if fue_satisfactorio_el_experimento:
            satisfactorios += 1
    
    return satisfactorios / num_experiments
