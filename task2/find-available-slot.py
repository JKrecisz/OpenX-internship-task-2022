import argparse
import datetime
import glob
import re

parser = argparse.ArgumentParser(description='Find available slot for a specific number of people and time')
parser.add_argument('--duration-in-minutes', type=int, required=True, metavar='',
                    help='Availability of people (minutes)')
parser.add_argument('--minimum-people', type=int, required=True, metavar='', help='Minimum number of people')
parser.add_argument('--calendars', required=True, metavar='', help='Name of the date folder')
args = parser.parse_args()

personsCalendars = glob.glob(f'.{args.calendars}/*.txt')
minutesDuration = datetime.timedelta(minutes=args.duration_in_minutes)
currentDate = datetime.datetime.now()


def findSlot(date, minNumOfPeople, calendarsPaths, minutes):
    busyTimes = []
    dateRegex = f'{date.strftime("%Y-%m-%d")} \d\d:\d\d:\d\d - {date.strftime("%Y-%m-%d")} \d\d:\d\d:\d\d|' \
                f'{date.strftime("%Y-%m-%d")}'

    if minNumOfPeople <= 0:
        return '--minimum-people must be >= 1'

    availableTime = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute)

    for filePath in calendarsPaths:
        busyTimes.append(re.findall(dateRegex, open(filePath).read()))

    if len(busyTimes) < minNumOfPeople:
        return f"Not enough people in calendars, currently in calendars is {len(busyTimes)} people"

    if busyTimes.count([]) >= minNumOfPeople:
        return datetime.datetime(date.year, date.month, date.day)

    counter = 0
    while availableTime.day == date.day:
        for personsBusyTimes in busyTimes:
            counter += findEachDaySlot(personsBusyTimes, minutes, availableTime)
            if counter == minNumOfPeople:
                return availableTime
        availableTime += datetime.timedelta(minutes=1)
        counter = 0


def findEachDaySlot(personsTimes, minutes, startingTime):
    endingTime = startingTime + minutes
    beginningOfTheDay = datetime.datetime(startingTime.year, startingTime.month, startingTime.day)
    endOfTheDay = beginningOfTheDay + datetime.timedelta(days=1)

    if not personsTimes:
        return 1

    for time in personsTimes:
        if ':' in time:
            busyTimeStarts = datetime.datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]),
                                               int(time[11:13]), int(time[14:16]), int(time[18:20]))
            busyTimeEnds = datetime.datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]),
                                             int(time[-8:-6]), int(time[-5: -3]), int(time[-2:]))

            if busyTimeStarts < startingTime < busyTimeEnds:
                return 0
            elif busyTimeStarts < endingTime < busyTimeEnds:
                return 0
            elif startingTime < beginningOfTheDay or endingTime > endOfTheDay:
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
