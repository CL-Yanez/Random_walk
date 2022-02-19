import csv

def get_word():
    '''Return a list of words from a csv'''
    with open('words.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        next(csv_reader) #Avoid showing the header of the column
        # for line in csv_reader:
        #     print(line)
        
        word_list = [','.join(lines) for lines in csv_reader]
    
    return word_list

obj = get_word()
# print(obj)