#
# autores: 
# Michel Silva
#
#data: 21/11/2022

# Para criar uma classe em Python que possa obter informações do hardware
# do computador, você pode utilizar a biblioteca psutil. Primeiro, você 
# precisa instalar a biblioteca executando o comando pip install psutil no terminal 
# ou prompt de comando. Ela fornece uma série de funções que permitem acessar. 

import psutil

class Hardware:
    def __init__(self):
        self.info = psutil.virtual_memory()

    def get_total_memory(self):
        # Retorna a quantidade total de memória RAM em bytes
        return self.info.total

    def get_used_memory(self):
        # Retorna a quantidade de memória RAM utilizada em bytes
        return self.info.used

    def get_free_memory(self):
        # Retorna a quantidade de memória RAM livre em bytes
        return self.info.free

# Essa classe possui o método __init__ que é executado automaticamente 
# quando uma nova instância da classe é criada. Nele, utilizamos a 
# função psutil.virtual_memory() para obter informações sobre a memória RAM do computador.

# Em seguida, criamos os métodos get_total_memory(), get_used_memory() 
# e get_free_memory() que retornam, respectivamente, a quantidade total 
# de memória RAM, a quantidade de memória utilizada e a quantidade de memória livre.


######################################################################
#
# Para utilizar essa classe, basta criar uma nova instância 
# dela e chamar os métodos que desejar:

hw = Hardware()

total_memory = hw.get_total_memory()
used_memory = hw.get_used_memory()
free_memory = hw.get_free_memory()

print(f"Total memory: {total_memory} bytes")
print(f"Used memory: {used_memory} bytes")
print(f"Free memory: {free_memory} bytes")