# KMA API Endpoint Reference

Complete reference of all KMA API endpoints with example URLs and parameters.

---

## Base URL Structure

All APIs use the same base URL pattern:
```
https://apihub.kma.go.kr/api/typ01/url/{endpoint}?authKey={YOUR_API_KEY}&{parameters}
```

**Note**: All examples below require `authKey` parameter which is automatically added by the client.

---

## Surface Observations (지표 관측)

### ASOS - Automated Synoptic Observing System (종관기상관측)

#### 1. Hourly Data - Single Time
**Endpoint**: `kma_sfctm2.php`
**Method**: `get_hourly_data(tm, stn=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?authKey=YOUR_KEY&tm=202501011200&stn=108&help=0
```
**Parameters**:
- `tm`: Time in YYYYMMDDHHmm format (e.g., 202501011200 = 2025-01-01 12:00)
- `stn`: Station number (0=all, 108=Seoul)
- `help`: Always 0

#### 2. Hourly Data - Period
**Endpoint**: `kma_sfctm3.php`
**Method**: `get_hourly_period(tm1, tm2, stn=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&stn=108&help=0
```
**Parameters**:
- `tm1`: Start time (YYYYMMDDHHmm)
- `tm2`: End time (YYYYMMDDHHmm, max 31 days from tm1)
- `stn`: Station number

#### 3. Daily Data - Single Day
**Endpoint**: `kma_sfcdd.php`
**Method**: `get_daily_data(tm, stn=0, disp=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd.php?authKey=YOUR_KEY&tm=20250101&stn=108&disp=0&help=0
```
**Parameters**:
- `tm`: Date in YYYYMMDD format
- `stn`: Station number
- `disp`: Display option (0=default)

#### 4. Daily Data - Period
**Endpoint**: `kma_sfcdd3.php`
**Method**: `get_daily_period(tm1, tm2, stn=0, obs='', mode=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd3.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=108&obs=&mode=0&help=0
```
**Parameters**:
- `tm1`: Start date (YYYYMMDD)
- `tm2`: End date (YYYYMMDD)
- `stn`: Station number
- `obs`: Observation element code (empty for all)
- `mode`: Mode option (0=default)

#### 5. Element-Specific Data
**Endpoint**: `kma_sfctm5.php`
**Method**: `get_element_data(tm1, tm2, obs, stn=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfctm5.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&obs=TA&stn=108&help=0
```
**Parameters**:
- `tm1`: Start time (YYYYMMDDHHmm)
- `tm2`: End time (YYYYMMDDHHmm)
- `obs`: Element code (TA=temperature, RN=precipitation, etc.)
- `stn`: Station number

---

### AWS - Automated Weather Station (방재기상관측)

#### 1. Minutely Data - Single Time
**Endpoint**: `kma_aws.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws.php?authKey=YOUR_KEY&tm=202501011200&stn=104&help=0
```

#### 2. Minutely Data - Period
**Endpoint**: `kma_aws2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws2.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501011300&stn=0&help=0
```

#### 3. Hourly Data - Single Time
**Endpoint**: `kma_aws3.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws3.php?authKey=YOUR_KEY&tm=202501011200&stn=0&help=0
```

#### 4. Hourly Data - Period
**Endpoint**: `kma_aws4.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws4.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501020000&stn=0&help=0
```

#### 5. Daily Data - Single Day
**Endpoint**: `kma_aws5.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws5.php?authKey=YOUR_KEY&tm=20250101&stn=0&help=0
```

#### 6. Daily Data - Period
**Endpoint**: `kma_aws6.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws6.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=0&help=0
```

---

### AWS OA - AWS Objective Analysis

#### 1. Analysis Data - Single Time
**Endpoint**: `kma_awsoa.php`
**Method**: `get_analysis_data(tm, x, y)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_awsoa.php?authKey=YOUR_KEY&tm=202501011200&x=127.0&y=37.5&help=0
```
**Parameters**:
- `x`: Longitude (e.g., 127.0 for Seoul)
- `y`: Latitude (e.g., 37.5 for Seoul)

#### 2. Analysis Data - Period
**Endpoint**: `kma_awsoa_2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_awsoa_2.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501011800&x=127.0&y=37.5&help=0
```

---

### Climate Statistics (기후평년값)

#### 1. Daily Normals
**Endpoint**: `kma_clm_daily.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_clm_daily.php?authKey=YOUR_KEY&stn=108&mm1=01&dd1=01&mm2=01&dd2=31&help=0
```
**Parameters**:
- `mm1`, `dd1`: Start month and day (MM, DD)
- `mm2`, `dd2`: End month and day

