#!/usr/bin/env python3
#########################################################
#   Author: VXL Software                                #
#   Description: Service Program for various services   #
#########################################################
import os
import sys
from service_files.pcscd_service import Pcscd

# Function: Print Help menu
def help_menu():
    print("""Usage: servicesw <option> service_name
Options:
    enable\tEnable and start the service
    start\tStart the service
    stop\tStop the service
    status\tCheck the status of service
    """)
    sys.exit(1)

# Function: Validate Arguments
def validate_args() -> bool:
    # Check valid number of arguments are passed
    # Valid number of Args: 3
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments")
        help_menu()

    # Check valid option argument
    if sys.argv[1] not in options_args_list:
        print("Error: Invalid option argument")
        help_menu()
    
    # Check valid service name
    if not os.path.exists(SERVICE_CONFIG_PATH+sys.argv[2]+".sw"):
        print(f"Error: {sys.argv[2]} service not available")
        help_menu()

    return True

# Function: Validate Options
def validate_options():
    pass

# Function: Start with Main
def main():
    if validate_args():
        match sys.argv[2]:
            case "pcscd":
                pcscd_obj = Pcscd(sys.argv[1],sys.argv[2])
                print(pcscd_obj.validate_option()["msg"])

if __name__ == '__main__':

    # Set Valid Options argument list
    options_args_list = ["enable","start","stop","status"]
    # Set Service config file path
    SERVICE_CONFIG_PATH="/usr/local/sw/"
    # Set Enabled Service config softlink path
    SERVICE_ENABLED_PATH="/var/sw/"
    # Set Service PID path
    SERVICE_PID_PATH="/var/run/sw/"

    main()