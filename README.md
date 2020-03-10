# wiki pageviews weekly
Calculate weekly data for pageviews of wikipedia pages downloaded from https://tools.wmflabs.org

# Backround:
I wanted to analyse some pageview date from the very convenient website https://tools.wmflabs.org where they offer daily and monthly data for wikipedia pages. Since I wanted weekly data, I created this script that takes a downloaded .csv file from wmflabs and converts it into a csv with weekly sums. This is nothing but a hobby project - there are probably many ways of doing this better and more efficient (for example directly through the wikimedia API).

# Run:
Execute script with python3 (minimum Python 3.6), use the --file argument to provide the filename of the downloaded csv-file.

eg: python3 weekly_numbers.py --file pageviews-FROM-TO.csv

When finished the script will display the name of the file with the weekly data.
