"""Module tests"""

from mercantile import Tile
import pytest

import mbtiles


@pytest.mark.parametrize('tile',
                         [Tile(36, 73, 7), Tile(0, 0, 0), Tile(1, 1, 1)])
def test_process_tile(data, tile):
    mbtiles.init_worker(
        str(data.join('RGB.byte.tif')), {
            'driver': 'PNG',
            'dtype': 'uint8',
            'nodata': 0,
            'height': 256,
            'width': 256,
            'count': 3,
            'crs': 'EPSG:3857'},
        'nearest')
    t, contents = mbtiles.process_tile(tile)
    assert t.x == tile.x
    assert t.y == tile.y
    assert t.z == tile.z
