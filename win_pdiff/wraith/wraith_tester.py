import yaml
import os
import time
import subprocess
import sys
sys.path.append('C:/Users/saart/wraith//bin')
import wraithpath

def setup_folders(tests):
    img_path = wraithpath.imgs()
    os.makedirs(img_path)
    for test in tests:
        os.makedirs(os.path.join(img_path, test))

    thumb_path = wraithpath.thumbs(img_path, 'thumbnails')
    for test in tests:
        os.makedirs(os.path.join(thumb_path, test))

def make_config(tests):
    dict = {}
    dict['domains'] = {}
    dict['domains']['new'] = '""'
    dict['domains']['current'] = '""'
    dict['threshold'] = 0
    dict['directory'] = os.path.basename(wraithpath.imgs())
    dict['mode'] = 'diffs_first'
    dict['paths'] = {}
    for test in tests:
        dict['paths'][str(test)] = "/"
    
    dict['browser'] = '""'
    dict['screen_widths'] = ['768x400']
    dict['gallery'] = {}
    dict['gallery']['template'] = 'slideshow_template'
    dict['gallery']['thumb_width'] = 200
    dict['gallery']['thumb_height'] = 200
    dict['fuzz'] = "2%"

    config_path = wraithpath.configs('test.yaml')
    outfile = open(config_path, 'w')
    outfile.write(yaml.dump(dict, default_flow_style=False))
    outfile.close()
    return config_path

def generate_images(force):
    cmd = wraithpath.sikuli() + ' -r ' + wraithpath.test('tests.sikuli')
    if force:
        cmd += ' -- current'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return p

def run_pdiff(config):
    os.chdir(wraithpath.root())
    cmd = 'wraith compare_images ' + str(config)
    os.system(cmd)
    cmd = 'wraith generate_thumbnails ' + str(config)
    os.system(cmd)
    cmd = 'wraith generate_gallery ' + str(config)
    os.system(cmd)
    
def main(force=False):
    # initialize tests and folders
    tests = ['testSecureEmail', 'testViewAccounts',
            'testAccountSettings',
            'testGeneralSettings','testServerSettings',
            'testAdvancedSettings']
    
    #setup_folders(tests)
    
    p = generate_images(force)
    
    fin = False
    while not fin:
        output = p.stdout.readline()
        if "done" in output:
            fin = True

    if not force:
        config = make_config(tests)
        run_pdiff(config)

if __name__ == '__main__':
    if '-f' in sys.argv or '--force' in sys.argv:
        main(force=True)
    else:
        main()
