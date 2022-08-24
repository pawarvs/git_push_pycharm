
import logging
logging.basicConfig(filename = " test1.log",level=logging.DEBUG, format= '%(levelname)s %(name)s %(asctime)s  %(message)s')
logging.info(" : This is a log message with timestamp")
