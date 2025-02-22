Work for Numerical Analysis

How to run the code:
Idea is to use a virtual environment to then install the dependencies then run python on the files.

windows: 
```
python -m venv .venv
source .venv/bin/Activate.ps1
pip install -r requirements.txt
python3 rootfinding.py
python3 tesla.py
```

mac:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 rootfinding.py
python3 tesla.py
```

NOTE: you can ignore creating a virtual environment if you don't want to, can just do pip install -r requirements.txt

BUT by doing so, these python packages will be on your computer globally.