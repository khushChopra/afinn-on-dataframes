import pandas as pd
from afinnScore import afinnScoreDataframeColumn   ### import function

testData = {
		"content":["good boy khush","bad","ugly"],
		"id":[432,23,1]
}
df = pd.DataFrame(testData) ### example dataframe


### result from the function
print(afinnScoreDataframeColumn(inputDF=df,inputColumnIndex=0))

### appending return to the original dataframe for ease
df["score"] = afinnScoreDataframeColumn(inputDF=df,inputColumnIndex=0)
print(df)