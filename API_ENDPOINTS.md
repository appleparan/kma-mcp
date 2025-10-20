# KMA API Endpoint Reference

Complete reference of all KMA API endpoints with example URLs and parameters.

---

## Base URL Structure

대부분의 API들은 다음과 같은 base URL 패턴이 있다. 일부 다를 수 있으나, Example URL을 참고하면 된다. 

```
https://apihub.kma.go.kr/api/typ01/url/{endpoint}?authKey={YOUR_API_KEY}&{parameters}
```
### 공통 파라미터 
* `help`: 도움말추가. 1 이면 필드에 대한 약간의 도움말 추가 (0 이거나 없으면 없음)
* `authKey`: 인증키. 발급된 API 인증키

**Note**: All examples below require `authKey` parameter which is automatically added by the client.

---

## Surface Observations (지표 관측)

### ASOS - Automated Synoptic Observing System (종관기상관측)

* 개요 : 종관기상관측이란 정해진 시각의 대기 상태를 파악하기 위해 모든 관측소에서 같은 시각에 실시하는 지상관측을 말합니다. 시정, 구름, 증발량, 일기현상 등 일부 목측 요소를 제외하고 관기상관측장비(ASOS, Automated Synoptic Observing System)를 이용해 자동으로 관측합니다.
* 요소 : 기온, 강수, 기압, 습도, 풍향, 풍속, 일사, 일조, 적설, 구름, 시정, 지면 · 초상온도 등
* 지점	: 96지점 (2020. 4. 1. 기준)
* 보유기간 : 1904년 4월 ~ 현재(지점별 상이함)
* 생산주기 : 분, 시간, 일, 월, 연 자료

#### 지상 관측자료 조회
##### 시간자료
**Endpoint**: `kma_sfctm2.php`
**Method**: `get_hourly_data(tm, stn=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?authKey=YOUR_KEY&tm=202501011200&stn=108&help=0
```
**Parameters**:
- `tm`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 해당 시간 (없으면 현재시간)
- `stn`: Station number (0=all, 108=Seoul)
- `help`: Always 0

##### 시간자료(기간 조회)
**Endpoint**: `kma_sfctm3.php`
**Method**: `get_hourly_period(tm1, tm2, stn=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&stn=108&help=0
```
**Parameters**:
- `tm1`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 시작시간 또는 시작일 (없으면 현재시간)
- `tm2`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 종료시간 또는 종료일 (없으면 현재시간), 최대 31일 조회 가능
- `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)

##### 일자료
**Endpoint**: `kma_sfcdd.php`
**Method**: `get_daily_data(tm, stn=0, disp=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd.php?authKey=YOUR_KEY&tm=20250101&stn=108&disp=0&help=0
```
**Parameters**:
- `tm`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 해당 시간 (없으면 현재시간)
- `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)
- `disp`: 표출. 0(빈칸없는 CSV파일), 1(일정 간격)

##### 일자료(기간 조회)
**Endpoint**: `kma_sfcdd3.php`
**Method**: `get_daily_period(tm1, tm2, stn=0, obs='', mode=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd3.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=108&obs=&mode=0&help=0
```
**Parameters**:
- `tm`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 해당 시간 (없으면 현재시간)
- `tm1`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 시작시간 또는 시작일 (없으면 현재시간)
- `tm2`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 종료시간 또는 종료일 (없으면 현재시간), 최대 31일 조회 가능
- `obs`: 관측종류. TA(기온), TD(이슬점온도), HM(습도), PV(증기압), PA(현지기압), PS(해면기압), CA_TOT(전운량), CA_MID(중하층운량), CH_MIN(최저온고(100m)),CT(운형(통계표)), VS(시정(10m)), TS(지면온도)
- `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)
- `mode`: 기타. 0:해독결과만 표출, 1:기사도 표출, 2:기사만 표출

##### 요소별 조회
**Endpoint**: `kma_sfctm5.php`
**Method**: `get_element_data(tm1, tm2, obs, stn=0)`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/kma_sfctm5.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&obs=TA&stn=108&help=0
```
**Parameters**:
- `tm1`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 시작시간 또는 시작일 (없으면 현재시간)
- `tm2`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 종료시간 또는 종료일 (없으면 현재시간), 최대 31일 조회 가능
- `obs`: 관측종류. TA(기온), TD(이슬점온도), HM(습도), PV(증기압), PA(현지기압), PS(해면기압), CA_TOT(전운량), CA_MID(중하층운량), CH_MIN(최저온고(100m)),CT(운형(통계표)), VS(시정(10m)), TS(지면온도)
- `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)

####  지상 평년값 조회

**Endpoint**: `kma_norm1.php`
**Method**: 

**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/url/sfc_norm1.php?norm=D&tmst=2021&stn=0&MM1=5&DD1=1&MM2=5&DD2=2&authKey=lY2IAXPgQdCNiAFz4BHQbQ
```
**Parameters**:
- `norm`: 평년종류. D(일), S(순), M(월), Y(연)
- `tmst`: 평년기간. 1991(1961~1990년), 2001(1971~2000년), 2011(1981~2010년), 2021(1991~2020년)
- `stn`: 지점번호, 0이면 전체지점
- `MM1`: 시작 월, 기간 : MM1월 DD1일 ~ MM2월 DD2일
- `DD1`: 시작 일, 순별 평년값인 경우, 100(상순), 200(중순), 300(하순)

