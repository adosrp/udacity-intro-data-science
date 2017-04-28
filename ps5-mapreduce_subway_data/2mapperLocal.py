import string

def mapper():

    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
            )

    f = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/turnstile_data_master_with_weather.csv', 'rb')
    g = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/turnstile_data_mapped.txt', 'wb')

    for line in f:
    	data = line.strip().split(',')

        if len(data) != 22 or data[1] == 'UNIT':
            continue

        weather = format_key(bool(float(data[14])), bool(float(data[15])))
        ENTRIESn_hourly = data[6]
        result = '{0}\t{1}\n'.format(weather, ENTRIESn_hourly)
        g.write(result)
        print result

    f.close()
    g.close()

mapper()
