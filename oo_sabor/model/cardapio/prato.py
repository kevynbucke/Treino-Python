from model.cardapio.item_cardapio import itemCardapio

class Prato(itemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao
    def __str__(self):
        return self._nome