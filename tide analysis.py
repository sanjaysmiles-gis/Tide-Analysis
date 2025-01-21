import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_and_analyze_tide_data(file_path):
    predicted_data = pd.read_csv(file_path)
    observed_tide = predicted_data['tide_height_m']
    valid_data = predicted_data.dropna(subset=['tide_height_m', 'tidal_prediction_utide', 'combined_prediction_savgol'])
    analysis_results = calculate_statistics(valid_data, observed_tide)
    create_tide_plots(predicted_data)
    display_statistics_table(analysis_results)
    return analysis_results

def calculate_statistics(valid_data, observed_tide):
    mean_tide_height = observed_tide.mean()
    rms_tide_height = np.sqrt(np.mean(observed_tide.dropna() ** 2))
    correlation_utide = valid_data['tide_height_m'].corr(valid_data['tidal_prediction_utide'])
    rmse_utide = np.sqrt(np.mean((valid_data['tide_height_m'] - valid_data['tidal_prediction_utide']) ** 2))
    mae_utide = np.mean(np.abs(valid_data['tide_height_m'] - valid_data['tidal_prediction_utide']))
    rmse_combined_savgol = np.sqrt(np.mean((valid_data['tide_height_m'] - valid_data['combined_prediction_savgol']) ** 2))
    mae_combined_savgol = np.mean(np.abs(valid_data['tide_height_m'] - valid_data['combined_prediction_savgol']))
    t_value = 1.96
    std_error = observed_tide.std() / np.sqrt(observed_tide.count())
    confidence_interval = (mean_tide_height - t_value * std_error, mean_tide_height + t_value * std_error)
    return {
        "Mean Tide Height (m)": mean_tide_height,
        "RMS Tide Height (m)": rms_tide_height,
        "Correlation (Observed vs UTide)": correlation_utide,
        "RMSE (UTide Predictions)": rmse_utide,
        "MAE (UTide Predictions)": mae_utide,
        "RMSE (Combined Predictions, Savitzky-Golay)": rmse_combined_savgol,
        "MAE (Combined Predictions, Savitzky-Golay)": mae_combined_savgol,
        "Confidence Interval (Observed Tide Height, 95%)": confidence_interval,
    }

def create_tide_plots(predicted_data):
    predicted_data['datetime'] = pd.to_datetime(predicted_data['Unnamed: 0'])
    
    plt.figure(figsize=(10, 6))
    plt.plot(predicted_data['datetime'], predicted_data['tide_height_m'], color='black', linewidth=1)
    plt.title('Observed Tide Height')
    plt.xlabel('Datetime')
    plt.ylabel('Tide Height (m)')
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.plot(predicted_data['datetime'], predicted_data['tidal_prediction_utide'], color='blue', linewidth=1)
    plt.title('UTide Prediction')
    plt.xlabel('Datetime')
    plt.ylabel('Tide Height (m)')
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.plot(predicted_data['datetime'], predicted_data['combined_prediction_savgol'], color='green', linewidth=1)
    plt.title('Combined Prediction (Savgol)')
    plt.xlabel('Datetime')
    plt.ylabel('Tide Height (m)')
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.scatter(predicted_data['tide_height_m'], predicted_data['tidal_prediction_utide'], alpha=0.3, color='blue', s=10)
    plt.plot([predicted_data['tide_height_m'].min(), predicted_data['tide_height_m'].max()],
             [predicted_data['tide_height_m'].min(), predicted_data['tide_height_m'].max()], 'r--')
    plt.title('UTide Predictions vs Observed')
    plt.xlabel('Observed Tide Height (m)')
    plt.ylabel('UTide Prediction (m)')
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.scatter(predicted_data['tide_height_m'], predicted_data['combined_prediction_savgol'], alpha=0.3, color='green', s=10)
    plt.plot([predicted_data['tide_height_m'].min(), predicted_data['tide_height_m'].max()],
             [predicted_data['tide_height_m'].min(), predicted_data['tide_height_m'].max()], 'r--')
    plt.title('Combined Predictions (Savgol) vs Observed')
    plt.xlabel('Observed Tide Height (m)')
    plt.ylabel('Combined Prediction (m)')
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    errors_utide = predicted_data['tide_height_m'] - predicted_data['tidal_prediction_utide']
    errors_combined = predicted_data['tide_height_m'] - predicted_data['combined_prediction_savgol']
    plt.hist(errors_utide.dropna(), bins=50, alpha=0.5, label='UTide Errors', color='blue')
    plt.hist(errors_combined.dropna(), bins=50, alpha=0.5, label='Combined Errors', color='green')
    plt.title('Error Distribution')
    plt.xlabel('Error (m)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

def display_statistics_table(results):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('off')
    table_data = [
        ['Metric', 'UTide Model', 'Combined Model (Savgol)'],
        ['RMSE', f"{results['RMSE (UTide Predictions)']:.4f}", 
         f"{results['RMSE (Combined Predictions, Savitzky-Golay)']:.4f}"],
        ['MAE', f"{results['MAE (UTide Predictions)']:.4f}", 
         f"{results['MAE (Combined Predictions, Savitzky-Golay)']:.4f}"]
    ]
    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.5)
    plt.title('Model Performance Metrics', pad=20, fontsize=14)
    plt.show()

if _name_ == "_main_":
    file_path = "predicted_data_combined_ml_savgol.csv"
    results = load_and_analyze_tide_data(file_path)