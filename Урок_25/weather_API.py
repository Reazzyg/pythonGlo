from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = OWM('your-api-key', config_dict)
owm = OWM('48230e4771f7fbb8867440d58f13cbd5', config_dict)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Москва')
w = observation.weather
print(w.detailed_status)
print(w.wind().get('speed'))
print(w.humidity)
print(w.temperature('celsius').get('temp'))
print(w.clouds)
print(w)
