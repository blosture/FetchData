# Data API access library.
# Author: Subrat Pathak

# This library wraps API calls for python environment.

import sys
import numpy as np
import requests
import random
import time
import datetime
import json
import os
import pandas as pd

session = requests.Session()

class blos:
	apiKey = "apiKey"
	endpointX = "http://ec2-13-127-55-193.ap-south-1.compute.amazonaws.com:4000/api/trainX"
	endpointY = "http://ec2-13-127-55-193.ap-south-1.compute.amazonaws.com:4000/api/trainY"
	# endpointX = "http://localhost:4000/api/trainX"
	# endpointY = "http://localhost:4000/api/trainY"
	projectId = "EEG"
	batchId = ""
	startSampleId = ""
	stopSampleId = ""
	payload = ""
	xFeature = ""
	yFeature = ""
	xRangeValues = ""
	xValue = ""
	yRangeValues = ""
	yValue = ""
	response = ""

	def __init__(self,apiKey):
		self.apiKey = apiKey
	
	def dataset(self,projectId,batchId):
		self.projectId = projectId
		self.batchId = batchId
		print "Set."

	def getTrainX(self,xFeature, startSampleId, stopSampleId):

		self.xFeature = xFeature
		self.startSampleId = startSampleId
		self.stopSampleId = stopSampleId
		
		payload = {
			 'apiKey': self.apiKey,
			 'batchId': self.batchId,
			 'projectId': self.projectId,
			 'xFeature': self.xFeature,
			 'startSampleId': self.startSampleId,
			 'stopSampleId': self.stopSampleId,
			}
		self.payload = payload
		self.response = session.post(self.endpointX, json=payload)
		xRangeData = self.response.json()
		if self.response.status_code == 200:
			xRangeDataSorted = sorted(xRangeData, key = lambda i: i['sampleID'])
			xRangeDataFrame = pd.DataFrame(xRangeDataSorted)
			self.xRangeValues = xRangeDataFrame['value']
			return self.xRangeValues
		else:
			print "Incorrect query, check input."
			return
		

	
	def getTrainY(self,yFeature, startSampleId, stopSampleId):

		self.yFeature = yFeature
		self.startSampleId = startSampleId
		self.stopSampleId = stopSampleId
		
		payload = {
			 'apiKey': self.apiKey,
			 'batchId': self.batchId,
			 'projectId': self.projectId,
			 'yFeature': self.yFeature,
			 'startSampleId': self.startSampleId,
			 'stopSampleId': self.stopSampleId,
			}
		self.payload = payload
		self.response = session.post(self.endpointY, json=payload)
		yRangeData = self.response.json()
		if self.response.status_code == 200:
			yRangeDataSorted = sorted(yRangeData, key = lambda i: i['sampleID'])
			yRangeDataFrame = pd.DataFrame(yRangeDataSorted)
			self.yRangeValues = yRangeDataFrame['value']
			return self.yRangeValues
		else:
			print "Incorrect query, check input."
			return
