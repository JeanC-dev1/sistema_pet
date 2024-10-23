from abc import ABC

class ServicoPet(ABC):

    def realizar(self, pet):
        pass

class Banho(ServicoPet):
    def realizar(self, pet):
        print(f"{pet} está recebendo banho.")

class Tosa(ServicoPet):
    def realizar(self, pet):
        print(f"{pet} está passando por tosa.")


class Recreacao(ServicoPet):
    def realizar(self, pet):
        print(f"{pet} está brincando na recreação.")


class PetShop:
    def __init__(self):
        self.servicos = {
            "banho": Banho(),
            "tosa": Tosa(),
            "recreacao": Recreacao()
        }

    def realizar_servico(self, tipo_servico, pet):
        servico = self.servicos.get(tipo_servico)
        if servico:
            servico.realizar(pet)
        else:
            print("Serviço não disponível.")


petshop = PetShop()
petshop.realizar_servico("banho", "Rex")
petshop.realizar_servico("tosa", "Bella")
petshop.realizar_servico("recreacao", "Max")
