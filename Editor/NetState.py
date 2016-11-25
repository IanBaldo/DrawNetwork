import json

netState = {}
netState['header'] = {}
netState['nodeList'] = []

def loadSafadao(file):
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
        netState['nodeList'].append(temp)

def setHeader(header):
    global netState
    netState['header']['corner'] = header[0]
    netState['header']['width']     = header[1]
    netState['header']['windowRatio'] = header[2]

def getNodeList():
    global netState
    return netState['nodeList']

def getHeader():
    global netState
    return (netState['header']['corner'], netState['header']['width'], netState['header']['windowRatio'])