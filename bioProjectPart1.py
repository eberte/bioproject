import math
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as pyplot2

def NB(hostPop, paraPop, r, c, a, years):
    '''
    description: model to observe population sizes over time of host and
    parasite populations and learn how various factors impact the populations.
    parameters: hostPop - host population sizes
                paraPop - parasite population size
                r - average number of surviving offspring from a unifected host
                c - average number of eggs that hatch inside a single host
                a - scaling factor describing the searching efficency or search
                area of the parasitoids (higher is more efficient)

    Return value: hostPop and paraPop
    '''
    hostPoplist = []
    paraPoplist = []

    for years in range(years):
        hostPop = hostPop * (math.exp(-a * (paraPop)))
        paraPop = hostPop * (1 - (math.exp(-a * (paraPop))))
        hostPoplist.append(hostPop)
        paraPoplist.append(paraPop)

    columns = ['years', 'hostPop']

    pyplot.plot(range(years + 1), hostPoplist)
    pyplot.plot(range(years + 1), paraPoplist)
    pyplot.ylabel('hostPop(b) and paraPop(g)')
    pyplot.xlabel('years')
    pyplot.show()

    # pyplot2.plot(range(years + 1), paraPoplist)
    # pyplot2.ylabel('paraPop')
    # pyplot2.xlabel('years')
    # pyplot2.show()

    # print(hostPoplist, years)


NB(24, 17, 2, 1, .09, 5)
