import csv
import sys, argparse

from datetime import datetime

def main ():

    ### Parse argument
    parser = argparse.ArgumentParser(description = 'Calculate weekly values for input file.')
    parser.add_argument('--file', help = 'Data file for processing', required = True)
    filename = parser.parse_args().file 

    print(f'Working on {filename}')
    
    with open(filename, 'r') as csvfile:
        imported_data = csv.reader(csvfile)
        next(imported_data)

        ### Remove all dates before the first Monday so that we always start with a whole week
        first_run = True
        raw_data = []
        for row in imported_data:
            datetime_object = datetime.strptime(row[0], '%Y-%m-%d')
            if first_run and 0 < datetime_object.weekday() < 6:
                first_run = True
            elif first_run and datetime_object.weekday() == 6:
                first_run = False
            else:
                first_run = False
                raw_data.append([datetime_object, row[1]])

        ### Remove left over days before last date so that we always end with a whole week       
        i = 0
        days = []
        week = raw_data[-7][0].isocalendar()[1]
        while i < 7:
            i += 1
            if not raw_data[-i][0].isocalendar()[1] == week:
                days.append(raw_data[-i])
        for day in days:
            raw_data.remove(day)

        ### Add up numbers for each week, append each week's result to new list
        weekly_data_list = []
        weekly_data = 0
        week = 0
        year = int(raw_data[0][0].strftime("%Y"))
        for element in raw_data:
            calendar_week = int(element[0].isocalendar()[1])
            # new week
            if calendar_week > week:
                week = calendar_week
                weekly_data = int(element[1])
                weekly_data_list.append([year, calendar_week, weekly_data])
            # new week and new year
            elif calendar_week < week:
                year += 1
                week = calendar_week
                weekly_data = int(element[1])
                weekly_data_list.append([year, calendar_week, weekly_data])
            else:
                weekly_data = weekly_data_list[-1][2] + int(element[1])
                weekly_data_list[-1] = [year, calendar_week, weekly_data]

        ### Add header for csv
        weekly_data_list.insert(0, ['Year', 'Week', 'Number'])

        ### Write results into new csv-file
        results_file_name = 'WEEKLY_' + filename 
        with open(results_file_name, 'w', newline='') as results_file:
            results = csv.writer(results_file, quoting=csv.QUOTE_ALL)
            for element in weekly_data_list:
                results.writerow(element)
        print('Done! Results saved to ', results_file_name)

if __name__ == '__main__':
    main()
