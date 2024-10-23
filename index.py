class PetShop:
    def realizar_servico(self, tipo_servico, pet):
        if tipo_servico == "banho":
            print(f"{pet} está recebendo banho.")
        elif tipo_servico == "tosa":
            print(f"{pet} está passando por tosa.")
        elif tipo_servico == "recreacao":
            print(f"{pet} está brincando na recreação.")
        else:
            print("Serviço não disponível.")


petshop = PetShop()
petshop.realizar_servico("banho", "Mica")