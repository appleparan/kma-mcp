# 지상관측

## Base URL Structure

대부분의 API들은 다음과 같은 base URL 패턴이 있다. 일부 다를 수 있으나, Example URL을 참고하면 된다.

```
https://apihub.kma.go.kr/api/typ01/url/{endpoint}?authKey={YOUR_API_KEY}&{parameters}
```
### 공통 파라미터
* `help`: 도움말추가. 1 이면 필드에 대한 약간의 도움말 추가 (0 이거나 없으면 없음)
* `authKey`: 인증키. 발급된 API 인증키

**Note**: All examples below require `authKey` parameter which is automatically added by the client.

## ASOS - Automated Synoptic Observing System (종관기상관측)

* 개요 : 종관기상관측이란 정해진 시각의 대기 상태를 파악하기 위해 모든 관측소에서 같은 시각에 실시하는 지상관측을 말합니다. 시정, 구름, 증발량, 일기현상 등 일부 목측 요소를 제외하고 관기상관측장비(ASOS, Automated Synoptic Observing System)를 이용해 자동으로 관측합니다.
* 요소 : 기온, 강수, 기압, 습도, 풍향, 풍속, 일사, 일조, 적설, 구름, 시정, 지면 · 초상온도 등
* 지점 : 96지점 (2020. 4. 1. 기준)
* 보유기간 : 1904년 4월 ~ 현재(지점별 상이함)
* 생산주기 : 분, 시간, 일, 월, 연 자료

### 지상 관측자료 조회

#### 시간자료

* Endpoint: `kma_sfctm2.php`
* Method: `get_hourly_data(tm, stn=0)`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?authKey=YOUR_KEY&tm=202501011200&stn=108&help=0
    ```
* Parameters:
    * `tm`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 해당 시간 (없으면 현재시간)
    * `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)
    * `help`: 도움말추가. 1 이면 필드에 대한 약간의 도움말 추가 (0 이거나 없으면 없음)

#### 시간자료(기간 조회)
* Endpoint:  `kma_sfctm3.php`
* Method: `get_hourly_period(tm1, tm2, stn=0)`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&stn=108&help=0
    ```
* Parameters:
    * `tm1`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 시작시간 또는 시작일 (없으면 현재시간)
    * `tm2`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 종료시간 또는 종료일 (없으면 현재시간), 최대 31일 조회 가능
    * `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)

#### 일자료
* Endpoint: `kma_sfcdd.php`
* Method: `get_daily_data(tm, stn=0, disp=0)`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd.php?authKey=YOUR_KEY&tm=20250101&stn=108&disp=0&help=0
    ```
* Parameters:
    * `tm`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 해당 시간 (없으면 현재시간)
    * `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)
    * `disp`: 표출. 0(빈칸없는 CSV파일), 1(일정 간격)

#### 일자료(기간 조회)
* Endpoint: `kma_sfcdd3.php`
* Method: `get_daily_period(tm1, tm2, stn=0, obs='', mode=0)`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd3.php?authKey=YOUR_KEY&tm1=20250101&tm2=20250131&stn=108&obs=&mode=0&help=0
    ```
* Parameters:
    * `tm`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 해당 시간 (없으면 현재시간)
    * `tm1`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 시작시간 또는 시작일 (없으면 현재시간)
    * `tm2`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 종료시간 또는 종료일 (없으면 현재시간), 최대 31일 조회 가능
    * `obs`: 관측종류. TA(기온), TD(이슬점온도), HM(습도), PV(증기압), PA(현지기압), PS(해면기압), CA_TOT(전운량), CA_MID(중하층운량), CH_MIN(최저온고(100m)),CT(운형(통계표)), VS(시정(10m)), TS(지면온도)
    * `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)
    * `mode`: 기타. 0:해독결과만 표출, 1:기사도 표출, 2:기사만 표출

