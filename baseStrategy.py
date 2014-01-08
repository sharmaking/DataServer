#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os

class CBaseStrategy(object):
	def __init__(self):
		super(CBaseStrategy, self).__init__()
		self.stockCode = ""
		self.customInit()
		#最新数据
		self.currentData = {}
		#连接池，用于发送信号
		self.requesHandlerObjList = []
	
	#------------------------------
	#listener 调用接口
	#------------------------------
	#自定义对象初始化
	def init(self, stockCode):
		self.stockCode = stockCode
		self.initCashe()
		pass

	#获得连接对象
	def getRequesHandlerObjList(self, requesHandlerObjList):
		self.requesHandlerObjList = requesHandlerObjList
	
	def dataListener(self, dataType, data):
		if dataType == 1:			#逐笔成交数据
			self.onRtnTradeSettlement(data)
		elif dataType == 2:			#
			self.onRtnOrderQueue(data)
		else:
			self.onRtnMarketData(data)
			#自动保存缓存触发
			if (datetime.datetime.now() - self.preSaveCacheTime)> datetime.timedelta(minutes = 5):
				self.autosaveCache()
	#------------------------------

	#------------------------------
	#cache 相关函数
	#------------------------------
	def initCashe(self):
		self.cacheFilePath = "cache/%s%s.cache" %(self.stockCode, self.name)
		self.preSaveCacheTime = datetime.datetime.now()
		self.loadCache()
		pass
    
	#读取缓存
	def loadCache(self):
		if not os.path.isfile(self.cacheFilePath):
			self.cacheFile = open(self.cacheFilePath, "w")
			self.cacheFile.close
		execfile(self.cacheFilePath)
    
	#保存缓存
	def saveCache(self, **objDict):
		self.cacheFile = open(self.cacheFilePath, "w")
		content = ""
		for key, value in objDict.items():
			content += "self.%s = %s\n" %(key, str(value))
		self.cacheFile.write(content)
		self.cacheFile.close()
		self.preSaveCacheTime = datetime.datetime.now()
		pass

	#------------------------------
	#继承重载函数
	#------------------------------
	#自定义初始化函数
	def customInit(self):
		self.name = "baseStrategy"
		pass
	#行情数据触发函数
	def onRtnMarketData(self, data):
		pass
	#逐笔成交触发函数
	def onRtnTradeSettlement(self, data):
		pass
	#买一队列触发函数
	def onRtnOrderQueue(self, data):
		pass
	def dayBegin(self):
		pass
	def dayEnd(self):
		pass
	#自动保存缓存触发函数
	def autosaveCache(self):
		#self.saveCache(data = self.data)
		pass