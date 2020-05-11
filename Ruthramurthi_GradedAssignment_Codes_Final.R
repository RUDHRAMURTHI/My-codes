setwd('E:\\Rudhra\\Study for reputation\\Jigsaw acadamy materials\\GLM_Statistical Modeling\\Case Study_Graded assignment')
list.files()
adult_data <- read.csv('adult.csv', header = T)
View(adult_data)
summary(adult_data)
str(adult_data)
dim(adult_data)

#############################################Data Exploration and preparation for practice##################################################

#age variable
summary(adult_data$age)
boxplot(adult_data$age)
hist(adult_data$age)
quantile(adult_data$age, p=c(1:100)/100)
quantile(adult_data$age, p=c(0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1))
nrow(adult_data[adult_data$age>=74,]) #522
nrow(adult_data[adult_data$age>=74,])
nrow(adult_data) #48842
#Age 90 seems possible as i don't have any business person to contact.

#work class variable
summary(adult_data$workclass)
table(adult_data$workclass)
str(adult_data$workclass)
nrow(adult_data[adult_data$workclass == '?',]) # 2799
nrow(adult_data[adult_data$workclass == '?',])/ nrow(adult_data) #0.057
#only 5.7% of the workclass is unexplainable so iam dropping these records
workclass_index <- which(adult_data$workclass == '?')
length(workclass_index)
adult_data1<- adult_data[-workclass_index,] #I don't want alter my original dataFrame for reference so iam creating new dataFrame

#Exploring new dataFrame adult_data1
View(adult_data1)
summary(adult_data1$workclass)# dropped level '?' is still retained. 
unique(adult_data1$workclass)
length(adult_data1$workclass)
adult_data1$workclass <- factor(adult_data1$workclass) # adjusting the levels of the variable work class
summary(adult_data1$workclass) # Now it's fine
summary(adult_data$workclass)



summary(adult_data1)
str(adult_data1)


#fnlwgt variable
summary(adult_data1$fnlwgt)
boxplot(adult_data1$fnlwgt)
hist(adult_data1$fnlwgt)
quantile(adult_data1$fnlwgt, p=c(1:100)/100)
#IQR = 3rd Qu - 1st Qu
IQR_fn1wgt <- 237857 - 117606 
#Expected max = 75% value +(1.5*IQR)
237857 + (1.5*IQR_fn1wgt) #418233.5
nrow(adult_data1[adult_data1$fnlwgt > 418233.5 ,])# 1362
nrow(adult_data1[adult_data1$fnlwgt > 418233.5 ,])/nrow(adult_data1) # 0.02958
nrow(adult_data1[adult_data1$fnlwgt > 509985.48 ,])
# Only 3% of our data contains outliers we will think about it later

plot(adult_data1$age, adult_data1$fnlwgt)

#education variable
summary(adult_data1$education)
str(adult_data1$education)
#education variable seems fine

#educational.num variable
summary(adult_data1$educational.num)
str(adult_data1$educational.num)
#educational.num variable seems fine

#marital.status variable
summary(adult_data1$marital.status)
str(adult_data1$marital.status)
#marital.status variable also seems fine

#occupation variable
summary(adult_data1$occupation)
str(adult_data1$occupation)
nrow(adult_data1[adult_data1$occupation == '?',]) # 10
nrow(adult_data1[adult_data1$occupation == '?',])/ nrow(adult_data1) #0.0002171883
#only 5.7% of the occupation is unexplainable so iam dropping these records
Occupation_Index <- which(adult_data1$occupation == '?')
adult_data1 <- adult_data1[-Occupation_Index,]
summary(adult_data1$occupation) # levels are not good
adult_data1$occupation <- factor(adult_data1$occupation) # adjusting the levels
summary(adult_data1$occupation) # now levels are good
summary(adult_data$occupation) # comparing with original dataFrame
#Now occupation variable is also fine


#relationship variable 
summary(adult_data1$relationship)
#relationship variable seems fine


#race variable
summary(adult_data1$race)
#race variable is also in good shape


#gender variable
summary(adult_data1$gender)
#gender variable also good