#### 2. Ten-Day Normals (Dekad)
**Endpoint**: `kma_clm_tenday.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_clm_tenday.php?authKey=YOUR_KEY&stn=108&mm1=01&dd1=1&mm2=01&dd2=3&help=0
```
**Parameters**:
- `dd1`, `dd2`: Period (1=1-10, 2=11-20, 3=21-end of month)

#### 3. Monthly Normals
**Endpoint**: `kma_clm_month.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_clm_month.php?authKey=YOUR_KEY&stn=108&mm1=01&mm2=12&help=0
```

#### 4. Annual Normals
**Endpoint**: `kma_clm_year.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_clm_year.php?authKey=YOUR_KEY&stn=108&help=0
```

---

### Yellow Dust / PM10 (황사관측)

#### 1. Hourly PM10 - Single Time
**Endpoint**: `kma_pm10.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_pm10.php?authKey=YOUR_KEY&tm=202501011200&stn=108&help=0
```

#### 2. Hourly PM10 - Period
**Endpoint**: `kma_pm10_2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_pm10_2.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501011800&stn=108&help=0
```

#### 3. Daily PM10 - Single Day
**Endpoint**: `kma_pm10_day.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_pm10_day.php?authKey=YOUR_KEY&tm=20250101&stn=108&help=0
```

#### 4. Daily PM10 - Period
**Endpoint**: `kma_pm10_day2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_pm10_day2.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=108&help=0
```

---

### UV Radiation (자외선지수)

#### 1-4. UV Index Endpoints
**Endpoints**: `kma_uv.php`, `kma_uv_2.php`, `kma_uv_day.php`, `kma_uv_day2.php`
Same pattern as PM10, just replace `pm10` with `uv`

---

### Snow Depth (적설관측)

#### 1-4. Snow Depth Endpoints
**Endpoints**: `kma_sd.php`, `kma_sd_2.php`, `kma_sd_day.php`, `kma_sd_day2.php`
Same pattern as PM10, just replace `pm10` with `sd`

---

### North Korea Observations (북한지역)

#### 1-4. NK Observation Endpoints
**Endpoints**: `kma_nkobs.php`, `kma_nkobs_2.php`, `kma_nkobs_day.php`, `kma_nkobs_day2.php`
Same pattern as PM10, just replace `pm10` with `nkobs`

---

### Seasonal Observations (계절관측)

#### 1. Observation Data - Single Year
**Endpoint**: `kma_season.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_season.php?authKey=YOUR_KEY&year=2025&stn=108&help=0
```

#### 2. Observation Data - Year Range
**Endpoint**: `kma_season_2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_season_2.php?authKey=YOUR_KEY&year1=2020&year2=2025&stn=108&help=0
```

---

### Station Information (관측소정보)

#### 1. ASOS Station List
**Endpoint**: `kma_stnlist.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_stnlist.php?authKey=YOUR_KEY&stn=0&help=0
```

#### 2. AWS Station List
**Endpoint**: `kma_aws_stnlist.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_aws_stnlist.php?authKey=YOUR_KEY&stn=0&help=0
```

---

## Upper Air Observations (고층 관측)

### Radiosonde (TEMP)

#### 1. Upper-Air Data
**Endpoint**: `upp_temp.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/upp_temp.php?authKey=YOUR_KEY&tm=202501010000&stn=47122&help=0
```
**Note**: Times are in UTC, not KST. Station 47122 = Seoul

**With pressure level**:
```
https://apihub.kma.go.kr/api/typ01/url/upp_temp.php?authKey=YOUR_KEY&tm=202501010000&stn=47122&pa=850&help=0
```
**Parameters**:
- `pa`: Pressure level in hPa (850, 700, 500, 300, 250, 200, etc.)

#### 2. Stability Indices
**Endpoint**: `upp_idx.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/upp_idx.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&stn=47122&help=0
```
**Returns**: CAPE, K-index, Lifted Index, Total Totals, etc.

#### 3. Maximum Altitude
**Endpoint**: `upp_raw_max.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/upp_raw_max.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=47122&help=0
```

---

## Marine Observations (해양 관측)

### Buoy

#### 1. Buoy Data - Single Time
**Endpoint**: `kma_buoy.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_buoy.php?authKey=YOUR_KEY&tm=202501011200&stn=0&help=0
```

#### 2. Buoy Data - Period
**Endpoint**: `kma_buoy2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_buoy2.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501020000&stn=0&help=0
```

#### 3. Comprehensive Marine Data
**Endpoint**: `sea_obs.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/sea_obs.php?authKey=YOUR_KEY&tm=202501011200&stn=0&help=0
```

