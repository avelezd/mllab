class textFileReader:

    default_mode_content = None

    def __init__(self, path):
        self.path = path
        # self.filename = filename

    def default_mode(self, filename, encode):

        try:

            data_file = open(self.path + filename, 'r', encoding=encode)
            data = data_file.read()

            self.default_mode_content = {'function': 'default_mode', 'filename': filename, 'length': len(data)}
            data_file.close()

        except:
            raise

        return 0


path = '/home/avelezd/repositories/01_parsingtextfiles/00_inputdata/'
meta_info = textFileReader(path)
meta_info.default_mode('books_uniq_weeks.csv', "ISO-8859-1")
print(meta_info.default_mode_content)
