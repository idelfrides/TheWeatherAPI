import requests
import json
# from pprint import pprint


class WeatherApiModule(object):

    def __init__(self, parm):
        self.parm = parm

    def app_info(self):
        print("\n\n ===================================\n app info goes hehe \n ===================================\n\n")
        print('\n The parametre is  ', self.parm)


    @staticmethod
    def conect2app():
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d5fa2c6c75946ef883d5fb4cd84eaadb&q='
        return api_address

    def get_data_api(self, api_address):
        city = input("\n\n Enter a valid city:  ")
        print('\n\n You choose the folling city: ', city)
        url = api_address + city
        json_dada = requests.get(url).json()
        valor = json_dada['main'][self.parm]
        return valor

    # recupera e retorna o codigo da cidade - city
    def get_code_city(self, city):
        # x = json.load('city_list.json').get('main')
        # x = json.load('teste.json')
        # print(x)
        try:
            # obj_json = open('teste.json', 'r')
            # data_json = json.load(obj_json)
            # print(data_json)
            with open('teste.json', 'r') as file:
                data = json.load(file)
            print('dados: {} '.format(data))
        except Exception as erro:
            print('\n Ocorreu um erro ao carregar o arquivo JSON')
            print('\n O erro é: {}'.format(erro))
        return city



