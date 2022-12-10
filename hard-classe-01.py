#
# autores: 
# Michel Silva
#
#data: 21/11/2022

# 
# Para criar uma classe em Python que possa obter informações sobre 
# o hardware do computador, você pode usar a biblioteca psutil. 
# Ela fornece uma série de funções que permitem acessar informações sobre o 
# sistema operacional, uso da CPU, memória, disco e outros recursos do computador.

import psutil

class HardwareInfo:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)
        self.memory_total = psutil.virtual_memory().total
        self.disk_total = psutil.disk_usage('/').total

    def get_cpu_percent(self):
        return f"{self.cpu_percent} %"

    def get_memory_total(self):
        return f"{self.memory_total} bytes"

    def get_disk_total(self):
        return f"{self.disk_total} bytes"


#######################################################################
# criar uma nova instância dela e chamar os métodos para obter as informações desejadas:

# caso de erro
#     import psutil
#  ModuleNotFoundError: No module named 'psutil'

# rode no terminal:  pip install psutil  

hardware_info = HardwareInfo()

# Obter o uso da CPU em porcentagem
cpu_percent = hardware_info.get_cpu_percent()
print(cpu_percent)

# Obter a quantidade total de memória do computador
memory_total = hardware_info.get_memory_total()
print(memory_total)

# Obter a quantidade total de espaço em disco
disk_total = hardware_info.get_disk_total()
print(disk_total)
