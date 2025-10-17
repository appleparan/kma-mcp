[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/base](../README.md) / KMAResponse

# Interface: KMAResponse\<T\>

Defined in: [src/clients/base.ts:12](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L12)

## Type Parameters

### T

`T` = `unknown`

## Properties

### response

> **response**: `object`

Defined in: [src/clients/base.ts:13](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L13)

#### body

> **body**: `object`

##### body.dataType

> **dataType**: `string`

##### body.items?

> `optional` **items**: `object`

##### body.items.item

> **item**: `T`[]

##### body.numOfRows?

> `optional` **numOfRows**: `number`

##### body.pageNo?

> `optional` **pageNo**: `number`

##### body.totalCount?

> `optional` **totalCount**: `number`

#### header

> **header**: `object`

##### header.resultCode

> **resultCode**: `string`

##### header.resultMsg

> **resultMsg**: `string`
