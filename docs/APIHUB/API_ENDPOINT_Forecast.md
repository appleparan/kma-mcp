# 예, 특보
초단기, 단기, 중기예보의 기온, 바람, 강수량 등 데이터를 제공하며, 폭염, 한파, 호우 등 10종의 기상특보 (주의보, 경보) 데이터를 제공합니다.

## Base URL Structure

대부분의 API들은 다음과 같은 base URL 패턴이 있다. 일부 다를 수 있으나, Example URL을 참고하면 된다.

```
https://apihub.kma.go.kr/api/typ01/url/{endpoint}?authKey={YOUR_API_KEY}&{parameters}
```
### 공통 파라미터
* `help`: 도움말추가. 1 이면 필드에 대한 약간의 도움말 추가 (0 이거나 없으면 없음)
* `authKey`: 인증키. 발급된 API 인증키

**Note**: All examples below require `authKey` parameter which is automatically added by the client.

## 단기예보

* 개요 : 단기예보란 예보기간과 구역을 시 · 공간적으로 세분화하여 발표하는 예보입니다. 지역별, 시간별 차이로 인한 수요자의 불편을 최소화하기 위해 전국을 5km * 5km 간격의 격자(동서 149(745km) × 남북 253(1.265km)), 총 37,697개로 나누어, 3시간 마다 읍, 면, 동 단위의 행정구역 중심으로 상세한 날씨를 제공합니다.
* 요소 : 3시간 기온, 낮 최고기온, 아침 최저기온, 풍향, 풍속, 동서바람성분, 남북바람성분, 하늘상태, 강수형태, 강수확률, 6시간 강수량, 6시간 신적설, 습도, 파고
* 지점 : 동사무소를 중심으로 하는 행정구역
* 보유기간 : 2008년 10월 30일 17:00KST(시행일 기준) ~ 현재
* 생산주기 : 2시부터 3시간 간격(일 8회)
### 단기예보자료(2001년 2월 이후) 조회

#### 단기 예보구역

* Endpoint: `fct_shrt_reg.php`
* Method: `ForecastClient.get_short_term_region()` / `AsyncForecastClient.get_short_term_region()`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_shrt_reg.php?tmfc=0&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)). 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)

#### 단기 개황, disp=1(JSON)
* Endpoint: `fct_afs_ds.php`
* Method: `ForecastClient.get_short_term_overview()` / `AsyncForecastClient.get_short_term_overview()`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_ds.php?stn=&tmfc1=2013121106&tmfc2=2013121118&disp=0&help=1&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)). 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)

#### 단기 육상예보
* Endpoint: `fct_afs_dl.php`
* Method: `ForecastClient.get_short_term_land()` / `AsyncForecastClient.get_short_term_land()`
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_dl.php?reg=&tmfc1=2013121106&tmfc2=2013121118&disp=0&help=1&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)). 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)

#### 단기 육상예보(2)
* Endpoint: `fct_afs_dl2.php`
* Method: `ForecastClient.get_short_term_land_v2()` / `AsyncForecastClient.get_short_term_land_v2()`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_dl2.php?reg=&tmfc1=2020052505&tmfc2=2020052517&disp=0&help=1&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)). 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)

