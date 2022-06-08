"""
----------------------------------------------------------------------
    The script print out the soonest date in the future when at least
    desired amount of people are available for given amount of time.
----------------------------------------------------------------------
    Autor: Jakub Krecisz                            Krakow, 27.04.2022
----------------------------------------------------------------------
"""

import argparse
import datetime
import glob
import re

# Defining arguments for retrieving the number of people, availability in minutes and calendars path
parser = argparse.ArgumentParser(description='Find available slot for a specific number of people and time')

parser.add_argument('--duration-in-minutes', type=int, required=True, metavar='',
                    help='Availability time of people (minutes)')
parser.add_argument('--minimum-people', type=int, required=True, metavar='', help='Minimum number of people')
parser.add_argument('--calendars', required=True, metavar='', help='Name of the date folder')

args = parser.parse_args()

# Variables in which we keep paths for calendars, duration in datetime type and current date
personsCalendars = glob.glob(f'.{args.calendars}/*.txt')
minutesDuration = datetime.timedelta(minutes=args.duration_in_minutes)
currentDate = datetime.datetime.now()


# A function that for a specific day checks minute by minute whether our availability slot fits
def findSlot(date, minNumOfPeople, calendarsPaths, minutes):
    busyTimes = []  # All busy hours for all people
    dateRegex = f'{date.strftime("%Y-%m-%d")} \d\d:\d\d:\d\d - {date.strftime("%Y-%m-%d")} \d\d:\d\d:\d\d|' \
                f'{date.strftime("%Y-%m-%d")}'
    availableTime = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute)

    if minNumOfPeople <= 0:
        return '--minimum-people must be >= 1'

    for filePath in calendarsPaths:
        busyTimes.append(re.findall(dateRegex, open(filePath).read()))

    if len(busyTimes) < minNumOfPeople:
        return f"Not enough people in calendars, currently in calendars: {len(busyTimes)} people"

    if busyTimes.count([]) >= minNumOfPeople:
        return datetime.datetime(date.year, date.month, date.day)

    counter = 0

    # We check for each possible slot whether enough people are available
    while availableTime.day == date.day:
        for personsBusyTimes in busyTimes:
            counter += findEachDaySlot(personsBusyTimes, minutes, availableTime)
            if counter == minNumOfPeople:
                return availableTime
        availableTime += datetime.timedelta(minutes=1)
        counter = 0


# The function checks if the specified availability slot falls within the specified hours for the period
def findEachDaySlot(personsTimes, minutes, startingTime):
    endingTime = startingTime + minutes
    beginningOfTheDay = datetime.datetime(startingTime.year, startingTime.month, startingTime.day)
    endOfTheDay = beginningOfTheDay + datetime.timedelta(days=1)

    if not personsTimes:
        return 1

    for time in personsTimes:
        # check by ':' because we take only those values where the person is occupied for a certain number of hours
        if ':' in time:
            busyTimeStarts = datetime.datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]),
                                               int(time[11:13]), int(time[14:16]), int(time[18:20]))
            busyTimeEnds = datetime.datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]),
                                             int(time[-8:-6]), int(time[-5: -3]), int(time[-2:]))

            if (busyTimeStarts < startingTime < busyTimeEnds) or (busyTimeStarts < endingTime < busyTimeEnds) or (
                    startingTime < beginningOfTheDay) or (endingTime > endOfTheDay):
                return 0
        else:
            return 0
    return 1


if __name__ == '__main__':
    while True:
        availableSlot = findSlot(currentDate, args.minimum_people, personsCalendars, minutesDuration)
        if availableSlot:
            print(availableSlot)
            break
        currentDate += datetime.timedelta(days=1)
