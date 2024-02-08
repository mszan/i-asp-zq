import click
from services.weather_service import WeatherService
import pandas as pd
import os


@click.command()
@click.option(
    '--input',
    '-i',
    required=True,
    type=click.File('rb'),
    help='Input CSV file. The file should contain at least two columns: date and parameter to forecast. The date should be in the format dd.mm.yyyy. The parameter to forecast should be a numerical value. The file should be separated by semicolon.'
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
    '--column-parameter',
    '-cfp',
    required=True,
    type=click.STRING,
    help='Name of the column in the input CSV file that contains the parameter to forecast. The parameter should be a numerical value.'
)
@click.option(
    '--column-date',
    '-cd',
    required=True,
    type=click.STRING,
    help='Name of the column in the input CSV file that contains the date of the data to forecast. The date should be in the format dd.mm.yyyy.'
)
@click.option(
    '--periods-in-days',
    '-pd',
    required=False,
    default=90,
    type=click.INT,
    help='Number of periods in days. Default is 90 days.'
)
@click.option(
    '--with-plot',
    '-wg',
    required=False,
    default=True,
    type=click.BOOL,
    help='Determinates whether to generate plot of predicted weather. The plot will be saved in the output directory as predicted_weather_[parameter].png. Default is True.'
)
@click.option(
    '--with-csv',
    '-wg',
    required=False,
    default=True,
    type=click.BOOL,
    help='Determinates whether to generate CSV of predicted weather. The CSV will be saved in the output directory as predicted_weather_[parameter].csv. Default is True.'
)
def predict(input, output, column_parameter, column_date, periods_in_days, with_plot, with_csv):
    """
    Predicts the weather for a specific location. Takes a CSV file as input and returns CSV file and graph as output.
    """

    weather_service = WeatherService()
    dfRaw = pd.read_csv(input, delimiter=';')
    df = weather_service.prepare_input_data(dfRaw, column_date, column_parameter)
    res = weather_service.predict_weather(df, periods_in_days, with_plot)

    if not os.path.exists(output):
        os.makedirs(output)

    if with_plot:
        res['plot_figure'].savefig(output + '/predicted_weather_' + column_parameter + '.png')

    if with_csv:
        res['forecast'].to_csv(output + '/predicted_weather_' + column_parameter + '.csv', index=False)

    click.echo(res)
