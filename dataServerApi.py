#!/usr/bin/python
# -*- coding: utf-8 -*-
#dataServerApi.py
from DataApi_32 import CDataApi
import time
import copy

class CDataServerApi(CDataApi):
	#初始化接口
	def init(self):
		#数据堆栈
		self.bufferStack = {}	#每个合约一个堆栈
	#数据接收接口
	def onRtnDepthMarketData(self, dataType, data):
		if dataType == 3:
			self.bufferStack[data["stockCode"][:6]].append((dataType,data))
		pass

