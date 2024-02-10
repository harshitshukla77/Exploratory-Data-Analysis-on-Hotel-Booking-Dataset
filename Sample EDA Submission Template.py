#!/usr/bin/env python
# coding: utf-8

# # **Project Name**    - 
# 
# 

# ##### **Project Type**    - EDA
# ##### **Contribution**    - Individual
# ##### **Name** - Harshit Shukla

# # **Project Summary -**

#     This data set contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces,weather the booking was successfull or canceled , was there any deposit made at the time of reservation or not, which type of customer made the booking , was the booking made by agent or not , time is also recorded by the hotels like which month did they check in , what was the week number of the check in among other things. All personally identifying information has been removed from the data 
# 
#     The hotel industry is one of the most prominent industries in the world, and with the increase in competition, it has become increasingly important to analyze data to better understand customers and optimize revenue and improve customer satisfaction. The Hotel Booking Dataset EDA project aimed to provide insights into the trends and patterns within the hotel booking industry using a hotel booking dataset.
# 
#     The dataset contained information on hotel bookings from two different hotels (City & Resort Hotels), including booking information, customer demographics, and hotel details etc for three years (2015, 2016 & 2017).
# 
#     After loading the dataset, I started with data preparation and cleaning before I moved to EDA to analyse it. The dataset has around 119,390 records (rows) with 32 features (columns). Out of which, there were 31994 duplicate data, so deleted those rows. Remaining number of rows was 87396.Now 4 columns (company, agent, country & children) out of 32 had missing values. I imputed them in following manner:
# 
#     Company: There may be some cases when customer didn't booked hotel via any company. Hence I will replace null values with0.
#     Agent: Similarly there can be bookings made without any agent, hence replaced them with 0.
#     Children: Children column is numeric and skewed, hence choose median for imputing missing values.
#     Country: country column is categorical column. We use mode of ‘country’ column, But it can lead to bias towards a specific country that occurs most frequently in the data. Hence I created a new category ‘others’ for missing values.
#     There were 166 rows with 0 adults, children and babies which seems unlikely hence dropped those rows. Then created new column for total_guest = (adults + children). Ignored babies because generally they are not charged. Some values in ‘adr’ were negative, which must be an error so imputed them with median since it was a skewed data. Created new column for total_stays_night = (weekend_nights + week_nights) to analyze average length of stay.Assigned appropriate data types for some columns.
# 
#     After cleaning the dataset, various exploratory data analysis techniques were used to better understand the dataset. Three broad categories for EDA are: Univariate, Bivariate, Multivariate
# 
#     I used different types of charts and metrics to visualize the relationships, trends, understand preferences etc. to better understand the data. 
#     Overall, the Hotel Booking Dataset EDA project provided valuable insights into the hotel booking industry, including customer preferences, booking patterns, and trends over time. These insights can help hotels optimize revenue and improve customer satisfaction by tailoring their services to meet customer needs and expectations.

# # **GitHub Link -**

# Provide your GitHub Link here.

# # **Problem Statement**
# 

# **Write Problem Statement Here.**

#     -The main problemns of the hotels are high cancellation rates which is basically due to the offers and discounts        provided by their competitors and the quality of service provided by the hotel, In this buisness the profit of the hotel depends mainly on how many days on an average customers are staying in their hotels, low cancellation rates, and traffic of customers . So to increase the revenue of the hotels we have to deal with these problems mentioned above by trying to work on the basics.

# #### **Define Your Business Objective?**

# We have to reduce the cancellation rate and increase bookings for hotels as a result

# # **General Guidelines** : -  

# 1.   Well-structured, formatted, and commented code is required. 
# 2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits. 
#      
#      The additional credits will have advantages over other students during Star Student selection.
#        
#              [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
#                        without a single error logged. ]
# 
# 3.   Each and every logic should have proper comments.
# 4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
#         
# 
# ```
# # Chart visualization code
# ```
#             
# 
# *   Why did you pick the specific chart?
# *   What is/are the insight(s) found from the chart?
# * Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.
# 
# 5. You have to create at least 10 logical & meaningful charts having important insights.
# 
# 
# [ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule. 
# 
# U - Univariate Analysis,
# 
# B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)
# 
# M - Multivariate Analysis
#  ]
# 
# 
# 
# 

