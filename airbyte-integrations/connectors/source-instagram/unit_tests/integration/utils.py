#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


from typing import List, Optional

from airbyte_cdk.models import AirbyteStateMessage, ConfiguredAirbyteCatalog, SyncMode
from airbyte_cdk.test.catalog_builder import CatalogBuilder
from airbyte_cdk.test.entrypoint_wrapper import EntrypointOutput, read

from ..conftest import get_source
from .config import ConfigBuilder


def catalog(stream_name: str, sync_mode: SyncMode) -> ConfiguredAirbyteCatalog:
    return CatalogBuilder().with_stream(stream_name, sync_mode).build()


def config() -> ConfigBuilder:
    return ConfigBuilder()


def read_output(
    config_builder: ConfigBuilder,
    stream_name: str,
    sync_mode: SyncMode,
    state: Optional[List[AirbyteStateMessage]] = None,
    expecting_exception: Optional[bool] = False,
) -> EntrypointOutput:
    _catalog = catalog(stream_name, sync_mode)
    _config = config_builder.build()
    return read(get_source(config=_config), _config, _catalog, state, expecting_exception)
