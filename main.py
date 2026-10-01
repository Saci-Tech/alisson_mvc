from app.controllers import CarroController

def main():
    print("Iniciando aplicação MVC...")
    
    # Instancia o controller principal
    controller = CarroController()
    
    # Executa a ação
    controller.listar_carros()

if __name__ == "__main__":
    main()