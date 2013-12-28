#!/usr/bin/python
# -*- coding: utf-8 -*-
#controller.py
import datetime
import dataServerApi
import dataListener
#-----------------------
#定义全局变量
#-----------------------
#数据监听对象
g_listenerDict = {}		#每个合约一个个对象
#策略对象列表
g_strategyDict = {}		#key: 策略名，value：策略对象
#订阅股票列表
g_subStocks = []
#-----------------------
#实现函数
#-----------------------
#读取设置参数
execfile("config.ini")
#读取订阅股票
def loadSubStocks():
	global g_subStocks
	_fileReader  = open("./subStock.csv","r")
	while 1:
		line = _fileReader.readline()
		line = line.replace("\n","")
		if not line:
			break
		g_subStocks.append(line)
#创建数据连接对象
def creatDataServerLink():
	dataServerInstance = dataServerApi.CDataServerApi(HOST,PORT)
	dataServerInstance.init()
	dataServerInstance.connectServer()
	return dataServerInstance
#创建监听对象
def creatListener(bufferStack):
	global g_listenerDict
	for stock in g_subStocks:
		if not g_listenerDict.has_key(stock):
			bufferStack[stock]    = [] 
			newListener           = dataListener.CDataListerner(bufferStack[stock])
			newListener.start()
			g_listenerDict[stock] = newListener
		pass
	pass

#主入口
def run():
	#载入订阅股票代码
	loadSubStocks()
	#创建数据连接对象
	dataServerInstance = creatDataServerLink()
	#创建数据监听器
	creatListener(dataServerInstance.bufferStack)
	
	dataServerInstance.subscibeStock(g_subStocks)
	dataServerInstance.requestData(2,0,datetime.datetime(2012,10,24,0,0,0),datetime.datetime(2012,10,25,0,0,0))
	