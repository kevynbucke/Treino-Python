from model.restaurante import Restaurante
from model.cardapio.bebiba import Bebida
from model.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0,'grande')
prato_paozinho = Prato('Paozinho',2.00, 'O melhor pão da cidade')


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()