# mobileForensics

The objective of this repository is to provide tools to help in mobile forensics investigations.

parseMapMyRide
Extracts Geo location data from parseMapMyRide workout application database workout.db as well as user related information extracted from mmkd_user file. These files are located in /apps/com.mapmyride.android2/db. 

Sample usage:

python parseMapMyRide.py
Workout(s) extracted: 3
Entries with GPS location extracted: 1407 Import the file workoutGPS.txt into excel using ; as delimiter.
Extracted user data into userMapMyRide.csv