#### 요소별 조회
* Endpoint: `kma_sfctm5.php`
* Method: `get_element_data(tm1, tm2, obs, stn=0)`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_sfctm5.php?authKey=YOUR_KEY&tm1=202501010000&tm2=202501020000&obs=TA&stn=108&help=0
    ```
* Parameters:
    * `tm1`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 시작시간 또는 시작일 (없으면 현재시간)
    * `tm2`: YYYYMMDDHHmm(KST), YYYYMMDD(KST). 기간: 종료시간 또는 종료일 (없으면 현재시간), 최대 31일 조회 가능
    * `obs`: 관측종류. TA(기온), TD(이슬점온도), HM(습도), PV(증기압), PA(현지기압), PS(해면기압), CA_TOT(전운량), CA_MID(중하층운량), CH_MIN(최저온고(100m)),CT(운형(통계표)), VS(시정(10m)), TS(지면온도)
    * `stn`: 지점번호. 해당 지점들(:로 구분)의 정보 표출 (0 이거나 없으면 전체지점)

### 지상 평년값 조회

* Endpoint: `kma_norm1.php`
* Method: ??

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_norm1.php?norm=D&tmst=2021&stn=0&MM1=5&DD1=1&MM2=5&DD2=2&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```
* Parameters:
    * `norm`: 평년종류. D(일), S(순), M(월), Y(연)
    * `tmst`: 평년기간. 1991(1961~1990년), 2001(1971~2000년), 2011(1981~2010년), 2021(1991~2020년)
    * `stn`: 지점번호, 0이면 전체지점
    * `MM1`: 시작 월, 기간 : MM1월 DD1일 ~ MM2월 DD2일
    * `DD1`: 시작 일, 순별 평년값인 경우, 100(상순), 200(중순), 300(하순)

### 지상기상연보 조회

Not yet implemented

#### 연요약자료조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getYearSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 연요약자료(2)조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getYearSumry2?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 평균기온평년차조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getAvgTaAnamaly?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 강수량평년차

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getRnAnamaly?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 지점별현상데이터조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData?pageNo=1&numOfRows=10&dataType=XML&year=2016&station=140&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 지점별현상데이터(2)조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData2?pageNo=1&numOfRows=10&dataType=XML&year=2016&station=140&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 지점별현상데이터(3)조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData3?pageNo=1&numOfRows=10&dataType=XML&year=2016&station=140&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

###  지상기상월보 조회

Not yet implemented

#### 일러두기조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getNote?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 지상관측지점일람표조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getSfcStnLstTbl?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 월요약자료조회


Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getMmSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 월요약자료(2)조회

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getMmSumry2?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

#### 해당월의일별기상자료조회


Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getDailyWthrData?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&station=90&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

### (그래픽) 지상기상현상(관서) 조회

Not yet implemented

#### 현상(관서)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/php/alw/sfc/sfc_ww_pnt.php?obs=ww_sfc&tm=202212221120&val=1&stn=1&obj=mq&map=HR&grid=2&legend=1&size=600&itv=5&zoom_level=0&zoom_x=0000000&zoom_y=0000000&gov=&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

### 연도별 특정일 기후통계 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_day_year.php?stn=108&mm=8&dd=15&authKey=lY2IAXPgQdCNiAFz4BHQbQ
    ```

## 방재기상관측(AWS)

* 개요 : 방재기상관측이란 지진 · 태풍 · 홍수 · 가뭄 등 기상현상에 따른 자연재해를 막기 위해 실시하는 지상관측을 말합니다. 관측 공백 해소 및 국지적인 기상 현상을 파악하기 위하여 전국 약 510여 지점에 자동기상관측장비(AWS, Automatic Weather System)를 설치하여 자동으로 관측합니다.
* 요소 : 기온, 강수, 풍향, 풍속 등
* 지점 : 510지점 (2020. 4. 1. 기준)
* 보유기간 : 1997년 1월 ~ 현재(지점별 상이함)
* 생산주기 : 분, 시간, 일, 월, 연 자료

### AWS 매분자료 조회

#### AWS 매분자료
* Endpoint: `nph-aws2_min`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min?tm2=202302010900&stn=0&disp=0&help=1&authKey=Pi8YfpSBTPivGH6Ugaz4Kg
    ```