#### 지상기상연보 조회

Not yet implemented

##### 연요약자료조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getYearSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 연요약자료(2)조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getYearSumry2?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ


##### 평균기온평년차조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getAvgTaAnamaly?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 강수량평년차

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getRnAnamaly?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 지점별현상데이터조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData?pageNo=1&numOfRows=10&dataType=XML&year=2016&station=140&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 지점별현상데이터(2)조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData2?pageNo=1&numOfRows=10&dataType=XML&year=2016&station=140&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 지점별현상데이터(3)조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData3?pageNo=1&numOfRows=10&dataType=XML&year=2016&station=140&authKey=lY2IAXPgQdCNiAFz4BHQbQ

####  지상기상월보 조회

Not yet implemented

##### 일러두기조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getNote?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 지상관측지점일람표조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getSfcStnLstTbl?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 월요약자료조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getMmSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 월요약자료(2)조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getMmSumry2?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ

##### 해당월의일별기상자료조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getDailyWthrData?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&station=90&authKey=lY2IAXPgQdCNiAFz4BHQbQ

#### (그래픽) 지상기상현상(관서) 조회

Not yet implemented
##### 현상(관서)
Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ03/php/alw/sfc/sfc_ww_pnt.php?obs=ww_sfc&tm=202212221120&val=1&stn=1&obj=mq&map=HR&grid=2&legend=1&size=600&itv=5&zoom_level=0&zoom_x=0000000&zoom_y=0000000&gov=&authKey=lY2IAXPgQdCNiAFz4BHQbQ

#### 연도별 특정일 기후통계 조회

Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ01/url/sfc_day_year.php?stn=108&mm=8&dd=15&authKey=lY2IAXPgQdCNiAFz4BHQbQ
---

### 방재기상관측(AWS)

* 개요 : 방재기상관측이란 지진 · 태풍 · 홍수 · 가뭄 등 기상현상에 따른 자연재해를 막기 위해 실시하는 지상관측을 말합니다. 관측 공백 해소 및 국지적인 기상 현상을 파악하기 위하여 전국 약 510여 지점에 자동기상관측장비(AWS, Automatic Weather System)를 설치하여 자동으로 관측합니다.
* 요소 : 기온, 강수, 풍향, 풍속 등
* 지점	: 510지점 (2020. 4. 1. 기준)
* 보유기간 : 1997년 1월 ~ 현재(지점별 상이함)
* 생산주기 : 분, 시간, 일, 월, 연 자료
#### AWS 매분자료 조회

##### AWS 매분자료
**Endpoint**: `nph-aws2_min`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min?tm2=202302010900&stn=0&disp=0&help=1&authKey=Pi8YfpSBTPivGH6Ugaz4Kg
```
**Parameters**:
- `tm1`: YYYYMMDDHHmm(KST). 조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
- `tm2`: YYYYMMDDHHmm(KST), 조회할 시간구간의 종료시간 (없으면 현재시간)
- `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
- `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
- `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 초상온도
**Endpoint**: `nph-aws2_min_lst`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_lst?tm2=202302010900&stn=0&disp=0&help=1&authKey=Pi8YfpSBTPivGH6Ugaz4Kg
```
**Parameters**:
- `tm`: YYYYMMDDHHmm(KST). 조회할 시간 (없으면 현재시간)
- `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
- `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
- `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
- `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
- `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 운고 운량
**Endpoint**: `nph-aws2_min_cloud`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_cloud?tm2=202302010900&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
```
**Parameters**:
- `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
- `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
- `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
- `itv`: 시간간격. (분)
- `sms`: 평활화여부. 0 or 1
- `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
- `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 운고 운량(특정기간 평균 값)
**Endpoint**: `nph-aws2_min_ca2`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ca2?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
```
**Parameters**:
- `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
- `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
- `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
- `range`: 평균을 위한 누적기간(분)
- `itv`: 시간간격. (분)
- `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
- `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 운고 운량(특정기간 최소/최고 값)
**Endpoint**: `nph-aws2_min_ca3`
**Example URL**:
```
https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ca3?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
```
**Parameters**:
- `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
- `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
- `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
- `range`: 평균을 위한 누적기간(분)
- `itv`: 시간간격. (분)
- `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
- `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS2 시정자료
Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_vis?tm2=201507140812&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow

#### AWS2 시정자료(평균·최소·최고 시정)
Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_vis3?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow

#### AWS2 현천자료
Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ww1?tm2=201503221200&itv=60&range=60&stn=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow

#### AWS2 현천, 분석
Not yet implemented
**Example URL**: https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ww2?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow

## 이동형 관측자료 조회
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