#### 단기 해상예보
* Endpoint: `fct_afs_do.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_do.php?reg=&tmfc1=2013121106&tmfc2=2013121118&disp=0&help=1&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)). 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST).  없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)

### 동네예보(단기예보, 초단기예보, 실황) 격자자료
#### 단기예보
* Endpoint: `nph-dfs_shrt_grd`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_shrt_grd?tmfc=2024022505&tmef=2024022506&vars=TMP&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 3시간 간격 생산(매일 2시, 5시, 8시, 11시, 14시, 17시, 20시, 23시 발표) 없으면, 전체 / 0이면, 가장 최근
    * `tmef`: YYYYMMDDHHmm(KST). 발효시간.
        * (2024.11.28. 14시 이전) 1시간 간격으로 제공(2, 5, 8, 11, 14시는 모레 자정까지, 17, 20, 23시는 글피 자정까지 제공)
        * (2024.11.28. 14시 이후) 1시간 간격으로 제공(2, 5, 8, 11, 14시는 글피 자정까지, 17, 20, 23시는 그글피 자정까지 제공)
    * `vars`: 예보변수. TMP(기온), TMX(최고기온), TMN(최저기온), UUU(동서바람성분), VVV(남북바람성분), VEC(풍향), WSD(풍속), SKY(하늘상태), PTY(강수형태), POP(강수유무), PCP(1시간 강수량), SNO(1시간 신적설), REH(상대습도), WAV(파고)

#### 초단기예보
* Endpoint: `nph-dfs_vsrt_grd`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_vsrt_grd?tmfc=202403011010&tmef=2024030111&vars=T1H&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 10분 간격 발표
    * `tmef`: YYYYMMDDHHmm(KST). 발효시간. 발표시간 기준 6시간 까지 1시간 간격으로 제공
    * `vars`: 예보변수. T1H(기온), UUU(동서바람성분), VVV(남북바람성분), VEC(풍향), WSD(풍속), SKY(하늘상태), LGT(낙뢰), PTY(강수형태), RN1(1시간 강수량), REH(상대습도)

#### 실황
* Endpoint: `nph-dfs_odam_grd`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_odam_grd?tmfc=202403051010&vars=T1H&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 10분 간격 발표
        * (2024.3.4. 오전 10시 이후) 10분 간격 발표
        * (2024.3.4. 오전 10시 이전) 1시간(매 정시) 간격 발표
    * `vars`: 예보변수. T1H(기온), UUU(동서바람성분), VVV(남북바람성분), VEC(풍향), WSD(풍속), PTY(강수형태), RN1(1시간 강수량), REH(상대습도)

#### 동네예보 격자 번호 → 위·경도 변환
* Endpoint: `nph-dfs_xy_lonlat`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_xy_lonlat?x=60&y=127&help=1&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `x`: 동네예보 격자 번호(동서방향). 범위: 1 ~ 149
    * `y`: 동네예보 격자 번호(남북방향). 범위: 1 ~ 253
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 임의 위·경도 → 인근 동네예보 격자 번호 변환
* Endpoint: `nph-dfs_xy_lonlat`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_xy_lonlat?lon=127.5&lat=36.5&help=0&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `x`: 동네예보 격자 번호(동서방향). 범위: 1 ~ 149
    * `y`: 동네예보 격자 번호(남북방향). 범위: 1 ~ 253
    * `lon`: 임의 경도. 범위: 123.310165 ~ 132.774963
    * `lat`: 임의 위도. 범위: 31.651814 ~ 43.393490
    * `help`: 도움말추가. 0(도움말 정보 표시 안됨), 1(도움말 정보 표시)

### 동네예보 통보문 조회

#### 기상개황조회

* Endpoint: `getWthrSituation`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstMsgService/getWthrSituation?pageNo=1&numOfRows=10&dataType=XML&stnId=108&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `stnId`: 발표관서. 108 기상청, 109 수도권(서울)..등 별첨 엑셀자료 참조(‘개황’ 구분 값 참고)

#### 육상예보조회

* Endpoint: `getLandFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstMsgService/getLandFcst?pageNo=1&numOfRows=10&dataType=XML&regId=11A00101&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `regId`: 예보구역코드. 11A00101(백령도), 11B10101 (서울), 11B20201(인천) 등... 별첨 엑셀자료 참조(‘육상’ 구분 값 참고)

#### 해상예보조회
* Endpoint: `getSeaFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstMsgService/getSeaFcst?pageNo=1&numOfRows=10&dataType=XML&regId=12A20100&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `regId`: 예보구역코드. 12A20100 (서해중부앞바다), 12B20100(남해동부앞바다) 등... 별첨 엑셀자료 참조(‘해상’ 구분 값 참고)

### 동네예보(초단기실황·초단기예보·단기예보) 조회
#### 초단기실황조회
* Endpoint: `getUltraSrtNcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getUltraSrtNcst?pageNo=1&numOfRows=1000&dataType=XML&base_date=20210628&base_time=0600&nx=55&ny=127&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `base_date`: 발표일자. ‘21년 6월 28일 발표
    * `base_time`: 발표일자. 06시 발표(정시단위)
    * `nx`: 예보지점 X 좌표. 예보지점의 X 좌표값
    * `ny`: 예보지점 Y 좌표. 예보지점의 Y 좌표값

