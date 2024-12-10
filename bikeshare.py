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
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("To explore a city data, Please Enter the city name (Chicago, New York City, Washington): \n").strip().lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Your Input is Invalid.")
    print(f"You selected {city.title()}.")
    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Select time period to filter the data  (All, January, February, March, April, May, June):\n ").strip().lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Your Input is Invalid.")
    print(f"You entered {month.title()}.")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        week_days = {"m": "Monday", "tu": "Tuesday", "w": "Wednesday", "th": "Thursday", "f": "Friday", "sa": "Saturday", "su": "Sunday"}
        days = input("Select day of the week. Please type: All, M, Tu, W, Th, F, Sa, Su: \n ").strip().lower()
        if days in ['all', 'm', 'tu', 'w', 'th', 'f', 'sa', 'su']:
            if days == 'all':
                day = 'all'
                break  
            else:
                day = week_days[days]
                break
        else:
            print("Your Input is Invalid.")
    print(f"You selected {day.title()}.")
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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filter by month if applicable to create new dataframe by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
     # Filter by day of week if applicable to create the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Find the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # Find the most commonn day of the week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day)

    # Display the most common start hour
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Find the most commonly used Start Station
    popular_sstation = df['Start Station'].mode()[0]
    print('Most Commonly used Start Station:', popular_sstation)

    # Find the most commonly used End Station
    popular_estation = df['End Station'].mode()[0]
    print('Most Commonly used End Station:', popular_estation)

    # Find the most frequent combination of start station and end station trip
    popular_cstation = df[['Start Station', 'End Station']].mode().iloc[0]
    print(f'Frequent combination of start station and end station are {popular_cstation[0]} and {popular_cstation[1]} respectively')

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Find the Total Travel Time and the  count of Trips
    tot_travel = df['Trip Duration'].sum()
    travel_count = df['Trip Duration'].count()
    print(f'Total travel time is {tot_travel} sec\nTrip Count is {travel_count}')

    # Find the Mean Travel time of the Trips
    avg_travel = df['Trip Duration'].mean()
    print(f'Mean Travel time of the Trips is {avg_travel} sec')

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Find the counts for each user type
    user_types = df['User Type'].value_counts()
    print(f'Counts for each user type are:\n{user_types}')

    # Find the counts of Genders
    try:
        gender = df['Gender'].value_counts()
        print(f'\nCounts for each Gender are:\n{gender}')
        
    # KeyError handling
    except KeyError:
        print('\nNo Gender data to display')     

    # Find the youngest, Oldest and the Common Birth Year
    try:
        Birth_max = df['Birth Year'].max()
        Birth_min = df['Birth Year'].min()
        Birth_com = df['Birth Year'].mode()[0]
        print(f'\nThe Youngest Birth Year is:{round(Birth_max)}')
        print(f'The Oldest Birth Year is:{round(Birth_min)}')
        print(f'The Common Birth Year is:{round(Birth_com)}')
          
    # KeyError handling
    except KeyError:
        print('\nNo Birth Year data to display')

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)

def raw_dat(df):
    """Displays Raw data to user."""
 
    # Ask if the user wants to see the Raw data
    request = input("Do you want to see the first 5 rows of Raw Data? Enter yes or no: \n").strip().lower()
    while True:
        if request in ['yes', 'no']:
            break
        else:
            print("Your Input is Invalid.") 
            request = input("Enter yes or no:\n").strip().lower()
  
    if request != 'yes':
        print("Raw Data will not be displayed.")
    else:
        # Initialize the indexing key
        indx = 0
        while True:
            # Display the next 5 rows
            print(df.iloc[indx:indx + 5])
    
            # Increase the indexing key by 5
            indx += 5
    
            # Check for more data to display
            if indx >= len(df):
                print("Exiting: No more data to display.")
                break
    
            # Check with user if more data is to be displayed
            request = input("Do you want to see the next 5 rows of Raw Data? Enter yes or no: \n").strip().lower()
            while True:
                if request in ['yes', 'no']:
                    break
                else:
                    print("Your Input is Invalid.")
                    request = input("Enter yes or no:\n").strip().lower()    
  
            if request != 'yes':
                print("Exiting: No more Data will be displayed.")
                break    
   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_dat(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
if __name__ == "__main__":
	main()