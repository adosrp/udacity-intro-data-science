import string

def mapper():

    f = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/turnstile_data_master_with_weather.csv', 'rb')
    g = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/turnstile_data_mapped.txt', 'wb')

    for line in f:
        data = line.strip().split(',')

        if len(data) != 22 or data[1] == 'UNIT':
            continue

        result = '{0}\t{1}\n'.format(data[1], data[6])
        g.write(result)
        print result

    f.close()
    g.close()

mapper()
