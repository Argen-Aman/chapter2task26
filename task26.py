def counting_stars():
    
    file_name = 'text1.txt' # replace with the name of your file

    lines = 0
    words = 0
    symbols = 0

    with open(file = file_name, mode = 'r') as f:
        for line in f:
            word_list = line.split()

            lines += 1
            words += len(word_list)
            symbols += len(line)
                
    print(f'Lines in the file: {lines}')
    print(f'Words in the file: {words}')
    print(f'Symbols in the file: {symbols}')

counting_stars()

""" Не смог посчитать кол-во только букв
    (перепробовал все что мог).
    Поэтому взял кол-во всех символов. """
