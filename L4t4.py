def file_search(folder, filename):
    way = folder[0]
    if filename in folder:
        return way + '/' + filename
    for item in folder:
        if isinstance(item, list):
            found_file = file_search(item, filename)
            if found_file != None:
                return way + '/' + found_file
        else:
            return False


if __name__ == '__main__':
    print(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
    print(file_search(
        ['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak']], 'hey.py'],
        'find.me'))
    print(file_search(['/tmp', ['1', ['2', ['3', ['4', ['5', 'key1', 'key2', 'key3']]]]]], 'key3'))
