import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import os

def perform_analysis(filepath):
    # Load dataset
    data = pd.read_csv(filepath, decimal=',')
    
    # Generate outputs
    outputs = {}
    outputs['data'] = data.to_html()
    outputs['null_values'] = data.isnull().sum().to_dict()

    
    # Replace missing values and perform preprocessing
    region_medians = data.groupby('Region')[['GDP ($ per capita)', 'Literacy (%)', 'Agriculture']].median()
    for col in data.columns.values:
        if data[col].isnull().sum() == 0:
            continue
        if col == 'Climate':
            guess_values = data.groupby('Region')['Climate'].apply(lambda x: x.mode().max())
        else:
            guess_values = data.groupby('Region')[col].median()
        for region in data['Region'].unique():
            data.loc[data['Region'] == region, col] = data.loc[data['Region'] == region, col].fillna(guess_values[region])
    
    
    
    outputs['region_medians'] = region_medians.to_html()
    
    # Save visualizations
    viz_dir = 'static/visualizations'
    if not os.path.exists(viz_dir):
        os.makedirs(viz_dir)
    
    # Top countries by GDP per capita
    fig, ax = plt.subplots(figsize=(16, 13))
    top_gdp_countries = data.sort_values('GDP ($ per capita)', ascending=False).head(20)
    sns.barplot(x='Country', y='GDP ($ per capita)', data=top_gdp_countries, palette='Set3', ax=ax)
    plt.xticks(rotation=90)
    top_gdp_path = os.path.join(viz_dir, 'top_gdp_countries.png')
    plt.savefig(top_gdp_path)
    outputs['top_gdp_countries'] = top_gdp_path

    # Heatmap
    plt.figure(figsize=(16, 18))
    sns.heatmap(data=data.iloc[:, 2:].corr(), annot=True, fmt='.2f', cmap='coolwarm')
    heatmap_path = os.path.join(viz_dir, 'heatmap.png')
    plt.savefig(heatmap_path)
    outputs['heatmap'] = heatmap_path

    ### New: Total GDP Bar and Pie Chart Visualization ###
    data['Total_GDP ($)'] = data['GDP ($ per capita)'] * data['Population']
    
    # Get top 10 countries by Total GDP
    top_gdp_countries = data.sort_values('Total_GDP ($)', ascending=False).head(10)
    
    # Create 'Other' category for countries not in top 10
    other = pd.DataFrame({
        'Country': ['Other'],
        'Total_GDP ($)': [data['Total_GDP ($)'].sum() - top_gdp_countries['Total_GDP ($)'].sum()]
    })
    
    # Concatenate the top countries and 'Other' category
    gdps = pd.concat([top_gdp_countries[['Country', 'Total_GDP ($)']], other], ignore_index=True)
    
    # Create side-by-side plots (Bar Plot + Pie Chart)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10), gridspec_kw={'width_ratios': [2, 1]})
    
    # Bar plot of Total GDP by Country
    sns.barplot(x='Country', y='Total_GDP ($)', data=gdps, ax=axes[0], palette='Set3')
    axes[0].set_xlabel('Country', labelpad=30, fontsize=16)
    axes[0].set_ylabel('Total GDP ($)', labelpad=30, fontsize=16)
    
    # Pie chart of Total GDP distribution by Country
    colors = sns.color_palette("Set3", gdps.shape[0]).as_hex()
    axes[1].pie(gdps['Total_GDP ($)'], labels=gdps['Country'], colors=colors, autopct='%1.1f%%', shadow=True)
    axes[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    # Save the visualizations
    total_gdp_path = os.path.join(viz_dir, 'total_gdp_countries.png')
    plt.savefig(total_gdp_path)
    outputs['total_gdp_country'] = total_gdp_path

    return outputs