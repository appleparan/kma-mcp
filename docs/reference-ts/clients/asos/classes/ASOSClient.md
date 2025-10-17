[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/asos](../README.md) / ASOSClient

# Class: ASOSClient

Defined in: [src/clients/asos.ts:33](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L33)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new ASOSClient**(`config`): `ASOSClient`

Defined in: [src/clients/asos.ts:34](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L34)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`ASOSClient`

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

### getDailyData()

> **getDailyData**(`tm`, `stn`): `Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

Defined in: [src/clients/asos.ts:76](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L76)

Get daily ASOS observation data for a single date

#### Parameters

##### tm

Date in YYYYMMDD format or Date object

`string` | `Date`

##### stn

`number` = `0`

Station ID (0 for all stations)

#### Returns

`Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

***

### getDailyPeriod()

> **getDailyPeriod**(`tm1`, `tm2`, `stn`): `Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

Defined in: [src/clients/asos.ts:90](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L90)

Get daily ASOS observation data for a date range

#### Parameters

##### tm1

Start date in YYYYMMDD format or Date object

`string` | `Date`

##### tm2

End date in YYYYMMDD format or Date object

`string` | `Date`

##### stn

`number` = `0`

Station ID (0 for all stations)

#### Returns

`Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

***

### getElementData()

> **getElementData**(`tm1`, `tm2`, `stn`, `element`): `Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

Defined in: [src/clients/asos.ts:111](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L111)

Get specific weather element data

#### Parameters

##### tm1

Start time

`string` | `Date`

##### tm2

End time

`string` | `Date`

##### stn

`number`

Station ID

##### element

`string`

Element code (e.g., 'ta' for temperature, 'rn' for precipitation)

#### Returns

`Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

***

### getHourlyData()

> **getHourlyData**(`tm`, `stn`): `Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

Defined in: [src/clients/asos.ts:43](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L43)

Get hourly ASOS observation data for a single time

#### Parameters

##### tm

Time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### stn

`number` = `0`

Station ID (0 for all stations)

#### Returns

`Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

***

### getHourlyPeriod()

> **getHourlyPeriod**(`tm1`, `tm2`, `stn`): `Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

Defined in: [src/clients/asos.ts:57](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/asos.ts#L57)

Get hourly ASOS observation data for a time period

#### Parameters

##### tm1

Start time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### tm2

End time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### stn

`number` = `0`

Station ID (0 for all stations)

#### Returns

`Promise`\<[`ASOSObservation`](../interfaces/ASOSObservation.md)[]\>

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
