import json

netState = {}
netState['header'] = {}
netState['nodeList'] = []

def load(file):
    global netState
    netState = json.load(file)
        
def save(file):
    global netState
    json.dump(netState,file)
    print "Saved"

def setNodeList(nodes):
    global netState
    netState['nodeList'] = []
    for node in nodes:
        temp = {}
        temp['id'] = node.getId()
        temp['pos'] = node.getPos()
        temp['name'] = node.getName()
        temp['radio'] = node.getRadioRange()
        netState['nodeList'].append(temp)

def setHeader(header):
    global netState
    netState['header']['corner'] = header[0]
    netState['header']['width']     = header[1]
    netState['header']['windowRatio'] = header[2]

def setConnections(connections):
    global netState
    netState['connections'] = connections

def getNodeList():
    global netState
    return netState['nodeList']

def getHeader():
    global netState
    return (netState['header']['corner'], netState['header']['width'], netState['header']['windowRatio'])

def getConnections():
    global netState
    return netState['connections']