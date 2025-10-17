[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/forecast](../README.md) / ForecastClient

# Class: ForecastClient

Defined in: [src/clients/forecast.ts:16](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/forecast.ts#L16)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new ForecastClient**(`config`): `ForecastClient`

Defined in: [src/clients/forecast.ts:17](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/forecast.ts#L17)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`ForecastClient`

#### Overrides

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`constructor`](../../base/classes/BaseKMAClient.md#constructor)

## Properties

### authKey

> `protected` **authKey**: `string`

Defined in: [src/clients/base.ts:43](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L43)

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`authKey`](../../base/classes/BaseKMAClient.md#authkey)

***

### client

> `protected` **client**: `AxiosInstance`

Defined in: [src/clients/base.ts:42](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L42)

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`client`](../../base/classes/BaseKMAClient.md#client)

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

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`formatDateTime`](../../base/classes/BaseKMAClient.md#formatdatetime)

***

### getMediumTermForecast()

> **getMediumTermForecast**(`tmFc`, `stn`): `Promise`\<[`ForecastData`](../interfaces/ForecastData.md)[]\>

Defined in: [src/clients/forecast.ts:38](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/forecast.ts#L38)

Get medium-term weather forecast (3-10 days)

#### Parameters

##### tmFc

`string`

Forecast time in YYYYMMDDHHmm format

##### stn

Station/region code (0 for all regions)

`string` | `number`

#### Returns

`Promise`\<[`ForecastData`](../interfaces/ForecastData.md)[]\>

***

### getShortTermForecast()

> **getShortTermForecast**(`tmFc`, `stn`): `Promise`\<[`ForecastData`](../interfaces/ForecastData.md)[]\>

Defined in: [src/clients/forecast.ts:26](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/forecast.ts#L26)

Get short-term weather forecast (up to 3 days)

#### Parameters

##### tmFc

`string`

Forecast time in YYYYMMDDHHmm format

##### stn

Station/region code (0 for all regions)

`string` | `number`

#### Returns

`Promise`\<[`ForecastData`](../interfaces/ForecastData.md)[]\>

***

### getWeeklyForecast()

> **getWeeklyForecast**(`tmFc`, `stn`): `Promise`\<[`ForecastData`](../interfaces/ForecastData.md)[]\>

Defined in: [src/clients/forecast.ts:50](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/forecast.ts#L50)

Get weekly weather forecast

#### Parameters

##### tmFc

`string`

Forecast time in YYYYMMDDHHmm format

##### stn

Station/region code (0 for all regions)

`string` | `number`

#### Returns

`Promise`\<[`ForecastData`](../interfaces/ForecastData.md)[]\>

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

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`makeRequest`](../../base/classes/BaseKMAClient.md#makerequest)
