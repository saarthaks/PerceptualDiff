import yaml
import os
import sys
sys.path.append('/Users/saart/wraith/bin')
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
    setup = wraithpath.sikuli() + ' -r ' + wraithpath.test('setup.sikuli')
    tests = wraithpath.sikuli() + ' -r ' + wraithpath.test('tests.sikuli')
    teardown = wraithpath.sikuli() +  ' -r ' + wraithpath.test('teardown.sikuli')
    
    if force:
        tests += ' -- current'
    os.system(setup)
    os.system(tests)
    os.system(teardown)

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
    tests = ['testSecureInbox', 'testAccountInformation',
            'testSMTPAccountInformation',
            'testSMTPAdvancedInformation','testMailboxBehaviors',
            'testAdvanced']
    
    #setup_folders(tests)
    
    generate_images(force)
    
    if not force:
        config = make_config(tests)
        run_pdiff(config)

if __name__ == '__main__':
    if '-f' in sys.argv or '--force' in sys.argv:
        main(force=True)
    else:
        main()
