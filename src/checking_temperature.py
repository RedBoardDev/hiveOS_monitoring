from discord.ext import tasks
from get_request import request_json, get_workers_metrics
from get_config import f_get_memtemp, f_get_temp
from lib_discord import send_message

####################INITS_VARIABLE####################
url = 'https://api2.hiveos.farm/api/v2/farms/776169/workers/1669282/metrics'
######################MAIN#################################

async def set_gpu_type(client, index:int, temp:int, type_memory:bool):
    req = request_json("https://api2.hiveos.farm/api/v2/farms/776169/workers/1669282")
    worker_name = req['name']
    gpu_info = ['gpu_info'][index]
    short_name = gpu_info['short_name']
    subvendor = gpu_info['details']['subvendor']
    gpu_type =  short_name + ' ' + subvendor
    if (type_memory):
        message:str = worker_name + " | High gpu temp: " + temp + "°C for " + gpu_type
    else: 
        message:str = worker_name + " | High memory temp: " + temp + "°C for " + gpu_type
    send_message(":fire:", message)

@tasks.loop(seconds=10)
async def checking_temperature(client, toggle_temp:list[bool], toggle_memtemp:list[bool]):
    req = get_workers_metrics()
    max_temp:int = f_get_temp()
    max_memtemp:int = f_get_memtemp()
    temp_gpu_l:list[int] = req['temp']
    memtemp_gpu_l:list[int] = req['memtemp']

    for i in range(len(temp_gpu_l)):
        print(temp_gpu_l[i], " | ", memtemp_gpu_l[i])

        if (toggle_temp[i] == False):
            if (temp_gpu_l[i] > max_temp):
                toggle_temp[i] == True
                await set_gpu_type(client, i, temp_gpu_l[i], True)
        else:
            if (temp_gpu_l[i] < max_temp - 1): # -1 pour si la temp est limite au max et oscille entre les deux pour pas spam, a voir entre -1 et -2
                toggle_temp[i] == False

        if (toggle_memtemp[i] == False):
            if (memtemp_gpu_l[i] > max_memtemp):
                toggle_memtemp[i] = True
                await set_gpu_type(client, i, memtemp_gpu_l[i], False)
        else:
            if (memtemp_gpu_l[i] < max_memtemp - 1): # -1 pour si la temp est limite au max et oscille entre les deux pour pas spam, a voir entre -1 et -2
                toggle_memtemp[i] = False