import shutil
import glob


def read_from_many_write_to_one(path):
    all_files = glob.glob(path + "/*.csv")
    with open('outputfile.csv', 'wb') as out_file:
        for number, file_name in enumerate(all_files):
            with open(file_name, 'rb') as in_file:
                if number != 0:
                    in_file.readline()  # Throw away header on all but first file
                shutil.copyfileobj(in_file, out_file)  # Block copy rest of file from input to output without parsing
                print(f'{number}. {file_name} imported.')


source = r'your/path/to/file'


read_from_many_write_to_one(source)