#### 초단기예보조회
* Endpoint: `getUltraSrtFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getUltraSrtFcst?pageNo=1&numOfRows=1000&dataType=XML&base_date=20210628&base_time=0630&nx=55&ny=127&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `base_date`: 발표일자. ‘21년 6월 28일 발표
    * `base_time`: 발표일자. 06시 발표(정시단위)
    * `nx`: 예보지점 X 좌표. 예보지점의 X 좌표값
    * `ny`: 예보지점 Y 좌표. 예보지점의 Y 좌표값

#### 단기예보조회
* Endpoint: `getVilageFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getVilageFcst?pageNo=1&numOfRows=1000&dataType=XML&base_date=20210628&base_time=0500&nx=55&ny=127&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `base_date`: 발표일자. ‘21년 6월 28일 발표
    * `base_time`: 발표일자. 06시 발표(정시단위)
    * `nx`: 예보지점 X 좌표. 예보지점의 X 좌표값
    * `ny`: 예보지점 Y 좌표. 예보지점의 Y 좌표값

#### 예보버전조회
* Endpoint: `getFcstVersion`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getFcstVersion?pageNo=1&numOfRows=1000&dataType=XML&ftype=ODAM&basedatetime=202106280800&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `basedatetime`: 발표일시분. 각각의 base_time 로 검색
    * `ftype`: 파일구분. 파일구분 -ODAM: 동네예보실황 -VSRT: 동네예보초단기 -SHRT: 동네예보단기

### (그래픽) 동네예보 분포도
* Endpoint: `nph-dfs_shrt_ana_5d_test`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/dfs/nph-dfs_shrt_ana_5d_test?data0=GEMD&data1=PTY&tm_ef=202212260000&tm_fc=202212221400&dtm=H0&map=G1&mask=M&color=E&size=600&effect=NTL&overlay=S&zoom_rate=2&zoom_level=0&zoom_x=0000000&zoom_y=0000000&auto_man=m&mode=I&interval=1&rand=1412&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `data0`: 자료 종류
    * `data1`: 변수 종류
    * `tm_ef`: 기준시간2
    * `tm_fc`: 기준시간1
    * `dtm`: 시간이동단위 및 이동값
    * `map`: 지도 종류
    * `mask`: 이미지 내륙구분
    * `color`: 이미지 색상표
    * `size`: 이미지 크기
    * `effect`: 이미지 효과
    * `overlay`: 이미지 중첩
    * `zoom_rate`: 확대율
    * `auto_man`: 자동(a), 수동(m)
    * `mode`: 표출양식. html(H), image(I), auto(A), file(F)
    * `interval`: 1시간 간격 표출
    * `rand`: 난수: 이미지 재생성 시간간격(분)

### (그래픽) 초단기예보 분포도
* Endpoint: `nph-nph-dfs_shrt_ana_5d_test`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/dfs/nph-dfs_shrt_ana_5d_test?data0=GEMD&data1=PTY&tm_ef=202212260000&tm_fc=202212221400&dtm=H0&map=G1&mask=M&color=E&size=600&effect=NTL&overlay=S&zoom_rate=2&zoom_level=0&zoom_x=0000000&zoom_y=0000000&auto_man=m&mode=I&interval=1&rand=1412&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `tm_fc`: 기준시간1
    * `data0`: 자료 종류
    * `data1`: 변수 종류
    * `tm_ef`: 기준시간2
    * `dtm`: 시간이동단위 및 이동값
    * `map`: 지도 종류
    * `mask`: 이미지 내륙구분
    * `color`: 이미지 색상표
    * `size`: 이미지 크기
    * `effect`: 이미지 효과
    * `overlay`: 이미지 중첩
    * `zoom_rate`: 확대율
    * `auto_man`: 자동(a), 수동(m)
    * `mode`: 표출양식. html(H), image(I), auto(A), file(F)
    * `interval`: 1시간 간격 표출
    * `rand`: 난수: 이미지 재생성 시간간격(분)

