#!/usr/bin/env python3
#########################################################
#   Author: VXL Software                                #
#   Description: PCSCD Service                          #
#########################################################
import os
import sys
from pathlib import Path

class Pcscd():
    # Set Service config file path
    SERVICE_CONFIG_PATH="/usr/local/sw/"
    # Set Enabled Service config softlink path
    SERVICE_ENABLED_PATH="/var/sw/"
    # Set Service PID path
    SERVICE_PID_PATH="/var/run/sw/"

    def __init__(self,option_arg:str,service_arg:str):
        self.option_arg = option_arg
        self.service_arg = service_arg

    def validate_option(self) -> dict:
        match self.option_arg:
            case "enable":
                try:
                    os.remove(self.SERVICE_ENABLED_PATH+self.service_arg+".sw")
                    os.symlink(self.SERVICE_CONFIG_PATH+self.service_arg+".sw",self.SERVICE_ENABLED_PATH+self.service_arg+".sw")
                    return {"status":"pass","msg":"Service "+self.service_arg+" enabled"}
                except OSError:
                    os.symlink(self.SERVICE_CONFIG_PATH+self.service_arg+".sw",self.SERVICE_ENABLED_PATH+self.service_arg+".sw")
                    return {"status":"pass","msg":"Enabling "+self.service_arg+" enabled"}
                
            case "start":
                pass
            case "stop":
                pass
            case "status":
                pass