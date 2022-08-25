# Python selenium framework skeleton

## Requirements
1. python3.7
2. pip | pip3
3. latest chrome browser

## Installation
`pip install -r requirements.txt` in project main folder

## Running tests
1. From Pycharm by running .feature file
2. From command line by running `behave --no-capture` command from project main folder

## Running available robot
1. python3 lib/robot.py
## Changing browser to Firefox (or any other)
Change in file `./features/environment.py` lines

```python
path = driver.install(browser=driver.chrome)
context.behave_driver = behave_webdriver.Chrome(path)
```

to 

```python
path = driver.install(browser=driver.firefox)
context.behave_driver = behave_webdriver.Firefox(path)
```

# MAC SET UP
Install Pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py

pip install autogui