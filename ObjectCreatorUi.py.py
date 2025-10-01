try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OperMayaUI as omui 
import os
import importlib
from . import primitiveCreatorUtil as primutil
importlib.reload(primutil)

ICON_PATH = os.path.join(os.path.dirname(__file__), 'icons').replace('\\','/')
print(ICON_PATH)

class objectCreatorDialog(QtWidgets.object):
	def __init__(self, arg=None):
		super().__init__(parent)

		self.resize(300, 300)
		self.setwindowTitle('object Creator❤️')

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.object_listWidget = QtWidgets.QListWidget()
		self.object_listWidget.setIconSize(QtCore.QSize(60,60))
		self.object_listWidget.setSpacing(5)
		self.object_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.object_listWidget.setMovement(QtWidgets.QListView.Static)
		self.object_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.object_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)
		self.name_label = QtWidgets.QLabel('Name:')
        self.name_lineEdit = QtWidgets.QLineEdit()
        self.name_lineEdit.setStyleSheet(
        	'''
				QlineEdit{
					border-radius: 5px;
					background-color: white;
					color: navy;
					font-size: 24px;
					font-family: Arial;
					}
			'''
		)

        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name_lineEdit)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.create_button = QtWidgets.QPushButton('😍Create')
        self.create_button.setStyleSheet(
			'''
				QpushButton {
					background-color: #ED378D
				}
			'''
		)

        self.cancel_button = QtWidgets.QPushButton('😒Cancel')
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.create_button)
        self.button_layout.addWidget(self.create_button)

        self.initlconWidget()

    def initlconWidget(self):
    	objs = ['cube', 'sphere', 'torus']
    	for obj in objs:
    		item = QtWidgets.QListwidetItem(obj)
    		item = setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{obj}.png')))
    		self.object_listWidget.addItem(item)

def run():

