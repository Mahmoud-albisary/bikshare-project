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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter the city you want to analyze (chicago, new york city or washington): ").lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        city = input("Please enter a valid input.(chicago, new york city or washington): ")

    # get user input for month (all, january, february, ... , june)
    month = input("Please enter the month you want to analyze (all, january, february, ... , june): ").lower()
    while month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june' and month != 'all':
        month = input("Please enter a valid month you want to analyze: ")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Please enter the day you want to analyze (all, monday, tuesday, ... sunday): ").lower()
    while day != "saturday" and day != "sunday" and day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "all":
        day = input("Please enter a valid day you want to analyze: ")
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
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_week"] = df["Start Time"].dt.day_name()
    if month != "all":
        all_months = ["january", "february", "march", "april", "may", "june"]
        month = all_months.index(month) + 1
        df = df[df["month"] == month ]
    if day != "all":
        df = df[df["day_week"] == day.title() ]

    df["hour"] = df["Start Time"].dt.hour
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == "all":
        all_months = ["january", "february", "march", "april", "may", "june"]
        common_month = int(df["month"].mode())
        if day != "all":
            print("The most frequent month is:",all_months[common_month - 1] ,"that had a trip on ",day)
        else:
            print("The most frequent month is: ",all_months[common_month - 1])
    # display the most common day of week
    if day == "all":
        common_day = df["day_week"].mode()
        if month == "all":
            print("The most frequent day in all months is:", common_day[0])
        else:
            print("The most frequent day in ",month," is:", common_day[0])
    # display the most common start hour
    if month == "all" and day == "all":
        print("The most common hour is:",df['hour'].mode()[0])
    elif month == "all":
        print("The most common hour on ",day," is:", df['hour'].mode()[0])
    elif day == "all":
        print("The most common hour in ",month," is:", df['hour'].mode()[0])
    else:
        print("The most common hour on ",day," in ", month," is:", df['hour'].mode()[0])





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,month,day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip
    Station = (df["Start Station"]+"  "+df["End Station"]).mode()[0]
    #I think there is a more efficient solution than the above line So please send a feedback
    #to inform me how to write a code that does the same but efficiently
    if month == "all" and day == "all":
        print("The most common start station is:",df["Start Station"].mode()[0])
        print("The most common end station is:",df["End Station"].mode()[0])
        print("The Most common combination is Start Station: "+ Station.split("  ")[0] +" and End Station: "+ Station.split("  ")[1])
    elif month == "all":
        print("The most common start station on",day,"is:",df["Start Station"].mode()[0])
        print("The most common end station on",day,"is:",df["End Station"].mode()[0])
        print("The Most common combination on "+ day +" is Start Station: "+Station.split("  ")[0] +" and End Station: "+ Station.split("  ")[1])
    elif day == "all":
        print("The most common start station in",month,"is:",df["Start Station"].mode()[0])
        print("The most common end station in",month,"is:",df["End Station"].mode()[0])
        print("The Most common combination in " + month +" is Start Station: "+Station.split("  ")[0] +" and End Station: "+ Station.split("  ")[1])
    else:
        print("The most common start station on",day, "in",month,"is:",df["Start Station"].mode()[0])
        print("The most common end station on",day, "in",month,"is:",df["End Station"].mode()[0])
        print("The Most common combination on "+day +" in "+ month +" is Start Station: "+Station.split("  ")[0] +" and End Station: "+ Station.split("  ")[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # display mean travel time
    Total_Time = df["Trip Duration"].sum()
    Average_Time = df["Trip Duration"].mean()
    if month == "all" and day == "all":
        print("Total travel time is:", Total_Time)
        print("Average time is:", Average_Time)
    elif month == "all":
        print("Total travel time on",day,"is:", Total_Time)
        print("Average travel time on",day,"is:", Average_Time)
    elif day == "all":
        print("Total travel time in",month,"is:", Total_Time)
        print("Average travel time in",month,"is:", Average_Time)
    else:
        print("Total travel time on",day,"in",month,"is:", Total_Time)
        print("Average travel time on",day,"in",month,"is:",  Average_Time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Display counts of gender
    #Did not use .value_counts() to be able to seperate the count of each item in a
    try:
        #Year of birth and gender are not present in the washington.csv file
        Genderdf = df[df["Gender"] == "Male"]
        males = Genderdf["Gender"].count()
        Genderdf = df[df["Gender"] == "Female"]
        females = Genderdf["Gender"].count()
        Early = int(df["Birth Year"].min())
        Recent = int(df["Birth Year"].max())
        Common = int(df["Birth Year"].mode()[0])
    except KeyError:
        pass
    User_Typedf = df[df["User Type"] == "Customer"]
    customers = User_Typedf["User Type"].count()
    User_Typedf = df[df["User Type"] == "Subscriber"]
    subscriber = User_Typedf["User Type"].count()

    if month == "all" and day == "all":
        print("Number of Cusromers:", customers)
        print("Number of Subscribers:", subscriber)
        try:
            print("Number of Males:", males)
            print("Number of Females:", females)
            print("The earliest year of birth:",Early)
            print("The most recent year of birth:", Recent)
            print("The most common year of birth:", Common)
        except UnboundLocalError:
            pass
    elif month == "all":
        print("Number of Cusromers on",day,":", customers)
        print("Number of Subscribers on",day,":", subscriber)
        try:
            print("Number of Males on",day,":", males)
            print("Number of Females on",day,":", females)
            print("The earliest year of birth on",day,":", Early)
            print("The most recent year of birth on",day,":", Recent)
            print("The most common year of birth on",day,":", Common)
        except UnboundLocalError:
            pass
    elif day == "all":
        print("Number of Cusromers in",month,":", customers)
        print("Number of Subscribers in",month,":", subscriber)
        try:
            print("Number of Males in",month,":", males)
            print("Number of Females in",month,":", females)
            print("The earliest year of birth in",month,":", Early)
            print("The most recent year of birth in",month,":", Recent)
            print("The most common of birth in",month,":", Common)
        except UnboundLocalError:
            pass
    else:
        print("Number of Cusromers on",day,"in", month,":", customers)
        print("Number of Subscribers on",day,"in", month,":", subscriber)
        try:
            print("Number of males on",day,"in", month,":", males)
            print("Number of Females on",day,"in", month,":", females)
            print("The earliest year of birth on",day, "in",month,":", Early)
            print("The most recent year of birth on",day,"in",month,":", Recent)
            print("The most common of birth on",day,"in",month,":", Common)
        except UnboundLocalError:
            pass



    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df, month, day)
        trip_duration_stats(df, month, day)
        user_stats(df, month, day)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
