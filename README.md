# python-framework
This is a Selenium with Python framework to demonstrate I can work with Python (learning from scratch)

## Learn this before installation 📓

Unlike Java _pom.xml_ or Javascript _package.json_, in Python there is not a file in which we have the packages/libraries used by the proyect. However there is something called _Python Virtual Environment_ (venv) in which you can install the packages for each project in a _venv_ folder. For this project we are goig to place this folder inside the python-framework folder. 

## Installing this framework 💾
- Clone the project
### Installating Python
- Download and Install Python
- Under System Variables, edit "Path" and add the following entries
    - Python installation folder. Example: "C:\Python313"
    - WebDriver folder. Example: "C:\python-framework\drivers". Take into account this specific framework is only currently configured for MS Edge Browser so you might have to download and copy the latest `msedgedriver.exe` into the corresponding _drivers_ folder.
- Install _Python Virtual environment_.
    - Open a Power Shell (PS📟) and navigate inside python-framework folder
    - Execute `python -m venv venv`
### Installing Packages
⚠️ Before installing packages packages inside your _venv_ you need to Activate it first. In 📟 inside python-framework folder execute `.\venv\Scripts\activate`. To Deactivate your _venv_ (maybe to switch to another project), execute `.\venv\Scripts\activate`. Note: if you close the 📟 _venv_ will be deactivated.
- Installing Pytest
    - In PS📟, inside python-framework folder, execute `python -m pip install pytest`.
- Installing Selenium
    - In PS📟, inside python-framework folder, execute `python -m pip install selenium`.

## Running Tests 🏃
As we installed our packages in _venv_ to run the project we need to make sure _venv_ is active. For this, in 📟 inside python-framework folder execute `.\venv\Scripts\activate`. You should now see **_venv_** at the prompt like this _**(venv)** PS C:\Programming\python-framework_:

From the top-level folder of the project run `pytest`. As pytest works with auto-discovery for this to work the following must be true:
    - Files containing tests must start with test_
    - Funcitons containig tests must start with test_
    - Classes containing tests must start with Test

## Troubleshooting 🔧
- If `pip`is not recognized, install it using `python -m ensurepip --default-pip` and add the folder where the scripts were installed into PATH System Variables.