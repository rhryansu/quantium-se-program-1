import csv
import glob
import os
import tempfile

import pandas
import shutil

# merge 3 csv's into one
files = os.path.join('data/', 'daily_sales_data_*.csv')
files = glob.glob(files)
df = pandas.concat(map(pandas.read_csv, files), ignore_index=True)
df.to_csv('merged_csv.csv', index=False, encoding='utf-8-sig')

# processing csv for only one having pink morsel
with open("merged_csv.csv", 'r') as inp, open("cleaned_file.csv", 'w') as out:
    writer = csv.writer(out)
    for line in csv.reader(inp):
        if "pink morsel" in line:
            writer.writerow(line)

# processing sales
with open("cleaned_file.csv", 'r+') as inp, open("pink_morsels.csv", 'w+') as out:
    writer = csv.writer(out)
    reader = csv.reader(inp)
    data = [row for row in reader]
    for i in data:
        sale = float(i[1].replace('$', '')) * float(i[2])
        # if dollar symbol is required this line can be uncommented.
        # i.append('$' + str(sale))
        i.append(str(sale))
        i.pop(1)
        i.pop(1)
        i[0] = i[len(i) - 1]
        i.pop(len(i) - 1)
    data.insert(0, ["sales", "date", "region"])
    writer.writerows(data)