---

## Weather Radar (기상레이더)

### Radar

#### 1. Radar Image - Single Time
**Endpoint**: `kma_radar.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_radar.php?authKey=YOUR_KEY&tm=202501011200&radar=ALL&help=0
```
**Radar IDs**:
- `ALL`: Composite of all radars
- `KSN`: Gangneung
- `KWK`: Gwangdeoksan
- `PSN`: Baengnyeongdo
- `JNI`: Jindo

#### 2. Radar Image Sequence
**Endpoint**: `kma_radar_2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_radar_2.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501011300&radar=ALL&help=0
```

#### 3. Radar Reflectivity at Location
**Endpoint**: `kma_radar_ref.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_radar_ref.php?authKey=YOUR_KEY&tm=202501011200&x=127.0&y=37.5&help=0
```

---

## Satellite Data (위성)

### GEO-KOMPSAT-2A (GK2A)

#### 1. Satellite File List
**Endpoint**: `sat_file_list.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/sat_file_list.php?authKey=YOUR_KEY&sat=GK2A&vars=L1B&area=FD&fmt=NetCDF&help=0
```
**Parameters**:
- `sat`: Satellite ID (GK2A)
- `vars`: Product type (L1B, L2)
- `area`: Region (FD=Full Disk, KO=Korea, EA=East Asia, ELA=Extended Local Area, TP=Target Point)
- `fmt`: File format (NetCDF)
- `tm`: Optional time filter (YYYYMMDDHHmm)

#### 2. Satellite Imagery
**Endpoint**: `sat_file_down2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/sat_file_down2.php?authKey=YOUR_KEY&lvl=l1b&dat=NR016&are=KO&tm=202501011200&typ=img&help=0
```
**Parameters**:
- `lvl`: Data level (l1b, l2)
- `dat`: Product/channel (NR016, SW038, CI, SST, etc.)
- `are`: Area code
- `typ`: Type (img=image)

**L1B Channels**:
- NR016: Near-IR 1.6μm
- SW038: Shortwave IR 3.8μm
- VI006: Visible 0.6μm
- And 13 more channels...

**L2 Products**:
- CI: Cloud Imagery
- SST: Sea Surface Temperature
- And more...

---

## Forecast & Warnings (예보/특보)

### Forecast

#### 1. Short-term Forecast (3 days)
**Endpoint**: `kma_sfcfct.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfcfct.php?authKey=YOUR_KEY&tm_fc=202501011200&stn=108&help=0
```

#### 2. Medium-term Forecast (3-10 days)
**Endpoint**: `kma_mtfcst.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_mtfcst.php?authKey=YOUR_KEY&tm_fc=202501011200&stn=108&help=0
```

#### 3. Weekly Forecast
**Endpoint**: `kma_wkfcst.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_wkfcst.php?authKey=YOUR_KEY&tm_fc=202501011200&stn=108&help=0
```

---

### Warnings

#### 1. Current Active Warnings
**Endpoint**: `kma_wn.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_wn.php?authKey=YOUR_KEY&stn=0&help=0
```

#### 2. Warning History
**Endpoint**: `kma_wn_2.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_wn_2.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=0&help=0
```

#### 3. Special Weather Report
**Endpoint**: `kma_swr.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_swr.php?authKey=YOUR_KEY&tm=202501011200&stn=0&help=0
```

---

## Typhoon (태풍)

### Typhoon Information

#### 1. Current Active Typhoons
**Endpoint**: `kma_typ.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_typ.php?authKey=YOUR_KEY&help=0
```

#### 2. Typhoon Details
**Endpoint**: `kma_typ_dtl.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_typ_dtl.php?authKey=YOUR_KEY&typ_id=2501&help=0
```
**Parameters**:
- `typ_id`: Typhoon ID (e.g., 2501 = first typhoon of 2025)

#### 3. Typhoon Forecast Track
**Endpoint**: `kma_typ_fcst.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_typ_fcst.php?authKey=YOUR_KEY&typ_id=2501&help=0
```

#### 4. Typhoon History
**Endpoint**: `kma_typ_hist.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_typ_hist.php?authKey=YOUR_KEY&year=2024&help=0
```

---

## Earthquake (지진)

### Earthquake Monitoring

#### 1. Recent Earthquake
**Endpoint**: `eqk_now.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/eqk_now.php?authKey=YOUR_KEY&disp=0&help=0
```
**Optional**: Add `tm` parameter to get earthquakes after specific time

#### 2. Earthquake List
**Endpoint**: `eqk_list.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/eqk_list.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501310000&disp=0&help=0
```

---

