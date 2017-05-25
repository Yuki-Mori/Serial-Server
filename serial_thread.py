import threading
import serial
import socket

class SerialThread(threading.Thread):
    def __init__(self, rate = 9600):
        threading.Thread.__init__(self)
        self.port = ''
        self.rate = rate
        self.myserial = serial.Serial()
        self.mysocket = socket.socket()

        self.is_running = True

    def run(self):

        while self.is_running:
            data_str = self.myserial.read_all()
            self.mysocket.sendall(data_str)

        self.myserial.close()

    def stop(self):
        self.is_running = False

    def connect(self, port, mysocket):
        self.port = port
        self.myserial = serial.Serial(self.port, self.rate)
        self.mysocket = mysocket