* Parameters:
    * `tm1`: YYYYMMDDHHmm(KST). 조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
    * `tm2`: YYYYMMDDHHmm(KST), 조회할 시간구간의 종료시간 (없으면 현재시간)
    * `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 초상온도
* Endpoint: `nph-aws2_min_lst`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_lst?tm2=202302010900&stn=0&disp=0&help=1&authKey=Pi8YfpSBTPivGH6Ugaz4Kg
    ```
* Parameters:
    * `tm`: YYYYMMDDHHmm(KST). 조회할 시간 (없으면 현재시간)
    * `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
    * `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
    * `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 운고 운량
* Endpoint: `nph-aws2_min_cloud`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_cloud?tm2=202302010900&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
    * `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
    * `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
    * `itv`: 시간간격. (분)
    * `sms`: 평활화여부. 0 or 1
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 운고 운량(특정기간 평균 값)

* Endpoint: `nph-aws2_min_ca2`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ca2?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
    * `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
    * `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
    * `range`: 평균을 위한 누적기간(분)
    * `itv`: 시간간격. (분)
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS 운고 운량(특정기간 최소/최고 값)
* Endpoint: `nph-aws2_min_ca3`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ca3?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `tm1`: YYYYMMDDHHmm(KST). 기조회할 시간구간의 시작시간 (없으면 종료시간과 같음)기간은 전체지점이면 10분, 1개 지점이면 하루이내로 처리
    * `tm2`: YYYYMMDDHHmm(KST). 조회할 시간구간의 종료시간 (없으면 현재시간)
    * `stn`: 지점번호, 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
    * `range`: 평균을 위한 누적기간(분)
    * `itv`: 시간간격. (분)
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default)1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말. 0 : 시작과 종료표시 + 변수명 (default)1 : 0 + 변수에 대한 설명2 : 전혀 표시않음 (값만 표시)

#### AWS2 시정자료

Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_vis?tm2=201507140812&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```

#### AWS2 시정자료(평균·최소·최고 시정)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_vis3?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```

#### AWS2 현천자료
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ww1?tm2=201503221200&itv=60&range=60&stn=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
#### AWS2 현천, 분석
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ww2?tm2=201503221200&itv=10&range=10&stn=0&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```

### 이동형 관측자료 조회

#### 이동형 관측자료
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws3_min_mob?tm1=202108011455&tm2=202108011500&stn=&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```

### AWS 시간통계 자료 조회

