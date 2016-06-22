import subprocess
import shutil
import time
import os
import sys
sys.path.append('/Users/saart/wraith/bin')
import wraithpath

def deleteAccounts():
    click(find("1466012962617.png"))
    type(",", KEY_CMD)
    found = find(Pattern("1466028126106.png").targetOffset(-212,0))
    click(found)
    found = find(Pattern("1466093214368.png").targetOffset(13,0))
    click(found)
    found = find(Pattern("1466093247108.png").targetOffset(94,0))
    click(found)
    found = find(Pattern("1466109435018.png").targetOffset(-16,-31))
    click(found)


def quitMail():
    wait("1466012962617-1.png")
    found = find("1466004846646.png")
    click(found)
    closeApp('Mail')

def main():
    deleteAccounts()
    quitMail()

if __name__ == '__main__':
    main()