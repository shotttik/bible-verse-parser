# Instructions to run the project in Linux

### Install pip3
> python3 -m pip install --user --upgrade pip

### Installing virtualenv
> python3 -m pip install --user virtualenv

### Creating a virtual environment¶
> python3 -m venv env

### Activating a virtual environment¶
> source env/bin/activate

### Installing packages
> python3 -m pip install -r requirements.txt


`Resources/config.json`
```
{
    "browser": "chrome",
    "base_url": "https://bible.com/",
    "options": [
        "--incognito",
        "--start-maximized"
    ],
    "wait_time": 10
}
```
`Resrouces/data.json`
```
{
    "start_url": "https://www.bible.com/bible/1/GEN.1.KJV",
    "save_file": "./Resources/full_verse.json"
}
```


## RUN PROJECT
> python3 main.py


### Check the result in the Resources folder file named `full_verse.json`.


# ATTENTION:
### Make sure you have filled `data.json` and `config.json`