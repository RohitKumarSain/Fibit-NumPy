import numpy as np

data = np.loadtxt("fitness.txt",dtype=str)

date,step_count,mood,calories_burned,hours_of_sleep,bool_of_active,weight=data.T

step_count = np.array(step_count,dtype=int)

mood= np.array(mood)

mood[mood=='300']="Happy"
mood[mood=='200']="Neutral"
mood[mood=='100']="Sad"

calories_burned = np.array(calories_burned,dtype=int)

hours_of_sleep = np.array(hours_of_sleep,dtype=int)

activness_status = np.array(bool_of_active)

activness_status[activness_status=="500"] = "Active"
activness_status[activness_status=="0"] = "Inactive"

weight = np.array(weight,dtype=int)

# EDA: Insights from the data

# What is the average step count?

print("Average step count:",step_count.mean())

# On which day the step count was highest?

print("Step count was highest on", date[step_count.argmax()])

# Lets check the calories burnt on the day?

print("Calories burnt on highest step count day: ",calories_burned[step_count.argmax()])

# Lets try to get the number of steps on that day as well

print("Number of Steps on", date[step_count.argmax()],"is", step_count.max())

# What is the most frequent mood?

# print(np.unique(mood, return_counts=True))

print("The happy mood count is",mood[mood=="Happy"].shape[0], "and", np.round(((mood[mood=="Happy"].shape[0])/mood.shape[0])*100), "% happy in", mood.size,"days")

# Comparing step counts on bad mood days and good mood days.

good_mood_days = mood[mood=="Happy"].size
bad_mood_days = mood[mood=="bad"].size

print("Average Step counts on Good Mood Days is",np.round(step_count[mood=="Happy"].mean()),"\nAverage Step counts on Bad Mood Days is",np.round(step_count[mood=="Sad"].mean()))

# How many Highest / Lowest calories burned on which day

highest_calories_burned = calories_burned.max()
lowest_calories_burned  = calories_burned.min()

print("Highest calories", highest_calories_burned,"burned on",date[calories_burned.argmax()])
print("Lowest calories", lowest_calories_burned,"burned on",date[calories_burned.argmin()])

#  Activness: How much active or inactive

print("Average Active days: ",np.count_nonzero(activness_status[activness_status=="Active"]))
print("Average Inactive days: ",np.count_nonzero(activness_status[activness_status=="Inactive"]))

# How much calories burned for 1 kg weight

unique_weight = np.unique(weight)

for w in unique_weight:
    print("Total Calories Burned:",calories_burned[weight==w].sum(),"for reducing weight",w,"kg")