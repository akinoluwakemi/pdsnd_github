#Welcome to Bikeshare
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york', 'washington']
    print(cities)
    city = input('Which city do you want to explore? \"Chicago, Washington or New York\"?\n')
       
    while city not in cities:
        print("Please, choose from the quoted options above.")
        city = input('Which city do you want to explore? \"Chicago, Washington or New York\"?\n')

    # get user input for month (all, january, february, ... , june)
    print(months)
    month = input('Enter a month to get month result.\n')
    while month not in months:
        print(months)
        print("Please, choose from the quoted options above.")
        month = input('Enter a month to get month result.\n')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(days)
    day = input('What day of the week do you want to see?\n')
    while day not in days:
        print(days)
        print("Please, choose from the quoted options above.")
        day = input('What day of the week do you want to see?\n')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if city == 'chicago':
            df = pd.read_csv("chicago.csv")
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month
            df['day'] = df['Start Time'].dt.day_name()
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month) + 1
                df = df[df['month'] == month]
            if day != 'all':
                df = df[df['day'] == day.title()]
 
    if city == 'new york':
            df = pd.read_csv('new_york_city.csv')
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month
            df['day'] = df['Start Time'].dt.day_name()
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month) + 1
                df1 = df[df['month'] == month]
            if day != 'all':
                 df = df[df['day'] == day.title()]

    if city == 'washington':
            df = pd.read_csv('washington.csv')
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month
            df['day'] = df['Start Time'].dt.day_name()
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month) + 1
                df = df[df['month'] == month]
            if day != 'all':
                df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('The most common month is ' + str(months[most_common_month-1].title()) + '.')
    
    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    most_common_day = df['day'].mode()[0]
    print('The most common day of the week is ' + str(days[most_common_day-1].title()) + '.')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mode_start_hour = df['hour'].mode()[0]
    print('The most common start hour is ' + str(mode_start_hour) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = str(df['Start Station'].mode()[0])
    print('The most commonly used start station is '+ str(most_used_start_station) + '.') 

    # display most commonly used end station
    most_used_end_station = str(df['End Station'].mode()[0])
    print('The most commonly used end station is '+ str(most_used_end_station) + '.') 

    # display most frequent combination of start station and end station trip
    df['Station Combination'] = (df['Start Station'] + ',' + df['End Station'])
    most_frequent_station_combination = df['Station Combination'].mode()[0]
    print("The most frequent combination of start and end station is " + str(most_frequent_station_combination.split(',')[0]) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ' + str(int(total_travel_time//60)) + 'minutes ' + str(int(total_travel_time % 60)) + 'seconds.')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is ' + str(int(mean_travel_time//60)) + 'minutes ' + str(int(mean_travel_time % 60)) + 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Counts of user types: " + str(len(user_types)) + '.')

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("male: " + str(gender_counts[0]), "female: " + str(gender_counts[1]))
    except:
        print('Sorry, there is no gender record for {}.'
             .format(city.title()))

    # Display earliest, most recent, and most common year of birth
    df['Birth Year'] = pd.to_datetime(df['Birth Year'])
    df['year'] = df['Birth Year'].dt.year
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth: ' + str(earliest_birth_year)) 
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth: ' + str(most_recent_birth_year)) 
        most_common_birth = df['Birth Year'].mode()
        print("The most common birth year: " + str(most_common_birth.mode()[0]) + ".")
                      
    except:
        print('Sorry, there is no birth year record available for {}.'
             .format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