# # ***Let's Begin !***

# ## ***1. Know Your Data***

# ### Import Libraries

# In[1]:


# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Dataset Loading

# In[2]:


# Load Dataset
df=pd.read_csv("C:/Users/harshit/Desktop/datasets/project_datsets/Hotel Bookings.csv")


# ### Dataset First View

# In[3]:


# Dataset First Look
df.head()


# ### Dataset Rows & Columns count

# In[4]:


# Dataset Rows & Columns count
df.shape


# ### Dataset Information

# In[5]:


# Dataset Info
df.info()


# #### Duplicate Values

# In[6]:


# Dataset Duplicate Value Count
df.duplicated().sum()   


# In[7]:


df=df[df.duplicated()!=True]
df.reset_index(inplace=True) 


# In[8]:


df.drop(["index"],axis=1,inplace=True)


# #### Missing Values/Null Values

# In[9]:


# Missing Values/Null Values Count
df.isnull().sum() 


# In[10]:


# Visualizing the missing values


# ### What did you know about your dataset?

#     Data available is of 119390 rows and 32 columns. This dataset has 12 categorical columns and 20 numerical columns. Columns such as country agent and company have high number of missing (NULL) values. 31994 duplicate rows are also present in the dataset. After removing those duplicate rows the remaining dataset left with us is of shape 32 columns and 87396 rows

# ## ***2. Understanding Your Variables***

# In[11]:


# Dataset Columns
df.columns


# In[12]:


# Dataset Describe
df.describe().T


# In[13]:


df.describe(include=["O"]).T


# ### Variables Description 

# - hotel: Name of hotel ( City or Resort)
# - is_canceled: Whether the booking is canceled or not (0 for no canceled and 1 for canceled)
# - lead_time: time (in days) between booking transaction and actual arrival.
# - arrival_date_year: Year of arrival
# - arrival_date_month: month of arrival
# - arrival_date_week_number: week number of arrival date.
# - arrival_date_day_of_month: Day of month of arrival date
# - stays_in_weekend_nights: No. of weekend nights spent in a hotel
# - stays_in_week_nights: No. of weeknights spent in a hotel
# - adults: No. of adults in single booking record.
# - children: No. of children in single booking record.
# - babies: No. of babies in single booking record. 
# - meal: Type of meal chosen 
# - country: Country of origin of customers (as mentioned by them)
# - market_segment: What segment via booking was made and for what purpose.
# - distribution_channel: Via which medium booking was made.
# - is_repeated_guest: Whether the customer has made any booking before(0 for No and 1 for 
#                      Yes)
# - previous_cancellations: No. of previous canceled bookings.
# - previous_bookings_not_canceled: No. of previous non-canceled bookings.
# - reserved_room_type: Room type reserved by a customer.
# - assigned_room_type: Room type assigned to the customer.
# - booking_changes: No. of booking changes done by customers
# - deposit_type: Type of deposit at the time of making a booking (No deposit/ Refundable/ No refund)
# - agent: Id of agent for booking
# - company: Id of the company making a booking
# - days_in_waiting_list: No. of days on waiting list.
# - customer_type: Type of customer(Transient, Group, etc.)
# - adr: Average Daily rate.
# - required_car_parking_spaces: No. of car parking asked in booking
# - total_of_special_requests: total no. of special request.
# - reservation_status: Whether a customer has checked out or canceled,or not showed 
# - reservation_status_date: Date of making reservation status.

# ### Check Unique Values for each variable.

# In[14]:


# Check Unique Values for each variable.
df.nunique()


# # 3. ***Data Wrangling***

# ### Data Wrangling Code

