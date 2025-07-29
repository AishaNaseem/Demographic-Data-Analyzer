import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv",header=None)
    df.columns=df.iloc[0]
    df=df.drop(df.index[0]).reset_index(drop=True)
    df['age']=pd.to_numeric(df['age'])
    df['hours-per-week']=pd.to_numeric(df['hours-per-week'])



    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    
    average_age_men =round(df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people=len(df)
    bachelors_count=len(df[df['education']=='Bachelors'])
    percentage_bachelors = round(((bachelors_count/total_people)*100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_edu=['Bachelors','Masters','Doctorate']
    advanced_df=df[df['education'].isin(advanced_edu)]
    non_advanced_df=df[~df['education'].isin(advanced_edu)]
    
    
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education=len(advanced_df[advanced_df['salary']=='>50K'])
    lower_education = len(non_advanced_df[non_advanced_df['salary']=='>50K'])
    higher_edu_total=len(advanced_df)
    lower_edu_total=len(non_advanced_df)
    # percentage with salary >50K
    higher_education_rich= round(((higher_education/higher_edu_total)*100) ,1)
    lower_education_rich = round(((lower_education/lower_edu_total)*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =df[df['hours-per-week']==min_work_hours]
    min_hour_rich=len(num_min_workers[num_min_workers['salary']=='>50K'])

    rich_percentage = round(((min_hour_rich/len(num_min_workers))*100),1)

    # What country has the highest percentage of people that earn >50K?
    country_counts=df['native-country'].value_counts()
    country_rich=df[df['salary']=='>50K']['native-country'].value_counts()
    rich_country_percent=((country_rich/country_counts)*100).dropna()
    highest_earning_country = rich_country_percent.idxmax()
    highest_earning_country_percentage = round(rich_country_percent.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
   
    india_rich= df[(df['native-country']=='India')&(df['salary']=='>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
