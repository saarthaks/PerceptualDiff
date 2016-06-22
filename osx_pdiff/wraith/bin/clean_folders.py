import os
import shutil
import sys
sys.path.append('C:\Users\saart\wraith\\bin')
import wraithpath


def delete_new_files():
    folder = wraithpath.imgs()
    tests = []
    for dirs in os.listdir(folder):
        if 'html' in dirs:
            os.remove(os.path.join(folder, dirs))
        if os.path.isdir(os.path.join(folder,dirs)):
            tests.append(dirs)

    for test in tests:
        files = os.path.join(folder, test)
	for fil in os.listdir(files):
            if 'current' in fil or 'test' in fil:
                continue
	    os.remove(os.path.join(files, fil))


def delete_thumbs():
    try:
        shutil.rmtree(os.path.join(wraithpath.imgs(), 'thumbnails'))
    except OSError:
        pass

def main():
    delete_new_files()
    delete_thumbs()

if __name__ == '__main__':
    main()
