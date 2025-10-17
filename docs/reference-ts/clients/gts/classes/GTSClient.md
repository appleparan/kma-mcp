[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/gts](../README.md) / GTSClient

# Class: GTSClient

Defined in: [src/clients/gts.ts:35](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L35)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new GTSClient**(`config`): `GTSClient`

Defined in: [src/clients/gts.ts:36](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L36)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`GTSClient`

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

### getAircraftReports()

> **getAircraftReports**(`tm`): `Promise`\<[`SynopObservation`](../interfaces/SynopObservation.md)[]\>

Defined in: [src/clients/gts.ts:74](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L74)

Get aircraft reports (AIREP)

#### Parameters

##### tm

`string`

Observation time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`SynopObservation`](../interfaces/SynopObservation.md)[]\>

***

### getBuoyObservations()

> **getBuoyObservations**(`tm`): `Promise`\<[`SynopObservation`](../interfaces/SynopObservation.md)[]\>

Defined in: [src/clients/gts.ts:64](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L64)

Get buoy observations from GTS network

#### Parameters

##### tm

`string`

Observation time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`SynopObservation`](../interfaces/SynopObservation.md)[]\>

***

### getShipObservations()

> **getShipObservations**(`tm`): `Promise`\<[`ShipObservation`](../interfaces/ShipObservation.md)[]\>

Defined in: [src/clients/gts.ts:54](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L54)

Get ship observations

#### Parameters

##### tm

`string`

Observation time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`ShipObservation`](../interfaces/ShipObservation.md)[]\>

***

### getSurfaceChart()

> **getSurfaceChart**(`tm`): `Promise`\<[`ChartData`](../interfaces/ChartData.md)[]\>

Defined in: [src/clients/gts.ts:84](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L84)

Get surface weather chart

#### Parameters

##### tm

`string`

Chart time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`ChartData`](../interfaces/ChartData.md)[]\>

***

### getSynopChart()

> **getSynopChart**(`tm`): `Promise`\<[`ChartData`](../interfaces/ChartData.md)[]\>

Defined in: [src/clients/gts.ts:94](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L94)

Get SYNOP chart (observation plot)

#### Parameters

##### tm

`string`

Chart time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`ChartData`](../interfaces/ChartData.md)[]\>

***

### getSynopObservations()

> **getSynopObservations**(`tm`): `Promise`\<[`SynopObservation`](../interfaces/SynopObservation.md)[]\>

Defined in: [src/clients/gts.ts:44](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/gts.ts#L44)

Get SYNOP (land station) observations

#### Parameters

##### tm

`string`

Observation time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`SynopObservation`](../interfaces/SynopObservation.md)[]\>

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
