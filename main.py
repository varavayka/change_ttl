

import os
from platform import system
from default_ttl_linux import change_ttl_linux


try:
    value_ttl = int(input('Введите значение: '))

    if system() == 'Linux':
        change_ttl_linux(value_ttl)
    elif system() == 'Windows':
        os.system(f"REG ADD HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters /v DefaultTTL /t REG_DWORD /d {value_ttl}")
        
        
except KeyboardInterrupt:
    print('\n[-] Отмена операции')
except ValueError:
    print('\n[!] Вы ввели не число или ввели не целое число!')
            