## Aviation (항공기상)

### AMOS (Aerodrome Meteorological Observation)

#### 1. Airport Observations
**Endpoint**: `amos.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/amos.php?authKey=YOUR_KEY&tm=202501011200&dtm=60&help=0
```
**Parameters**:
- `dtm`: Time interval in minutes (default: 60)

#### 2. AMDAR Aircraft Data
**Endpoint**: `amdar_kma.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/amdar_kma.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501011300&st=E&help=0
```
**Parameters**:
- `st`: Status filter (E=default)

---

## Global Meteorology (전지구 기상)

### GTS (Global Telecommunication System)

#### 1. SYNOP Surface Observations
**Endpoint**: `gts_bufr_syn.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/gts_bufr_syn.php?authKey=YOUR_KEY&tm=202501011200&dtm=3&stn=0&help=0
```
**Parameters**:
- `dtm`: Time window in hours (default: 3)

#### 2. Ship Observations
**Endpoint**: `gts_bufr_ship.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/gts_bufr_ship.php?authKey=YOUR_KEY&tm=202501011200&dtm=3&help=0
```

#### 3. Global Buoy Observations
**Endpoint**: `gts_bufr_buoy.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/gts_bufr_buoy.php?authKey=YOUR_KEY&tm=202501011200&dtm=3&stn=&help=0
```

#### 4. Aircraft Reports (AIREP)
**Endpoint**: `gts_airep1.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/gts_airep1.php?authKey=YOUR_KEY&tm=202501011200&dtm=60&stn=0&help=0
```

#### 5. Surface Weather Chart
**Endpoint**: `gts_cht_sfc.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/gts_cht_sfc.php?authKey=YOUR_KEY&tm=202501011200&help=0
```

#### 6. SYNOP Analysis Chart
**Endpoint**: `gts_cht_syn.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/gts_cht_syn.php?authKey=YOUR_KEY&tm=202501011200&help=0
```

---

## Integrated Data (통합자료)

### Integrated Meteorology

#### 1. Lightning Detection
**Endpoint**: `lgt_kma_np3.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/lgt_kma_np3.php?authKey=YOUR_KEY&tm1=202501011200&tm2=202501011300&help=0
```

#### 2. Wind Profiler
**Endpoint**: `kma_wpf.php`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_wpf.php?authKey=YOUR_KEY&tm=202501011200&stn=0&mode=L&help=0
```
**Parameters**:
- `mode`: L (Low mode) or H (High mode)

---

## Common Station IDs

### ASOS Stations
- 108: Seoul (서울)
- 112: Incheon (인천)
- 119: Suwon (수원)
- 133: Daejeon (대전)
- 143: Daegu (대구)
- 146: Jeonju (전주)
- 156: Gwangju (광주)
- 159: Busan (부산)
- 184: Jeju (제주)
- 185: Seogwipo (서귀포)

### Upper-Air Stations (WMO codes)
- 47122: Seoul
- 47138: Baengnyeongdo
- 47158: Gwangju
- 47185: Gosan (Jeju)

### AWS Stations
- 104: Bukgangneung
- Use station list APIs to get complete list

---

## Time Format Reference

| Format | Description | Example | Used In |
|--------|-------------|---------|---------|
| YYYYMMDDHHmm | Full datetime | 202501011200 | Most APIs |
| YYYYMMDD | Date only | 20250101 | Daily data APIs |
| YYYY | Year | 2025 | Seasonal, typhoon history |
| MM | Month | 01 | Climate normals |
| DD | Day | 15 | Climate normals |

**Important**:
- Surface observations (ASOS, AWS) use **KST (Korea Standard Time, UTC+9)**
- Upper-air observations (Radiosonde) use **UTC**
- Check API documentation for specific timezone requirements

---

## Response Format

All APIs return JSON with structure similar to:
```json
{
  "header": {
    "resultCode": "00",
    "resultMsg": "NORMAL_SERVICE"
  },
  "body": {
    "dataType": "JSON",
    "items": {
      "item": [
        {
          // observation data fields
        }
      ]
    },
    "pageNo": 1,
    "numOfRows": 100,
    "totalCount": 100
  }
}
```

---

## Summary Statistics

- **Total Endpoints**: 73
- **Total Clients**: 21
- **Base URLs**: 1 (all use typ01)
- **Authentication**: authKey parameter required for all

---

## Getting Your API Key

1. Visit https://apihub.kma.go.kr/
2. Sign up for an account
3. Apply for API key
4. Set environment variable: `export KMA_API_KEY=your_key_here`
5. Or create `.env` file in project root with `KMA_API_KEY=your_key_here`
