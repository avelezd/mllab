# Reading and parsing textfiles
The class textFileReader defines some methods to read text files during the process data about the content of the file is logged into a dictionary, I named it metadata.

**default_mode:** 
Is the default way to read a file in python, it not requires additional libraries. The metadata structure generated by is _default_mode_content_

`{'function': <<Function_name>>, 'filename': <<file_name>>, 'length': len(<<data_readed>>)}`