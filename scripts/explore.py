# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Set-Up

# %%
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt 

# read crop data
df = pd.read_csv('../data/crop_production.csv')

# read shape file
shp_gdf = gpd.read_file('../data/Indian_states.shp')


# %%
merged = shp_gdf.set_index('st_nm').join(df.set_index('State_Name'))
merged.head()


# %%
fig, ax = plt.subplots(1, figsize=(5, 12))
ax.axis('off')
ax.set_title('Crop Production in India (1997)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged[merged['Crop_Year'] == 1997.0].plot(column='Production', cmap='RdYlGn', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)


# %%



