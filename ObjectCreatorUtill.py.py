import maya.cmds as cmds

def doCreateItem(shape,name):

	if shape == "cone":
		if len(name)!= 0 :
			cmds.polyCone(n= name)
		else:
			cmds.polyCone(n = "polyCone_geo")
	elif shape == "cube":
		
		if len(name)!= 0 :
			cmds.polyCube(n= name)
		else:
			cmds.polyCube(n = "polyCube_geo")
	elif shape == "torus":
		cmds.polyTorus(n= name)
		if len(name)!= 0 :
			cmds.polyTorus(n= name)
		else:
			cmds.polyTorus(n = "polyTorus_geo")
	elif shape == "sphere":
		if len(name)!= 0 :
			cmds.polySphere(n= name)
		else:
			cmds.polySphere(n = "polySphere_geo")