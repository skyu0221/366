import mountaincar
from Tilecoder import numTilings, numTiles, tilecode
from pylab import *  # includes numpy

numRuns = 50
n = numTiles * 3

part2_return = zeros( [500, 200] )
part2_step   = zeros( [500, 200] )
counter      = 0

def learn(alpha=0.1 / numTilings, epsilon=0.0, numEpisodes=200):
    global counter
    theta1 = -0.001 * rand(n)
    theta2 = -0.001 * rand(n)
    returnSum = 0.0
    
    for episodeNum in range(numEpisodes):

        G = 0.0

        step = 0

        terminate = False

        S = mountaincar.init()

        S_tile = tilecode( S[0], S[1], [-1] * numTilings )

        while not terminate:

            step     += 1

            if random() <= epsilon:
                A = randint( 0, 3 )
            else:
                A = argmax( Qs( S_tile, theta1 + theta2 ) )

            R, S_next = mountaincar.sample( S, A )

            if S_next == None:
                terminate = True
                
            else:
                S_next_tile = tilecode( S_next[0], S_next[1], [-1] * numTilings )

            if randint( 0, 2 ):
                if not terminate:
                    q1     = Qs( S_tile, theta1 )
                    q2     = Qs( S_next_tile, theta2 )
                    update = alpha * ( R + q2[ argmax( q1 ) ] - q1[A] )

                for i in S_tile:

                    theta1[i + A * numTiles] += update

            else:
                if not terminate:
                    q1     = Qs( S_next_tile, theta1 )
                    q2     = Qs( S_tile, theta2 )
                    update = alpha * ( R + q1[ argmax( q2 ) ] - q2[A] )

                for i in S_tile:

                    theta2[i + A * numTiles] += update

            S = S_next
            S_tile = S_next_tile

            G += R
        #print("Episode:", episodeNum, "Steps:", step, "Return: ", G)
        part2_return[episodeNum][counter] = G
        part2_step[episodeNum][counter]   = step
        returnSum += G
    #print("Average return:", returnSum / numEpisodes)
    counter += 1
    return returnSum, theta1, theta2

def myWrite():
    fout = open( 'part2', 'w' )
    for i in range( 500 ):
        for j in range( 200 ):
            fout.write("%i " %part2_step[i][j])
        for j in range( 200 ):
            fout.write("%f " %part2_return[i][j])
        fout.write('\n')
    fout.close()
    


#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF(theta1, theta2):
    fout = open('value', 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            F = [-1] * numTilings
            tilecode(-1.2 + (i * 1.7 / steps), -0.07 + (j * 0.14 / steps), F)
            height = -max(Qs(F, theta1 + theta2 / 2))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()
    
def Qs(tileIndices, theta):
    '''
    Write code to calculate the Q-values for all actions for the state represented by tileIndices
    '''
    q = list()

    for i in range( 3 ):

        q.append( sum( theta[ [ j + i * numTiles for j in tileIndices ] ] ) )

    return q
    

if __name__ == '__main__':
    runSum = 0.0
    for run in range(numRuns):
        returnSum, theta1, theta2 = learn()
        print("%i Runs finished." %run)
        runSum += returnSum
    myWrite()
    print("Overall performance: Average sum of return per run:", end="")
    print(runSum / numRuns)
