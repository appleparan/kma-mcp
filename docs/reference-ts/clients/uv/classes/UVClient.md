[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/uv](../README.md) / UVClient

# Class: UVClient

Defined in: [src/clients/uv.ts:15](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/uv.ts#L15)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new UVClient**(`config`): `UVClient`

Defined in: [src/clients/uv.ts:16](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/uv.ts#L16)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`UVClient`

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

> **getDailyData**(`tm`, `stn`): `Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

Defined in: [src/clients/uv.ts:58](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/uv.ts#L58)

Get daily UV observation data for a single day

#### Parameters

##### tm

Date in YYYYMMDD format or Date object

`string` | `Date`

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

***

### getDailyPeriod()

> **getDailyPeriod**(`tm1`, `tm2`, `stn`): `Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

Defined in: [src/clients/uv.ts:72](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/uv.ts#L72)

Get daily UV observation data for a date range

#### Parameters

##### tm1

Start date in YYYYMMDD format or Date object

`string` | `Date`

##### tm2

End date in YYYYMMDD format or Date object

`string` | `Date`

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

***

### getHourlyData()

> **getHourlyData**(`tm`, `stn`): `Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

Defined in: [src/clients/uv.ts:25](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/uv.ts#L25)

Get hourly UV observation data for a single time

#### Parameters

##### tm

Time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

***

### getHourlyPeriod()

> **getHourlyPeriod**(`tm1`, `tm2`, `stn`): `Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

Defined in: [src/clients/uv.ts:39](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/uv.ts#L39)

Get hourly UV observation data for a time period

#### Parameters

##### tm1

Start time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### tm2

End time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`UVObservation`](../interfaces/UVObservation.md)[]\>

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
