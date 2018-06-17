#Group Mushy Bread - KoreanConflict_Dataset - Arkadiusz
import webget as wg
import pandas as pd


url = 'https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/KoreanConflict.csv'
response = wg.download(url)
print(response + 'downloaded')

Conflict = pd.read_csv('KoreanConflict.csv')


# Question 1: How many soldiers entered from a marine corps branch?
Soldiers = Conflict[Conflict["BRANCH"] == "MARINE CORPS"]
print("Marine Corps: ")
print(len(Soldiers.index))
# Answer: 4509

# Question 2: Which entrollment was the most common?
Soldiers = Conflict.groupby("ENROLLMENT").count()
print(Soldiers.iloc[:,2])
# Answer: Active - Regular (23973)

# Question 3: Was there an ethnicity majority throughout the war - If so, which?
Soldiers = Conflict.groupby("ETHNICITY").count()
print(Soldiers.iloc[:,2])
# Answer: Yes there was by a huge margin, White. Roughly 80 % of total.

# Question 4: Which division had the most casualties?
Soldiers = Conflict.groupby("DIVISION").count()
maxValue = Soldiers.iloc[:,2].max()
mask = (Soldiers.iloc[:,2]==maxValue)
print("Division : "+Soldiers[mask].index.values+" had the most casualties with a total of: "+str(Soldiers[mask].iloc[0,0]))
# Answer: 38 INF 2 DIV with a total of 1755.

# Question 5: Which Home state suffered the most losses?
Soldiers = Conflict.groupby("HOME_STATE").count()
maxValue = Soldiers.iloc[:,2].max()
mask = (Soldiers.iloc[:,2]==maxValue)
print("The state of : "+Soldiers[mask].index.values+" suffered the most, with a count of: " +str(Soldiers[mask].iloc[0,0]))
# Answer: California with a count of 2571 in total.