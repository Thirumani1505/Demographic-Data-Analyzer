import pandas as pd

def demographic_data_analyzer():
    # Read dataset
    df = pd.read_csv("adult.data.csv")
    
    # Number of people of each race
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # Advanced education
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round((df[advanced_edu]['salary'] == '>50K').mean() * 100, 1)
    
    # People without advanced education
    lower_edu_rich = round((df[~advanced_edu]['salary'] == '>50K').mean() * 100, 1)
    
    # Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()
    
    # Percentage of people who work minimum hours and earn >50K
    min_workers = df['hours-per-week'] == min_work_hours
    rich_min_workers = round((df[min_workers]['salary'] == '>50K').mean() * 100, 1)
    
    # Country with highest percentage of high earners
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    country_percentage = (country_salary / country_count * 100).dropna()
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)
    
    # Most popular occupation for high earners in India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_edu_rich': higher_edu_rich,
        'lower_edu_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Run function for testing
demographic_data_analyzer()
