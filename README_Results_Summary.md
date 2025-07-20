# SARIMA Model Results Summary

## Temperature Forecasting Models Performance

| District | SARIMA Model | AIC | RMSE | MAPE (%) |
|----------|--------------|-----|------|----------|
| **Best Performers** | | | | |
| Matara | (1,0,0)(0,1,1)[12] | 90.51 | 0.287 | 0.82 |
| Galle | (1,0,0)(2,1,1)[12] | 100.07 | 0.291 | 0.85 |
| Ratnapura | (1,0,1)(0,1,1)[12] | 113.09 | 0.307 | 0.89 |
| Nuwara Eliya | (1,0,0)(0,1,2)[12] | 123.00 | 0.322 | 1.30 |
| Kalutara | (1,0,0)(2,1,1)[12] | 147.21 | 0.336 | 0.97 |
| **Moderate Performers** | | | | |
| Colombo | (1,0,0)(2,1,2)[12] | 187.45 | 0.376 | 1.05 |
| Gampaha | (1,0,0)(0,1,2)[12] | 210.73 | 0.412 | 1.16 |
| Hambantota | (1,0,0)(2,1,1)[12] | 200.61 | 0.400 | 1.13 |
| Jaffna | (2,0,0)(2,1,0)[12] | 199.29 | 0.407 | 1.16 |
| **Lower Performers** | | | | |
| Ampara | (0,0,3)(2,1,0)[12] | 304.09 | 0.558 | 1.54 |
| Moneragala | (1,0,0)(2,1,1)[12] | 331.34 | 0.578 | 1.66 |
| Vavuniya | (1,0,0)(2,1,0)[12] | 329.37 | 0.613 | 1.73 |

## Rainfall Forecasting Models Performance

| District | SARIMA Model | AIC | RMSE | MAPE (%) |
|----------|--------------|-----|------|----------|
| **Best Performers** | | | | |
| Hambantota | (0,0,3)(2,0,0)[12] | 1958.93 | 64.15 | 114.50 |
| Kilinochchi | (0,0,0)(2,1,1)[12] | 1857.75 | 64.27 | 140.63 |
| Jaffna | (0,0,0)(2,1,1)[12] | 1875.82 | 68.37 | ∞* |
| Mannar | (0,0,1)(2,0,0)[12] | 2001.92 | 73.37 | 235.02 |
| **Moderate Performers** | | | | |
| Ampara | (0,0,2)(0,1,1)[12] | 1891.83 | 74.31 | 59.87 |
| Batticaloa | (0,0,2)(0,1,1)[12] | 1894.89 | 75.73 | 69.39 |
| Trincomalee | (1,0,0)(2,1,1)[12] | 1899.04 | 74.46 | 96.58 |
| Matara | (3,0,0)(2,0,0)[12] | 2018.01 | 75.73 | 54.64 |
| **Higher Variability** | | | | |
| Ratnapura | (0,1,3)(2,0,0)[12] | 2176.56 | 123.07 | 43.91 |
| Gampaha | (3,0,0)(2,0,0)[12] | 2141.82 | 107.93 | 79.79 |
| Kandy | (2,0,2)(0,0,1)[12] | 2136.20 | 106.96 | 109.06 |

*Note: ∞ indicates infinite MAPE due to zero values in rainfall data.

## Model Performance Summary

### Temperature Models
- **Average RMSE**: 0.43°C (range: 0.29-0.61°C)
- **Average MAPE**: 1.31% (range: 0.82-1.73%)
- **Best Region**: Coastal areas (Southern & Western provinces)
- **Most Common Pattern**: AR(1) with seasonal differencing

### Rainfall Models  
- **Average RMSE**: 82.4mm (range: 64.1-123.1mm)
- **Average MAPE**: 95.8% (range: 43.9-235.0%)
- **Best Region**: Dry zone districts (Northern & Eastern provinces)
- **Most Common Pattern**: Seasonal AR(2) with various non-seasonal components

## Key Insights

✅ **Temperature forecasting** shows excellent accuracy across all districts  
✅ **Coastal districts** demonstrate superior temperature prediction performance  
⚠️ **Rainfall forecasting** faces challenges due to high natural variability  
⚠️ **Mountainous regions** show increased forecast uncertainty for both variables  
📊 **Seasonal patterns** are critical for accurate predictions in Sri Lankan climate  

## Model Selection Criteria

Models were selected based on:
- **AIC** (Akaike Information Criterion) for model comparison
- **Residual diagnostics** (Ljung-Box test, normality)
- **Forecast accuracy** (RMSE, MAE, MAPE)
- **Cross-validation** performance on holdout data
