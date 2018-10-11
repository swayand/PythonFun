import logging
import os


class Frida():
    def __init__(self):
        self.name = "Frida"
        self.switch = {}
        self.switch["Fr"+"ida"] = "Mat"+"ilda"
        self.switch["Mat"+"ilda"] = "Fr"+"ida"
        self.log = logging.getLogger()
        with open(self.name+".py") as in_file:
            self.schwester= in_file.read().replace(self.name , self.switch[self.name])


    def run(self):
        print (self.name)

    def close(self):
        with open(self.switch[self.name]+".py","w") as out_file:
            out_file.write(self.schwester)


if __name__ == '__main__':
    pp = Frida()
    pp.run()
    pp.close()