#Before starting with the data visualization task, it is necessary to install
#and request these libraries to obtain and manipulate the dataset.
library(MASS)
install.packages("ISLR")
library(ISLR)

#After, it is possible to define the dataset requested and translate it into a 
#readable file, inspect it through 
#the function str and manipulate it as our dataframe.
datasets <- "C:/Users/nikig/Desktop/anime_project.csv"
#str(datasets)
my_data <- read.csv(file = datasets, sep = ',')

#SCATTERPLOT
#Through the function pairs() it is possible to create scatter plots for each 
#variable of our datase. In this case we have worked with quantitative variables 
#to obtain different information about the dispersion of our data. We have 
#selected 7 parameters.
pairs(my_data)
pairs(~ scored_by + likes + anime_id + episodes + score + rank + popularity, my_data)

#For each single variable together with the variable popularity. In this way it 
#is possible to visualize how different sets of data are comparable.
pairs(my_data)
pairs(~scored_by + popularity, my_data)

pairs(my_data)
pairs(~likes + popularity, my_data)

pairs(my_data)
pairs(~anime_id+ popularity, my_data)

pairs(my_data)
pairs(~score + popularity, my_data)

pairs(my_data)
pairs(~rank + popularity, my_data)


#BOXPLOTS
#For same variables (except for the one "anime-id" inhering in the 
#identification of anime), it is possible to visualize different boxplots that
#represents the distribution of a sample through easy indeces. The box figured is 
#delimitated by the first and the third quartile and divided into two parts from
#the median.In the external part, the segments in this case represent the minimun 
#and the maximum.

boxplot(my_data$scored_by)

boxplot(my_data$popularity)

boxplot(my_data$likes)

boxplot(my_data$score)

boxplot(my_data$rank)


