from os.path import basename, exists
import re

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename

download('https://github.com/AllenDowney/ThinkPython/raw/v3/pg345.txt');

reader = open('pg345.txt', encoding='utf-8')

def is_special_line(line):
    return line.startswith('*** ')

for line in reader:
    if is_special_line(line):
        print(line.strip())

reader = open('pg345.txt', encoding='utf-8')
writer = open('pg345_cleaned.txt', 'w', encoding='utf-8')

for line in reader:
    if is_special_line(line):
        break
print(line)

for line in reader:
    if is_special_line(line):
        break
    writer.write(line)
print(line)

reader.close()
writer.close()

for line in open('pg345_cleaned.txt', encoding='utf-8'):
    line = line.strip()
    if len(line) > 0:
        print(line)
    if line.endswith('Stoker'):
        break

total = 0
for line in open('pg345_cleaned.txt', encoding='utf-8'):
    if 'Jonathan' in line:
        total += 1

print(total)

total = 0
for line in open('pg345_cleaned.txt', encoding='utf-8'):
    total += line.count('Jonathan')

print(total)

writer = open('pg345_replaced.txt', 'w', encoding='utf-8')

for line in open('pg345_cleaned.txt', encoding='utf-8'):
    line = line.replace('Jonathan', 'Thomas')
    writer.write(line)

total = 0
for line in open('pg345_replaced.txt', encoding='utf-8'):
    total += line.count('Thomas')

print(total)

pattern = 'Mina|Murray'

def find_first(pattern):
    for line in open('pg345_cleaned.txt', encoding='utf-8'):
        result = re.search(pattern, line)
        if result != None:
            return result

result = find_first(pattern)
print(result.string)

