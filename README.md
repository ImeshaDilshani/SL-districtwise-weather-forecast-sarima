# Sri Lanka District-wise Weather Forecasting using SARIMA

## 📈 Project Overview

This project implements a comprehensive time series analysis and forecasting system for weather data across different districts in Sri Lanka using Seasonal Autoregressive Integrated Moving Average (SARIMA) models. The system performs complete data preprocessing, exploratory data analysis (EDA), and generates accurate weather forecasts for temperature and rainfall patterns.

## 🎯 Objectives

- Analyze historical weather patterns across Sri Lankan districts
- Implement robust data preprocessing and quality assessment
- Perform comprehensive exploratory data analysis
- Build SARIMA models for temperature and rainfall forecasting
- Generate reliable forecasts with confidence intervals
- Evaluate model performance and residual diagnostics

## 📊 Dataset Description

The project uses two main datasets:

### 1. Weather Data (`weatherData.csv`)
- **Content**: Historical weather observations
- **Variables**: 
  - Date information
  - Temperature measurements (mean)
  - Precipitation/rainfall data (sum)
  - Humidity measurements
  - Wind speed data
  - Location identifiers

### 2. Location Data (`locationData.csv`)
- **Content**: District/city information
- **Variables**:
  - Location IDs
  - City/district names
  - Geographic identifiers

## 🏗️ Project Structure

```
SL-districtwise-weather-forecast-sarima/
├── 1.R                           # Main analysis script
├── weatherData.csv              # Historical weather data
├── locationData.csv             # Location reference data
├── Missing_Values_Pattern.png   # Missing data visualization
├── assignmnt 2.Rproj           # R project file
├── EDA_Plots/                  # Exploratory analysis plots
│   ├── {District}_Temperature_TimeSeries.png
│   ├── {District}_Rainfall_TimeSeries.png
│   ├── {District}_Temperature_Decomposition.png
│   ├── {District}_Rainfall_Decomposition.png
│   ├── {District}_ACF_PACF.png
│   ├── Correlation_Matrix.png
│   └── Monthly_Seasonal_Patterns.png
├── Forecast_Plots/             # SARIMA forecast visualizations
│   ├── {District}_Temp_Forecast.png
│   ├── {District}_Rain_Forecast.png
│   └── Ljung_Box_Test_Summary.csv
├── Forecast_Results/           # Forecast data outputs
│   └── {District}_Forecast.csv
└── Summary_Statistics/         # Statistical summaries
    ├── Descriptive_Statistics.csv
    ├── Time_Series_Characteristics.csv
    ├── Data_Quality_Report.txt
    └── SARIMA_Model_Summaries-2.txt
```

## 🔧 Installation and Setup

### Prerequisites
- R (version 4.0 or higher)
- RStudio (recommended)

### Required R Packages
```r
# Install pacman if not available
if (!require(pacman)) install.packages("pacman")

# Load all required packages
pacman::p_load(
  forecast,    # SARIMA modeling and forecasting
  tseries,     # Time series analysis tools
  ggplot2,     # Data visualization
  dplyr,       # Data manipulation
  lubridate,   # Date/time handling
  readr,       # Data import/export
  VIM,         # Missing value visualization
  mice,        # Multiple imputation
  corrplot,    # Correlation plots
  plotly,      # Interactive plots
  gridExtra,   # Grid layouts
  psych,       # Descriptive statistics
  zoo,         # Time series objects
  imputeTS,    # Time series imputation
  outliers,    # Outlier detection
  robustbase   # Robust statistical methods
)
```

### Installation Steps
1. Clone or download the project repository
2. Open `assignmnt 2.Rproj` in RStudio
3. Install required packages using the code above
4. Ensure `weatherData.csv` and `locationData.csv` are in the project directory
5. Run `1.R` script

## 🚀 Usage

### Running the Analysis
```r
# Open R/RStudio and navigate to project directory
# Run the main script
source("1.R")
```

The script will automatically:
1. Load and inspect the data
2. Perform data preprocessing and cleaning
3. Generate exploratory data analysis plots
4. Fit SARIMA models for each district
5. Create forecasts and save results
6. Generate comprehensive reports

### Key Functions

#### Data Preprocessing
- **Missing Value Imputation**: Spline interpolation for time series data
- **Outlier Treatment**: IQR method with capping at 1st and 99th percentiles
- **Data Aggregation**: Monthly aggregation from daily observations
- **Date Processing**: Comprehensive date feature engineering

