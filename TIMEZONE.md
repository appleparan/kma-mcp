# KMA API Timezone Reference

**⚠️ Important**: Different KMA APIs use different timezones!

## Timezone Summary

- **KST (Korea Standard Time, UTC+9)**: Most surface observations
- **UTC**: Upper-air observations, some international data

---

## 1. 지상관측 (Surface Observations) - **KST**

### 1.1 ASOS (종관기상관측)
#### 지상 관측자료 조회
1. **시간자료** (Hourly) - **KST**
   - Endpoint: `kma_sfctm2.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=202211300900&stn=0&help=1&authKey=YOUR_KEY

2. **시간자료 (기간조회)** (Hourly Period) - **KST**
   - Endpoint: `kma_sfctm3.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php?tm1=201512110100&tm2=201512140000&stn=108&help=1&authKey=YOUR_KEY

3. **일자료** (Daily) - **KST**
   - Endpoint: `kma_sfcdd.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd.php?tm=20150715&stn=0&help=1&authKey=YOUR_KEY

4. **일자료 (기간 조회)** (Daily Period) - **KST**
   - Endpoint: `kma_sfcdd3.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd3.php?tm1=20151211&tm2=20151214&stn=108&help=1&authKey=YOUR_KEY

5. **요소별 조회** (Element Query) - **KST**
   - Endpoint: `kma_sfctm5.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/kma_sfctm5.php?tm1=201504060000&tm2=201504060900&obs=TA&stn=0&help=1&authKey=YOUR_KEY

#### 지상평년값 (Climate Normals)
- Endpoint: `sfc_norm1.php`
- Example: https://apihub.kma.go.kr/api/typ01/url/sfc_norm1.php?norm=D&tmst=2021&stn=0&MM1=5&DD1=1&MM2=5&DD2=2&authKey=YOUR_KEY

### 1.2 AWS (방재기상관측) - **KST**
All AWS endpoints use KST:
- `kma_aws.php` - Minutely
- `kma_aws2.php` - Minutely Period
- `kma_aws3.php` - Hourly
- `kma_aws4.php` - Hourly Period
- `kma_aws5.php` - Daily
- `kma_aws6.php` - Daily Period

### 1.3 AWS OA (AWS Objective Analysis) - **KST**
- `kma_awsoa.php`
- `kma_awsoa_2.php`

### 1.4 황사관측 (Yellow Dust / PM10) - **KST**
- `kma_pm10.php` - Hourly
- `kma_pm10_2.php` - Hourly Period
- `kma_pm10_day.php` - Daily
- `kma_pm10_day2.php` - Daily Period

### 1.5 자외선지수 (UV Radiation) - **KST**
- `kma_uv.php` - Hourly
- `kma_uv_2.php` - Hourly Period
- `kma_uv_day.php` - Daily
- `kma_uv_day2.php` - Daily Period

### 1.6 적설관측 (Snow Depth) - **KST**
- `kma_sd.php` - Hourly
- `kma_sd_2.php` - Hourly Period
- `kma_sd_day.php` - Daily
- `kma_sd_day2.php` - Daily Period

### 1.7 북한지역 (North Korea) - **KST**
- `kma_nkobs.php` - Hourly
- `kma_nkobs_2.php` - Hourly Period
- `kma_nkobs_day.php` - Daily
- `kma_nkobs_day2.php` - Daily Period

### 1.8 계절관측 (Seasonal) - **KST**
- `kma_season.php`
- `kma_season_2.php`

### 1.9 관측소정보 (Station Info)
- `kma_stnlist.php`
- `kma_aws_stnlist.php`

---

## 2. 고층기상관측 (Upper-Air Observations) - **UTC**

### 2.1 Radiosonde (TEMP) - **UTC** ⚠️
**Important**: These use UTC, not KST!

1. **고층관측자료** (Upper-Air Data) - **UTC**
   - Endpoint: `upp_temp.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/upp_temp.php?tm=202201010000&stn=47122&help=1&authKey=YOUR_KEY
   - Station 47122 = Seoul (WMO code)

2. **안정도지수** (Stability Indices) - **UTC**
   - Endpoint: `upp_idx.php`
   - Example: https://apihub.kma.go.kr/api/typ01/url/upp_idx.php?tm1=202201010000&tm2=202201020000&stn=47122&help=1&authKey=YOUR_KEY

3. **최대고도** (Maximum Altitude) - **UTC**
   - Endpoint: `upp_raw_max.php`

---

## 3. 해양기상관측 (Marine Observations) - **KST (likely)**

