df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv', skiprows = 4)
df = df.rename(columns = {'Country Name': 'Country', 'Country Code': 'Country_Code'})
df = df.dropna(axis = 1, how = 'all')

years = [str(year) for year in range(1960, 2024)]
df_population = df[['Country'] + years]

most_recent_year = str(df_population.columns[-1])
df_recent = df_population[['Country', most_recent_year]]
df_recent = df_recent.dropna()
df_recent_sorted = df_recent.sort_values(by = most_recent_year, ascending = False)

top_n = 20
df_top_n = df_recent_sorted.head(top_n)

plt.figure(figsize = (12, 8))
plt.bar(df_top_n['Country'], df_top_n[most_recent_year], color = 'skyblue')

plt.title(f'Top {top_n} Countries by Population ({most_recent_year})', fontsize = 16)
plt.xlabel('Country', fontsize = 12)
plt.ylabel('Population (Total)', fontsize = 12)
plt.xticks(rotation=45, ha='right', fontsize = 10)
plt.yticks(fontsize = 10)
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
