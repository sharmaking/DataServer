#!/usr/bin/python
# -*- coding: utf-8 -*-
#baseMultiple.py
import sys
sys.path.append("..")
import baseStrategy

class CBaseMultiple(baseStrategy.CBaseStrategy):	
	def init(self, stockCode):
		self.stockCode = stockCode
		self.initCashe()
		pass

	#自定义初始化函数
	def customInit(self):
		"""需要重载"""
		self.name = "baseMultiple"
		pass

	def dayBegin(self):
		"""需要重载"""
		pass
	
	def dayEnd(self):
		"""需要重载"""
		pass

	#数据监听函数相关函数  需要重载
	def dataListenning(self, data):
		"""需要重载"""
		pass
	#自动保存缓存触发函数
	def autosaveCache(self):
		"""需要重载"""
		#self.saveCache(data = self.data)
		pass