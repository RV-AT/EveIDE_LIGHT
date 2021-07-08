import json
import logging
import os
class cfgRead():
    def __init__(self,cfgPath):
        self.cfgPath = cfgPath

    def check_path(self):
        if os.path.exists(self.cfgPath):
            return 1
        else:
            logging.debug("Path is not exists:"+self.cfgPath)
            return 0

    def get_dict(self):
        with open(self.cfgPath,"r") as readFile:
            dictNow = json.load(readFile)
            logging.debug("Successfully read Dict: "+str(dictNow)+"from :"+ self.cfgPath)
            return dictNow
    def write_dict(self,dictNow):
        with open(self.cfgPath,"w") as writeFile:
            json.dump(dictNow,writeFile)
            logging.debug("Successfully store Dict: "+str(dictNow)+"into :"+ self.cfgPath)

