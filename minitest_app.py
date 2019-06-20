
import WeatherApiModule as wpm

def minitest_app():
    wpmo = wpm.WeatherApiModule('humidity')
    wpmo.app_info()
    api_address = wpmo.conect2app()
    valor = wpmo.get_data_api(api_address)
    print('\n\n THE VALUE OF THE PARAMTER {} IS: '.format(wpmo.parm))
    if valor > 70:
        print('\n\n It´s gonna rain on this day.\n\n')
    else:
        print('\n\n It´s not gonna rain on this day.')
    print('\n')


minitest_app()

