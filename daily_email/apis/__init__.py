print(__name__)

try:
    from .weather import sunset
except ImportError:
    from weather import sunset

print(sunset)

def api_func():
    print('hi')