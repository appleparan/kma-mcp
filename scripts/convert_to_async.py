#!/usr/bin/env python3
"""Convert sync client to async client."""

import re
import sys
from pathlib import Path


def convert_sync_to_async(sync_content: str, class_name: str) -> str:
    """Convert synchronous client code to asynchronous."""
    async_content = sync_content

    # Replace class name
    async_class_name = f'Async{class_name}'
    async_content = async_content.replace(f'class {class_name}:', f'class {async_class_name}:')
    async_content = async_content.replace(f"'{class_name}'", f"'{async_class_name}'")
    async_content = async_content.replace('"""Client for', '"""Async client for')

    # Update docstring title
    first_line_pattern = r'"""(.+?) API client\.'
    async_content = re.sub(first_line_pattern, r'"""Async \1 API client.', async_content)

    # Replace httpx.Client with httpx.AsyncClient
    async_content = async_content.replace('httpx.Client(', 'httpx.AsyncClient(')

    # Replace context manager methods
    async_content = async_content.replace('def __enter__(self)', 'async def __aenter__(self)')
    async_content = async_content.replace('def __exit__(self', 'async def __aexit__(self')
    async_content = async_content.replace(
        '"""Context manager entry."""', '"""Async context manager entry."""'
    )
    async_content = async_content.replace(
        '"""Context manager exit."""', '"""Async context manager exit."""'
    )

    # Replace close method
    async_content = async_content.replace(
        'def close(self) -> None:\n        """Close the HTTP client."""\n        self._client.close()',  # noqa: E501
        'async def close(self) -> None:\n        """Close the HTTP client."""\n        await self._client.aclose()',  # noqa: E501
    )

    # Add async to all method definitions (except __init__)
    async_content = re.sub(
        r'\n    def (?!__init__)([a-z_]+)\(', r'\n    async def \1(', async_content
    )

    # Add await to all self._make_request calls
    async_content = re.sub(
        r'return self\._make_request\(', r'return await self._make_request(', async_content
    )

    # Add await to client.get() calls
    async_content = re.sub(r'self\._client\.get\(', r'await self._client.get(', async_content)

    # Update example usage in docstrings to use async
    async_content = re.sub(r'>>> client = (\w+)\(', r'>>> async with Async\1(', async_content)
    async_content = re.sub(
        r'>>> data = client\.(\w+)\(', r'>>> ...     data = await client.\1(', async_content
    )

    return async_content


def main() -> None:
    """Convert all sync clients to async."""
    if len(sys.argv) > 1:
        # Convert specific file
        sync_file = Path(sys.argv[1])
        if not sync_file.exists():
            print(f'File not found: {sync_file}')
            sys.exit(1)

        # Extract class name from file
        content = sync_file.read_text()
        class_match = re.search(r'class (\w+Client):', content)
        if not class_match:
            print(f'No client class found in {sync_file}')
            sys.exit(1)

        class_name = class_match.group(1)
        async_content = convert_sync_to_async(content, class_name)

        # Write async version
        async_file = sync_file.parent / f'async_{sync_file.name}'
        async_file.write_text(async_content)
        print(f'Created {async_file}')
    else:
        # Convert all clients
        base_dir = Path(__file__).parent.parent / 'src' / 'kma_mcp'

        # Find all client files
        client_files = []
        for pattern in [
            'surface/*_client.py',
            'forecast/*_client.py',
            'radar/*_client.py',
            'typhoon/*_client.py',
            'marine/*_client.py',
            'upper_air/*_client.py',
            'earthquake/*_client.py',
        ]:
            client_files.extend(base_dir.glob(pattern))

        # Filter out async files
        client_files = [f for f in client_files if not f.name.startswith('async_')]

        for sync_file in client_files:
            content = sync_file.read_text()
            class_match = re.search(r'class (\w+Client):', content)
            if not class_match:
                continue

            class_name = class_match.group(1)
            async_content = convert_sync_to_async(content, class_name)

            async_file = sync_file.parent / f'async_{sync_file.name}'
            async_file.write_text(async_content)
            print(f'Created {async_file}')


if __name__ == '__main__':
    main()