#capital.gain variable
summary(adult_data1$capital.gain)
boxplot(adult_data1$capital.gain)
hist(adult_data1$capital.gain)
quantile(adult_data1$capital.gain, p=c(1:100)/100)
nrow(adult_data1[adult_data1$capital.gain >15024,])# 378
unique(adult_data1[adult_data1$capital.gain >15024,]$capital.gain)
nrow(adult_data1[adult_data1$capital.gain >=99999,]) #239
nrow(adult_data1[adult_data1$capital.gain >=99999,])/ nrow(adult_data1) #0.005191928
# It seems 99999 is an improbable value

#capital.loss variable
summary(adult_data1$capital.loss)
boxplot(adult_data1$capital.loss)
hist(adult_data1$capital.loss)
quantile(adult_data1$capital.loss, p=c(1:100)/100)
nrow(adult_data1[adult_data1$capital.loss >1980,])
unique(adult_data1[adult_data1$capital.loss >1980,]$capital.loss)
sort(unique(adult_data1[adult_data1$capital.loss >1980,]$capital.loss))
#capital.loss does not have potential outliers


#hours.per.week variable
summary(adult_data1$hours.per.week)
boxplot(adult_data1$hours.per.week)
hist(adult_data1$hours.per.week)
quantile(adult_data1$hours.per.week, p=c(1:100)/100)
#IQR = 3rd Qu - 1st Qu
IQR_hours.per.week <- 45 - 40 
#Expected max = 75% value +(1.5*IQR)
45 + (1.5*IQR_hours.per.week) # 52.5
#Expected min = 25% value -(1.5*IQR)
40 - (1.5*IQR_hours.per.week) #32.5 
nrow(adult_data1[adult_data1$hours.per.week > 52.5,]) # 5080
nrow(adult_data1[adult_data1$hours.per.week < 32.5,]) # 7030 
nrow(adult_data1[adult_data1$hours.per.week > 80,])   # 300
nrow(adult_data1[adult_data1$hours.per.week < 10,])   # 452
# seems there are outliers in this variable


#native.country varialble
summary(adult_data1$native.country)
nrow(adult_data1[adult_data1$native.country =='?',])# 811
nrow(adult_data1[adult_data1$native.country =='?',])/ nrow(adult_data1) # 0.0176178
#only 2% of the occupation is unexplainable so iam dropping these records
native.country_index <- which(adult_data1$native.country == '?')
adult_data1 <- adult_data1[-native.country_index,]
summary(adult_data1$native.country) # levels are not good
adult_data1$native.country <- factor(adult_data1$native.country)# adjusting the levels
summary(adult_data1$native.country)# now levels are good.

#income variable the dependent variable
summary(adult_data1$income)
#This variable is fine but i have to code 0 and 1 for it.

str(adult_data1)
summary(adult_data1)


####################################################Creating the Target variable ############################################


#Target variable creation for the adult_data1 dataFrame
summary(adult_data1$income)# <=50K : 34014 , >50K : 11208
adult_data1$Target <- ifelse(adult_data1$income == ">50K", 1, 0)
sum(adult_data1$Target) # 11208

#Target veriable creation for the adult_data dataframe
summary(adult_data$income)# <=50K : 37155 , >50K : 11687
adult_data$Target <- ifelse(adult_data$income == ">50K", 1, 0)
sum(adult_data$Target)# 11687


##################################################fitting the basic modal#################################################

adult_mod <-glm(formula = Target~age+fnlwgt+educational.num+capital.gain+capital.loss+hours.per.week+gender+occupation, family = "binomial", data = adult_data)
summary(adult_mod) # AIC: 36987 iam choosing this dataset

adult_mod1 <- glm(formula = Target~age+fnlwgt+educational.num+capital.gain+capital.loss+hours.per.week+gender+occupation, family = "binomial", data = adult_data1)
summary(adult_mod1) # AIC: 35065

#As clearly mentioned in the Business Problem iam not treating the '?' in the data so iam choosing adult_data dataFrame.


###########################################################Question 1 & 2 ####################################################################

#Modal building 

adult_mod2 <- glm(formula = Target~age+fnlwgt+educational.num+capital.gain+capital.loss+hours.per.week+gender+occupation, 
                  family = "binomial", data = adult_data)

summary(adult_mod2) #AIC: 36987


# Null deviance: 53751 , Residual deviance: 36943

