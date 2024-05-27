import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('ted_data.csv')
print(df.head())

# Most popular TED talks
most_popular_talks = df.sort_values(by='views', ascending=False).head(10)
print("Most popular TED talks:\n", most_popular_talks[['title', 'author', 'views']])

# Most popular TED talks Speaker (by number of talks)
popular_speakers = df['author'].value_counts().head(10)
print("Most popular TED talks Speaker (by number of talks):\n", popular_speakers)

# Month-wise Analysis of TED talk frequency
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
monthly_frequency = df['month'].value_counts().sort_index()
print("Month-wise TED talk frequency:\n", monthly_frequency)
monthly_frequency.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Number of Talks')
plt.title('Month-wise TED Talk Frequency')
plt.show()

# Year-wise Analysis of TED talk frequency
df['year'] = df['date'].dt.year
yearly_frequency = df['year'].value_counts().sort_index()
print("Year-wise TED talk frequency:\n", yearly_frequency)
yearly_frequency.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Number of Talks')
plt.title('Year-wise TED Talk Frequency')
plt.show()

# TED talks of favorite author
favorite_author = 'Your Favorite Author'
favorite_author_talks = df[df['author'] == favorite_author]
print(f"TED talks of {favorite_author}:\n", favorite_author_talks[['title', 'date', 'views', 'likes']])

# TED talks with best view to like ratio
df['view_like_ratio'] = df['views'] / df['likes']
best_view_like_ratio_talks = df.sort_values(by='view_like_ratio', ascending=False).head(10)
print("TED talks with best view to like ratio:\n", best_view_like_ratio_talks[['title', 'author', 'view_like_ratio']])

# TED talks based on tags
tag = 'climate'
tag_based_talks = df[df['title'].str.contains(tag, case=False, na=False)]
print(f"TED talks based on tag '{tag}':\n", tag_based_talks[['title', 'author', 'views', 'likes']])

# Most popular TED talks Speaker (by views)
speaker_views = df.groupby('author')['views'].sum().sort_values(ascending=False).head(10)
print("Most popular TED talks Speaker (by views):\n", speaker_views)
