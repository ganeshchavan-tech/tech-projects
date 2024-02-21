
def read_file(file_path, encoding='latin-1'):
    with open(file_path, encoding=encoding or 'utf-8') as f:
        return f.read()
    

def zeros_dict(words_list):
    return dict(zip(words_list,[0]*len(words_list)))