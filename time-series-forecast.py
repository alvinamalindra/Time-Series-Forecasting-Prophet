import pandas as pd
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import matplotlib.pyplot as plt

# Read data from Excel file
# Replace 'your_file.xlsx' with the actual name of your Excel file
# Replace 'Sheet1' with the name of the sheet containing your data
df = pd.read_excel('your_file.xlsx', sheet_name='Sheet1')

# Ensure the date column is named 'ds' and the volume column is named 'y'
df = df.rename(columns={'Date': 'ds', 'Volume': 'y'})

# Convert date to datetime format if it's not already
df['ds'] = pd.to_datetime(df['ds'])

# Create and fit the model
model = Prophet()
model.fit(df)

# Create future dates for forecasting
future_dates = model.make_future_dataframe(periods=30)  # 30 days into September

# Make predictions
forecast = model.predict(future_dates)

# Plot the forecast
fig1 = model.plot(forecast)
plt.title('Incoming Volume Forecast')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

# Plot the components of the forecast
fig2 = model.plot_components(forecast)
plt.show()

# Print the forecast for September
september_forecast = forecast[forecast['ds'].dt.month == 9][['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
print("September Forecast:")
print(september_forecast)

# Calculate and print average forecasted volume for September
september_avg = september_forecast['yhat'].mean()
print(f"\nAverage forecasted volume for September: {september_avg:.2f}")

# Perform cross-validation
cv_results = cross_validation(model, initial='180 days', period='30 days', horizon='30 days')

# Calculate performance metrics
cv_metrics = performance_metrics(cv_results)

# Print performance metrics
print("\nCross-Validation Performance Metrics:")
print(cv_metrics[['horizon', 'mae', 'mape', 'mse', 'rmse']])

# Plot the cross-validation results
fig3 = plt.figure(figsize=(10, 6))
plt.plot(cv_results['ds'], cv_results['y'], 'b.', alpha=0.5, label='Actual')
plt.plot(cv_results['ds'], cv_results['yhat'], 'r-', label='Predicted')
plt.fill_between(cv_results['ds'], cv_results['yhat_lower'], cv_results['yhat_upper'], color='r', alpha=0.1)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Cross-Validation Results')
plt.legend()
plt.show()
