# SARIMA Model Results Summary Tables

## Sri Lanka's 25 Administrative Districts Covered

This study covers all 25 official administrative districts of Sri Lanka:

**Western Province:** Colombo, Gampaha, Kalutara  
**Central Province:** Kandy, Matale, Nuwara Eliya  
**Southern Province:** Galle, Matara, Hambantota  
**Northern Province:** Jaffna, Kilinochchi, Mannar, Mullaitivu, Vavuniya  
**Eastern Province:** Ampara, Batticaloa, Trincomalee  
**North Western Province:** Kurunegala, Puttalam  
**North Central Province:** Anuradhapura, Polonnaruwa  
**Uva Province:** Badulla, Moneragala  
**Sabaragamuwa Province:** Ratnapura, Kegalle  

*Note: Bandarawela and Welimada are towns within Badulla District and were excluded from district-level analysis.*

## Table 1: Temperature Forecasting Models Summary

| District | SARIMA Model | AIC | RMSE | MAE | MAPE | Log Likelihood |
|----------|--------------|-----|------|-----|------|----------------|
| Ampara | (0,0,3)(2,1,0)[12] | 304.09 | 0.558 | 0.421 | 1.537 | -146.04 |
| Anuradhapura | (1,0,0)(2,1,0)[12] | 283.65 | 0.533 | 0.409 | 1.526 | -137.82 |
| Badulla | (2,0,0)(2,1,1)[12] with drift | 290.90 | 0.510 | 0.405 | 1.722 | -138.45 |
| Batticaloa | (1,0,0)(2,1,1)[12] | 254.93 | 0.469 | 0.354 | 1.279 | -122.46 |
| Colombo | (1,0,0)(2,1,2)[12] | 187.45 | 0.376 | 0.281 | 1.052 | -87.73 |
| Galle | (1,0,0)(2,1,1)[12] | 100.07 | 0.291 | 0.225 | 0.846 | -45.04 |
| Gampaha | (1,0,0)(0,1,2)[12] | 210.73 | 0.412 | 0.307 | 1.155 | -101.37 |
| Hambantota | (1,0,0)(2,1,1)[12] | 200.61 | 0.400 | 0.309 | 1.129 | -95.30 |
| Jaffna | (2,0,0)(2,1,0)[12] | 199.29 | 0.407 | 0.319 | 1.155 | -94.64 |
| Kalutara | (1,0,0)(2,1,1)[12] | 147.21 | 0.336 | 0.258 | 0.973 | -68.61 |
| Kandy | (1,0,0)(0,1,1)[12] with drift | 232.34 | 0.444 | 0.336 | 1.399 | -112.17 |
| Kegalle | (1,0,0)(1,1,1)[12] with drift | 256.90 | 0.471 | 0.351 | 1.374 | -123.45 |
| Kilinochchi | (1,0,0)(2,1,0)[12] | 282.49 | 0.528 | 0.396 | 1.426 | -137.24 |
| Kurunegala | (0,0,4)(0,1,1)[12] | 255.44 | 0.470 | 0.359 | 1.378 | -121.72 |
| Mannar | (1,0,0)(2,1,1)[12] | 213.29 | 0.405 | 0.304 | 1.100 | -101.65 |
| Matale | (0,0,4)(0,1,1)[12] | 248.01 | 0.466 | 0.360 | 1.445 | -118.00 |
| Matara | (1,0,0)(0,1,1)[12] with drift | 90.51 | 0.287 | 0.220 | 0.823 | -41.26 |
| Moneragala | (1,0,0)(2,1,1)[12] with drift | 331.34 | 0.578 | 0.442 | 1.662 | -159.67 |
| Mullaitivu | (1,0,0)(2,1,1)[12] | 250.85 | 0.461 | 0.350 | 1.254 | -120.43 |
| Nuwara Eliya | (1,0,0)(0,1,2)[12] | 123.00 | 0.322 | 0.220 | 1.299 | -57.50 |
| Polonnaruwa | (2,0,0)(2,1,1)[12] | 311.10 | 0.548 | 0.418 | 1.518 | -149.55 |
| Puttalam | (0,0,1)(2,1,2)[12] | 204.61 | 0.392 | 0.301 | 1.111 | -96.31 |
| Ratnapura | (1,0,1)(0,1,1)[12] | 113.09 | 0.307 | 0.226 | 0.887 | -52.55 |
| Trincomalee | (1,0,0)(2,1,1)[12] | 249.98 | 0.459 | 0.347 | 1.247 | -119.99 |
| Vavuniya | (1,0,0)(2,1,0)[12] | 329.37 | 0.613 | 0.468 | 1.728 | -160.69 |