#### 기온
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/awsh.php?var=TA&tm=201508121500&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```

#### 바람
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/awsh.php?var=WD&tm=201508121500&help=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

#### 강수
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/awsh.php?var=WD&tm=201508121500&help=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

#### 습도
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/awsh.php?var=HM&tm=201508121500&help=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 기압
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/awsh.php?var=PS&tm=201508121500&help=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 정시자료
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/awsh.php?tm=201508121500&help=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

### 지상 및 AWS 일통계 자료 조회
Not yet implemented

#### 요소별 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_aws_day.php?tm2=20150406&obs=ta_max&stn=0&disp=0&help=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

### 방재기상연보 조회
Not yet implemented
#### 지점별월요약자료조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getStnbyMmSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&station=96&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 연요약자료조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getYearSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

#### 방재기상관측지점일람표조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getAwsStnLstTbl?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 일러두기조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getNote?pageNo=1&numOfRows=10&dataType=XML&year=2016&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
### 방재기상월보 조회
Not yet implemented
#### 일별방재기상관측자료조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getDailyAwsData?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&station=129&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 월요약자료조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getMmSumry?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 방재기상관측지점일람표조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getAwsStnLstTbl?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 일러두기조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getNote?pageNo=1&numOfRows=10&dataType=XML&year=2016&month=09&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

### (그래픽) 지상기상현상(관서) 조회
Not yet implemented

#### 현상(현천계)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/php/alw/aws/aws_ww_pnt.php?obs=ww_vis&tm=202212221120&val=1&stn=1&obj=mq&map=HR&grid=2&legend=1&size=600&itv=5&zoom_level=0&zoom_x=0000000&zoom_y=0000000&gov=&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
### (그래픽) 일기상통계 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_day_img1?obs=rn_day&tm=202212221315&val=1&stn=1&obj=mq&map=HR&grid=2&legend=1&size=600&zoom_level=0&zoom_x=0000000&zoom_y=0000000&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
### (그래픽) AWS 분포도 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_img1?obs=rn_ex&tm=202305021355&val=1&stn=1&obj=mq&map=D3&grid=2&legend=1&size=330.00&itv=5&zoom_level=0&zoom_x=0000000&zoom_y=0000000&gov=&_DT=RSW:RNEX&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_img2?obs=wv_10m&tm=202305021405&val=1&stn=1&obj=mq&ws_ms=kh&map=D3&grid=2&legend=1&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
    ```text
    https://apihub.kma.go.kr/api/typ03/php/alw/aws/aws_obs_pnt.php?obs=vs&tm=202305030945&val=1&stn=1&obj=bn&map=D3&grid=2&legend=1&size=330.00&itv=10&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
    ```text
    https://apihub.kma.go.kr/api/typ03/php/alw/sea/sea_obs_pnt.php?obs=sea_wh&tm=202305030950&val=1&stn=1&obj=mq&map=D3&grid=2&legend=1&size=330.00&itv=5&zoom_level=0&zoom_x=0000000&zoom_y=0000000&gov=&_DT=RSW:SEAWH&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
### (그래픽) AWS 시계열 조회
Not yet implemented
#### 6시간
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-awsm_tms_h06?202305031000&0&108,419,415,421,413,408,409,414,424,406,407,416,412,411,405,404,110,423,417,418,510,889,410,509,425,401,400,403,402&m&108,419,415,421,413,408,409,414,424,406,407,416,412,411,405,404,110,423,417,418,510,889,410,509,425,401,400,403,402&kh&_DT=RSW:AWSCHART&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 12시간
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-awsm_tms_h12?202305030900&0&108,419,415,421,413,408,409,414,424,406,407,416,412,411,405,404,110,423,417,418,510,889,410,509,425,401,400,403,402&m&0&108,419,415,421,413,408,409,414,424,406,407,416,412,411,405,404,110,423,417,418,510,889,410,509,425,401,400,403,402&kh&_DT=RSW:AWSCHART&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 24시간
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_h24?202212291159&0&239,494,496,611,629&m&239,494,496,611,629&ms&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 2일
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d02?202212291158&0&239,494,496,611,629&m&0&239,494,496,611,629&ms&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 4일
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d04?202212291157&0&239,494,496,611,629&m&239,494,496,611,629&ms&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 8일
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d08?202212291156&0&239,494,496,611,629&m&239,494,496,611,629&ms&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 12일
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d12?202212291155&0&239,494,496,611,629&m&239,494,496,611,629&ms&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```

### (그래픽) AWS 분포도 조회(배경지도 없음)
** 출력결과는 투영법, 이미지파일 위치 등이 JSON 포맷으로 표출됨
* url 이후 나오는 경로 앞에 https://apihub.kma.go.kr을 붙여서 사용
Not yet implemented

