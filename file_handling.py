def import_data_from_file(filename='outputfile.csv'):
    """
    get data file convert lines to list of lists,
    cut new line tags, double quotation
    and replace ampersand with coma
    """
    temp_list = []
    with open(filename, 'r') as datafile:
        for line in datafile.readlines():
            temp_list.append(line.strip().split(','))
        cuted_quotation = [[entry.strip('"') for entry in entry] for entry in temp_list]
        result = [[entry.replace(' &amp;', ' &').replace('&#39;', "'") for entry in entry] for entry in cuted_quotation]
        indexes = [-1, -3]
        for entry in result:
            del entry[-1]
        return result


albums = import_data_from_file(filename='outputfile.csv')


def export_to_file(data, filename='readable_playlist.csv', mode='a'):
    with open(filename, mode) as datafile:
        for entry in albums:
            datafile.write(','.join(entry) + '\r\n')


export_to_file(import_data_from_file('outputfile.csv'), filename='readable_playlist.csv', mode='a')
