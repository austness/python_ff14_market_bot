##############################################################
# Imports
##############################################################

import sys
import os
sys.path.append('../python_ff14_market_bot')
from data import *

##############################################################
# Main
##############################################################

datacenter_id = "8"

def main():
    world_ids = datacenter(datacenter_id)
    print(str(world_ids))
    # print("yes")

main()