#### 일 최고기온
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_day_imgp1?PROJ=LCC&map=D&grid=2&itv=5&dataDtlCd=aws_ta_max_0&obs=ta_max&stn=0&size=320&STARTX=-384032.28285233676&STARTY=4878817.500765007&ENDX=758967.7171476632&ENDY=3778150.834098339&ZOOMLVL=11&selWs=kh&tm=202307121600&tm_st=202307121600&tm_ed=202307121600&tm2=202307121600&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 강우감지
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_imgp1?PROJ=LCC&map=D&grid=2&itv=5&dataDtlCd=aws_rn_ex_0&obs=rn_ex&stn=0&size=320&STARTX=-384032.28285233676&STARTY=4878817.500765007&ENDX=758967.7171476632&ENDY=3778150.834098339&ZOOMLVL=11&selWs=kh&tm=202307121600&tm_st=202307121600&tm_ed=202307121600&tm2=202307121600&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
#### 바람벡터
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_imgp2?PROJ=LCC&map=D&grid=2&itv=5&dataDtlCd=aws_rn_ex_0&obs=rn_ex&stn=0&size=320&STARTX=-384032.28285233676&STARTY=4878817.500765007&ENDX=758967.7171476632&ENDY=3778150.834098339&ZOOMLVL=11&selWs=kh&tm=202307121600&tm_st=202307121600&tm_ed=202307121600&tm2=202307121600&authKey=Ek1C8O-0RwSNQvDvtAcEpw
    ```
## 기후 통계

* 개요 : 기후통계란 기상요소를 대상으로 한 통계입니다. 어느 기간 전체의 기상상태를 알기 위해서 해당 기간의 기상요소 관측값(또는 통계값) 전체에 대하여 합계, 평균, 누적값, 극값 등의 통계를 산출한 기상통계값을 사용한다.
* 요소 : 기압, 바람, 기온, 이슬점온도, 지면온도, 초상온도, 지중온도, 습도, 증기압, 구름, 시정, 강수량, 적설, 신적설, 일사, 일조, 증발량, 황사, 안개
* 지점 : 종관기상관측(ASOS) 및 방재기상관측(AWS) 700여 지점
* 보유기간 : 1904년 ~
* 생산주기 : 일, 월, 연

Not yet implemented
### 기온 기후통계데이터 조회
Not yet implemented
#### 기온 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기온 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기온 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기온 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기온 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기온 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
### 일사 기후통계데이터 조회
Not yet implemented
#### 일사 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_si.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일사 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_si.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일사 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_si.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일사 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_si.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일사 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_si.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일사 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_si.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 일조 기후통계데이터 조회
Not yet implemented
#### 일조 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ss.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일조 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ss.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일조 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ss.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일조 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ss.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일조 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ss.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일조 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ss.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 기압 기후통계데이터 조회
Not yet implemented

#### 기압 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pa.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기압 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pa.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기압 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pa.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기압 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pa.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기압 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pa.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 기압 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pa.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 바람 기후통계데이터 조회
Not yet implemented

#### 바람 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_wind.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 바람 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_wind.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 바람 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_wind.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 바람 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_wind.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 바람 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_wind.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 바람 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_wind.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 이슬점온도 기후통계데이터 조회
Not yet implemented

#### 이슬점온도 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_td.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 이슬점온도 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_td.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 이슬점온도 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_td.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 이슬점온도 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_td.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 이슬점온도 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_td.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 이슬점온도 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_td.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 지면온도 기후통계데이터 조회
Not yet implemented

#### 지면온도 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ts.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지면온도 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ts.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지면온도 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ts.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지면온도 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ts.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지면온도 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ts.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지면온도 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ts.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 초상온도 기후통계데이터 조회
Not yet implemented

#### 초상온도 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_tg.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 초상온도 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_tg.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 초상온도 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_tg.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 초상온도 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_tg.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 초상온도 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_tg.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 초상온도 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_tg.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 지중온도 기후통계데이터 조회
Not yet implemented

#### 지중온도 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_te.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지중온도 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_te.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지중온도 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_te.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지중온도 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_te.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지중온도 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_te.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 지중온도 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_te.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 습도 기후통계데이터 조회
Not yet implemented

#### 습도 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rhm.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 습도 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rhm.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 습도 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rhm.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 습도 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rhm.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 습도 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rhm.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 습도 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rhm.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 증기압 기후통계데이터 조회
Not yet implemented

#### 증기압 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pv.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증기압 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pv.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증기압 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pv.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증기압 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pv.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증기압 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pv.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증기압 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_pv.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 구름 기후통계데이터 조회
Not yet implemented

#### 구름 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_cloud.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 구름 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_cloud.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 구름 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_cloud.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 구름 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_cloud.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 구름 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_cloud.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 구름 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_cloud.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 시정 기후통계데이터 조회
Not yet implemented

#### 시정 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_vs.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 시정 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_vs.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 시정 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_vs.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 시정 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_vs.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 시정 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_vs.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 일조 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_vs.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 강수량 기후통계데이터 조회
Not yet implemented

#### 강수량 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rn.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 강수량 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rn.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 강수량 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rn.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 강수량 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rn.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 강수량 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rn.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 강수량 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_rn.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```

