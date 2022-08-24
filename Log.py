
import logging
logging.basicConfig(filename = 'test.log',level= logging.INFO)
logging.info("The very first code for logging")
# l = [1,2,34,11,"vishal"]
# logging.info(l)
logging.warning(" Try to load warning message")
logging.error("This is error message from the system")

# for i in l :
#     if i == 'vishal' :
#         logging.info(i)

logging.shutdown()