#### Time Series Analysis
- **Stationarity Testing**: Augmented Dickey-Fuller, Phillips-Perron, and KPSS tests
- **Seasonal Decomposition**: STL decomposition for trend and seasonal components
- **Autocorrelation Analysis**: ACF and PACF plots for model identification

#### SARIMA Modeling
- **Automatic Model Selection**: Uses `auto.arima()` for optimal parameter selection
- **Seasonal Modeling**: Accounts for monthly seasonal patterns
- **Forecast Generation**: 48-month ahead forecasts with confidence intervals

## 📈 Key Features

### 1. Comprehensive Data Preprocessing
- Automatic encoding issue resolution
- Robust missing value treatment
- Outlier detection and handling
- Time series-specific imputation methods

### 2. Advanced Exploratory Data Analysis
- District-wise time series visualization
- Seasonal decomposition analysis
- Autocorrelation function analysis
- Cross-variable correlation analysis
- Monthly seasonal pattern identification

### 3. Robust SARIMA Modeling
- Automatic parameter selection
- Seasonal component modeling
- Model diagnostics and validation
- Residual analysis with Ljung-Box tests

### 4. Comprehensive Output Generation
- High-quality visualization plots
- Detailed statistical summaries
- Model performance metrics
- Forecast data with confidence intervals

## 📊 Output Interpretation

### Generated Plots
1. **Time Series Plots**: Historical trends for temperature and rainfall
2. **Decomposition Plots**: Trend, seasonal, and residual components
3. **ACF/PACF Plots**: Autocorrelation patterns for model identification
4. **Forecast Plots**: Future predictions with confidence bands
5. **Correlation Matrix**: Relationships between weather variables

### Statistical Reports
1. **Descriptive Statistics**: Summary statistics for all variables
2. **Time Series Characteristics**: Stationarity test results and basic statistics
3. **Data Quality Report**: Missing values, outliers, and data issues
4. **Model Summaries**: SARIMA model parameters and diagnostics

### Forecast Files
- CSV files containing 24-month forecasts for each district
- Includes point forecasts and 80% confidence intervals
- Separate predictions for temperature and rainfall

## 🔍 Model Validation

### Diagnostic Tests
- **Ljung-Box Test**: Tests for autocorrelation in residuals
- **Residual Analysis**: Visual inspection of model residuals
- **Forecast Accuracy**: Out-of-sample validation metrics

### Performance Metrics
- **AIC/BIC**: Model selection criteria
- **RMSE**: Root Mean Square Error
- **MAE**: Mean Absolute Error
- **MAPE**: Mean Absolute Percentage Error

## 📋 Results Summary

The analysis generates forecasts for multiple Sri Lankan districts including:
- Ampara, Anuradhapura, Badulla, Bandarawela
- Batticaloa, Colombo, Galle, Gampaha
- Hambantota, Jaffna, Kalutara, and others

Each district receives:
- 48-month temperature and rainfall forecasts
- Confidence intervals for uncertainty quantification
- Model diagnostic reports
- Visual forecast presentations

## 🔬 Technical Details

### SARIMA Model Specification
- **Seasonal Differencing**: Applied when necessary
- **Frequency**: Monthly data (frequency = 12)
- **Parameter Selection**: Stepwise = FALSE, Approximation = FALSE for accuracy
- **Seasonal Patterns**: Automatically detected and modeled

### Data Quality Assurance
- Minimum 36 observations required per district
- Automatic handling of insufficient data scenarios
- Robust imputation methods for missing values
- Systematic outlier detection and treatment

## 📝 Citation and References

If you use this project for academic purposes, please cite:

```
Sri Lanka District-wise Weather Forecasting using SARIMA Models
Time Series Analysis for Data Science Project
[Your Institution], [Year]
```

### Key References
- Hyndman, R.J., & Athanasopoulos, G. (2021). Forecasting: principles and practice
- Box, G.E.P., Jenkins, G.M., Reinsel, G.C., & Ljung, G.M. (2015). Time Series Analysis: Forecasting and Control

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is created for academic purposes as part of the Time Series Analysis for Data Science course.

## 📞 Contact

For questions or support regarding this project, please contact:
- Course: DSCI 44052 - Time Series Analysis for Data Science
- Institution: University of Kelaniya

---

**Note**: This project demonstrates advanced time series analysis techniques and serves as a comprehensive template for weather forecasting applications in tropical climates.