### 적설 기후통계데이터 조회
Not yet implemented

#### 적설 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_sd.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 적설 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_sd.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 적설 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_sd.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 적설 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_sd.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 적설 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_sd.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 적설 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_sd.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```


### 증발량 기후통계데이터 조회
Not yet implemented

#### 증발량 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ev.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증발량 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ev.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증발량 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ev.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증발량 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ev.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증발량 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ev.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 증발량 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ev.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
### 황사 기후통계데이터 조회
Not yet implemented

#### 황사 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ydst.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 황사 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ydst.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 황사 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ydst.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 황사 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ydst.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 황사 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ydst.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 황사 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_ydst.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
### 안개 기후통계데이터 조회
Not yet implemented

#### 안개 기후통계 데이터 일자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_fog.php?tm1=20250201&tm2=20250201&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 안개 기후통계 데이터 월자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_fog.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 안개 기후통계 데이터 연자료 조회(전체지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_fog.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 안개 기후통계 데이터 일자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_fog.php?tm1=20250201&tm2=20250201&lat=36.5&lon=126.5&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 안개 기후통계 데이터 월자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_fog.php?tm1=202502&tm2=202502&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
#### 안개 기후통계 데이터 연자료 조회(임의의 위경도와 가까운 3개 지점)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sts_fog.php?tm1=2024&tm2=2024&stn_id=0&help=1&disp=1&authKey=zxiqblJaSgSYqm5SWioEeA
    ```
## 북한기상관측
Not yet implemented
* 개요 : 북한이 세계기상기구(WMO, World Meteorogical Organization)의 기상통신망(GTS)을 통해 보낸 27개 지점의 관측 자료입니다.
* 요소 : 기온, 강수, 바람, 기압, 습도, 구름, 시정
* 지점 : 27지점
* 보유기간 : 1973년 1월 ~ 현재(지점별 상이함)
* 생산주기 : 시간, 일 자료

### 북한 지상 자료 조회
Not yet implemented
#### 북한 지상관측
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/nko_sfctm.php?tm=201703300900&stn=&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
### 북한 지상 평년값 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_nko_norm1.php?norm=D&tmst=2011&stn=0&MM1=5&DD1=1&MM2=5&DD2=2&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```

## 황사관측(PM10)
Not yet implemented
* 개요 : 황사관측(PM10)는 대기 중에 부유하는 에어로졸 중 직경이 10㎛ 이하인 입자의 농도를 연속 측정합니다. 먼지(황사 포함)가 필터에 침적되고, 동위원소 C-14에서 방출되는 베타선을 필터 여지에 쏘아 감쇄된 베타선을 검출기로 측정하여 황사의 농도를 산출합니다.
* 요소 : 부유분진 농도
* 지점 : 27지점 (2020. 4. 1. 기준)
* 보유기간 : 2003년 4월 ∼ 현재(지점별 상이함)
* 생산주기 : 분(5분 주기), 시간 자료

### 기상청 PM10 관측자료 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_pm10.php?tm1=201708011215&tm2=201708011230&authKey=dsi6kOLASrGIupDiwPqxYA
    ```
### 황사관측자료 조회
Not yet implemented
#### 황사지점정보
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/stn_pm10_inf.php?inf=kma&stn=&tm=201011110000&help=1&authKey=dsi6kOLASrGIupDiwPqxYA
    ```
