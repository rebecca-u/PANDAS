#import pandas
import pandas as pd

#read csv file Holiday using pd.read_csv and store in variable holiday_destinations
holiday_destinations = pd.read_csv("Holiday.csv")
print(holiday_destinations)

#print first 4 rows of data
print(holiday_destinations[0:4])

#print last 5 rows
print(holiday_destinations.tail())

##retrieving multiple columns as dataframe
print(holiday_destinations[["Destination", "Feedback", "All-inclusive hotels"]])


#Task1
#print the number of rows and columns
holiday_destinations.shape

#task2
#print rows 3 to 8
print(holiday_destinations.iloc[3:9])

#Task3
#Find mean number of all-inclusive hotels
print(holiday_destinations["All-inclusive hotels"].mean())

#task4
#create variable to store lowest score
minValue= holiday_destinations["Feedback"].min()
print("Lowest scoring destination: ", minValue)

#create variable to store information for destination with lowest score
low_score_destination = holiday_destinations[(holiday_destinations.Feedback == 1)]
print(low_score_destination)

#task5
#create variable to store highest score
maxValue= holiday_destinations["Feedback"].max()
print("Highest scoring destination: ", maxValue)

#create variable to store information for destination with lowest score
high_score_destination = holiday_destinations[(holiday_destinations.Feedback == 10)]
print(high_score_destination)

#task6
#find all the destinations where there are more than 9 all-inclusive hotels
x = holiday_destinations[(holiday_destinations["All-inclusive hotels"]>9)]

print(x)

#task7
#filter data by destinationand score above 8
y = holiday_destinations[(holiday_destinations["Feedback"]>8)]

print(y)

#task8
#filter data by destination and score below 2
#need to know if these destinations should be removed or there is a problem

c = holiday_destinations[(holiday_destinations["Feedback"]<2)]

print(c)

#Extension task 9
#Is there a correlation between number of all-inclusive hotels and score.

a = holiday_destinations["All-inclusive hotels"].corr(holiday_destinations["Feedback"]).round(2)

print(a)


#Extension task 10
#create data visualisation diagram to show destination and highest scores
holiday_destinations.plot.bar(y = "Feedback", x = "Destination", title = "A bar chart showing: feedback VS destinations")






