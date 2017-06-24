import pygame, sys, json, os
import Button


GREY = (230,230,230)
GREEN = (0,150,0)
BLUE = (100,100,250)
RED = (200,0,0)
ORANGE =  (200,100,0)
AQUA = (22, 160, 133)

class MenuClass(object):
	__isClicked = False
	__surface = None
	__buttonList = None
	__networkObj = None
	__gridRows = None
	__gridCols = None

	def __init__(self,surface, networkObj, gridRows=16, gridCols=4):
		self.__buttonList = []
		self.__surface = surface
		self.__networkObj = networkObj
		self.__gridRows = gridRows
		self.__gridCols = gridCols

		# Create Buttons Here
		# self.addButton(text,gridX,gridY,width,height,callback,color)
		self.addButton("Save Network",0,0,4,1,self.save,BLUE) 
		self.addButton("Load Network",0,1,4,1,self.load,BLUE)
		self.addButton("RUN TosVis",0,3,4,2,self.run,AQUA)
		self.addButton("Add Node",0,6,4,2,self.addNode,GREEN)
		self.addButton("Delete Node", 0,8,4,1,self.deleteNode,ORANGE)
		self.addButton("Exit",0,15,4,1, self.quit_now,RED)
		
	
	def getSurface(self):
		return self.__surface

	def refresh(self):
		self.__surface.fill(GREY)
		for button in self.__buttonList:
			button.draw(self.__surface)
	
	def addNode(self):
		self.__networkObj.newNode()

	def deleteNode(self):
		self.__networkObj.deleteSelectedNodes()
	
	def addButton(self,text,gridX,gridY,sizeCols,sizeRows,callback,color):
		posX = (float(self.__surface.get_width() / self.__gridCols ) * gridX)
		posY = (float(self.__surface.get_height() / self.__gridRows) * gridY)
		height = (float(self.__surface.get_height() / self.__gridRows) * sizeRows)
		width = (float(self.__surface.get_width() / self.__gridCols ) * sizeCols)
		# print float(self.__surface.get_height()) / float(self.__gridRows)
		self.__buttonList.append(Button.BtnClass(text,posX,posY,width,height,callback,color))

	def quit_now(self):
		pygame.quit()
		sys.exit()

	def clicked(self,mouse_position):
		for btn in self.__buttonList:
			if (btn.clicked(mouse_position)):
				self.__isClicked = True
				break
		
	def procMenu(self, mouse_pos):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.eventsHandler("mouse","BUTTONDOWN", values={"key":event.button,"mouse_pos":mouse_pos})
			elif event.type == pygame.MOUSEBUTTONUP:
				self.eventsHandler("mouse","BUTTONUP"  , values={"key":event.button,"mouse_pos":mouse_pos})

	def __mouseHandler(self, evtType, values=None):
		if values == None:
			return # Something went wrong...
		if evtType == "BUTTONDOWN":
			if values["key"] == 1: # LEFT Mouse button
				if (not self.__isClicked):
					self.__isClicked = True
					self.clicked(values["mouse_pos"])

		#	if values["key"] == 3: # Right Mouse button
				

		elif evtType == "BUTTONUP":
			if values["key"] == 1: # LEFT Mouse button
				self.__isClicked = False

		#	if values["key"] == 3: # Right Mouse button
		

	def eventsHandler(self, source, eType, values=None):
		if source == "mouse":
			self.__mouseHandler(eType,values)
		# elif source == "keyboard":
		#     self.__keyboardHandler(eType,values)
		else:
			print "Unknown input source"


	def save(self):
		self.__networkObj.save()

	def load(self):
		self.__networkObj.load()

	def listConnections(self):
		print "###### \tListing connections \t######\n"
		self.__networkObj.findConnections()
		print "\n\n"

	def run(self):
		self.__networkObj.save()
		os.system('python '+os.getcwd()+'/tosvis/tvRun.py')