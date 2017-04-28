import string

def mapper():

    f = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/aadhaar_data.csv', 'rb')
    g = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/aadhaar_data_mapped.txt', 'wb')

    for line in f:
        data = line.strip().split(",")

        if len(data) != 12 or data[0] == 'Registrar':
            continue

        result = '{0}\t{1}\n'.format(data[3], data[8])
        g.write(result)
        print result

    f.close()
    g.close()

mapper()
