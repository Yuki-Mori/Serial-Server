import threading

class ServerInput(threading.Thread):
    __server_on = True
    __is_running = True

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while self.__is_running:
            command = input()
            if command == 'exit':
                self.__server_on = True

    def is_server_on(self):
        return self.__server_on

    def stop(self):
        self.__is_running = False
