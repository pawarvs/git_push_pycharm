
import logging
logging.basicConfig(filename = "divide.log",level= logging.INFO, format= '%(levelname)s %(name)s %(asctime)s  %(message)s')

def divide(a,b) :
    logging.info(": The number entered by the user is %s and %s", a,b)
    try:
        logging.info(": We are into function ")
        div = a/b
        logging.info(": We have completed the division operation ")
        logging.info(": The result of a code is %s ",div)
        return div
    except Exception as e :
        logging.exception(e)
        print(e)


#(divide(3,6))
(divide(3,0))


#print(divide(3,0))
#print(divide(3,4))


