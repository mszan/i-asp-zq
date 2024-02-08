from neuralprophet import NeuralProphet

class WeatherService:
    def predict_weather(self, df, periodsInDays):
        df.dropna(inplace=True)
        df.columns = ['ds', 'y']
        model = NeuralProphet(quantiles=[0.05, 0.95])
        model.fit(df)
        future = model.make_future_dataframe(df, periods=periodsInDays)
        forecast = model.predict(future)
        return forecast
