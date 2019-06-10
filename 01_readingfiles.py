import logging
import sys
import os

import pandas as pd
import cchardet as chardet # find file encoding

class textFileReader:
    # [B]-Log configuration--------------------------------------------------------------------------------------------#
    _LOG_FILEPATH_ = "01_logs/"
    _LOG_FILENAME_ = "01_processtrace.log"
    _LOG_LEVEL_ = logging.INFO
    _LOG_FORMAT_ = "[%(asctime)s] %(levelname)s %(message)s (%(filename)s:%(funcName)s():%(lineno)s)"

    logging.basicConfig(filename=_LOG_FILEPATH_ + _LOG_FILENAME_, level=_LOG_LEVEL_, format=_LOG_FORMAT_)
    logger = logging.getLogger()
    # [E]-Log configuration--------------------------------------------------------------------------------------------#

    metadata_dfmode = None
    metadata_pdmode = None

    def __init__(self, path):
        self.path = path
        self.logger.info('textFileReader instance created with path %s' % (path))

    # def get_file_encoding(self, filepath):
    #
    #     with open(self.path+filepath, "rb") as f:
    #         msg = f.read()
    #         result = chardet.detect(msg)
    #         print(result)
    #     return 0

    def default_mode(self, filename, encode):

        try:

            self.logger.info('Opening file %s' % (filename))
            data_file = open(self.path + filename, 'r', encoding=encode)
            data = data_file.read()

        except IOError as ioe:
            self.logger.info("I/O error({0}): {1}".format(ioe.errno, ioe.strerror))
            raise
        except:
            self.logger.info("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            self.logger.info('file OK')

            self.metadata_dfmode = {'function': 'default_mode', 'filename': filename, 'length': len(data)}
            data_file.close()
            return 0

    # def convert_bytes(num):
    #     """
    #     this function will convert bytes to MB.... GB... etc
    #     """
    #     for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
    #         if num < 1024.0:
    #             return "%3.1f %s" % (num, x)
    #         num /= 1024.0

    def __get_file_size__(self, filepath):
        """
        this function will return the file size
        """
        if os.path.isfile(filepath):
            file_info = os.stat(filepath)
            return file_info.st_size

    def pandas_mode(self, filename, encode):

        try:
            filedata = pd.read_csv(self.path + filename, encoding=encode)
        except IOError as ioe:
            self.logger.info("I/O error({0}): {1}".format(ioe.errno, ioe.strerror))
            raise
        except:
            self.logger.info("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            self.logger.info('file OK')

            # Get the missing data variables
            nullcols = filedata.isnull().sum()
            nullcols = nullcols[nullcols != 0]


            self.metadata_dfmode = {
                                    'function': 'pandas_mode',
                                    'file_name': filename,
                                    'length': filedata.shape,
                                    'columns': filedata.columns,
                                    'null_cols': nullcols.to_dict(),
                                    'file_size': self.__get_file_size__(self.path + filename)
                                    }

            return 0




path = '00_inputdata/'
meta_info = textFileReader(path)
# meta_info.get_file_encoding('books_uniq_weeks.csv')
# meta_info.default_mode('books_uniq_weeks.csv', "ISO-8859-1")
meta_info.pandas_mode('books_uniq_weeks.csv', "ISO-8859-1")
print(meta_info.metadata_dfmode)
