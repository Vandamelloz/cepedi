from factorymethod import AnimalFactory
from caoFactory import CaoFactory
from gatoFactory import GatoFactory

if __name__ == "__main__":
    fabricaCaes= CaoFactory().CriarAnimais()
    fabricaGatos=GatoFactory().CriarAnimais()
    fabricaCaes.fazSom()
    fabricaGatos.fazSom()