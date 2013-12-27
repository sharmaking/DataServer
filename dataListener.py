#!/usr/bin/python
# -*- coding: utf-8 -*-
#dataListener.py
import threading

class CDataListerner(threading.Thread):
	def __init__(self, buffStack):
		super(CDataListerner, self).__init__()
		self.buffStack = buffStack

	def run(self):
		while 1:
			if self.buffStack:
				dataType, data = self.buffStack.pop(-1)
				self.dataListening(dataType, data)
			pass
		pass

	def dataListening(self, dataType, data):
		print data
		pass