### 동네예보 격자데이터 위경도 조회
#### 동네예보 격자데이터 위경도 조회
* Endpoint: `dfs_latlon_api`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_latlon_api?fct=SHRT&latlon=lon&disp=A&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `fct`: 예보종류. SHRT(단기예보), VSRT(초단기예보, 실황)
    * `latlon`: 위도경도 선택. lon(경도), lat(위도).
        * lon 입력시 좌하단에서 우상단으로 이동하며 격자별 위도값 표출
        * lat 입력시 좌하단에서 우상단으로 이동하며 격자별 경도값 표출
    * `disp`: 표출방식. A(ASCII) - 격자점수 + 자료 출력, B(BINARY) - 격자갯수((short)nx * (short)ny)가 정수로 조회(4byte) + 자료가 실수로 조회, 자료 순서는 격자자료가 저장된 순서대로 출력됨

#### 동네예보 격자데이터 위경도 파일(NetCDF) 다운로드
* Endpoint: `dfs_latlon_api`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-dfs_latlon_api?fct=SHRT&latlon=lon&disp=A&authKey=-oe-oHSOQSKHvqB0juEieQ
    ```
* Parameters:
    * `fct`: 예보종류. SHRT(단기예보), VSRT(초단기예보, 실황)

## 중기예보
* 개요 : 중기예보란 예보일로부터 3일에서 10일까지의 기간에 대한 예보를 뜻합니다. 3일에서 7일까지는 오전과 오후로 구분하여 예보하고, 8일에서 10일까지는 일 단위로 구분하여 예보합니다
* 요소 : 기상전망, 최고 · 최저기온, 최고 · 최저기온 범위 상 · 하한값, 강수확률, 날씨(강수형태 및 하늘상태), 파고(해상)
* 지점 : 서울 · 인천 · 경기도, 강원도 영서, 강원도 영동, 충청북도, 대전 · 세종 · 충청남도, 전라북도, 광주 · 전라남도, 대구 · 경상북도, 부산 · 울산 · 경상남도, 제주도
* 보유기간 : 2008년 10월 30일 17:00KST(시행일 기준) ~ 현재
* 생산주기 : 2시부터 3시간 간격(일 8회)
### 중기예보자료(2001년 2월 이후) 조회
#### 중기 예보구역
* Endpoint: `fct_medm_reg.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_medm_reg.php?tmfc=0&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)) 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `mode`: 표출방식. 0 : 예보값만 표시(속도 빠름) 1 : 예보관ID, 예보관명, 예보구역명 포함
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 중기 개황, disp=1(JSON)
* Endpoint: `fct_afs_ws.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_ws.php?stn=&tmfc1=2013121106&tmfc2=2013121118&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)) 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `mode`: 표출방식. 0 : 예보값만 표시(속도 빠름) 1 : 예보관ID, 예보관명, 예보구역명 포함
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 중기 육상예보
* Endpoint: `fct_afs_wl.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_wl.php?reg=&tmfc1=2013121106&tmfc2=2013121118&tmef1=20131214&tmef2=20131219&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)) 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 중기 기온예보
* Endpoint: `fct_afs_wc.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_wc.php?reg=&tmfc1=2013121106&tmfc2=2013121118&tmef1=20131214&tmef2=20131219&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)) 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 중기 해상예보
* Endpoint: `fct_afs_wo.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/fct_afs_wo.php?reg=&tmfc1=2013121106&tmfc2=2013121118&tmef1=20131214&tmef2=20131219&disp=0&help=1&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `stn`: 발표관서번호. 없으면 전체
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc`: YYYYMMDDHHmm(KST). 발표시간. 예보구역조회에서 사용(기준시각의미, 년월일시(KST)) 없으면, 전체 / 0이면, 가장 최근
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmef1`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `tmef2`: YYYYMMDDHHmm(KST). 발효시간 (기간). 기간: [tmef1 ~ tmef2] : 년월일시(KST). 없으면, 해당 발표시간에 예보된 기간 전체
    * `disp`: 표출형태. 0 : 변수별로 일정한 길이 유지, 포트란에 적합 (default) 1 : 구분자(,)로 구분, 엑셀에 적합
    * `help`: 도움말추가. 1(도움말 정보 표시)
### 중기예보 조회

