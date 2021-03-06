import os


ROOT_DIR = 'C:\Users\saart\wraith'
SIKULI_DIR = os.path.join('C:\\', 'Sikuli_X')

def configs(name):
    return os.path.join(os.path.join(ROOT_DIR, 'configs'), name)

def root():
    return ROOT_DIR

def imgs():
    folder = 'shots'
    return os.path.join(ROOT_DIR, folder)

def thumbs(img_dir, file_name):
    return os.path.join(img_dir, file_name)

def sikuli():
    return os.path.join(SIKULI_DIR, 'Sikuli-IDE.exe')

def test(file_name):
	return os.path.join(SIKULI_DIR, file_name)

