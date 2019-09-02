import csv
import pandas as pd

def sentimentScore(inputString, d):
	inputList = inputString.lower().split()
	score = 0
	for word in inputList:
		if word in d:
			score += d[word]
	return score


def afinnScoreDataframeColumn(inputDF,inputColumnIndex):
	"""
	returns a dataframe column of score calculated for each row

	inputDF : input dataframe to compute on
	inputColumnIndex : column index of the string column to apply afinn on
	"""
	with open("info.txt") as f:
		reader = csv.reader(f,delimiter="\t")
		d=list(reader)
		d = { i[0]: int(i[1]) for i in d}
	return inputDF.apply(lambda row : sentimentScore(row[inputColumnIndex],d), axis=1)