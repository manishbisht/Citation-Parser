input_file = open('input.txt')
output_file = open('output.txt', 'w')
line = input_file.readline()
while line:
    line = line.replace('\n', '')
    line = line.replace('\xe2\x80\x93', '-')
    #output_file.write("Input:\n{}\n".format(line))
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
            if text[0:-1].isdigit():
                check['author'] = 1
            elif line[i+1][-1] == ':' or (i+2 < len(line) and line[i+2][-1] == ':') and text[-1] == ',':
                result['author'] += text
                check['author'] = 1
            else:
                result['author'] += text
                if text[-1] == '.' and '.' not in result['author'][0:-1] and len(result['author']) > 2:
                    result['author'] = result['author'][:-1]
                    check['author'] = 1
                elif 'and' in result['author'] and result['author'][-1] ==',':
                    result['author'] = result['author'][:-1]
                    check['author'] = 1
                else:
                    result['author'] += ' '
        elif check['year'] == 0 and len(text[:-1]) == 4 and text[:-1].isdigit():
            result['year'] = text[:-1]
            check['year'] = 1
        elif check['title'] == 0:
            result['title'] += text
            if text[-1] == '.' or line[i+1] == 'vol.' or line[i+1] == 'pp.' or line[i+1] == 'In':
                result['title'] = result['title']
                check['title'] = 1
            else:
                result['title'] += ' '
        elif check['journal'] == 0 and line[i] != 'pp.' and line[i] != 'vol.':
            result['journal'] += text
            if text[-1] == '.' or line[i+1].isdigit() or line[i+1][0:-1].isdigit() or line[i+1] == 'pp.' or line[i+1] == 'vol.':
                result['journal'] = result['journal'][:-1]
                check['journal'] = 1
            else:
                result['journal'] += ' '
        elif check['volume'] == 0 and text != 'pp.':
            check['journal'] = 1
            if text == 'Vol' or text == 'vol.':
                i += 1
                result['volume'] = line[i]
                if not result['volume'].isdigit():
                    result['volume'] = result['volume'][:-1]
                check['volume'] = 1
                i += 1
                text = line[i]
                if line[i] == 'No.' or line[i] == 'no.':
                    i += 1
                    result['issue'] = line[i][0:-1]
            elif text.isdigit() and line[i+1][0] == '(':
                result['volume'] = text
                i += 1
                text = line[i]
                if text[0] == '(' and text[-1] == ',':
                    result['issue'] = text[1:-2]
                check['volume'] = 1
        elif check['pages'] == 0:
            check['volume'] = 1
            if text == 'pages' or text == 'pp.':
                i += 1
                text = line[i]
                result['pages'] = text[0:-1]
                check['pages'] = 1
            elif text[0] =='e':
                result['pages'] = text[0:-1]
                check['pages'] = 1
    if 'In' in result['journal'][0:2]:
        result['book-title'] = result['journal']
        result['journal'] = ''
    output_file.write("Output:\n")
    for i in result:
        if result[i]:
            output_file.write("{}: {}\n".format(i, result[i]))
    output_file.write("\n")
    line = input_file.readline()
