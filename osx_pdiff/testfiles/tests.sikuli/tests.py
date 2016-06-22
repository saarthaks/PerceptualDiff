import subprocess
import shutil
import time
import os
import sys
sys.path.append('/Users/saart/wraith/bin')
import wraithpath


def viewMailboxes():
    subprocess.Popen('open /Applications/Mail.app', shell=True)
    time.sleep(4)
    try:
        found = find("1466545891606.png")
    except FindFailed:
        found = find("1466004846646.png")
        click(found)

def testSecureInbox(new):
    hover("1466012962617.png")
    MailApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(MailApp)
    final_path = os.path.join(wraithpath.imgs(), 'testSecureInbox')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'secureInbox_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'secureInbox_current.png'))

def testAccountInformation(new):
    hover("1466012962617.png")
    click(find("1466012962617.png"))
    type(",", KEY_CMD)
    wait("1466542498260.png")
    AccountsApp = App.focusedWindow()
    time.sleep(5)
    old_path = capture(AccountsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testAccountInformation')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'secureAccountInformation_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'secureAccountInformation_current.png'))

def testSMTPAccountInformation(new):
    found = find(Pattern("1466027142566.png").targetOffset(163,0))
    click(found)
    click(found.right(163).below(45))
    wait("1466027610988.png")
    SMTPApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SMTPApp)
    final_path = os.path.join(wraithpath.imgs(), 'testSMTPAccountInformation')
    if new: 
        shutil.move(old_path, os.path.join(final_path, 'secureSMTPInformation_new.png'))
    else: 
        shutil.move(old_path, os.path.join(final_path, 'secureSMTPInformation_current.png'))

def testSMTPAdvancedInformation(new):
    found = find("1466027610988.png")
    click(found)
    SMTPApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(SMTPApp)
    final_path = os.path.join(wraithpath.imgs(), 'testSMTPAdvancedInformation')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'secureSMTPAdvancedInformation_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'secureSMTPAdvancedInformation_current.png'))
    found = find("1466027971013.png")
    click(found)
    
def testMailboxBehaviors(new):
    wait("1466542676821.png")
    found = find(Pattern("1466028126106.png").targetOffset(-83,0))
    click(found)
    AccountsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(AccountsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testMailboxBehaviors')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'secureMailboxBehaviors_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'secureMailboxBehaviors_current.png'))

def testAdvanced(new):
    found = find("1466028126106.png")
    click(found)
    AccountsApp = App.focusedWindow()
    time.sleep(2)
    old_path = capture(AccountsApp)
    final_path = os.path.join(wraithpath.imgs(), 'testAdvanced')
    if new:
        shutil.move(old_path, os.path.join(final_path, 'secureAdvanced_new.png'))
    else:
        shutil.move(old_path, os.path.join(final_path, 'secureAdvanced_current.png'))

def teardown():
    found = find(Pattern("1466109435018.png").targetOffset(-16,-31))
    click(found)

def main(new = True):
    viewMailboxes()
    testSecureInbox(new)
    testAccountInformation(new)
    testSMTPAccountInformation(new)
    testSMTPAdvancedInformation(new)
    testMailboxBehaviors(new)
    testAdvanced(new)
    teardown()

if __name__ == '__main__':
    if 'current' in sys.argv:
        main(new=False)
    else:
        main()