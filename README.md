# The Converter App
A Simple Measurement Unit Converter built on Django

# Setup
1. Clone this repo in your projects folder.

```
git clone git@github.com:lewisemm/converter.git
```

2. Create a virtual environment and install the dependencies.

```
# create and activate the virtual env
virtualenv -p python3.7 env
source env/bin/activate

# install dependencies
pip install -r requirements.txt
```
3. Run the tests to ensure everything is in working order.

```
python manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.022s

OK
Destroying test database for alias 'default'...
```

4. Access the length measurement converter via [http://127.0.0.1:8000/length/convert](http://127.0.0.1:8000/length/convert)
