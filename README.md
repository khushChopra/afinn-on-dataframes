Afinn sentiment score in english for pandas dataframe
=====

USE
---
	>>> testData = {
			"content":["good boy khush","bad","ugly"],
			"id":[432,23,1]
		}
	>>> df = pd.DataFrame(testData) ### example dataframe
	>>> from afinnScore import afinnScoreDataframeColumn
	>>> afinnScoreDataframeColumn(df,0)
	>>> 0    3
	1   -3
	2   -3
	dtype: int64

