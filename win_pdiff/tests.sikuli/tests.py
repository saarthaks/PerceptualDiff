import time
import os
import shutil
import sys
sys.path.append(os.path.join('C:\Users\saart\wraith', 'bin'))
import wraithpath


def setup(path):
    App.open(path)
    time.sleep(2)
    
def testSecureEmail(new):
    wait("testSecureImages4.PNG")
    OutlookApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(OutlookApp)
    final_path = os.path.join(wraithpath.imgs(), 'testSecureEmail')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'secureEmail_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'secureEmail_current.png'))

def testViewAccounts(new):
    type(Key.ALT)
    time.sleep(0.5)
    type('f')
    time.sleep(0.5)
    type('i')
    time.sleep(0.5)
    type('s')
    time.sleep(0.5)
    type(Key.ENTER)
    wait("testViewImages.PNG")
    SettingsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SettingsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testViewAccounts')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'viewAccounts_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'viewAccounts_current.png'))

def testAccountSettings(new):
    type('a', KEY_ALT)
    wait("testAccountImages.PNG")
    SettingsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SettingsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testAccountSettings')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'accountSettings_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'accountSettings_current.png'))
        
def testGeneralSettings(new):
    type('m', KEY_ALT)
    wait("testGeneralImages.PNG")
    SettingsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SettingsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testGeneralSettings')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'generalSettings_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'generalSettings_current.png'))
        
def testServerSettings(new):
    find("testGeneralImages.PNG")
    click("testGeneralImages.PNG")
    SettingsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SettingsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testServerSettings')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'serverSettings_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'serverSettings_current.png'))
        
def testAdvancedSettings(new):
    find("testAdvancedImages.PNG")
    click(Pattern("testAdvancedImages.PNG").targetOffset(93,0))
    SettingsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SettingsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testAdvancedSettings')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'advancedSettings_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'advancedSettings_current.png'))
        
def teardown():
    found = find(Pattern("teardownImages-1.PNG").targetOffset(230,-85))
    hover(found)
    click(found)
    found = find(Pattern("teardownImages2.PNG").targetOffset(10,-36))
    click(found)
    type('c', KEY_ALT)
    found = find(Pattern("teardownImages3.PNG").targetOffset(63,-6))
    click(found)

def main(new): 
    testSecureEmail(new)
    testViewAccounts(new)
    testAccountSettings(new)
    testGeneralSettings(new)
    testServerSettings(new)
    testAdvancedSettings(new)

if __name__ == '__main__':
    path = 'C:\\' + 'Program Files (x86)\\' + 'Microsoft Office\\' + 'root\\' + 'Office16\\' + 'OUTLOOK.exe'
    new = True
    if 'current' in sys.argv:
        new = False
    
    setup(path)
    main(new)
    teardown()
    print "done"