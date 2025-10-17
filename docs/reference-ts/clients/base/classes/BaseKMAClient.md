[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/base](../README.md) / BaseKMAClient

# Abstract Class: BaseKMAClient

Defined in: [src/clients/base.ts:41](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L41)

## Extended by

- [`AMOSClient`](../../amos/classes/AMOSClient.md)
- [`ASOSClient`](../../asos/classes/ASOSClient.md)
- [`AWSClient`](../../aws/classes/AWSClient.md)
- [`AWSOAClient`](../../aws_oa/classes/AWSOAClient.md)
- [`BuoyClient`](../../buoy/classes/BuoyClient.md)
- [`ClimateClient`](../../climate/classes/ClimateClient.md)
- [`DustClient`](../../dust/classes/DustClient.md)
- [`EarthquakeClient`](../../earthquake/classes/EarthquakeClient.md)
- [`ForecastClient`](../../forecast/classes/ForecastClient.md)
- [`GTSClient`](../../gts/classes/GTSClient.md)
- [`IntegratedClient`](../../integrated/classes/IntegratedClient.md)
- [`NKClient`](../../nk/classes/NKClient.md)
- [`RadarClient`](../../radar/classes/RadarClient.md)
- [`RadiosondeClient`](../../radiosonde/classes/RadiosondeClient.md)
- [`SatelliteClient`](../../satellite/classes/SatelliteClient.md)
- [`SeasonClient`](../../season/classes/SeasonClient.md)
- [`SnowClient`](../../snow/classes/SnowClient.md)
- [`StationClient`](../../station/classes/StationClient.md)
- [`TyphoonClient`](../../typhoon/classes/TyphoonClient.md)
- [`UVClient`](../../uv/classes/UVClient.md)
- [`WarningClient`](../../warning/classes/WarningClient.md)

## Constructors

### Constructor

> **new BaseKMAClient**(`config`): `BaseKMAClient`

Defined in: [src/clients/base.ts:45](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L45)

#### Parameters

##### config

[`KMAClientConfig`](../interfaces/KMAClientConfig.md)

#### Returns

`BaseKMAClient`

## Properties

### authKey

> `protected` **authKey**: `string`

Defined in: [src/clients/base.ts:43](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L43)

***

### client

> `protected` **client**: `AxiosInstance`

Defined in: [src/clients/base.ts:42](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L42)

## Methods

### formatDateTime()

> `protected` **formatDateTime**(`date`, `includeTime`): `string`

Defined in: [src/clients/base.ts:96](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L96)

Format datetime to KMA API format (YYYYMMDDHHmm or YYYYMMDD)

#### Parameters

##### date

`Date`

##### includeTime

`boolean` = `true`

#### Returns

`string`

***

### makeRequest()

> `protected` **makeRequest**\<`T`\>(`endpoint`, `params`): `Promise`\<`T`[]\>

Defined in: [src/clients/base.ts:56](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L56)

#### Type Parameters

##### T

`T` = `unknown`

#### Parameters

##### endpoint

`string`

##### params

`Record`\<`string`, `unknown`\>

#### Returns

`Promise`\<`T`[]\>
