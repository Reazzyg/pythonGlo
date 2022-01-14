from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('48230e4771f7fbb8867440d58f13cbd5')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Moskow')
w = observation.weather
