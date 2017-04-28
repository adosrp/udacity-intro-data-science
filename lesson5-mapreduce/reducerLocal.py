import string

def reducer():

    f = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/aadhaar_data_mapped.txt', 'rb')
    g = open('C:/Users/Augusto/Dropbox/Atom Projects/Intro to Data Science - Udacity/Datasets/aadhaar_data_mapreduced.txt', 'wb')

    aadhaar_generated = 0
    old_key = None

    for line in f:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        this_key, count = data

        if old_key != None and old_key != this_key:
            result = '{0}\t{1}\n'.format(old_key, aadhaar_generated)
            g.write(result)
            print result
            aadhaar_generated = 0

        old_key = this_key
        aadhaar_generated += float(count)

    if old_key != None:
        result = '{0}\t{1}\n'.format(old_key, aadhaar_generated)
        g.write(result)
        print result

    f.close()
    g.close()

reducer()
