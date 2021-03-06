import os


ROOT_DIR = ''           # change to base directory for wraith folder, 
                        # e.g., /Users/saart/PerceptualDiff/osx_pdiff/wraith

SIKULI_DIR = ''         # change to base directory for SikuliX folder,
                        # e.g., /Users/saart/SikuliX

def configs(name):
    return os.path.join(os.path.join(ROOT_DIR, 'configs'), name)

def root():
    return ROOT_DIR

def imgs():
    folder = 'shots'
    return os.path.join(ROOT_DIR, folder)

def thumbs(img_dir, file):
    return os.path.join(img_dir, file)

def sikuli():
    return os.path.join(SIKULI_DIR, 'runsikulix')

def test(file):
    return os.path.join(SIKULI_DIR, 'testfiles/{}'.format(file))
