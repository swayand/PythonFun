import logging
import subprocess
import sys
import string
import random


class Matilda():
    def __init__(self, count):
        self.name = "Matilda"
        try:
          self.count = int(count) + 1
        except:
          self.count = 1
        try:
            from Matildacmds import cmds
            self.cmds = list(cmds)
        except:
            self.cmds = []
        self.switch = {}
        self.switch["Fr"+"ida"] = "Mat"+"ilda"
        self.switch["Mat"+"ilda"] = "Fr"+"ida"
        self.log = logging.getLogger()
        with open(self.name+".py") as in_file:
            self.schwester= in_file.read().replace(self.name , self.getSchwester())


    def getSchwester(self):
        return self.switch[self.name]

    def run(self):
        print("{} count: {}".format(self.name, self.count))
        try:
            cmds_str = self.chaos()
            if cmds_str not in self.cmds:
                subprocess.call([cmds_str])
                self.cmds.append(cmds_str)
        except:
            pass
    def chaos(self):
        str = self.str_generator(2)
        return str

    def str_generator(self, size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))

    def get_count(self):
        return self.count

    def close(self):
        with open(self.switch[self.name]+".py","w") as out_file:
            out_file.write(self.schwester)
        with open(self.name + "cmds.py", "w") as out_file:
                out_file.write("cmds = {}".format(str(self.cmds)))


if __name__ == '__main__':
    pp = Matilda(sys.argv[1])
    pp.run()
    pp.close()
    if pp.get_count()<1:
        subprocess.call(['python',pp.getSchwester()+".py",str(pp.get_count())])