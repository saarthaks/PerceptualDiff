# PerceptualDiff for Windows
##### Visual test automation for Microsoft Outlook

This system relies on two major tools for carrying out the visual automation, effectively splitting it up into two stages: generating the screenshots, and performing an image comparison between the new build and the accepted build. The first stage is handled by [Sikuli](http://www.sikuli.org), which supports scripting through its own IDE, Sikuli X, and allows for visual automation and screen capture. The second stage is handled by [Wraith](http://bbc-news.github.io/wraith/), which carries out perceptual diff operation on the captured images and creates an HTML file to view the results. 

## Getting Started
### Prerequesites
##### 1. Sikuli
Sikuli is primarily written in Java, but fortunately supports scripting in other languages, like Python. To begin, ensure that you have valid Java installation of at least Java 7. If not, download and install either the JRE or the JDK from [Oracle](http://www.oracle.com/technetwork/java/javase/downloads/index.html). Then continue on with the installation for Sikuli as detailed below.

Download the [setup file](https://launchpad.net/sikuli/sikulix/1.1.0) and prepare a folder for the program (e.g., ~\Sikuli_X), which will house its all artifacts and scripts pertaining to SikuliX. Move the downloaded file **sikulixsetup**...**.jar** into this folder and run via double-click or through the command line with `java -jar sikulixsetup...jar`, and select Option 1 for configuration. This configuration will provide the SikuliX IDE for development and scripting, as well as allow you to select Python as a the desired scripting language.

For more information on using SikuliX, look at the documentation [here](http://sikulix.com/quickstart/).
##### 2. Wraith
The second stage of configuration requires installing Wraith's dependencies. First, ensure you have Ruby and RubyGems. You can check by running `ruby --version` and `gem --version` via the command line. If not, you can download and install both through [RubyInstaller](http://rubyinstaller.org/downloads/), the preferred installer for Windows. Start by choosing a Ruby version 2.0+ which matches your either 32 or 64-bit machine, and running the downloaded installer. Most of the installation is simple to walk through, but when you are asked to confirm your installation location, check the boxes _"Add Ruby executables to your PATH"_ and _"Associate .rb and .rbw files with this installation"_. Then, to install Gems, return to RubyInstaller and download and install the appropriate DevKit. To setup RubyGems, change into the DevKit directory and on the command line, enter the following commands:
```
ruby dk.rb init
ruby dk.rb install
```
The tool which does the heavy-lifting for image processing is ImageMagick. To install, download from the Windows binary release [here](http://www.imagemagick.org/script/binary-releases.php#windows). Installing from here automatically adds ImageMagick to your path. With Wraith's dependencies handled, install Wraith with `gem install wraith`. To confirm proper installation, make sure both imagemagick and wraith can be run as commmands, by typing `compare` and `wraith` into your terminal. If this fails, find the installation locations and make sure they are in your PATH.

### Setup
Start out by cloning the repository with `git clone https://github.com/saarthaks/PerceptualDiff`. You can delete the osx version as there are no cross dependencies. The first step in being able to run Wraith in Windows involves editing a few of its Ruby files. Find the base directory where the Wraith gem was installed and remove the following files:
* wraith-3.2.0\lib\wraith\compare_images.rb
* wraith-3.2.0\lib\wraith\thumbnails.rb

Then, replace them with the files `win-wraith-3.2.0\compare_images.rb` and `win-wraith-3.2.0\thumbnails.rb`. Originally, wraith depends on parallel processing via Process.fork() and Process.spawn(), which are not available operations in a Windows environment. With the updated files, I've reverted to running the image comparison and editing sequentially, and has minimal impact on the runtime of the script. 

Next, setup the base directories in wraithpath.py by editing the following lines at the top of wraith/bin/wraithpath.py: 
```
...
ROOT_DIR = ''     # change to base directory for wraith folder, e.g., C:\Users\saart\PerceptualDiff\win_pdiff\wraith
SIKULI_DIR = os.path.join('C:\\','path','to','Sikuli_X')   # change to base directory for SikuliX folder, e.g., C:\Users\saart\SikuliX
...
```
Then, for the following python files
 * wraith\bin\clean_folders.py
 * wraith\wraith_tester.py
 * tests.sikuli\tests.py

change the following line at the top of the file:
```
...
sys.path.append('C:/Absolute/path/to/wraith//bin')
...
```
Finally, move tests.sikuli into the base directory for SikuliX, for example via 
```
$ cd ..\win_pdiff
$ mv tests.sikuli C:\Users\saart\SikuliX\tests.sikuli
```

## How to use
The main script to run the perceptual diff is wraith/wraith_tester.py. This script runs the Sikuli test files starting with the account setup, running the tests and capturing screenshots, and tearing down the account. It then goes on to creating a config file as wraith/configs/test.yaml, which defines where the screenshots are stored and the parameters for the image comparison. It finishes off by generating and returning HTML document with the visual result of the test, and, crucially, prints warnings if any image fails. This script is run as follows:
```
$ cd wraith
$ python wraith_tester.py
```
**Note:** Do not interfere with the mouse or keyboard during the execution of the Sikuli scripts, as this may cause the script to fail.

To run this script multiple times, it is imperative to clean out the wraith/shots directory between runs. To that end, I've included a utility script in wraith/bin, "clean_folders.py", which deletes the new screenshots and comparison results, leaving only the directory structure and the baseline images. To run this script, do the following:
```
$ cd wraith
$ python bin/clean_folders.py
```
##### Setting a (new) baseline
On the occasion when the baseline images are outdated and must be replaced, or when we are establishing our baseline for initial setup, we can use the same script, wraith_tester.py. Simply add the flag `-f` or `--force` like so:
```
$ cd wraith
$ python wraith_tester.py -f
```
In this operation, the script goes through the same Sikuli tests but names the screenshots "testXXXXXX_current.png" as opposed to "testXXXXXX_new.png". 
##### Debugging tools
A notable quirk of Wraith is during its image comparison, it requires a clean directory in its wraith/shots folder. It functions properly when each test folder within shots contains two pictures -- "testXXXXXX_current.png" and "testXXXXXX_new.png". This is a frequent source of error when consecutive pdiff scripts are run without cleaning the folders in between, resulting in mismatched comparisons and false failures. Indeed, this action can sometimes even currupt the baseline images.
The solution, fortunately, is simple. Start by cleaning out the folders with `python bin/clean_folders.py` and then reload new baseline images with `python wraith_tester.py -f`.
Other issues such as false positives are rare, but are easily debugged when viewed in the returned HTML file. Viewing the screenshots and their diffs can often help determine the cause.

## Acknowledgements
Thanks to the wonderful developers at MIT who developed SikuliX and at BBC-News who developed Wraith. This software depends heavily on their functionality and wouldn't be possible without their efforts.
