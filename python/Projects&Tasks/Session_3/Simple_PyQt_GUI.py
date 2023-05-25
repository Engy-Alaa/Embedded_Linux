
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qtwidgets import *


carspeed = 0
class CarInterface(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		
		self.setFixedSize(1117, 636)# set the window geometry
		self.setStyleSheet("background-color: rgb(10, 24, 62);")
		self.setWindowTitle('Car Interface') # set the window title


		# create buttons for controlling the car
		self.forward_button = QPushButton('Forward')
		self.backward_button = QPushButton('Backward')
		self.left_button = QPushButton('Left')
		self.right_button = QPushButton('Right')
		self.stop_button = QPushButton('Stop')
		self.speed_inc_button = QPushButton('Speed +')
		self.speed_dec_button = QPushButton('Speed -')
		# create a palette for the buttons

		# set the palette for the buttons
		
		self.speed_inc_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.speed_dec_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.forward_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.backward_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.left_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.right_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.stop_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")

		# connect the buttons to their corresponding functions
		self.forward_button.clicked.connect(self.forward)
		self.backward_button.clicked.connect(self.backward)
		self.left_button.clicked.connect(self.left)
		self.right_button.clicked.connect(self.right)
		self.stop_button.clicked.connect(self.stop)
		self.speed_inc_button.clicked.connect(self.speed_inc)
		self.speed_dec_button.clicked.connect(self.speed_dec)

		# create horizontal layout for the buttons
		button_layout = QHBoxLayout()
		button_layout.addWidget(self.forward_button)
		button_layout.addWidget(self.backward_button)
		button_layout.addWidget(self.left_button)
		button_layout.addWidget(self.right_button)
		button_layout.addWidget(self.stop_button)
		button_layout.addWidget(self.speed_inc_button)
		button_layout.addWidget(self.speed_dec_button)
		
		self.speed_label = QLabel('Speed:')
		self.speed_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12 12pt \"Nirmala UI\";")
		# create labels for speed and direction
		self.speed = QTextEdit()
		self.speed.setReadOnly(True) 
		self.speed.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.speed.setFixedSize(1000, 100)
		self.direction = QTextEdit()
		self.direction.setReadOnly(True) 
		self.direction.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:rgba(0,171,169,100);")
		self.direction.setFixedSize(1000, 100)
		self.direction_label = QLabel('Direction: ')
		self.direction_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12 12pt \"Nirmala UI\";")
		
	

		
		# create vertical layout for the labels and buttons
		layout = QVBoxLayout()	
		layout.addWidget(self.speed_label)
		layout.addWidget(self.speed)
		layout.addWidget(self.direction_label)
		layout.addWidget(self.direction)
		layout.addLayout(button_layout)
		


		self.setLayout(layout)
	
		self.show() # show the window

	def forward(self):
		self.direction.clear()
		self.direction.append('Forward')	
		print('Forward')

	def backward(self):
		self.direction.clear()
		self.direction.append('Backward')
		print('Backward')

	def left(self):
		self.direction.clear()
		self.direction.append('Left')
		print('Left')

	def right(self):
		self.direction.clear()
		self.direction.append('Right')
		print('Right')

	def stop(self):
		self.direction.clear()
		self.direction.append('Stop')		
		print('Stop')
	
	def speed_inc(self):
		global carspeed
		self.speed.clear()
		carspeed = carspeed +10
		if carspeed > 220:
			self.speed.clear()
			self.speed.append('Full Speed')
			
		else:	
			self.speed.append(str(carspeed))		
		print('Inc')
	def speed_dec(self):
		global carspeed
		self.speed.clear()
		carspeed = carspeed -10	
		if carspeed == 0 or carspeed < 0:
			self.direction.clear()
			self.direction.append('Stop')	
			carspeed = 0
		else:
			self.speed.append(str(carspeed))	
		print('Dec')		

app = QApplication(sys.argv)
car_interface = CarInterface()
sys.exit(app.exec_())
