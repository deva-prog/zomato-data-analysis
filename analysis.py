import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
s = pd.read_csv("yt zomato file.csv")

#data cleaning
#print(s.head())
#print(s.dtypes)
#print(s.info())
#print(s.tail())
#print(s.describe())
#print(s.shape)
#print(s.isnull().sum())

s['rate'] = s['rate'].astype(str)

# unwanted values remove
s['rate'] = s['rate'].replace(['NEW', '-'], None)

# /5 remove
s['rate'] = s['rate'].str.replace('/5', '')

# convert to float
s['rate'] = pd.to_numeric(s['rate'], errors='coerce')
#print(s.dtypes)
#print(s['rate'].isnull().sum())

#✅ Q1: Which type of restaurant do the majority of customers order from?
#print("Q1: Majority restaurant type")
#print(s['listed_in(type)'].value_counts())
#print(s['listed_in(type)'].value_counts(normalize=True) * 100)

#Graphical representation of "Restaurant type distribution"

sns.countplot(x='listed_in(type)', data=s)
plt.xticks(rotation=45)
plt.title("Restaurant Type Distribution")
#plt.show()
#Majority of customers prefer Dining type restaurants, as it has the highest number of orders (110), compared to Cafe, Buffet, and other types.

# ✅ Q2: How many votes has each type of restaurant received?
#print(s.groupby('listed_in(type)')['votes'].sum())

#Graphical representation of "votes by restaurant type"
votes_data = s.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)
#print(votes_data)
sns.barplot(x=votes_data.index, y=votes_data.values)
plt.title("Votes by Restaurant Type")
plt.xlabel("Restaurant Type")
plt.ylabel("Total Votes")
plt.xticks(rotation=45)
#plt.show()
#Dining restaurants have received the highest number of votes from customers, indicating higher customer engagement compared to other types like Cafe and Buffet.

#✅Q3: What are the ratings that majority of restaurants have received?
#Frequency count:
#print(s['rate'].value_counts())
#print(s['rate'].value_counts().head())   #majority rating of restaurant

#GRAPH VISUALIZATION

sns.histplot(s['rate'], bins=10)
plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")
#plt.show()

#✅Q4:Zomato has observed that most couples order food online — what is their average spending?

#print(s['approx_cost(for two people)'].mean())
#Couples order online
online_s = s[s['online_order'] == 'Yes']
#print(online_s['approx_cost(for two people)'].mean())

#GRAPH VISUALIZATION

plt.figure(figsize=(8,5))
sns.kdeplot(s['approx_cost(for two people)'], fill=True)
plt.title("Cost Distribution (Boxplot)", fontsize=14)
plt.xlabel("Cost(₹)")
#plt.show()
#The average cost for two people is approximately ₹400–₹500, indicating that most restaurants fall in a moderate price range.

#✅ Q5:Which mode (online / offline) has received maximum rating?
s['online_order'] = s['online_order'].replace({
    'Yes': 'Online',
    'No': 'Offline'
})
#print(s.groupby('online_order')['rate'].mean())
#print(s['online_order'].value_counts())
#GRAPH VISUALIZATION
plt.figure(figsize=(6,4))
sns.barplot(x='online_order', y='rate', data=s)
plt.title("Average Rating: Online vs Offline")
plt.xlabel("Order Mode")
plt.ylabel("Average Rating")
#plt.show()
#Restaurants offering online ordering have higher average ratings (3.85) compared to offline restaurants (3.48), indicating better customer satisfaction in online services.

#✅Q6:Which type of restaurant received more offline orders, so that Zomato can give offers?
offline_s = s[s['online_order'] == 'Offline']
print(offline_s)

print(offline_s['listed_in(type)'].value_counts())

#GRAPH VISUALIZATION
plt.figure(figsize=(8,5))

sns.countplot(x='listed_in(type)', data=offline_s)

plt.title("Offline Orders by Restaurant Type")
plt.xlabel("Restaurant Type")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.show()


