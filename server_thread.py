import threading
import serial_thread

class ServerThread(threading.Thread):

    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.max_size = 1000
        self.is_running = True
        self.is_connected = False
        self.client.sendall('>>'.encode('utf-8'))
        self.serial = serial_thread.SerialThread()

    def run(self):
        while self.is_running:
            data = self.client.recv(self.max_size)
            data_str = data.decode('utf-8')[:-1]

            #終了処理
            if 'exit' in data_str:
                msg = '[Server]: See you.'
                self.client.sendall(msg.encode('utf-8'))
                self.is_running = False
                self.client.close()
                print('Do you close the server? [Y|n]: ')
                break

            #connectコマンドの処理
            data = data_str.split()
            if 'connect' in data[0] and self.is_connected == False:
                self.is_connected = True
                #self.client.sendall( ('[Server]: ' + data[1] + '\n').encode('utf-8'))
                self.serial = serial_thread.SerialThread()
                self.serial.connect(data[1], self.client)
                self.serial.start()

            #disconnectコマンドの処理
            elif ('disconnect' in data[0]) and self.is_connected:
                self.is_connected = False
                self.serial.stop()
                self.client.sendall('[Server]: Device is disconnected!\n'.encode('utf-8'))

            print('[Client]:', data_str)
            msg = '[Server]: Hello, Client!\n>>'
            self.client.sendall(msg.encode('utf-8'))

    def stop(self):
        self.is_running = False