# In[15]:


# Checking null values percentage of each column
    
round((df.isnull().sum()/df.shape[0])*100)    


# In[16]:


# We will be removing company column here because it has 94% of NULL values

df.drop("company", inplace= True , axis=1)


# In[17]:


# Combining children and baby column into 1 column as total_children and then dropping old columns

df["Total_children"] =  df["babies"] + df["children"]

df.drop(["children","babies"],axis=1,inplace= True)


# In[18]:


# Combining children and adults into one column    

df["Total_persons"] = df["Total_children"] + df["adults"]


# In[55]:


# making a date column by combining 3 columns arrival_date_year , arrival_date_month and arrival_date_day_of_month

df["date"]=df["arrival_date_year"].astype(str)+"/"+df["arrival_date_month"]+"/"+df["arrival_date_day_of_month"].astype(str)


# In[58]:


# converting newly made date column to datetime column and then verifying the correction

df["date"]=pd.to_datetime(df["date"])
df.dtypes


# In[81]:


# Dropping the old columns as everything can be accessed using this new column

df.drop(["arrival_date_day_of_month","arrival_date_year","arrival_date_month"], inplace= True , axis=1)


# In[19]:


df.head()            # verifying new columns by observing them


# In[20]:


df.columns           # displaying data with added new columns


# <span style = "color:blue">
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# <span>    

# ### Canceled bookings and Repeated guests

# In[53]:


repeat=df.groupby ("hotel")["is_repeated_guest"].value_counts(normalize=True).unstack()

cancel=df.groupby (["hotel"] )["is_canceled"].value_counts( normalize = True).unstack()


# In[54]:


print(repeat)
print("-"*100)
print("*"*50)
print("-"*100)
print(cancel)


# <span style = "color:darkblue">
# 
# - Repeated guests in City Hotel is around 3.1 %
# - Canceled bookings in City hotel is around 30 %
# -----------------------------------------------------------------------------------------------------------------
# - Repeated guests in Resort Hotel is around 5.0 %
# - Canceled bookings in Resort hotel is around 23 %
# <span>

# ### Cancellations  Based on Distribution Channel

# In[23]:


total_bookings=df.groupby("distribution_channel")["booking_changes"].count() 
total_bookings


# <span style = "color:darkblue">
# 
# - Most number of bookings is done by TA/TO followed by Direct and then Corporate
#     <span>    

# In[24]:


bookings_cancel=df[df["is_canceled"]!=0].groupby("distribution_channel")["is_canceled"].count()
bookings_cancel


# <span style = "color:darkblue">
# 
# - Most number of Booking cancellation is done by TA/TO followed by Direct and then Corporate
#     <span>    

# In[25]:


((bookings_cancel / total_bookings)*100)[0:4]


# <span style = "color:darkblue">
# 
# - 30.9% of bookings given by Travel agents/ Tour Operator are getting cancelled  
# 
# <span>

# <span style = "color:blue">
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# <span>    

# ### Booking changes

# In[26]:


total_bookings


# 
# <span style = "color:darkblue">
# 
# - Most number of bookings are done by TA/TO followed by Direct and then Corporate
# <span>
# 
#     

# In[27]:


booking_changes=df[df["booking_changes"]!=0].groupby("distribution_channel")["booking_changes"].sum()
booking_changes


# <span style = "color:darkblue">
# 
# - Most number of bookings changes are done by TA/TO followed by Direct and then Corporate
# <span>
# 
#     

# In[28]:


(booking_changes / total_bookings ) * 100


# <span style = "color: darkblue">
# 
# - 42.8% of Corporate customers are making changes in their bookings
# - 42.6% of Direct customers are making changes in their bookings
# 
# <span>
# 
# <span style = "color:blue">
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# <span>    

# ### Arrival Date Month

# In[84]:


print("City Hotel monthwise bookings")
print(50*"*")
df[df["hotel"]=="City Hotel"]["date"].dt.month_name().value_counts()


