from tosvis import *
from random import random

###############################
class MyNode(Node):
    def animateAmSend(self,time,amtype,amlen,amdst):
#        if amtype in MONITORED_AM:
            Node.animateAmSend(self,time,amtype,amlen,amdst)

    def animateAmRecv(self,time,amtype,amlen):
            Node.animateAmRecv(self,time,amtype,amlen)

############################### 
tv = TosVis(100, showDebug=False, file='/home/terra/Documents/DrawNetwork/drawnetwork.json')
MONITORED_AM = [0x71]

tv.addNetworkNodes()
tv.run()