#### 황사(PM10) 관측자료
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/dst_pm10_tm.php?tm=201012310900&org='kma'&stn=&data=&mode=1&help=1&authKey=dsi6kOLASrGIupDiwPqxYA
    ```
#### 황사(PM10) 시간통계자료
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/dst_pm10_hr.php?tm=201012310900&org='kma'&stn=&mode=1&help=1&authKey=dsi6kOLASrGIupDiwPqxYA
    ```

### 황사정보(위성영상, 일기도, 관측자료) 조회서비스
Not yet implemented
#### 황사위성영상조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/YdstInfoService/getYdstSatlitImg?pageNo=1&numOfRows=10&dataType=XML&time=202409060000&authKey=dsi6kOLASrGIupDiwPqxYA
    ```
#### 황사관측조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/YdstInfoService/getYdstObs?pageNo=1&numOfRows=10&dataType=XML&authKey=dsi6kOLASrGIupDiwPqxYA
    ```
#### 황사일기도조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/YdstInfoService/getYdstSfcChart?pageNo=1&numOfRows=10&dataType=XML&time=202409050000&authKey=dsi6kOLASrGIupDiwPqxYA
    ```
## 적설관측
Not yet implemented
* 개요 : 적설이란 고체상의 강수(눈, 싸락눈 등)가 지면에 내려 쌓여 있는 수직 깊이를 말합니다. 눈이 관측장소 또는 관측장소 주위의 지면에 반 이상을 덮었을 때를 적설이 있는 것으로 판단합니다. 목측관측을 비롯하여 레이저식, 초음파식, 영상식 등 적설계로 적설을 측정합니다.
* 요소 : 적설, 신적설
* 생산주기 : 일, 3시간, 6시간, 24시간(관측방법에 따라 상이함)

### 적설관측자료 조회
Not yet implemented
#### 적설관측지점
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/stn_snow.php?stn=&tm=201601051200&mode=0&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 적설
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow1.php?sd=tot&tm=201412051800&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 일신적설
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow1.php?sd=day&tm=201412051800&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 3시간 신적설
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow1.php?sd=3hr&tm=201412051800&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 24시간 신적설
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow1.php?sd=24h&tm=201412051800&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
### 기간
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow2.php?tm=201412051800&tm_st=201412040100&snow=0&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 최심적설,최심
Not yet implemented신적설
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow_day.php?sd=tot&tm=20150131&tm_st=20150125&stn=0&snow=0&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 최심적설
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow_day.php?sd=tot&tm=20150131&tm_st=20150125&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```
#### 최심신적설
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_snow_day.php?sd=day&tm=20150131&tm_st=20150125&help=1&authKey=Qesc6Lz3Tz6rHOi89w8-QQ
    ```

## 자외선관측
Not yet implemented
* 개요 : 자외선 복사는 일반적으로 자외선A(315~400nm), 자외선B(280~315nm), 자외선C(100~280nm)로 나뉘며, 이 중 자외선A와 자외선B는 오존층에 일부가 흡수되고 그 나머지가 지표에 도달합니다. 지표에 도달하는 자외선은 적은 양이지만 인간과 동 · 식물에게 큰 피해를 줄 뿐만 아니라 광화학 반응에도 영향을 미치면서 대기 환경을 변화시킵니다.
기상청은 자외선 복사 중 자외선A(320~400nm)와 자외선B 영역 중 인체에 홍반을 발생시키는 홍반자외선B(280~320nm)를 관측합니다.
* 요소 : 자외선A, 홍반자외선B
* 지점 : 안면도, 고산, 울릉도, 서울, 포항, 목포, 강릉
* 보유기간 : 1994년 1월 ~ 현재
* 생산주기 : 일, 월, 연 자료
### 자외선관측자료 조회
* Endpoint: `kma_sfctm_uv.php`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/kma_sfctm_uv.php?tm=202203211500&stn=0&help=1&authKey=kkB1a-YrSriAdWvmK4q4Jg
    ```
