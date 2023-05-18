#!/usr/bin/env python3

import subprocess
import fn
from time import sleep

def get_cpu_temperature_as_str():
    try:
        output = subprocess.check_output(['sensors'], text=True)
        temperature_lines = []
        for line in output.splitlines():
            if 'Core' in line:
                temperature_lines.append(line)
        
        if temperature_lines:
            return '\n'.join(temperature_lines)
        else:
            return 'Unable to retrieve CPU temperature'
    except subprocess.CalledProcessError:
        return 'Error while retrieving CPU temperature'

if __name__ == "__main__":
    try:
        channel = fn.connect_to_rabbitmq(queue_name='my_queue')

        while True:
            channel.basic_publish(
                exchange='', routing_key='my_queue', body=get_cpu_temperature_as_str())
            sleep(5)
    except:
        fn.print_with_time('Error ao executar o programa')
