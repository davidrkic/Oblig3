import pandas as pd
import numpy as np
import altair as alt

# Last inn Excel-fil og sett opp data
data = pd.read_excel(
    "ssb-barnehager-2015-2023-alder-1-2-aar.xlsm", 
    sheet_name="KOSandel120000", 
    header=3,
    names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
    na_values=['.', '..']
)

# Fjerner verdier over 100 for å unngå feil
for year in ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']:
    data.loc[data[year] > 100, year] = np.nan

# Rydder opp i 'kom'-kolonnen
data.loc[724:779, 'kom'] = np.nan
data['kom'] = data['kom'].apply(lambda x: x.split(" ")[1] if isinstance(x, str) and " " in x else "")

# Fjern metadata-rader
data_cleaned = data.drop(index=range(724, len(data)))

# Funksjon for å hente de n høyeste eller laveste verdiene i en kolonne
def get_top_n(df, column, n=1, ascending=False):
    return df.nlargest(n, column) if not ascending else df.nsmallest(n, column)

# A. Høyeste prosent i 2023 (oppg a)
highest_2023 = get_top_n(data_cleaned, 'y23')
print("A. Kommune med høyest prosent i 2023:")
for _, row in highest_2023.iterrows():
    print(f"{row['kom']}: {row['y23']:.1f}%")

# B. Laveste prosent i 2023 (oppg b)
lowest_2023 = get_top_n(data_cleaned, 'y23', ascending=True)
print("\nB. Kommune med lavest prosent i 2023:")
for _, row in lowest_2023.iterrows():
    print(f"{row['kom']}: {row['y23']:.1f}%")

# C og D. Definer årskolonner og finn høyeste og laveste gjennomsnitt for 2015-2023
year_columns = ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']
data_cleaned['avg_2015_2023'] = data_cleaned[year_columns].mean(axis=1).round(1)

# C og E. Høyeste gjennomsnittlig prosent for 2015-2023
highest_avg = get_top_n(data_cleaned, 'avg_2015_2023')
print("\nC. Kommune(r) med høyest gjennomsnittlig prosent (2015-2023):")
for _, row in highest_avg.iterrows():
    print(f"{row['kom']}: {row['avg_2015_2023']:.1f}%")

# D. Laveste gjennomsnittlig prosent for 2015-2023
lowest_avg = get_top_n(data_cleaned, 'avg_2015_2023', ascending=True)
print("\nD. Kommune(r) med lavest gjennomsnittlig prosent (2015-2023):")
for _, row in lowest_avg.iterrows():
    print(f"{row['kom']}: {row['avg_2015_2023']:.1f}%")

# F. Gjennomsnittlig prosent i 2023 for alle kommuner
avg_2023_all = data_cleaned['y23'].mean()
print(f"\nF. Gjennomsnittlig prosent for alle kommuner i 2023: {avg_2023_all:.1f}%")

# G. Funksjon for å lage en Altair-graf for en gitt kommune
def generate_chart(df, kommune_name):
    kommune_data = df[df['kom'] == kommune_name]
    kommune_long = kommune_data.melt(id_vars=['kom'], value_vars=year_columns,
                                     var_name='year', value_name='percentage')
    kommune_long['year'] = kommune_long['year'].str.replace('y', '20').astype(int)
    
    chart = alt.Chart(kommune_long).mark_line(point=True).encode(
        x=alt.X('year:O', title='År'),
        y=alt.Y('percentage:Q', title='Prosent', scale=alt.Scale(zero=False)),
        tooltip=['year', 'percentage']
    ).properties(
        title=f'Prosent av barn 1-2 år i barnehage i {kommune_name} (2015-2023)',
        width=600,
        height=400
    )
    
    return chart

# Lagre graf for valgt kommune
selected_kommune = "Oslo"
generate_chart(data_cleaned, selected_kommune).save(f"{selected_kommune}_barnehage_prosent_2015_2023.html")
print(f"G. Graf for {selected_kommune} er lagret som en HTML-fil.")

# H. Generer graf for topp 10 kommuner basert på gjennomsnittlig prosent i 2015-2023
# Filtrer for kommuner med data for alle årene og beregn gjennomsnitt
full_data = data_cleaned.dropna(subset=year_columns).copy()
full_data['avg_2015_2023'] = full_data[year_columns].mean(axis=1)

# Hente topp 10 kommunene basert på gjennomsnittlig prosent
top_10 = full_data.nlargest(10, 'avg_2015_2023')

# Lag graf for topp 10 kommuner
top_chart = alt.Chart(top_10).mark_bar().encode(
    x=alt.X('kom:N', sort='-y', title='Kommune'),
    y=alt.Y('avg_2015_2023:Q', title='Gjennomsnittlig prosent (2015-2023)'),
    tooltip=['kom', 'avg_2015_2023']
).properties(
    title='Topp 10 kommuner med høyest gjennomsnittlig prosent barn i barnehage (1-2 år) 2015-2023',
    width=600,
    height=400
)

# Lagre topp 10 graf
top_chart.save('topp_10_kommuner_barnehage_2015_2023.html')
print("H. Graf for topp 10 kommuner er lagret som en HTML-fil.")
