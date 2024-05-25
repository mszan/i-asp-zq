from neuralprophet import NeuralProphet
import matplotlib.pyplot as plt
import pandas as pd


class WeatherService:
    def prepare_input_data(self, df, column_date, column_parameter):
        """
        Prepares input data for weather prediction by selecting specific columns,
        dropping missing values, and converting date column to datetime format.

        Parameters:
        df (pd.DataFrame): Input dataframe containing weather data.
        column_date (str): Name of the date column in the dataframe.
        column_parameter (str): Name of the weather parameter column in the dataframe.

        Returns:
        pd.DataFrame: Processed dataframe with date and parameter columns.
        """

        # Select only the specified date and parameter columns
        df = df[[column_date, column_parameter]]

        # Remove rows with missing values
        df.dropna(inplace=True)

        # Convert date column to datetime format
        df[column_date] = pd.to_datetime(df[column_date], format='%d.%m.%Y')

        return df

    def predict_weather(self, df, periods_in_days, with_plot):
        """
        Predicts future weather parameters using the NeuralProphet model.

        Parameters:
        df (pd.DataFrame): Input dataframe with date and parameter columns.
        periods_in_days (int): Number of future periods (days) to predict.
        with_plot (bool): Flag to indicate whether to plot the results.

        Returns:
        dict: Dictionary containing the forecast and plot figure (if generated).
        """

        # Identify the parameter to forecast (assumed to be the second column)
        parameter_to_forecast = df.columns[1]

        # Rename columns for compatibility with NeuralProphet
        df.columns = ['ds', 'y']

        # Initialize NeuralProphet model with specified quantiles
        model = NeuralProphet(quantiles=[0.05, 0.95])

        # Fit the model to the data
        model.fit(df)

        # Create future dataframe for the specified number of periods
        future = model.make_future_dataframe(df, periods=periods_in_days)

        # Generate the forecast
        forecast = model.predict(future)

        plot_figure = None
        if with_plot:
            # Plot forecast components and parameters using NeuralProphet built-in methods
            model.plot(forecast)
            model.plot_components(forecast)
            model.plot_parameters()

            # Create a custom plot to visualize the input data and predictions
            plot_figure = plt.figure(figsize=(10, 6))
            plt.plot(df['ds'], df['y'], label='Input data')
            plt.plot(forecast['ds'], forecast['yhat1'], label='Predicted data', color='red')
            plt.xlabel('Date')
            plt.ylabel("Value")
            plt.title('Prediction of ' + parameter_to_forecast + ' parameter')
            plt.legend()

        # Return the forecast and plot figure in a dictionary
        return {
            'forecast': forecast,
            'plot_figure': plot_figure,
        }
