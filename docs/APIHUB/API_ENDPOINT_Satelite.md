
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
