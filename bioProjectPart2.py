import math
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as pyplot2


def NB_CC(hostPop, paraPop, r, c, a, k, years):
    '''
    description: model to observe population sizes over time of host and
    parasite populations and learn how various factors impact the populations.

    parameters: hostPop - host population sizes
                paraPop - parasite population size
                e ** r - average number of surviving offspring from an
                unifected host
                c - average number of eggs that hatch inside a single host
                a - scaling factor describing the searching efficency or
                 search
                area of the parasitoids (higher is more efficient)
                k - carrying capacity

    Return value: hostPop and paraPop
    '''
    hostPoplist = []
    paraPoplist = []

    while (hostPop < K):
        for years in range(years):
            hostPop = hostPop * (math.e ** -a * (paraPop)) * (math.e ** r * (1-hostPop / K)
            paraPop = hostPop * (1 - (math.e ** -a * (paraPop)))
            hostPoplist.append(hostPop)
            paraPoplist.append(paraPop)

        columns = ('years', 'hostPop')

        pyplot.plot(range(years + 1), hostPoplist)
        pyplot.ylabel('hostPop')
        pyplot.xlabel('years')
        pyplot.show()

        pyplot2.plot((range(years + 1), paraPoplist))
        pyplot2.ylabel('paraPop')
        pyplot2.xlabel('years')
        pyplot2.show()

            # print(hostPoplist, years)

NB_CC(24, 12, 1.5, 1, 0.056, 40, 35)
