# Time Series Forecasting with Prophet

## Project Overview
This project uses Facebook's Prophet library to forecast incoming volume based on historical data. It's designed to work with daily data stored in an Excel file, perform time series forecasting, and provide visualizations and performance metrics.

## Features
- Data import from Excel files
- Time series forecasting using Prophet
- Visualization of forecast and its components
- Cross-validation for model performance evaluation
- Performance metrics calculation (MAE, MAPE, MSE, RMSE)

## Requirements
- Python 3.7+
- pandas
- prophet
- matplotlib
- openpyxl

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/alvinamalindra/Time-Series-Forecasting-Prophet
   ```

2. Install the required packages:
   ```
   pip install pandas prophet matplotlib openpyxl
   ```

## Usage
1. Prepare your data in an Excel file with columns 'Date' and 'Volume'.
2. Update the `your_file.xlsx` and `Sheet1` in the script to match your Excel file name and sheet name.
3. Run the script:
   ```
   python time-series-forecast.py
   ```
4. The script will generate forecasts, display visualizations, and print performance metrics.

## Output
- Forecast plot
- Forecast components plot
- Cross-validation results plot
- Printed forecast for the next month
- Printed average forecasted volume
- Printed cross-validation performance metrics

## Customization
- Adjust the forecast period by changing the `periods` parameter in `model.make_future_dataframe()`.
- Modify cross-validation parameters in the `cross_validation()` function call.

## Contributing
Contributions, issues, and feature requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)


