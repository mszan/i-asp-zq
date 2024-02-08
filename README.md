# weather-predict-cli

Simple weather prediction app.

## Usage

1. Create and enable virtual environment.

```
$ python3 -m venv .venv
```

```
$ source .venv/bin/activate
```

2. Setup CLI app.

```
(.venv) $ pip install --editable .
```

3. Run the app.

```
(.venv) $ weatherpredict --help
```

```
(.venv) $ weatherpredict predict --help
```

```
(.venv) $ weatherpredict predict --input=input.csv --output=./output --periods-in-days=360 --column-date=datetime --column-parameter=temp
```
