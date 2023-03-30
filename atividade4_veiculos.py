class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def distancia_percorrida(self, tempo):
        return self.velocidade * tempo


class Carro(Veiculo):
    def __init__(self):
        super().__init__(velocidade=110)


class Caminhao(Veiculo):
    def __init__(self):
        super().__init__(velocidade=80)


def tempo_distancia_veiculos():
    """
    A função cria objetos para um carro e um caminhão,
    em seguida calcula o tempo que eles levarão para se cruzar na estrada e a distância percorrida por cada veiculo.
    Em seguida, calcula a distância de cada veículo em relação à cidade de Ribeirão Preto
    e compara essas distâncias para determinar qual deles está mais próximo da cidade.
    Por fim exibe o resultado na tela.
    """
    carro = Carro()
    caminhao = Caminhao()

    tempo = 100 / (carro.velocidade + caminhao.velocidade)

    distancia_carro = carro.distancia_percorrida(tempo)
    distancia_caminhao = caminhao.distancia_percorrida(tempo)

    distancia_restante_carro = 100 - distancia_carro
    distancia_restante_caminhao = 100 - distancia_caminhao

    if distancia_restante_caminhao < distancia_restante_carro:
        print("O caminhão está mais próximo da cidade de Ribeirão Preto.")
    else:
        print("O carro está mais próximo da cidade de Ribeirão Preto.")

tempo_distancia_veiculos()
