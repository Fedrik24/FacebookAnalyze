import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#Buka JSON FILE
df = pd.read_json("your_posts_1.json")

#Ganti Semua nama TimeStamp yang ada di JSON dengan Date
df.rename(columns={'timestamp': 'date'}, inplace=True)

#Buang Parameter/Argument di JSON file yang gk penting
df = df.drop(['attachments', 'title', 'tags'], axis=1)

#Cari Parameter/Argument "Date" di JSON
pd.to_datetime(df['date'],unit='s')

#Jadikanlah "Date" menjadi Index untuk X axis nanti!
df = df.set_index('date')

#Gk tau ini gunanya apa nemu di StackOVerFlow :V
post_counts = df['data'].resample('MS').size()

#Buat Schema/Canvas lah make Figure serta besar dan lebarnya
sns.set(rc={'figure.figsize':(20,10)})

#Gede Font
sns.set(font_scale=3)

# Variable X sama dengan X yang ada di line 20
#ini akan digunakan untuk matplotlib nanti
label_x = post_counts.index

#Buat PLOTBAR agar ditampilkan nanti...
sns.barplot(label_x, post_counts, color="orange")

# Make Numpy untuk membuat Data.
tick_positions = np.arange(10, len(label_x), step=24)

#Format ulang untuk Y AXIS agar "Date"nya bisa muncul
plt.xticks(tick_positions, label_x[tick_positions].strftime("%Y"))

# Tampilkan Matplotlib
plt.tight_layout()
plt.show()
