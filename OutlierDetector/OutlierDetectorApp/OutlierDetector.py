import pandas as pd
from sklearn.ensemble import IsolationForest
import json
import numpy as np
from scipy.stats import iqr

class GetOutlierClass(object):

	def __init__(self, *args, **kw):
		self.arg1=args[0]

	#using Isolation Forest alforithm to find Outliers
	def find_outlier_method1(self):
		result1=json.loads(self.arg1)
		data = pd.DataFrame(list(result1))
		iso_for = IsolationForest(contamination=0.1).fit(data)

		#predict method will return predicted outliers with value -1
		iso_for = iso_for.predict(data)
		data_out = data[iso_for == -1]
		data_out = json.loads(data_out.to_json(orient='split'))
		del data_out['index']
		del data_out['columns']
		data_out = json.dumps(data_out['data'])
		return data_out

	def find_outlier_method2(self):

		#determined the outliers in every column by using formula: min_value = Q1 - 1.5 * IQR and max_value = Q3 + 1.5 * IQR
		#where Q1 is the first quartile value, Q3 is the third quartile value and IQR is InterQuartileRange
		result1=json.loads(self.arg1)
		data = np.array(result1)
		data_out = pd.DataFrame()
		q1 = np.percentile(data,25,axis=0)
		q3 = np.percentile(data,75,axis=0)
		iqr_val = 1.5 * iqr(data,axis=0)
		ind_arr = []
		data = pd.DataFrame(data)
		n = len(data.columns) 
		if n == 1: 
		    min_val = [q1 - iqr_val]
		    max_val = [q3 + iqr_val]
		else:
		    min_val = q1 - iqr_val
		    max_val = q3 + iqr_val 
		
		#checking the entries if they are in between min_value and max_value or not    
		for i in range(0,n):
		    a = data[(data[i] < min_val[i]) | (data[i] > max_val[i])]
		    data_out = data_out.append(a)
		    
		data_out = data_out.drop_duplicates()
		data_out = json.loads(data_out.to_json(orient='split'))
		del data_out['index']
		del data_out['columns']
		data_out = json.dumps(data_out['data'])
		return data_out
		
