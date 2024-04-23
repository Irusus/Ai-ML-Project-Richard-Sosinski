#import necessary libraries
import pandas as pd
import os

#get all files in the directory provided
fileList = os.listdir('C:\\Users\sosin\Desktop\AIMLProjectFInal\Dataset\DF')
print(fileList)


#f = pd.read_csv("C:\\Users\sosin\Desktop\AIMLProjectFInal\Dataset\DF\ds (1).csv")
#print(f)

#create the data frame
df_append=pd.DataFrame()

#used to split the files into blocks of 50 i.e. 1-51; 51-101; 101-151; 151-170.
#the loop opens the file and appends it into a dataframe
for i in range(151,170):
    csvReader = pd.read_csv("C:\\Users\sosin\Desktop\AIMLProjectFInal\Dataset\DF\ds ("+str(i)+").csv")
    df_append = df_append._append(csvReader, ignore_index=True)
print(df_append)

#the data frame is cleaned and looks out for BenignTraffic
#this same file was used for dictionary attack, the value "BenignTraffic" just needs to be changed to "DictionaryBruteForce"
df_append = df_append[df_append["label"] == "BenignTraffic"]

#the output is appended to file
#This whole process is repeated until 4 files are made due to the blocks of 50
#in total 8 files were created 4 for benign 4 for dictionary attack
df_append.to_csv("cleanedBenignV1_4.csv", index=False)

'''
df_append = pd.DataFrame()

for file in fileList:
    dfTemp = pd.read_csv(file)
    df_append = df_append.append(dfTemp, ignore_index=True)

print(df_append)
'''