# In[85]:


print("Resort Hotel monthwise bookings")
print(50*"*")
df[df["hotel"]=="Resort Hotel"]["date"].dt.month_name().value_counts()


# <span style = "color:darkblue">
#         
# - Using the above data we can derive that peak season for City Hotel is from April -to- August 
# - Using the above data we can derive that peak season for Resort Hotel are July and August
#     
# <span>
# <span style = "color:darkblue">
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# <span>    

# ### Country

# In[30]:


df.value_counts("country", normalize=True).iloc[0:3]


# <span style = "color: darkblue">
# 
# - Most number of bookings is coming from PORTUGAL 30% and Great Britain 11%
# <span>

# ### Agent

# In[31]:


df.value_counts("agent").iloc[0:3]


# <span style = "color: darkblue">
# 
# - Highest number of bookings (38%) is done by agent with ID number 9.0
#     <span>

# In[32]:


df[df["hotel"]=="City Hotel"]["agent"].value_counts(normalize=True).iloc[0:3]


# <span style = "color: darkblue">
# 
# - Highest number of bookings 60% is done by agent with ID number 9.0 in City Hotel
#     <span>

# In[33]:


df[df["hotel"]=="Resort Hotel"]["agent"].value_counts(normalize=True).iloc[0:3]


# <span style = "color: darkblue">
# 
# - Highest number of bookings (47.5%) is done by agent with ID number 240 in Resort Hotel
#     <span>
# <span>
#     
# <span style = "color:darkblue">
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# <span>    

# ### Deposit type

# In[34]:


df.groupby(["deposit_type"])["is_canceled"].sum()


# <span style = "color: darkblue">
# 
# - Highest number of cancellations is done when NO DEPOSIT is made at the time of reservation
#     <span>

# ### What all manipulations have you done and insights you found?

# Answer Here.

# ## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

# #### Chart - 1

# In[36]:


plt.figure(figsize=(4,4))
plt.pie(df["is_canceled"].value_counts(),shadow=True,autopct="%1.1f%%",labels=["Not Canceled bookings","Canceled bookings"],explode=(0,0.2),startangle=90,colors=["lightcoral","hotpink"])
plt.show()


# ##### 1. Why did you pick the specific chart?

#     In pie chart it is easy to explain the comparison between two or more variables using the percentage terms through area covered in a circle with different colors. So, I used Pie chart and which helped me to get the percentage comparision between canceled and Not canceled bookings.

# ##### 2. What is/are the insight(s) found from the chart?

#     From the above pie chart we can clearly see that the percentage of 
#     - Not canceled bookings is 72.5%
#     - Canceled bookings is 27.5%  

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     - Not canceled-----72.5%
#     - Cancelled---------27.5%  
#     
#     Using the data we can clearly say that the average cancellation percentage of these hotels is much higher than the industry average cancelltaion rate. So, if this cancellation rate continues or increases in the future this will lead to major problems for the hotels

# #### Chart - 2

# In[71]:


sns.countplot(x=df["is_canceled"],hue=df["hotel"],palette="rocket")
plt.title("Cancellations as per Hotels")
plt.xticks(ticks=[0,1],labels=[" Not Canceled","Canceled"])
plt.xlabel("")
plt.ylabel("Number of Bookings")
plt.show()
print(cancel)


# ##### 1. Why did you pick the specific chart?

# 
#     The countplot is used to represent the occurrence(counts) of the observation present in the categorical variable. So i decided to use this plot so as to visualise the number of canceled bookings and not canceled bookings on both Resort hotel and City hotel

# ##### 2. What is/are the insight(s) found from the chart?

#     - Percentage of canceled booking in Resort hotel is 23.48%
#     - Percentage of canceled booking in City hotel is 30%
# 
#     We can clearly see that no of canceled bookings in the City hotel is much higher when compared to Resort hotel. Average cancellation rate of both hotels combined is 27.5% whereas cancellation rate of City hotel is 30% which is higher than average percentage but in resort hotel cancellation percentage is 23.48% which is less than average percentage 
# 
# 

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     We can see that cancellation rate of City hotel is higher than the average cancellation rate of both combined which is a major problematic factor for them. So they need to revise their cancellation policies so as to get more positive impact on their hotel

