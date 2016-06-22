import subprocess
import shutil
import time
import os
import sys
sys.path.append('/Users/saart/wraith/bin')
import wraithpath


def createMailbox():
    subprocess.Popen('open /Applications/Mail.app', shell=True)
    wait("1466019864835.png")
    found = find(Pattern("1466019914076.png").targetOffset(-55,0))
    click(found)
    time.sleep(1)
    found = find(Pattern("1466020044430.png").targetOffset(101,0))
    click(found)
    time.sleep(10)
    wait("1466020818972.png")
    found = find("1466023649896.png")
    click(found)
    type('visual.test10@gmail.com' + Key.ENTER)
    wait("1466020330038.png")
    type('visualtest123' + Key.ENTER)
    wait("1466020393357.png")
    time.sleep(2)
    type(Key.ENTER)
    time.sleep(10)
    closeApp('Mail')

def createSecureAccount():
    subprocess.Popen("open /Applications/'Google Chrome.app'", shell=True)
    wait("1466023746595.png")
    type('relay.preveil.com/newInstallation' + Key.ENTER)
    wait("1466023014110.png")
    found = find(Pattern("1466023014110.png").targetOffset(0,-57))
    click(found)
    type('visual.test10@gmail.com' + Key.ENTER)
    wait("1466023146573.png")
    closeApp('Google Chrome')

def main():
    #createMailbox()
    createSecureAccount()


if __name__ == '__main__':
    main()