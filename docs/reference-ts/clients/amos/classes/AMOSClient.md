[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/amos](../README.md) / AMOSClient

# Class: AMOSClient

Defined in: [src/clients/amos.ts:30](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/amos.ts#L30)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new AMOSClient**(`config`): `AMOSClient`

Defined in: [src/clients/amos.ts:31](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/amos.ts#L31)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`AMOSClient`

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

### getAirportObservations()

> **getAirportObservations**(`tm`, `dtm`): `Promise`\<[`AMOSObservation`](../interfaces/AMOSObservation.md)[]\>

Defined in: [src/clients/amos.ts:40](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/amos.ts#L40)

Get aerodrome meteorological observations

#### Parameters

##### tm

`string`

Observation time in YYYYMMDDHHmm format

##### dtm

`number` = `60`

Data time range in minutes before tm (default: 60)

#### Returns

`Promise`\<[`AMOSObservation`](../interfaces/AMOSObservation.md)[]\>

***

### getAmdarData()

> **getAmdarData**(`tm1`, `tm2`, `st`): `Promise`\<[`AMDARData`](../interfaces/AMDARData.md)[]\>

Defined in: [src/clients/amos.ts:53](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/amos.ts#L53)

Get AMDAR aircraft meteorological data

#### Parameters

##### tm1

`string`

Start time in YYYYMMDDHHmm format

##### tm2

`string`

End time in YYYYMMDDHHmm format

##### st

`string` = `'E'`

Station type filter (default: 'E' for all)

#### Returns

`Promise`\<[`AMDARData`](../interfaces/AMDARData.md)[]\>

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