* Parameters:
    * `tm`: YYYYMMDDHHmm(KST), 해당 시점에 존재하는 지점목록 (없으면 현재시간)
    * `stn`: 지점번호. 해당 지점의 정보 표출 (0 이거나 없으면 전체지점)
    * `help`: 도움말추가. 1 이면 필드에 대한 약간의 도움말 추가 (0 이거나 없으면 없음)
## AWS 객관분석
Not yet implemented

### AWS 객관분석 격자자료 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/aws/nph-aws_min_obj?obs=ta&tm=201709181230&obj=mq&map=D3&grid=1&stn=0&gov=&authKey=8HIhwkFJRcmyIcJBSQXJyw
    ```
### AWS 객관분석 분포도 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/aws/nph-sfc_obs_img?tm=202204050930&obs=ta&acc=10&val=1&stn=1&obj=mq&map=HD&xp=350&yp=850&lon=&lat=&zoom=1.2&size=600&legend=1&lonlat=1&typ=0&wv=0&gov=KMA&authKey=8HIhwkFJRcmyIcJBSQXJyw
    ```
## 계절관측
Not yet implemented
* 개요 :계절관측 데이터는 계절의 빠르고 늦음의 지역적인 차이 등을 합리적으로 관특 및 통계 분석하여 기후변화의 추이를 통괄적으로 파악하기 위해 관측장소에서 관측차가 지정된 식물, 동물, 기후계절 등을 관측한 자료입니다.
* 요소 :
    * 식물계절관측: 개나리, 진달래, 벚나무, 단풍나무 등
    * 동물계절관측: 제비, 개구리, 나비, 잠자리, 뻐꾸기, 매미 등
    * 기후계절관측: 눈, 서리, 얼음, 강·하천 결빙 및 해빙 등
* 지점 : 87지점 (목측관측 중단에 따라 현행 계절관측 지점수와 차이 발생)
* 보유기간 : 1904년 ~ 현재(요소별, 지점별 상이함)
* 생산주기 : 연 자료

### 계절관측 자료 조회
Not yet implemented
#### 단일지점 전요소 기간조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_ssn.php?stn=108&tm1=20200101&tm2=20221030&authKey=tfCSyWZ-QEewkslmflBHbg
    ```
#### 전지점 단일요소 기간조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_ssn.php?stn=0&tm1=20210101&tm2=20221030&ssn=302&authKey=tfCSyWZ-QEewkslmflBHbg
    ```
### 계절관측 평년자료 조회
#### 전지점 전요소 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_ssn_norm.php?tmst=2011&stn=0&MM1=4&DD1=1&MM2=8&DD2=2&authKey=tfCSyWZ-QEewkslmflBHbg
    ```
#### 전지점 단일요소 조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/sfc_ssn_norm.php?stn=0&MM1=4&DD1=1&MM2=8&DD2=2&ssn=201&authKey=tfCSyWZ-QEewkslmflBHbg
    ```
## 지상관측 지점정보
Not yet implemented

### 지상관측 지점정보 조회
Not yet implemented
#### 지상
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/stn_inf.php?inf=SFC&stn=&tm=202211300900&help=1&authKey=pUXotX9hRMyF6LV_YQTMnA
    ```
#### AWS
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/stn_inf.php?inf=AWS&stn=&tm=202211300900&help=1&authKey=pUXotX9hRMyF6LV_YQTMnA
    ```
#### 북한
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/stn_inf.php?inf=NKO&stn=&tm=202211300900&help=1&authKey=pUXotX9hRMyF6LV_YQTMnA
    ```
#### 자외선
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/stn_inf.php?inf=UV&stn=&tm=202211300900&help=1&authKey=pUXotX9hRMyF6LV_YQTMnA
    ```

## Getting Your API Key

1. Visit https://apihub.kma.go.kr/
2. Sign up for an account
3. Apply for API key
4. Set environment variable: `export KMA_API_KEY=your_key_here`
5. Or create `.env` file in project root with `KMA_API_KEY=your_key_here`
