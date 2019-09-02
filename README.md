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


Citation
--------

* Finn Årup Nielsen, "A new ANEW: evaluation of a word list for sentiment analysis in microblogs", Proceedings of the ESWC2011 Workshop on 'Making Sense of Microposts': Big things come in small packages. Volume 718 in CEUR Workshop Proceedings: 93-98. 2011 May. Matthew Rowe, Milan Stankovic, Aba-Sah Dadzie, Mariann Hardey (editors)