#### 중기해상예보조회
* Endpoint: `getMidSeaFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/MidFcstInfoService/getMidSeaFcst?pageNo=1&numOfRows=10&dataType=XML&regId=12A20000&tmFc=201404080600&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `regId`: 예보구역코드. 12A20000 서해중부, 12B10000 남해서부등.. 하단 참고자료 참조
    * `tmFc`: 발표시각. 
        * 일 2회(06:00,18:00)회 생성 되며 발표시각을 입력
        * YYYYMMDD0600(1800) 최근 24시간 자료만 제공
#### 중기기온조회
* Endpoint: `getMidTa`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/MidFcstInfoService/getMidTa?pageNo=1&numOfRows=10&dataType=XML&regId=11B10101&tmFc=201309030600&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `regId`: 예보구역코드. 11B10101 서울, 11B20201 인천 등 ( 별첨엑셀자료 참고)
    * `tmFc`: 발표시각. 
        * 일 2회(06:00,18:00)회 생성 되며 발표시각을 입력
        * YYYYMMDD0600(1800) 최근 24시간 자료만 제공
#### 중기육상예보조회
* Endpoint: `getMidLandFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/MidFcstInfoService/getMidLandFcst?pageNo=1&numOfRows=10&dataType=XML&regId=11B00000&tmFc=202107300600&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `regId`: 예보구역코드. 11B0000 서울, 인천, 경기도 11D10000 등 (활용가이드 하단 참고자료 참조)
    * `tmFc`: 발표시각. 
        * 일 2회(06:00,18:00)회 생성 되며 발표시각을 입력
        * YYYYMMDD0600(1800) 최근 24시간 자료만 제공
#### 중기전망조회
* Endpoint: `getMidFcst`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/MidFcstInfoService/getMidFcst?pageNo=1&numOfRows=10&dataType=XML&stnId=108&tmFc=201310170600&authKey=R_zkyTnBQfy85Mk5wWH8Ow
    ```
* Parameters:
    * `pageNo`: 페이지 번호
    * `numOfRows`: 한 페이지 결과 수
    * `dataType`: 응답자료형식. 요청자료형식(XML/JSON), Default: XML.
    * `stnId`: 지점번호. 108 전국, 109 서울, 인천, 경기도 등 (활용가이드 하단 참고자료 참조)
    * `tmFc`: 발표시각. 
        * 일 2회(06:00,18:00)회 생성 되며 발표시각을 입력
        * YYYYMMDD0600(1800) 최근 24시간 자료만 제공
## 기상특보
* 개요 : 중기예보란 예보일로부터 3일에서 10일까지의 기간에 대한 예보를 뜻합니다. 3일에서 7일까지는 오전과 오후로 구분하여 예보하고, 8일에서 10일까지는 일 단위로 구분하여 예보합니다
* 요소 : 기상전망, 최고 · 최저기온, 최고 · 최저기온 범위 상 · 하한값, 강수확률, 날씨(강수형태 및 하늘상태), 파고(해상)
* 지점 : 서울 · 인천 · 경기도, 강원도 영서, 강원도 영동, 충청북도, 대전 · 세종 · 충청남도, 전라북도, 광주 · 전라남도, 대구 · 경상북도, 부산 · 울산 · 경상남도, 제주도
* 보유기간 : 2008년 10월 30일 17:00KST(시행일 기준) ~ 현재
* 생산주기 : 2시부터 3시간 간격(일 8회)
### 특.정보 자료 조회
#### 특보구역
* Endpoint: `wrn_reg.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_reg.php?tmfc=0&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `wrn`: 특보종류. W: 강풍, R: 호우, C: 한파, D: 건조, O: 해일, N: 지진해일, V:풍랑, T: 태풍, S: 대설, Y: 황사, H: 폭염, F: 안개 (없으면 전체)
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `subcd`: 날씨해설 부제목코드. 11(초단기), 12(단기), 13(중기), 99(직접입력), 없으면 전체
    * `disp`: 표출단계. 0(기본), 1(+특보내용), 2(+입력자)
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 특보자료
* Endpoint: `wrn_met_data.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_met_data.php?reg=0&wrn=A&tmfc1=201501010000&tmfc2=201502010000&disp=0&help=1&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `wrn`: 특보종류. W: 강풍, R: 호우, C: 한파, D: 건조, O: 해일, N: 지진해일, V:풍랑, T: 태풍, S: 대설, Y: 황사, H: 폭염, F: 안개 (없으면 전체)
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `subcd`: 날씨해설 부제목코드. 11(초단기), 12(단기), 13(중기), 99(직접입력), 없으면 전체
    * `disp`: 표출단계. 0(기본), 1(+특보내용), 2(+입력자)
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 기상정보
* Endpoint: `wrn_inf_rpt.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_inf_rpt.php?tmfc1=201505010000&tmfc2=201506010000&stn=0&disp=0&help=1&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `wrn`: 특보종류. W: 강풍, R: 호우, C: 한파, D: 건조, O: 해일, N: 지진해일, V:풍랑, T: 태풍, S: 대설, Y: 황사, H: 폭염, F: 안개 (없으면 전체)
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `subcd`: 날씨해설 부제목코드. 11(초단기), 12(단기), 13(중기), 99(직접입력), 없으면 전체
    * `disp`: 표출단계. 0(기본), 1(+특보내용), 2(+입력자)
    * `help`: 도움말추가. 1(도움말 정보 표시)
