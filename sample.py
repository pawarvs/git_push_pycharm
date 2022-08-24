
import logging
logging.basicConfig(filename = "sample.log",level= logging.INFO, format= '%(levelname)s %(name)s %(asctime)s  %(message)s')

try :
    logging.info(": I am trying to read a file ")
    with open("vish.txt","r") :
        logging.info(" : Sucessfully it has read the file ")

except Exception as e :
    logging.critical(": This is a situation for us ")
    logging.error(e)
    logging.exception(e)