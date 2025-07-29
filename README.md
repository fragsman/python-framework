# python-framework
This is a Selenium with Python framework to demonstrate I can work with Python (learning from scratch)

## Learn this before installation 📓

Unlike Java _pom.xml_ or Javascript _package.json_, in Pytoh there is not a file in which we have the packages/libraries used by the proyect. It is important that we careful follow the installation instructions as we will have to install all the libraries. Actual libraries will be installed in your Python installation folder. Note: You might find libraries installed in a user-installation folder in Users/JohnDoe/AppData/Roaming/Python instead of the main Python folder.

## Installing this framework 💾
- Clone the project
- Download and Install Python
- Under System Variables, edit "Path" and add the following entries
    - Python installation folder. Example: "C:\Python313"
    - Python Scripts folder. Example: :\Python313\scripts"
    - WebDriver folder. Example: "C:\python-framework\drivers"
    - Take into account this specific framework is only currently configured for MS Edge Browser so you might have to download and copy the latest `msedgedriver.exe` into the corresponding _drivers_ folder.
- Install Selenium with `pip install selenium`. If `pip`is not recognized, install it using `python -m ensurepip --default-pip` and add the folder where the scripts were installed into PATH System Variables