########################################################Question 3###########################################################


#Finding McFadden's pseudo-R^2 
#Likelihood Ratio or McFadden's R2 = 1 - (residual.deviance/null.deviance)

1-(36943/53751) # 0.3127012


########################################################Question 4###########################################################

exp(coef(adult_mod2)) # Odds Ratio of Males against Females is 3.2659362912
?coef()

library(DescTools)
?OddsRatio()
OddsRatio(adult_mod2)# 3.266

exp(1.184e+00) # 3.267418

#Odds Ratio of Males against Females is 3.2659362912

###########################################################Question 5####################################################

library(caret)

pred <-predict(adult_mod2, type = "response")
class(adult_data$Target)
table(adult_data$Target)/nrow(adult_data)
pred_d<-ifelse(pred >=0.50,1,0)
sum(pred_d)
pred_df <- as.factor(pred_d)
target <- as.factor(adult_data$Target)
confusionMatrix(pred_df,target, positive = "1")# 0.8296 

#Another method
yhat = numeric(length(pred))
yhat[pred>=0.5]=1


table(adult_data$Target, yhat)

(35050+5471)/(35050+2105+6216+5471) #0.8296343

# So prediction accuracy is 0.83

########################################################Question 6 & 7#########################################################

adult_mod3 <- glm(formula = Target~gender,family = "binomial", data = adult_data)
summary(adult_mod3) #AIC: 51270

adult_mod3 <- glm(formula = Target~educational.num,family = "binomial", data = adult_data)
summary(adult_mod3) #AIC: 47779

adult_mod3 <- glm(formula = Target~occupation,family = "binomial", data = adult_data)
summary(adult_mod3) #AIC: 47561

adult_mod3 <- glm(formula = Target~age,family = "binomial", data = adult_data)
summary(adult_mod3) #AIC: 51218

adult_mod3 <- glm(formula = Target~fnlwgt,family = "binomial", data = adult_data)
summary(adult_mod3) #AIC: 53753

adult_mod3 <- glm(formula = Target~capital.gain,family = "binomial", data = adult_data)
summary(adult_mod3) # AIC: 48704

adult_mod3 <- glm(formula = Target~capital.loss,family = "binomial", data = adult_data)
summary(adult_mod3) # AIC: 52853

adult_mod3 <- glm(formula = Target~hours.per.week,family = "binomial", data = adult_data)
summary(adult_mod3) # AIC: 51164

sort(c(51270, 47779, 47561, 51218, 53753, 48704, 52853, 51164))

#sorted values: 47561 47779 48704 51164 51218 51270 52853 53753
#occupation > educational.num > capital.gain > hours.per.week > age > gender > capital.loss > fnlwgt


###########################################################Question 8####################################################

adult_mod4 <- glm(formula = Target~age+fnlwgt+educational.num+capital.gain+capital.loss+hours.per.week+gender+occupation+workclass+ 
                    education+marital.status+relationship+race+native.country,family = "binomial", data = adult_data)
summary(adult_mod4)

library(car)
vif(adult_mod4) # there are aliased coefficients in the model
VIF(adult_mod4)
#This denotes there is perfect correlation between two variables

# I believe education and education.num variable correlated as they refer to same information and based on data exploration

adult_mod4 <- glm(formula = Target~age+fnlwgt+capital.gain+capital.loss+hours.per.week+gender+workclass+education
                  +occupation+marital.status+relationship+race+native.country,family = "binomial", data = adult_data1)

# So i removed education variable.
summary(adult_mod4)

vif(adult_mod4) 
VIF(adult_mod4)
alias(adult_mod4)

adult_mod4 <- glm(formula = Target~age+fnlwgt+capital.gain+capital.loss+hours.per.week+gender+workclass+education+educational.num
                  +occupation+marital.status+relationship+race+native.country,family = "binomial", data = adult_data1)
summary(adult_mod4)

vif(adult_mod4)

alias(adult_mod4)

adult_mod4 <- glm(formula = Target~education+educational.num, family = "binomial", data = adult_data1)
summary(adult_mod4)
vif(adult_mod4)

?hatvalues()
hatvalues(adult_mod4)
plot(hatvalues(adult_mod4))

#Clearly there is a perfect correlation between education and educational.num