# #### Chart - 3

# In[38]:


plt.figure(figsize=(4,3))
sns.histplot(data=df,x="market_segment",color="chocolate")
plt.xticks(rotation="vertical")
plt.title("Number of bookings as per Market Segment")
plt.ylabel("Number of Customers")
plt.xlabel("Market Segments")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     A histogram is a graph that shows the frequency of numerical data using rectangle which are joined together. The height of a rectangle (the vertical axis) represents the distribution frequency of a variable. I wanted to know how many bookings are made through various market segments

# ##### 2. What is/are the insight(s) found from the chart?

#     we can clearly see that from above histogram most number of bookings is coming from 
#     - (**1**) Online TA
#     - (**2**) Offline TA/TO
# 

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     Hotels need to focus more on other market segments such as Direct Corporate Complementary Groups and AViation by providing offers so that the bookings by these market segments gets increased.

# #### Chart - 4

# In[39]:


plt.figure(figsize=(4,3))
valuedf=pd.DataFrame(df["country"].value_counts())[0:6]
sns.barplot(x=valuedf.index,y=valuedf["country"],palette="rocket")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     The Barplot represents the frequency of the observation present in the data provided to it. So i decided to use this plot so as to visualise the frequency of the bookings from the particular country in both hotels

# ##### 2. What is/are the insight(s) found from the chart?

#     I found out that most number of bookings are coming from Portugal followed by the Great Britain. We can also see that a large chunk of customers are coming from only two countries and rest other countries customers are less in number

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     Using this gained insight we can say that both hotels should work on gaining more and mnore customers from the countries like Spain Italy and Denmark

# #### Chart - 5

# In[75]:


