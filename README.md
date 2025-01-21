# Tide Analysis Project

This project provides a comprehensive analysis of tide data, comparing observed tide heights with predictions from UTide model and a combined model using Savitzky-Golay filtering.

## Features

- Load and analyze tide data from CSV files
- Calculate key statistical metrics:
  - Mean and RMS tide height
  - Correlation between observed and predicted tides
  - RMSE (Root Mean Square Error)
  - MAE (Mean Absolute Error)
  - 95% Confidence Intervals

- Generate visualization plots:
  - Time series plots of observed and predicted tides
  - Scatter plots comparing predictions vs observations
  - Error distribution histograms
  - Performance metrics table

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

## Usage

1. Place your tide data CSV file in the project directory
2. The CSV should contain the following columns:
   - datetime
   - tide_height_m (observed tide heights)
   - tidal_prediction_utide (UTide model predictions)
   - combined_prediction_savgol (Combined model predictions with Savitzky-Golay filtering)

3. Run the script:
```python
python "tide analysis.py"
```

## Code Structure

The code is organized into several main functions:

- `load_and_analyze_tide_data()`: Main function that orchestrates the analysis
- `calculate_statistics()`: Computes various statistical metrics
- `create_tide_plots()`: Generates visualization plots
- `display_statistics_table()`: Creates a summary table of model performance

## Output

The script generates multiple visualizations:
1. Time series plots of observed and predicted tides
2. Scatter plots comparing predictions with observations
3. Error distribution histograms
4. Performance metrics table comparing UTide and Combined models

## License

This project is open source and available under the MIT License.
