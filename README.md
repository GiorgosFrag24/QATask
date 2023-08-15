# QATaskForMoroTech
The aim of this project is the creation of a mobile application testing framework 
using Appium with Python, along with PyTest. 

# Set up instructions
Make sure you have Python 3.11 installed in your system .

Create a virtual environment and install the dependencies listed on requirements.txt,
using 'pip install -r requirements.txt'

Install Appium using 'npm i --location=global appium'

Install UIautomator2 driver using 'appium driver install uiautomator2'

Make sure that 'Developer Options' are enabled in your Android device.

Enable the following options on 'Developer Options' :
  
 1. Install via USB
  
 2. USB debugging (Security Settings)
  
 3. Disable adb authorization timeout

If you would like to run the tests on an emulated device, follow the instructions listed on
https://appium.io/docs/en/2.0/quickstart/uiauto2-driver

# Running tests instructions

Start the Appium server by typing 'appium' in the command line.

To run the tests, simply type 'pytest' in the terminal.

To generate an html report at the end of the test run, type 'pytest --html=report.html'

The logs generated during the test run, are exported to pytest_logs.logs

The configuration settings regarding pytest and its logging behaviour are included in the 'pytest.ini' file

