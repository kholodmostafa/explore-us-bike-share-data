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
    city = input("write the name of the city,chicago, new york city, washington :")
    while city not in (CITY_DATA.keys()):
        print("sorry its not a valid city , please enter the city name correctly")
        city = input("write the name of the city,chicago, new york city, washington :").lower()
    


    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june']
    month = input("write the month you want to filter  january, february, march, april, may, june :").lower()
    while month not in months:
        print("not a valid month , please enter the month from January to june")
        month = input(" write the month you want to filter , january, february, ... , june :").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    day = input("enter the name of the day you want to filter with: ").lower()
    while day not in days:
        print("invalid day ! please enter a valid day")
        day = input("enter the name of the day you want to filter with ").lower()
        


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['sunday','monday','tuesday','wednesday','thursday','friday']
    if month in months:
        month = months.index(month)+1
        df = df[df['month'] == month]
    
    if day in days:
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print(f'the common month is {months[common_month-1]}')


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f'the common day is {common_day}')
    


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'the most popular hour is {common_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'the popular sart station is : {common_start_station}')


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'the popular end station is : {common_end_station}')


    # TO DO: display most frequent combination of start station and end station trip
    from_to_state = df['Start Station'] + "to " + df['End Station']
    print(f'the most popular trip is {from_to_state.mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_trip_time.days
    hours = total_trip_time.seconds // (60*60)
    minutes = total_trip_time.seconds % (60*60)//60
    seconds = total_trip_time.seconds %(60*60) %60                   
                       
    print(f'the whole duration trip is {days} days : {hours} hours : {minutes} minutes and {seconds} seconds')
                       
        


    # TO DO: display mean travel time
    average_trip_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = average_trip_time.days
   
    hours = average_trip_time.seconds // (60*60)
    
    minutes = average_trip_time.seconds % (60*60)//60
    seconds = average_trip_time.seconds %(60*60) %60
    
    print(f'the average duration trip is {days} days: {hours} hours : {minutes} minutes and {seconds} seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print('\n')

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):  
        gender = df['Gender'].value_counts()
        
        print(gender)
        print('\n')  
        print('-'*40)
    else:
              print('gender data is not found')
              
    print('\n')  

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        df['Birth Year'] = df['Birth Year'].fillna(df['Birth Year'].mean()).astype('int64')
        earlist = df['Birth Year'].min()
        mostrecent = df['Birth Year'].max()
        mostcommon = df['Birth Year'].mode()[0]
        print(f'the earliest year is: {earlist} , and most recent year is :{mostrecent} , the most common year is :{mostcommon}') 
   
    else:   
        print("birth day data not found!")
     
         
    
           


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        # Check if response is yes, print the raw data and increment count by 5
        if answer.lower() =='yes':
            count = 0
            while True:
                print(df.iloc[count :count +5])
                count = count +5
                ask_again =input('do you want to show the next 5 rows ?')
                if ask_again.lower() !='yes':
                    break;
            

        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
