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
        self.cpu = psutil.cpu_count()
        self.disk = psutil.disk_usage('/')

    def get_total_memory(self):
        # Retorna a quantidade total de memória RAM em bytes
        return self.info.total

    def get_used_memory(self):
        # Retorna a quantidade de memória RAM utilizada em bytes
        return self.info.used

    def get_free_memory(self):
        # Retorna a quantidade de memória RAM livre em bytes
        return self.info.free
      
    def get_cpu_percent(self):
        # Retorna a quantidade de porcentagem de uso da CPU
        return self.cpu.percent
      
    def get_cpu_count(self):
        # Retorna a quantidade de núcleos da CPU
        return self.cpu.count
      
    def get_cpu_freq(self):
        # Retorna a frequência da CPU em MHz
        return self.cpu.freq
    
    def get_disk_total(self):
        # Retorna o tamanho total do disco em bytes
        return self.disk.total 
      
    def get_disk_used(self):
        # Retorna o espaço usado no disco em bytes
        return self.disk.used
      
    def get_disk_free(self):
        # Retorna o espaço livre no disco em bytes
        return self.disk.free




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

# memoria
total_memory = hw.get_total_memory()
used_memory = hw.get_used_memory()
free_memory = hw.get_free_memory()

# cpu 
uso_cpu = hw.get_cpu_percent()
quantidade_nucleos = hw.get_cpu_count()
freq_cpu = hw.get_cpu_freq()

# memoria
print(f"Total memory: {total_memory} bytes")
print(f"Used memory: {used_memory} bytes")
print(f"Free memory: {free_memory} bytes")

# cpu
