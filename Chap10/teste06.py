from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename

download('https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt');

word_list = open('words.txt').read().split()

word_dict = {}
for word in word_list:
    word_dict[word] = 1

def reverse_word(word):
    return ''.join(reversed(word))

def much_faster():
    count = 0
    for word in word_dict:
        if reverse_word(word) in word_dict:
            count += 1
    return count

print(much_faster())
