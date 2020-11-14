
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('https://storage.googleapis.com/introduction-to-data-science/spotify-dataset.csv', index_col=0);
dataset = dataset.drop(['danceability', 'energy', 'liveness', 'release_date'], axis = 1)

#Question 1 - Display the first ten rows 
first_ten_rows = dataset.head(10);
print(first_ten_rows);

#Question 2 - Missing values ?
missing_values = dataset.isna().sum().sum();
print("There are {} missing values in this dataset.".format(missing_values));

#Question 3 - How many songs ?
number_of_songs = dataset.shape[0];
print("There are {} songs in this dataset".format(number_of_songs));

#Question 4 - How many (unique) artists ?
artists = dataset.artists.nunique();
print("There are {} different artists.".format(artists));

#Question 5 - What's the average duration of a song (minutes) ?
average_song_duration_milliseconds = dataset.duration_ms.mean();
average_sons_duration_minutes = average_song_duration_milliseconds / 60000;
print(average_sons_duration_minutes);

#Question 6 & 7 - Can you plot the distribution of the durations ?
plt.hist(dataset.duration_ms, range = (10000,300000), color='lightblue', histtype='step');
plt.xlabel("Duration in ms");
plt.ylabel("Number of songs");
plt.title("Distribution of durations");
plt.savefig('Distribution of durations.png')
plt.show();

#Question 8 - Whar are the top 10 longest songs (duration) ?
longest_songs = dataset.sort_values('duration_ms')[['name', 'duration_ms']].tail(10);
print(longest_songs);

#Question 9 - How long would it take to listen to all the songs ?
listening_time_ms = dataset['duration_ms'].sum();

listening_time_in_days = round( listening_time_ms / (60000*60*24) );
print("It would take {} days to listen to all the songs...".format(listening_time_in_days));

#Question 10 - What are the top 10 most popular songs? Only the columns artists, name and popularity as output!
top_ten_most_popular_songs = dataset.sort_values('popularity')[['name', 'artists', 'popularity']].tail(10);
print(top_ten_most_popular_songs);

#Question 11 - What is the most popular song before 2000?
most_popular_song_before_2000 = dataset[dataset['year']< 2000][['name', 'year', 'popularity']].sort_values('popularity').tail(1);
print(most_popular_song_before_2000);

#Question 12 - What are the top 10 artists in terms of number of songs made?
top_10_artists = dataset.artists.value_counts().head(10);
print(top_10_artists);

#Question 13 - Barchart out of this result
df = pd.DataFrame({'artists':['Эрнест Хемингуэй', 'Francisco Canaro', 'Эрих Мария Ремарк', 'Ignacio Corsini', 'Frank Sinatra', 
                              'Bob Dylan', 'The Rolling Stones', 'Johnny Cash', 'The Beach Boys', 'Elvis Presley'], 
                   'number_of_songs':[1215, 938, 781, 620, 592, 539, 512, 502, 491, 488]});
df.plot.bar(x='artists', y='number_of_songs', color = 'lightpink');
plt.savefig('Number of songs per artist.png');
plt.show();

#Question 14 - How many songs by key?
sorted_number_of_songs_by_key = dataset['key'].value_counts().sort_index();
print(sorted_number_of_songs_by_key);

#Question 15 - Can you plot a bar chart using Seaborn? Make sure the keys are sorted in a descending order.
df = pd.DataFrame({'keys':[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
                   'number_of_songs':[21499, 12816, 18821, 7185, 12921, 16336, 8586, 20757, 10711, 17628, 12056, 10593]});

sns.barplot(x="keys", y="number_of_songs", data = df, order=[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]);
plt.savefig('Number of songs per key.png');
plt.show();


#Question 16 - Can you plot a line graph representing the annual number of songs since 1921?
number_of_songs_per_year = dataset['year'].value_counts().sort_index();
print(number_of_songs_per_year);

number_of_songs_per_year.plot.line(color="purple");
 
#Question 17 - Can you visually check if there is relationship between year and popularity?
print( dataset['year'].corr(dataset['popularity']) );
#value = 0.88, there is a high correlation between year and popularity

corr = dataset.corr();
sns.heatmap(corr, 
            xticklabels = corr.columns.values,
            yticklabels = corr.columns.values);
plt.savefig('Correlation_matrix.png');
plt.show();


