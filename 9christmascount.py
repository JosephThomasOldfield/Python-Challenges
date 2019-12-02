'''
Calculate the number of days till Christmas.
'''

from datetime import datetime



def date_dif(d2):
    d1 = datetime.now()
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    print(" ",abs((d2 - d1).days)," days until christmas ")

date_dif("2019-12-25")