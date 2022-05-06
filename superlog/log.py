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
        self.logger =  self.__getLogger(app_name)

    def __getLogger(self, name: str) -> JSONLogger:
        """
            Function que inicializa el logger
        :param name:
        :return:
        """
        logging.basicConfig(format=self._FORMAT)
        manager = logging.Manager(JSONLogger.root)
        manager.setLoggerClass(JSONLogger)
        logger = manager.getLogger(name)
        logger.setLevel("INFO")
        return logger

    def __exception_error(self,message, execution, i=0):
        """
            Metodo que genera el json con la informacion proveniente del trace de errores
        :param message:
        :param execution:
        :param i:
        :return:
        """

        message = '''{"message":"%s","execution":%s,"file":"%s","line": "%s","function":"%s","statement":"%s","error":"%s","text":"%s","manual": false}''' % ( message
                                                            , execution
                                                            , inspect.trace()[i][1].replace('\\','\\\\')
                                                            , inspect.trace()[i][2]
                                                            , inspect.trace()[i][3]
                                                            , str(inspect.trace()[i][4]).replace('"','\'').replace("    ","")
                                                            , str(sys.exc_info()[0]).replace('"','\'')
                                                            , sys.exc_info()[1]
                                                          )

        return message

    def time_func_analyze(self, total_execution=False, *args, **kwargs):
        """
            Metodo decorador que permite calcular el tiempo total de una funcion
        :param total_execution:
        :param args:
        :param kwargs:
        :return:
        """
        def decorator(function):
            def func(*args, **kwargs):
                inicio = time.time()
                result = function(*args, **kwargs)
                if total_execution:
                    message = '{"total_execution":%s}' % (round(time.time() - inicio, 2))
                else:
                    message = '{"total":%s, "function": "%s"}' % (round(time.time() - inicio, 2), function.__name__)
                self.logger.info(json.loads(message))
                return result
            return  func
        return decorator


    def error(self, message):
        """
            Funcion que imprime un error, en caso de no usar try y except se recomienda usar esta funcion
            para imprimir los errores
        :param message:
        :return:
        """
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time, 2)
        to_send = '{"message":"%s", "execution":%s, "function":"%s", "manual": true}' % (message, execution, function)
        self.logger.error(json.loads(to_send))
        self.time = time.time()

    def print(self, message):
        """
            Funcion que imprime informacion adicional de un proceso, adicionalmente reconoce automaticamente un error despues de un try: except:
            imprimiendo el error en el codigo
        :param message:
        :return:
        """
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time,2)
        message = message


        if len(inspect.trace()) != 0:

            self.logger.error(json.loads(self.__exception_error(message, execution)))
        else:
            to_send = '{"message":"%s", "execution":%s, "function":"%s"}' % (message, execution, function)
            self.logger.info(json.loads(to_send))
            self.time = time.time()





if __name__ == '__main__':
    log = SuperLog(app_name='my_app')




    @log.time_func_analyze(total_execution=True)
    def main():
        log.error("Hola mundo error")

    main()

