import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""
the three functions below ask user to specify a city, month, and day to analyze.

Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""
def get_city():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while True:
        city = input("Would you like to look at data for New York City, Chicago or Washington?").lower()
         
        if city == 'new york city' or city ==  'chicago' or city == 'washington':
            break
        else:
            print('that is not a valid input please select one of the 3 possible cities: New York City, Chicago or Washington')
    # get user input for month (all, january, february, ... , june)

    return city
def get_month():
    month = ''
    while True:
        month = input("Would you like to look at data for january, february, march, april, may , june or all months? please type in a name of the month or all for all months ").lower()
     
        if month == 'january' or month ==  'february' or month ==  'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            break
        else:
            print('that is not a valid input please select one of the 6 possible or type in all')
    return month
def get_day():
    day = ''
    while True:
        day = input("Would you like to look at data for a specific day of the week or all days? please type in a name of a day or all for all days ").lower()
         
        if day == 'monday' or day ==  'tuesday' or day ==  'wensday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            break
        else:
            print('that is not a valid input please choose a day of the week or type in all for all days')
    return day

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month_index'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month_index'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wensday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['day_of_week'] == days.index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if month == 'all':
        month_dictionary = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        top_month_int = df['month_index'].mode()[0]
        top_month = month_dictionary[top_month_int]
    
        print(f"Top Month: {top_month}")
    else:
        print('As you chose {} as a filter it is the most popular month in this dataset by default'.format(month))
    # display the most common day of week
    if day == 'all':
        top_day_int = df['day_of_week'].mode()[0]
        day_dictionary = {0: 'Monday', 1: 'Tuesday', 2: 'Wensday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday' }
        top_day = day_dictionary[top_day_int]
        print(f"\nTop Day: {top_day}")
    else:
        print('As you chose {} as a filter it is the most popular day in this dataset by default'.format(day))
    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour

    #Uses mode method to find the most popular hour
    top_hour = df['hour'].mode()[0]
    
    print(f"\nMost popular hour: {top_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('\nThe most used start station in the selected data set was {}'.format(top_start_station))

    # display most commonly used end station
    top_end_station = df['End Station'].mode()[0 ]
    print('\nWhile the most used end station was {}'.format(top_end_station))

    # display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
    top_route = df['Route'].mode()[0]
    print('\n The most common route taken by users was {}'.format(top_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_hours = df['Trip Duration'].sum()/3600
    total_travel_time_days = total_travel_time_hours/24
    print('\nTotal travel time for this data set amounted to: {} hours which is equal to {} days'.format(total_travel_time_hours, total_travel_time_days))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_minutes = int(mean_travel_time/60)
    mean_travel_time_seconds = int(mean_travel_time%60)
    print('\nThe average trip took {} minutes and {} seconds'.format(mean_travel_time_minutes, mean_travel_time_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_shared(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type= df['User Type'].value_counts()
    print("The amount of subscribers and customers is given below\n\n{}".format(user_type))

    # Display counts of gender
    if city == 'washington':
        print('Gender data for users is not availeble for {}, which you have chosen'.format(city))
        print('Year of birth data for users is not availeble for {}, which you have chosen'.format(city))
    else:
        gender= df['Gender'].value_counts()
        print("The count for genders is given below \n\n{}".format(gender))
        # Display earliest, most recent, and most common year of birth
        most_common_year = int(df['Birth Year'].mode())
        most_recent_year = int(df['Birth Year'].max())
        earliest_year = int(df['Birth Year'].min())
        print('The most common birth year for users was {}.The oldest user was born in {} while the youngest in {}'. format(most_common_year, earliest_year, most_recent_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_unique(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    gender= df['Gender'].value_counts()
    print("The count for genders is given below \n\n{}".format(gender))
    # Display earliest, most recent, and most common year of birth
    most_common_year = int(df['Birth Year'].mode())
    most_recent_year = int(df['Birth Year'].max())
    earliest_year = int(df['Birth Year'].min())
    print('The most common birth year for users was {}.The oldest user was born in {} while the youngest in {}'. format(most_common_year, earliest_year, most_recent_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    view_data = ''
    while view_data != 'no':
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while view_data == 'yes':
            print(df[start_loc : start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            if view_data == 'no':
                break

def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
        elif restart.lower() == 'yes':
            city = get_city()
            month = get_month()
            day = get_day()
            df = load_data(city, month, day)
    
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            if city == 'washington':
                print('Gender data for users is not availeble for {}, which you have chosen'.format(city))
                print('Year of birth data for users is not availeble for {}, which you have chosen'.format(city))
                raw_data(df)
            else:
                user_stats_unique(df)
                raw_data(df)
                main()
        else:
            print('Incorect input please type in yer or no')
            main()
city = get_city()
month = get_month()
day = get_day()
df = load_data(city, month, day)
time_stats(df)
station_stats(df)
trip_duration_stats(df)
user_stats_shared(df)
if city == 'washington':
    print('Gender data for users is not availeble for {}, which you have chosen'.format(city))
    print('Year of birth data for users is not availeble for {}, which you have chosen'.format(city))
else:
    user_stats_unique(df)
raw_data(df)
main()