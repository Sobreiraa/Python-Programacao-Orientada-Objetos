from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Makalister')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()