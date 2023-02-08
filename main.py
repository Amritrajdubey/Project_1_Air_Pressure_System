from sensor.logger import logging
from sensor.exceptition import SensorException

def test_logger_exceptition():
     try:
          result = 3/0
          print(result)
     except Exception as e:
          raise e

if __name__ == "__main__" :
     
     try:
          pass
     except Exception as e:
          print(e)

