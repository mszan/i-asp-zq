# weather-predict-cli

Simple weather prediction app.
Based on following example, in output folder, you will get csv file with achieved result and png file with graphical interpretation.

## Usage MAC

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

## Usage Windows CMD

1. Create and enable virtual environment.

```
python -m venv .venv
```
```
.venv\Scripts\activate
```


2. Setup CLI app.

```
pip install --editable .
```

3. Run the app.

```
weatherpredict --help
```

```
weatherpredict predict --help
```

```
weatherpredict predict --input=input.csv --output=./output --periods-in-days=360 --column-date=datetime --column-parameter=temp
```