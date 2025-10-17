[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/radar](../README.md) / RadarClient

# Class: RadarClient

Defined in: [src/clients/radar.ts:21](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/radar.ts#L21)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new RadarClient**(`config`): `RadarClient`

Defined in: [src/clients/radar.ts:22](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/radar.ts#L22)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`RadarClient`

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

### getRadarImage()

> **getRadarImage**(`tm`, `radarId`): `Promise`\<[`RadarImage`](../interfaces/RadarImage.md)[]\>

Defined in: [src/clients/radar.ts:31](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/radar.ts#L31)

Get radar image for a specific time

#### Parameters

##### tm

Observation time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### radarId

`string` = `'KWK'`

Radar station ID (default: 'KWK' for nationwide composite)

#### Returns

`Promise`\<[`RadarImage`](../interfaces/RadarImage.md)[]\>

***

### getRadarImageSequence()

> **getRadarImageSequence**(`tm1`, `tm2`, `radarId`): `Promise`\<[`RadarImage`](../interfaces/RadarImage.md)[]\>

Defined in: [src/clients/radar.ts:45](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/radar.ts#L45)

Get radar image sequence (animation)

#### Parameters

##### tm1

Start time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### tm2

End time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### radarId

`string` = `'KWK'`

Radar station ID (default: 'KWK')

#### Returns

`Promise`\<[`RadarImage`](../interfaces/RadarImage.md)[]\>

***

### getRadarReflectivity()

> **getRadarReflectivity**(`tm`, `lat`, `lon`): `Promise`\<[`RadarReflectivity`](../interfaces/RadarReflectivity.md)[]\>

Defined in: [src/clients/radar.ts:65](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/radar.ts#L65)

Get radar reflectivity data for a specific location

#### Parameters

##### tm

Observation time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### lat

`number`

Latitude

##### lon

`number`

Longitude

#### Returns

`Promise`\<[`RadarReflectivity`](../interfaces/RadarReflectivity.md)[]\>

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
