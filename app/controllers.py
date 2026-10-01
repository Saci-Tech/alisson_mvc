from app.models import CarroModel
from app.views import CarroView

class CarroController:
    def __init__(self):
        self.view = CarroView()

    def listar_carros(self):
        """Busca os dados no Model e envia para a View exibir."""
        carros = CarroModel.obter_todos()
        if carros:
            self.view.mostrar_lista_carros(carros)
        else:
            self.view.mostrar_mensagem("Nenhum carro encontrado.")