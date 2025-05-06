import webbrowser
import time

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months =["janvier", "février", "mars" ,"avril" ,"mai", "juin", "juillet", "août", "septembre", "octobre" ,"novembre", "decembre"]

for i in range(len(months)):
    for j in range(1, days[i]+1):
        link = f"https://fr.wikipedia.org/wiki/{j}_{months[i]}"
        webbrowser.open(link)
        time.sleep(1)
