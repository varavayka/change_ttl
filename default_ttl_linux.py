import re
from pathlib import Path


def change_ttl_linux(value_ttl):

    
    try:
    
        if type(value_ttl) is int:

            path_sysctl  = Path('/etc/sysctl.conf')
            serach_line_change_ttl = re.compile(r'net.ipv4.ip_default_ttl')

            with open(path_sysctl) as sysctl:
                
                default_ttl_line = serach_line_change_ttl.findall(str(sysctl.readlines()))

                if default_ttl_line:
                    print('[!] Значение TTL уже изменено')
                    return
                
            if not default_ttl_line :

                with open(path_sysctl, 'a') as append_sysctl:
                    append_sysctl.write(f"net.ipv4.ip_default_ttl = {value_ttl}")
                    print(f"Стандартное значение TTL изменено на: {value_ttl}")
            
    except ValueError as e:
        print(f"[!] В аргумент вызова программы было передано не число ---> {e}")



