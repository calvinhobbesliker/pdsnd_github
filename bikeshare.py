import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Choose a city: Chicago, New York City, or Washington.')
    city = input()
    city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Choose a month between January and June to filter by, or type "All" to analyze data from all months.')
    month = input()
    month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Choose a day of the week to filter by, or type "All" to analyze data from all days of the week.')
    day = input()
    day = day.lower()

    print('-'*40)
    return city, month, day

#get_filters()


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).dayofweek

    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['zero', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
    
        # filter by month to create the new dataframe
        df = df.loc[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week']==day]

    return df

#print(load_data('chicago', 'january', 'monday'))


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    months = ['zero', 'January', 'February', 'March', 'April', 'May', 'June']
    popular_month = months[int(df.mode()['month'][0])]
    print('The most popular month is ', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    popular_day_of_week = days_of_the_week[int(df.mode()['day_of_week'][0])]
    print('The most popular day of the week is ', popular_day_of_week)
    
    # TO DO: display the most common start hour
    df['starting_hour'] = pd.DatetimeIndex(df['Start Time']).hour
    popular_hour = str(int(df.mode()['starting_hour'][0]))+':00'
    print('The most popular starting hour is ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#print(time_stats(pd.read_csv(CITY_DATA['chicago'])))
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df.mode()['Start Station'][0]
    print('The most popular start station is ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df.mode()['End Station'][0]
    print('The most popular end station is ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip_stations'] = df['Start Station']+' to '+df['End Station']
    popular_combination = df.mode()['trip_stations'][0]
    print('The most popular trip is ', popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#print(station_stats(pd.read_csv(CITY_DATA['chicago'])))
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is ', total_time, ' seconds.')


    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print('The average travel time is ', average_time, ' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#print(trip_duration_stats(pd.read_csv(CITY_DATA['chicago'])))

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is ', int(earliest_birth_year))

        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is ', int(most_recent_birth_year))

        most_common_birth_year = df.mode()['Birth Year'][0]
        print('The most common birth year is ', int(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#print(user_stats(pd.read_csv(CITY_DATA['chicago'])))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        individual_data = 'yes'
        start, end = -5, 0
        
        while individual_data == 'yes':
            print('Do you want to see some individual rows of data? Enter yes or no.')
            individual_data = input().lower()
            if individual_data == 'yes':
                start +=5
                end += 5
                print(df[start:end])
            
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
