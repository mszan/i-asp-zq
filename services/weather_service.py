from neuralprophet import NeuralProphet
import matplotlib.pyplot as plt
import pandas as pd


class WeatherService:
    def prepare_input_data(self, df, column_date, column_parameter):
        df = df[[column_date, column_parameter]]
        df.dropna(inplace=True)
        df[column_date] = pd.to_datetime(df[column_date], format='%d.%m.%Y')
        return df

    def predict_weather(self, df, periods_in_days, with_plot):
        parameter_to_forecast = df.columns[1]
        df.columns = ['ds', 'y']
        model = NeuralProphet(quantiles=[0.05, 0.95])
        model.fit(df)
        future = model.make_future_dataframe(df, periods=periods_in_days)
        forecast = model.predict(future)

        plot_figure = None
        if with_plot:
            model.plot(forecast)
            model.plot_components(forecast)
            model.plot_parameters()

            plot_figure = plt.figure(figsize=(10, 6))
            plt.plot(df['ds'], df['y'], label='Input data')
            plt.plot(forecast['ds'], forecast['yhat1'],
                     label='Predicted data', color='red')
            plt.xlabel('Date')
            plt.ylabel("Value")
            plt.title('Prediction of ' + parameter_to_forecast + ' parameter')
            plt.legend()

        return {
            'forecast': forecast,
            'plot_figure': plot_figure,
        }