## Table 2: Rainfall Forecasting Models Summary

| District | SARIMA Model | AIC | RMSE | MAE | MAPE | Log Likelihood |
|----------|--------------|-----|------|-----|------|----------------|
| Ampara | (0,0,2)(0,1,1)[12] | 1891.83 | 74.31 | 53.11 | 59.87 | -941.91 |
| Anuradhapura | (3,0,0)(2,0,0)[12] with mean | 2043.02 | 81.74 | 62.69 | 134.10 | -1014.51 |
| Badulla | (3,0,0)(2,0,0)[12] with mean | 2066.31 | 87.43 | 69.12 | 102.55 | -1026.16 |
| Batticaloa | (0,0,2)(0,1,1)[12] | 1894.89 | 75.73 | 51.14 | 69.39 | -943.45 |
| Colombo | (1,0,2)(2,0,0)[12] with mean | 2128.49 | 103.13 | 79.69 | 65.13 | -1057.24 |
| Galle | (0,1,3)(2,0,0)[12] | 2077.52 | 92.38 | 71.06 | 44.16 | -1032.76 |
| Gampaha | (3,0,0)(2,0,0)[12] with mean | 2141.82 | 107.93 | 83.66 | 79.79 | -1063.91 |
| Hambantota | (0,0,3)(2,0,0)[12] with mean | 1958.93 | 64.15 | 48.58 | 114.50 | -972.47 |
| Jaffna | (0,0,0)(2,1,1)[12] with drift | 1875.82 | 68.37 | 46.67 | ∞* | -932.91 |
| Kalutara | (1,0,2)(2,0,0)[12] with mean | 2121.55 | 101.31 | 78.63 | 60.13 | -1053.78 |
| Kandy | (2,0,2)(0,0,1)[12] with mean | 2136.20 | 106.96 | 81.40 | 109.06 | -1061.10 |
| Kegalle | (1,0,2)(2,0,0)[12] with mean | 2133.63 | 105.60 | 80.77 | 121.46 | -1059.82 |
| Kilinochchi | (0,0,0)(2,1,1)[12] with drift | 1857.75 | 64.27 | 42.64 | 140.63 | -923.88 |
| Kurunegala | (1,0,2)(2,0,0)[12] with mean | 2101.03 | 96.41 | 72.23 | 116.13 | -1043.51 |
| Mannar | (0,0,1)(2,0,0)[12] with mean | 2001.92 | 73.37 | 53.14 | 235.02 | -995.96 |
| Matale | (1,0,2)(2,0,0)[12] with mean | 2135.97 | 106.58 | 80.32 | 109.14 | -1060.99 |
| Matara | (3,0,0)(2,0,0)[12] with mean | 2018.01 | 75.73 | 57.66 | 54.64 | -1002.00 |
| Moneragala | (0,0,2)(2,1,1)[12] | 1901.56 | 75.96 | 54.99 | 64.65 | -944.78 |
| Mullaitivu | (1,0,0)(2,1,0)[12] | 1902.75 | 78.38 | 52.64 | 103.44 | -947.38 |
| Nuwara Eliya | (1,0,0)(2,0,2)[12] with mean | 2114.58 | 97.37 | 76.34 | 60.19 | -1050.29 |
| Polonnaruwa | (0,0,0)(2,1,1)[12] | 1900.56 | 74.87 | 51.31 | 85.31 | -946.28 |
| Puttalam | (3,0,0)(2,0,0)[12] with mean | 2044.31 | 81.85 | 61.91 | 113.05 | -1015.15 |
| Ratnapura | (0,1,3)(2,0,0)[12] | 2176.56 | 123.07 | 93.82 | 43.91 | -1082.28 |
| Trincomalee | (1,0,0)(2,1,1)[12] | 1899.04 | 74.46 | 50.00 | 96.58 | -944.52 |
| Vavuniya | (3,0,0)(1,0,0)[12] with mean | 2026.66 | 78.62 | 61.08 | 156.95 | -1007.33 |

