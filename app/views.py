class CarroView:
    @staticmethod
    def mostrar_lista_carros(carros):
        print("\n--- LISTA DE CARROS CADASTRADOS ---")
        for i, carro in enumerate(carros, 1):
            print(f"{i}. {carro.marca} {carro.modelo} ({carro.ano}) - {carro.portas} portas")
        print("-" * 35)

    @staticmethod
    def mostrar_mensagem(mensagem: str):
        print(f"[INFO] {mensagem}")