from logging import Logger
import logging
import inspect
import time
import json
import sys



class JSONLogger(Logger):
    def _log(self, level, msg, *args, **kwargs):
        """
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        """
        msg = json.dumps(msg)
        super()._log(level, msg, *args, **kwargs)

class SuperLog:

    def __init__(self, app_name: str):
        self._FORMAT = '{"level":"%(levelname)s","timestamp":"%(asctime)s","app":"%(name)s","log":%(message)s}'
        self.time = time.time()
        self.traceback = 0
        self.start_time = time.time()
        self.logger =  self.getLogger(app_name)

    def getLogger(self, name: str) -> JSONLogger:

        logging.basicConfig(format=self._FORMAT)
        manager = logging.Manager(JSONLogger.root)
        manager.setLoggerClass(JSONLogger)
        logger = manager.getLogger(name)
        logger.setLevel("INFO")
        return logger

    def exception_error(self,message, execution, i=0):

        message = '''{"message":"%s","execution":%s,"file":"%s","line": "%s","function":"%s","statement":"%s","error":"%s","text":"%s"}''' % ( message
                                                            , execution
                                                            , inspect.trace()[i][1]
                                                            ,inspect.trace()[i][2]
                                                            , inspect.trace()[i][3]
                                                            , str(inspect.trace()[i][4]).replace('"','\'').replace("    ","")
                                                            , str(sys.exc_info()[0]).replace('"','\'')
                                                            , sys.exc_info()[1]
                                                          )

        return message


    def time_analyze(self, funcion):
        def callf(*args, **kwargs):
            inicio = time.time()
            c = funcion(*args, **kwargs)
            message = '{"total_execution":%s}' % (round(time.time() - inicio,2))
            self.logger.info(json.loads(message))
            return c

        return callf


    def print(self, message):
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time,2)
        message = message


        if len(inspect.trace()) != 0:

            self.logger.error(json.loads(self.exception_error(message, execution)))
        else:
            to_send = '{"message":"%s", "execution":%s, "function":"%s"}' % (message, execution, function)
            self.logger.info(json.loads(to_send))
            #print("mensaje:{} - duracion: {} - funcion: {}\n".format(message, self.time - time.time(), inspect.stack()[1].function))
            self.time = time.time()


l = SuperLog("Prueba")

@l.time_analyze
def main():
    time.sleep(1)

    try:
        dasda
    except:
        l.print("prueba")

    time.sleep(1)

    l.print("inicio")

    try:
        raise Exception("Error 202")
    except:
        l.print("error 2")

    l.print("inicio 2")


if __name__ == '__main__':
    main()

    #print('{"message": %s, "time": %s, "funtion": "%s"}' % (1,2,3))