import maya.cmds as cmds

def doCreateItem(shape, name):
	default_names = {
		"cone": "polyCone_geo",
		"cube": "polyCube_geo",
		"torus": "polyTorus_geo",
		"sphere": "polySphere_geo"
	}

	if shape not in default_names:
		cmds.warning(f"Unknown shape type: {shape}")
		return

	obj_name = name if len(name) != 0 else default_names[shape]

	if shape == "cone":
		cmds.polyCone(n=obj_name)
	elif shape == "cube":
		cmds.polyCube(n=obj_name)
	elif shape == "torus":
		cmds.polyTorus(n=obj_name)
	elif shape == "sphere":
		cmds.polySphere(n=obj_name)