#### 날씨해설
* Endpoint: `wthr_cmt_rpt.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wthr_cmt_rpt.php?tmfc1=202004130000&tmfc2=202004140000&stn=0&subcd=0&disp=0&help=1&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `wrn`: 특보종류. W: 강풍, R: 호우, C: 한파, D: 건조, O: 해일, N: 지진해일, V:풍랑, T: 태풍, S: 대설, Y: 황사, H: 폭염, F: 안개 (없으면 전체)
    * `reg`: 예보구역코드. 없으면 전체
    * `tmfc1`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `tmfc2`: YYYYMMDDHHmm(KST). 발표시간 (기간). 기간: [tmfc1 ~ tmfc2] : 년월일시(KST). 없으면, 가장 최근 발표시간자료
    * `subcd`: 날씨해설 부제목코드. 11(초단기), 12(단기), 13(중기), 99(직접입력), 없으면 전체
    * `disp`: 표출단계. 0(기본), 1(+특보내용), 2(+입력자)
    * `help`: 도움말추가. 1(도움말 정보 표시)
### 특보현황 조회

#### 특보현황 조회(1)
* Endpoint: `wrn_now_data.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_now_data.php?fe=f&tm=&disp=0&help=1&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `fe`: 기준. f: 발표시간기준(default), e: 발효시간기준
    * `tm`:	기준시각. YYYYMMDDHHmm(KST)
    * `help`: 도움말추가. 1(도움말 정보 표시)

#### 특보현황 조회(1)
* Endpoint: `wrn_now_data_new.php`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_now_data_new.php?fe=f&tm=&disp=0&help=1&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `fe`: 기준. f: 발표시간기준(default), e: 발효시간기준
    * `tm`:	기준시각. YYYYMMDDHHmm(KST)
    * `help`: 도움말추가. 1(도움말 정보 표시)

### 특보 발표/발효 현황 이미지 조회

#### 임의지역 특보이미지
* Endpoint: `nph-wrn7`

* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ03/cgi/wrn/nph-wrn7?out=0&tmef=1&city=1&name=0&tm=201611082300&lon=127.7&lat=36.1&range=300&size=685&wrn=W,R,C,D,O,V,T,S,Y,H,&authKey=3vOvAIAXRQKzrwCAF7UC2g
    ```
* Parameters:
    * `tm`: 조회시각(특보 발표시각).  YYYYMMDDHHmm(KST)
    * `lat`: 경도. 임의지역 특보이미지의 중심 경도
    * `lon`: 위도. 임의지역 특보이미지의 중심 위도
    * `range`: 표출반경(km). 특보 이미지의 중심(위경도)으로부터 표출반경
    * `size`: 크기(px). 특보 이미지 크기
    * `tmef`: 발표/발효 구분. 발표/발효 구분 (0:발표시각기준, 1:발효시각기준).
    * `city`: 시군경계. 시군경계 표시유무 (0:미표시, 1:표시).
    * `name`: 행정동명. 행정동명 표시유무 (0:미표시, 1:표시)
    * `stn`: 지방청별 조회. 특보이미지 지방청별 조회(기존 통보문 이미지)
        * 108: 본청, 133: 대전, 159: 부산, 156: 광주, 184: 제주, 105: 강원
    * `wrn`: 특보종류. 특보종류(여러유형 선택시 델리미터(|)로 구분)
        * W: 강풍, R: 호우, C: 한파, D: 건조, O: 해일, N: 지진해일, V:풍랑, T: 태풍, S: 대설, Y: 황사, H: 폭염, F: 안개

## 영향예보
* 개요 : 영향예보는 날씨 뿐만 아니라 시간과 장소에 따라 달라지는 날씨의 영향을 고려하여 기상 현상별 위험수준에 따른 분야별 상세 영향정보와 대응요령을 제공합니다.
이를 통해 유관기관에 실효적 정보를 제공하여 방재업무를 지원하고, 기상재해로부터 국민의 안전을 보호하고자 합니다.
* 요소 : 폭염, 한파(영향 전망, 피해 현황, 기상 전망, 분야별 위험수준 및 대응요령)
* 지점 : 전국 174개 시 · 군 단위 및 4개 산지(특보구역과 동일)
* 보유기간 : 2019년 6월 ~ 현재
* 생산주기 : 발표기준 부합시 일 1회 발표(11시 30분)

Not yet implemented

### 영향예보 발표 현황(발표구역별 위험수준) 조회
Not yet implemented
#### 폭염영향예보 기간 조회(발효시각 기준)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_fct_pstt.php?tmef1=20210701&tmef2=20210730&ifpar=hw&help=1&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 한파영향예보 기간 조회(발표시각 기준)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_fct_pstt.php?tmfc1=20210101&tmfc2=20210131&ifpar=cw&help=1&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 기간, 특보구역 조회(발효시각 기준)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_fct_pstt.php?tmef1=20210701&tmef2=20210730&ifarea=0&regid=L1050100&help=1&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
### 영향예보 위험수준별 발표지역 수 조회
Not yet implemented
#### 기간 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_zone_cnt.php?help=1&tmfc1=20210701&tmfc2=20210730&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 기준일 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_zone_cnt.php?help=1&tmef1=20210701&tmef2=20210730&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 기준일, 영향분야, 관서코드 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_zone_cnt.php?help=1&tmef1=20210701&tmef2=20210730&ifarea=0&stn=108&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 기준일, 위험수준 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_zone_cnt.php?help=1&tmef1=20210701&tmef2=20210730&ilvl=1&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
###  영향예보 위험수준 분포도
Not yet implemented
#### 일 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_dmap.php?tmfc=20220601&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 일, 관서코드 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_dmap.php?tmfc=20220601&stn=108&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 일, 영향예보요소 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_dmap.php?tmfc=20220601&ifpar=hw&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
#### 일, 영향분야 설정
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/ifs_ilvl_dmap.php?tmfc=20220601&ifarea=1&authKey=MIgxK1f5QjaIMStX-dI2PQ
    ```
## 예,특보 구역정보

Not yet implemented
### 예보구역정보 조회서비스
Not yet implemented
#### 예보구역코드조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/FcstZoneInfoService/getFcstZoneCd?pageNo=1&numOfRows=10&dataType=XML&regId=11A00101&authKey=cJGQY1PQTnuRkGNT0H57zQ
    ```
### 특보구역 조회
Not yet implemented
#### 특보구역코드조회
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ02/openApi/WethrBasicInfoService/getWrnZoneCd?pageNo=1&numOfRows=10&dataType=XML&korName=&authKey=cJGQY1PQTnuRkGNT0H57zQ
    ```
### AWS 속한 특보구역 코드 조회
Not yet implemented
#### AWS가 속한 특보구역 코드
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_reg_aws.php?tm=&disp=1&help=1&authKey=cJGQY1PQTnuRkGNT0H57zQ
    ```
#### AWS가 속한 특보구역 코드(특보구역명 포함)
Not yet implemented
* Example URL:
    ```text
    https://apihub.kma.go.kr/api/typ01/url/wrn_reg_aws2.php?tm=&disp=1&help=1&authKey=cJGQY1PQTnuRkGNT0H57zQ
    ```