temp=df["date"].dt.month_name().value_counts()
months_list=['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
data={}
for i in months_list:
    data[i]=temp[i]

plt.plot(data.keys(),data.values(),color="hotpink",marker=".",markersize=10,linestyle="--")
plt.xticks(rotation="vertical")
plt.title("Peak Season for Buisness")
plt.xlabel("Months")
plt.ylabel("Number of Bookings")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     A line chart is used to represent data points and then connecting them by straight lines. This type of chart is particularly useful for visualizing trends, changes, and relationships in data over a period of time.

# ##### 2. What is/are the insight(s) found from the chart?

#     We can clearly see that the number of bookings are increasing during the summer months and are decreasing in winter months. The trend of which is that bookings are increasing from January to August making a peak in August months and then it starts decreasing making the foot of the graph in december month

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     Hotels should targets months between May to August so as to capture more and more bookings in these peak season

# #### Chart - 6

# In[41]:


temp=pd.DataFrame(df["meal"].value_counts())
plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.barplot(x=temp.index,y=temp["meal"],palette="crest")
plt.title("Meal preference of customers")
plt.ylabel("Number of meals consumed")
plt.xlabel("Type of meal")

plt.subplot(1,2,2)
sns.countplot(data=df,x="meal",hue="hotel",palette="inferno")
plt.title("Meal preference of customers hotelwise")
plt.ylabel("Number of meals consumed")
plt.xlabel("Type of meal")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     Subplots are used to make a grid of more than one plots and then we can compare those charts side by side. I have used subplots in this visualisation and then in the subplots i have used barplots to show the results

# ##### 2. What is/are the insight(s) found from the chart?

#      - We have found that BB (Bed and Breakfast) is the most preferred type of meal plan among the customers followed by SC (Self catering) and HB(Half Board)
#      - In both the hotels BB (Bed and Breakfast) is the most preferred meal plan followed by HB(Half board) in Resort hotel and SC(Self Catering) in City hotel

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     - City hotel should focus on HB (Half board) meal plan
#     - Resort hotel should focus on SC (Self Catering) meal plan
#     - Both hotel should focus on FB (Full Board) meal plan

# #### Chart - 7

# In[42]:


plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.countplot(data=df,x="customer_type",palette="rocket")
plt.title("Booking overview by customer type ")
plt.ylabel("Number of bookings")

plt.subplot(1,2,2)
sns.countplot(data=df,x="customer_type",hue="hotel",palette="magma")
plt.ylabel("Number of bookings")
plt.title("Booking overview by customer type of each hotel")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     Subplots are used to make a grid of more than one plots and then we can compare those charts side by side. I have used subplots in this visualisation and then in the subplots i have used countplot to show the results of various observations. 

# ##### 2. What is/are the insight(s) found from the chart?

#     - We found out that number of customers coming through the Transient customer type is much than than any of the other customer types

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     Hotels should try to retain more and more Transient type customers and also come up with more offers for the other customer types, and this will positively impact their bookings in a good way.

# #### Chart - 8

# In[43]:


plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.countplot(x=df["date"].dt.year,palette="rocket")
plt.title("Booking overview yearwise")
plt.ylabel("Number of bookings")

plt.subplot(1,2,2)
sns.countplot(x=df["date"].dt.year,hue=df["hotel"],palette="magma")
plt.ylabel("Number of bookings")
plt.title("Booking overview year and hotelwise")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     Subplots are used to make a grid of more than one plots and then we can compare those charts side by side. I have used subplots in this visualisation and then in the subplots i have used countplot to show the results of various observations. 

# ##### 2. What is/are the insight(s) found from the chart?

#     As per the data  available to us we can say that there is a increasing trend in the number of customers coming to the hotels making a peak in the year 2016

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     Both the hotels have uptrend in their number of customers coming to thier hotels  

# #### Chart - 9

# In[44]:


plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.countplot(data=df,x="deposit_type",palette="rocket")
plt.title("Booking distribution on basis of deposit type")
plt.ylabel("Number of bookings")

plt.subplot(1,2,2)
sns.countplot(data=df,x="deposit_type",hue="is_canceled",palette="magma")
plt.ylabel("Number of bookings")
plt.title("Cancellations on basis of deposit type")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     Subplots are used to make a grid of more than one plots and then we can compare those charts side by side. I have used subplots in this visualisation and then in the subplots i have used countplot to show the results of various observations. 

# ##### 2. What is/are the insight(s) found from the chart?

#     - We can see that most numbers of customers who are making bookings are not making any deposit.
#     - Cancellation rate among the customers not making any deposit is also higher than any other .

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     This insight will help the hotels by encouraging them to come up with various ways so as to make customers pay for the   bookings in advance and this will as a result decrease the cancellation rate 

# #### Chart - 10

# In[45]:


plt.figure(figsize=(17,8))
sns.heatmap(df.corr(),annot=True)
plt.show()


# ##### 1. Why did you pick the specific chart?

#     A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table shows the correlation between two variables. A correlation matrix is used to summarize data, as an input into a more advanced analysis, and as a diagnostic for advanced analyses. The range of correlation is [-1,1].
# 
#     Thus to know the correlation between all the variables along with the correlation coeficients, i used correlation       heatmap.

# ##### 2. What is/are the insight(s) found from the chart?

#     There is no considerable amount of correlation between the variables other than the ones which are derived from each    other 

# #### Chart - 11

# In[69]:


sns.lineplot(y=df["adr"],x=df["date"].dt.month_name(),hue =df["hotel"])
plt.xticks(rotation="vertical")
plt.show()


# ##### 1. Why did you pick the specific chart?

#     Line chart is chosen for this visualisation because it helps in observing the trend of the variables over time and in this chart i wanted to look for the trend of the ADR over the year how the ADR varies over time.

# ##### 2. What is/are the insight(s) found from the chart?

#     -Adr for resort hotel makes peak in august month same as for city hotel.
#     -Using the graph we can clearly observe that adr of peak months of resort hotel is much higher than city hotel , it can also be observed that the ADR of normal months of resort hotels is much less as compared to city hotels .

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

#     -Customers prefer city hotels in normal months and for holiday months which is around August as according to the dataset customer's prefer Resort hotels.

# #### Chart - 12

# In[47]:


# Chart - 12 visualization code


# ##### 1. Why did you pick the specific chart?

# Answer Here.

# ##### 2. What is/are the insight(s) found from the chart?

# Answer Here

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

# Answer Here

# #### Chart - 13

# In[48]:


# Chart - 13 visualization code


# ##### 1. Why did you pick the specific chart?

# Answer Here.

# ##### 2. What is/are the insight(s) found from the chart?

# Answer Here

# ##### 3. Will the gained insights help creating a positive business impact? 
# Are there any insights that lead to negative growth? Justify with specific reason.

# Answer Here

# #### Chart - 14 - Correlation Heatmap

# In[49]:


# Correlation Heatmap visualization code


# ##### 1. Why did you pick the specific chart?

# Answer Here.

# ##### 2. What is/are the insight(s) found from the chart?

# Answer Here

# #### Chart - 15 - Pair Plot 

# In[50]:


# Pair Plot visualization code


# ##### 1. Why did you pick the specific chart?

# Answer Here.

# ##### 2. What is/are the insight(s) found from the chart?

# Answer Here

# ## **5. Solution to Business Objective**

# #### What do you suggest the client to achieve Business Objective ? 
# Explain Briefly.

#     - We can see that no of repeated customers are very low in both the hotels so they should really focus on retaining       their some of the old customers 
#     -Try giving more discount on deposits made at the time of reservation in this way less cancellations will be made.
#     -Try offering some rewards to the agents giving more reservations this will encourage them to continue giving the hotel reservations 
#     -Hotels should also reduce the cost of the bookings in their non peak season so as to attaract more customers

# # **Conclusion**

#     -Out of all the customers , If we talk about percentages 27.5% of bookings got canceled whereas 72.5% of customers did check-in. So, we realise that there is a high rate of cancellations which can be due to various reasons one of which can be due to no deposit policies.
# 
#     -We can see that 2016 seems to be the year where hotel booking is at its highest among all the data available.And we can also say that there is an increasing trend in the number of customers.
#     
#     -We can also see an increasing trend in booking around the middle of the year, with making a peak in August followed by July and May.We can also see that January has lowest number of customers followed by Novemeber and Decemeber .It seems Winter period is at lowest peak for hotel booking.
#     
#     -Majority of the customers are from Portugal followed by Great Britain. So the bookings are mostly with European countries.So we should target this area for more customers.
#     
#     -Majority of the bookings are transient. This means that the booking is not part of a group or contract. With the ease  of booking directly from the website, most people tend to skip the middleman to ensure quick response from their booking.
#     
#     -Online TA (Travel Agency) segment gives high amount of customers and then Offline TA/TO, Groups, Direct etc. respectively. So, from this we can conclude that we can target our marketing area to be focus on these travel agencies website and work with them since majority of the visitors tend to reach out to them.
#     
#     -Maximum of the bookings are made with bed and breakfast .So, BB type of meal category is the most preferable in all type of customers.So we can also try to focus our offers and discounts around this BB category so as to retain these customers and ,to gain more customers of other category try giving new and better offers.
#     
#     -We can see that no of repeated customers are very low in both the hotels so they should really focus on retaining       their some of the old customers 
#     
#     -Adr for resort hotel makes peak in august month same as for city hotel.
#      Using the graph we can clearly observe that adr of peak months of resort hotel is much higher than city hotel , it can also be observed that the ADR of normal months of resort hotels is much less as compared to city hotels. This means that customers prefer city hotels in normal months and for holiday months which is around August as according to the dataset customer's prefer Resort hotels.
# 

# ### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
