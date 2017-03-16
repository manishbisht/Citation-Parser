input_file = open('input.txt')
output_file = open('output.txt', 'w')
line = input_file.readline()
while line:
    line = line.replace('\n', '')
    line = line.replace('\xe2\x80\x93', '-')
    output_file.write("Input:\n{}".format(line))
    line = line.split(' ')
    result = {
        'author': '',
        'year': '',
        'title': '',
        'journal': '',
        'volume': '',
        'issue': '',
        'pages': ''
    }
    check = {
        'author': 0,
        'year': 0,
        'title': 0,
        'journal': 0,
        'volume': 0,
        'pages': 0
    }
    for i in xrange(len(line)):
        text = line[i]
        if check['author'] == 0:
            result['author'] += text
            if text[-1] == '.':
                result['author'] = result['author'][:-1]
                check['author'] = 1
            else:
                result['author'] += ' '
        elif check['year'] == 0 and len(text[:-1]) == 4 and text[:-1].isdigit():
            result['year'] = text[:-1]
            check['year'] = 1
        elif check['title'] == 0:
            result['title'] += text
            if text[-1] == '.':
                result['title'] = result['title'][:-1]
                check['title'] = 1
            else:
                result['title'] += ' '
        elif check['journal'] == 0:
            result['journal'] += text
            if text[-1] == '.' or text[-1] == ':':
                result['journal'] = result['journal'][:-1]
                check['journal'] = 1
            else:
                result['journal'] += ' '
        elif check['volume'] == 0:
            if text == 'Vol':
                i += 1
                result['volume'] = line[i]
                check['volume'] = 1
                i += 1
                text = line[i]
                if line[i] == 'No.':
                    i += 1
                    result['issue'] = line[i][0:-1]
            elif text.isdigit():
                result['volume'] = text
                i += 1
                text = line[i]
                if text[0] == '(' and text[-1] == ',':
                    result['issue'] = text[1:-2]
                check['volume'] = 1
        elif check['pages'] == 0:
            if text == 'pages':
                i += 1
                text = line[i]
                result['pages'] = text[0:-1]
                check['pages'] = 1
            elif text[0] =='e':
                result['pages'] = text[0:-1]
                check['pages'] = 1
    output_file.write("\nOutput:\n")
    for i in result:
        output_file.write("{}: {}\n".format(i, result[i]))
    output_file.write("\n")
    line = input_file.readline()
