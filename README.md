<p id="p7">
<h3>Contents:</h3>
<a href="#p1">Overview</a></br>
<br><a href="#p2">Terminal Run Commands</a></br>

<p id="p1">
<h3>Overview:</h3>
<br>The project goal is to create a library of useful methods to imitate most common actions on web-page for UI testing. </br>
<br>Chromedriver is added in the project files</br>
<br>The sets of input data, including test URL's, are stored in test_data.py</br>
<br>Browser fixture is in conftest.py</br></p>

<p id="p2"><h3>Terminal Run Commands:</h3>

Create virtual environment:
>python -m venv venv

Activate the virtual environment scripts:
>venv\scripts\activate

Install requirements:
>pip install requirements.txt -r

To launch webstore testing in scandi_tests.py:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/scandi_tests.py

To launch webstore testing in scandi_tests.py with allure reports:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/scandi_tests.py --alluredir=allureres

Generate allure reports summary:
>allure serve allureres

To launch miscellaneous tests to demonstrate some BasePage methods in misc_tests.py:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/misc_tests.py

<a href="#p7">Back to top</a>