### 3.1 부이 (Buoy) - **KST**
- `kma_buoy.php`
- `kma_buoy2.php`
- `sea_obs.php`

---

## 4. 기상레이더 (Weather Radar) - **KST**

### 4.1 Radar - **KST**
- `kma_radar.php`
- `kma_radar_2.php`
- `kma_radar_ref.php`

---

## 5. 위성 (Satellite) - **UTC (likely)**

### 5.1 GEO-KOMPSAT-2A - **UTC (likely)**
- `sat_file_list.php`
- `sat_file_down2.php`

**Note**: Satellite observations typically use UTC for international compatibility.

---

## 6. 예보/특보 (Forecast & Warnings) - **KST**

### 6.1 예보 (Forecast) - **KST**
- `kma_sfcfct.php` - Short-term
- `kma_mtfcst.php` - Medium-term
- `kma_wkfcst.php` - Weekly

### 6.2 특보 (Warnings) - **KST**
- `kma_wn.php`
- `kma_wn_2.php`
- `kma_swr.php`

---

## 7. 태풍 (Typhoon) - **KST**

### 7.1 태풍정보 - **KST**
- `kma_typ.php`
- `kma_typ_dtl.php`
- `kma_typ_fcst.php`
- `kma_typ_hist.php`

---

## 8. 지진 (Earthquake) - **KST**

### 8.1 지진정보 - **KST**
- `eqk_now.php`
- `eqk_list.php`

---

## 9. 항공기상 (Aviation) - **UTC (likely)**

### 9.1 AMOS - **UTC (likely)**
- `amos.php`
- `amdar_kma.php`

**Note**: Aviation meteorology typically uses UTC for international standards.

---

## 10. 전지구 기상 (Global Meteorology) - **UTC**

### 10.1 GTS - **UTC** ⚠️
All GTS endpoints use UTC (international standard):
- `gts_bufr_syn.php` - SYNOP
- `gts_bufr_ship.php` - Ship
- `gts_bufr_buoy.php` - Buoy
- `gts_airep1.php` - Aircraft
- `gts_cht_sfc.php` - Surface Chart
- `gts_cht_syn.php` - SYNOP Chart

---

## 11. 통합자료 (Integrated Data)

### 11.1 낙뢰 (Lightning) - **KST**
- `lgt_kma_np3.php`

### 11.2 윈드프로파일러 (Wind Profiler) - **KST (likely)**
- `kma_wpf.php`

---

## Quick Reference Table

| Category | APIs | Timezone | Notes |
|----------|------|----------|-------|
| Surface (ASOS, AWS) | All surface observation | **KST** | Most common |
| Upper-Air (Radiosonde) | upp_temp, upp_idx, upp_raw_max | **UTC** | International standard |
| Marine (Buoy) | kma_buoy, sea_obs | **KST** | Domestic waters |
| Radar | kma_radar | **KST** | Domestic coverage |
| Satellite | sat_file | **UTC (likely)** | International standard |
| Forecast/Warnings | kma_sfcfct, kma_wn | **KST** | Domestic forecasts |
| Typhoon | kma_typ | **KST** | Domestic service |
| Earthquake | eqk | **KST** | Domestic service |
| Aviation (AMOS) | amos, amdar | **UTC (likely)** | International aviation |
| GTS | gts_bufr, gts_airep | **UTC** | International exchange |
| Lightning | lgt_kma_np3 | **KST** | Domestic detection |

---

## Implementation Notes

### For KST APIs:
```python
from zoneinfo import ZoneInfo
from datetime import datetime

KST = ZoneInfo('Asia/Seoul')
now_kst = datetime.now(KST)
time_str = now_kst.strftime('%Y%m%d%H%M')
```

### For UTC APIs:
```python
from datetime import datetime, UTC

now_utc = datetime.now(UTC)
time_str = now_utc.strftime('%Y%m%d%H%M')
```

### Converting KST to UTC:
```python
from zoneinfo import ZoneInfo
from datetime import datetime, UTC

KST = ZoneInfo('Asia/Seoul')
kst_time = datetime(2025, 1, 1, 12, 0, tzinfo=KST)
utc_time = kst_time.astimezone(UTC)
```

---

## ⚠️ Critical Points

1. **ASOS/AWS**: Always use KST
2. **Radiosonde**: Always use UTC (9 hours behind KST)
3. **GTS**: Always use UTC (international)
4. **When in doubt**: Check if data is domestic (KST) or international (UTC)
5. **API validation**: Server may reject requests with wrong timezone

---

## See Also
- [API_ENDPOINTS.md](API_ENDPOINTS.md) - Complete endpoint reference
- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) - KST support implementation plan
