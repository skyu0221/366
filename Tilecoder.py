from math import floor

numTilings = 4
tilingSize = [ 9, 9 ]
xBound     = [ -1.2, 0.5 ]
yBound     = [ -0.07, 0.07 ]
numTiles   = numTilings * tilingSize[0] * tilingSize[1]

def tilecode(in1, in2, tileIndices):

    in1 = in1 - xBound[0]
    in2 = in2 - yBound[0]

    for i in range( len( tileIndices ) ):
        x              = xBound[1] - xBound[0]
        y              = yBound[1] - yBound[0]
        offset_x       = -1 / numTilings * x / ( tilingSize[0] - 1 )
        offset_y       = -1 / numTilings * y / ( tilingSize[1] - 1 )
        tileSize       = [ x / ( tilingSize[0] - 1 ), \
                           y / ( tilingSize[0] - 1 ) ]
        tileIndices[i] = int( floor( ( in1 - i * offset_x ) / tileSize[0] ) + \
                              floor( ( in2 - i * offset_y ) / tileSize[1]) * 9 \
                              + i * 81 )
    return tileIndices
    
    
def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2,') are : ', tileIndices)

if __name__ == '__main__':
    printTileCoderIndices(-1.2, -0.07)
    printTileCoderIndices(-1.2, 0.07)    
    printTileCoderIndices(0.5, -0.07)    
    printTileCoderIndices(0.5, 0.07)
    printTileCoderIndices(-0.35, 0.0)
    printTileCoderIndices(0.0, 0.0)
    
