# Problem Statement

The main problems of the hotels are high cancellation rates which is basically due to the offers and discounts provided by their competitors and the quality of service provided by the hotel, In this business the profit of the hotel depends mainly on how many days on an average customers are staying in their hotels, low cancellation rates, and traffic of customers. So We have to reduce the cancellation rate and increase bookings for hotels as a result

# Project Summary -

This data set contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, weather the booking was successful or canceled, was there any deposit made at the time of reservation or not, which type of customer made the booking , was the booking made by agent or not , time is also recorded by the hotels like which month did they check in , what was the week number of the check in among other things. All personally identifying information has been removed from the data 

The hotel industry is one of the most prominent industries in the world, and with the increase in competition, it has become increasingly important to analyze data to better understand customers and optimize revenue and improve customer satisfaction. The Hotel Booking Dataset EDA project aimed to provide insights into the trends and patterns within the hotel booking industry using a hotel booking dataset.

The dataset contained information on hotel bookings from two different hotels (City & Resort Hotels), including booking information, customer demographics, and hotel details etc for three years (2015, 2016 & 2017).

After loading the dataset, I started with data preparation and cleaning before I moved to EDA to analyze it. The dataset has around 119,390 records (rows) with 32 features (columns). Out of which, there were 31994 duplicate data, so deleted those rows. Remaining number of rows was 87396.Now 4 columns (company, agent, country & children) out of 32 had missing values. I imputed them in following manner:

Company: There may be some cases when customer didn't booked hotel via any company. Hence I will replace null values with 0.

Agent: Similarly there can be bookings made without any agent, hence replaced them with 0.

Children: Children column is numeric and skewed, hence choose median for imputing missing values.

Country: country column is categorical column. We use mode of ‘country’ column, But it can lead to bias towards a specific country that occurs most frequently in the data. Hence I created a new category ‘others’ for missing values.

There were 166 rows with 0 adults, children and babies which seems unlikely hence dropped those rows. Then created new column for total_guest = (adults + children). Ignored babies because generally they are not charged. Some values in ‘adr’ were negative, which must be an error so imputed them with median since it was a skewed data. Created new column for total_stays_night = (weekend_nights + week_nights) to analyze average length of stay.Assigned appropriate data types for some columns.

After cleaning the dataset, various exploratory data analysis techniques were used to better understand the dataset. Three broad categories for EDA are: Univariate, Bivariate, Multivariate

I used different types of charts and metrics to visualize the relationships, trends, understand preferences etc. to better understand the data. 
Overall, the Hotel Booking Dataset EDA project provided valuable insights into the hotel booking industry, including customer preferences, booking patterns, and trends over time. These insights can help hotels optimize revenue and improve customer satisfaction by tailoring their services to meet customer needs and expectations.

# Technologies Used

• Programming Language: Python

• Libraries: Pandas, NumPy, Matplotlib, Seaborn
 
