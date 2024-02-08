import click
from services.weather_service import WeatherService
import pandas as pd

@click.command()
@click.option(
    '--input',
    '-i',
    required=True,
    type=click.File('rb'),
    help='Input CSV file.'
)
@click.option(
    '--output',
    '-o',
    required=True,
    type=click.Path(
        exists=False,
        file_okay=False,
        dir_okay=True,
        readable=True
    ),
    help='Output directory.'
)
@click.option(
    '--with-graphs',
    '-wg',
    required=False,
    default=True,
    type=click.BOOL,
    help='Determinates whether to generate graphs.'
)
@click.option(
    '--periods-in-days',
    '-pd',
    required=False,
    default=90,
    type=click.INT,
    help='Number of periods in days.'
)
def predict(input, output, with_graphs, periods_in_days):
    """
    Predicts the weather for a specific location. Takes a CSV file as input and returns CSV file and graph (if --with-graph is set to True) as output.
    """
    
    df = pd.read_csv(input, delimiter=';')
    df['datetime'] = pd.to_datetime(df['datetime'],format='%d.%m.%Y')
    df = df[['datetime', 'temp']]
    df.dropna(inplace=True)

    weather_service = WeatherService()
    res = weather_service.predict_weather(df, periods_in_days)

    click.echo(res)
