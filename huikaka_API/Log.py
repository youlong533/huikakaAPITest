import logging
from TestCase_Lib import __main__


logging.basicConfig(filename='power_test.log', level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(message)s - %(funcName)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('{}'.format(__main__))
#logger = logging.getLogger()
#logger.addHandler(logging.FileHandler('power_test.log','a'))
#print = logging.info
#print('power_test')