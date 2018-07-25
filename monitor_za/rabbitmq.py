#!/usr/bin/env python

import json
import optparse
import socket
import urllib2
import subprocess
import tempfile
import os
import logging
import sys

class RabbitMQAPI(object):

	def __init__(self,user_name='dev',password='YuN#tnZ$%!qoGXUo',host_name='172.16.0.126',port=15672):

		self.user_name = user_name
		self.password = password
		self.host_name = host_name or socket.gethostname()
		self.port = port 


	def call_api(self,path):

		url = 'http://{0}:{1}/api/{2}'.format(self.host_name,self.port,path)
		password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
		password_mgr.add_password(None,url,self.user_name,self.password)
		handler =  urllib2.HTTPBasicAuthHandler(password_mgr)
		return json.loads(urllib2.build_opener(handler).open(url).read())

	def RabbitMQQueueName(self,queue):
		
		queues = []
		for queue in self.call_api(queue):
			element = {'vhost':queue['vhost'],'queuename':queue['name']}
			queues.append(element)
		return queues
				
	def QueueMessagesLength(self,queue_name,messages):
		
		for queue in self.call_api('queues'):
			if queue['name'] == queue_name:
				return queue['messages']
		
def RabbitMQStatus():

	api = RabbitMQAPI()
	args = sys.argv[1]
	args2 = sys.argv[2]

	print api.QueueMessagesLength(args2,args)

if __name__ == '__main__':
	RabbitMQStatus()
