import string
from datetime import datetime

def reducer():

    f = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/turnstile_data_mapped.txt', 'rb')
    g = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/turnstile_data_mapreduced.txt', 'wb')

    max_entries = 0
    old_key = None
    max_dt = ''

    for line in f:
        data_temp = line.strip().split('\t')
        data_temp2 = ' '.join(data_temp[2:4])
        data = [data_temp[0], data_temp[1], data_temp2]

        if len(data) != 3 or datetime.strptime(data[2], '%Y-%m-%d %H:%M:%S').strftime('%b') != 'May':
            continue

        this_key, entries, dt = data

        if old_key != None and old_key != this_key:
            result = '{0}\t{1}\t{2}\n'.format(old_key, max_dt, max_entries)
            g.write(result)
            print result
            max_entries = 0
            max_dt = ''

        old_key = this_key

        if float(entries) >= max_entries:
            max_entries = float(entries)
            max_dt = dt

    if old_key != None:
        result = '{0}\t{1}\t{2}\n'.format(old_key, max_dt, max_entries)
        g.write(result)
        print result

    f.close()
    g.close()

reducer()