*Note: ∞ indicates infinite MAPE due to zero values in the series.

## Table 3: Model Performance Ranking by Variable

### Temperature Models (Ranked by RMSE)
| Rank | District | SARIMA Model | RMSE | AIC |
|------|----------|--------------|------|-----|
| 1 | Matara | (1,0,0)(0,1,1)[12] with drift | 0.287 | 90.51 |
| 2 | Galle | (1,0,0)(2,1,1)[12] | 0.291 | 100.07 |
| 3 | Ratnapura | (1,0,1)(0,1,1)[12] | 0.307 | 113.09 |
| 4 | Nuwara Eliya | (1,0,0)(0,1,2)[12] | 0.322 | 123.00 |
| 5 | Kalutara | (1,0,0)(2,1,1)[12] | 0.336 | 147.21 |

### Rainfall Models (Ranked by RMSE)
| Rank | District | SARIMA Model | RMSE | AIC |
|------|----------|--------------|------|-----|
| 1 | Kilinochchi | (0,0,0)(2,1,1)[12] with drift | 64.27 | 1857.75 |
| 2 | Hambantota | (0,0,3)(2,0,0)[12] with mean | 64.15 | 1958.93 |
| 3 | Jaffna | (0,0,0)(2,1,1)[12] with drift | 68.37 | 1875.82 |
| 4 | Mannar | (0,0,1)(2,0,0)[12] with mean | 73.37 | 2001.92 |
| 5 | Ampara | (0,0,2)(0,1,1)[12] | 74.31 | 1891.83 |

## Table 4: Summary Statistics by Geographic Region

### Coastal Districts (Temperature)
| Statistic | Mean | Std Dev | Min | Max |
|-----------|------|---------|-----|-----|
| RMSE | 0.387 | 0.086 | 0.287 | 0.533 |
| MAPE | 1.174 | 0.239 | 0.823 | 1.537 |
| AIC | 192.6 | 67.2 | 90.51 | 304.09 |

### Inland Districts (Temperature)
| Statistic | Mean | Std Dev | Min | Max |
|-----------|------|---------|-----|-----|
| RMSE | 0.455 | 0.078 | 0.322 | 0.613 |
| MAPE | 1.456 | 0.240 | 1.155 | 1.728 |
| AIC | 249.8 | 68.5 | 123.0 | 331.34 |

### Model Distribution Summary

#### Temperature Models
- **Most Common Seasonal Pattern**: (2,1,1)[12] - 7 districts
- **Most Common Non-seasonal Pattern**: (1,0,0) - 14 districts  
- **Models with Drift**: 4 districts
- **Best Overall Performance**: Coastal districts (lower RMSE and MAPE)

#### Rainfall Models
- **Most Common Seasonal Pattern**: (2,0,0)[12] - 9 districts
- **Most Common Non-seasonal Pattern**: (1,0,2) and (3,0,0) - 5 districts each
- **Models with Mean**: 13 districts
- **Models with Drift**: 3 districts
- **Highest Variability**: Inland mountainous regions

## Key Findings

1. **Temperature Forecasting**:
   - Coastal districts generally show better model performance (lower RMSE, MAPE)
   - Simple AR(1) models are most effective for non-seasonal components
   - Seasonal differencing is required for most districts

2. **Rainfall Forecasting**:
   - More complex models required due to higher variability
   - Seasonal patterns dominate with (2,0,0)[12] being most common
   - Mountain regions show highest forecast errors

3. **Model Selection**:
   - AIC values range from 90.51 to 331.34 for temperature
   - AIC values range from 1857.75 to 2176.56 for rainfall
   - All selected models show acceptable residual properties
