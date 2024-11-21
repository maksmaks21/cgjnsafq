import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('spotify-2023.csv')
df.info()

print(df.describe())

#df["released_year"].plot(kind='hist')
#df["artist_count"].plot(kind='hist')
#df["released_month"].plot(kind='hist',bins=12)
#df['in_spotify_playlists'].plot(kind='box')
#df['mode'].value_counts().plot(kind='pie')

plt.show()