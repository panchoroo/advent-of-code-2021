# with open('/Users/amieeverett/Sites/advent-of-code-2021/day12/input-test2.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day12/input-test.txt') as f:
    # with open('/Users/amieeverett/Sites/advent-of-code-2021/day12/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]


def findCavePaths(shipData):
    # make a dict with entry for each node, value is paths that connect to it
    mapOfCaves = {}
    for datum in shipData:
        node, connection = datum.split("-")
        if node not in mapOfCaves.keys():
            mapOfCaves[node] = [connection]
        else:
            mapOfCaves[node].append(connection)
        # print("keys", connection not in mapOfCaves.keys())
        # print("upper", connection[0].isupper())
        if connection not in mapOfCaves.keys() and node[0].isupper() and connection != "start":
            mapOfCaves[connection] = [node]
        elif node[0].isupper() and connection != "start" and connection != "end":
            mapOfCaves[connection].append(node)
            # if connection[0].isupper() and connection not in mapOfCaves.keys():
        #     mapOfCaves[connection] = [node]
        # elif connection[0].isupper():
        #     mapOfCaves[node].append(connection)

    print("mapOfCaves", mapOfCaves)

    def pathFinder(start, nodes, caveMap):
        print("start", start, "nodes", nodes)
        print("caveMap", caveMap)
        solutions = []
        newCaveMap = {}
        for key in caveMap.keys():
            newCaveMap[key] = caveMap[key]
        print("newCaMp", newCaveMap)
        if start == "end":
            print(solutions)
            print("---------- ending ------------ ")
            return [start]
        if nodes:
            for n in nodes:
                # for n in mapOfCaves[start].remove(start):
                # if start is lowercase ?
                # newNodes = []
                if n in newCaveMap.keys():
                    new = newCaveMap[n]
                    # print("new", new)
                    # new = []
                    newNodes = []
                    if start in newCaveMap[n] and start[0].islower() and start != "end":
                        for x in new:
                            if x != start:
                                newNodes.append(x)
                        print("newNodes", newNodes)
                        newCaveMap[n] = newNodes
                    else:
                        print("newNodes", newNodes)
                        newNodes = newCaveMap[n]
                else:
                    newNodes = [start]
                # newNodes = mapOfCaves[n]
                print("newNodes", newNodes)
                print("newCaMp", newCaveMap)
                paths = pathFinder(n, newNodes, newCaveMap)
                # print("paths", paths)
                # solutions = []
                for path in paths:
                    if start[0].islower():
                        if path.find(start) < 0:
                            solutions.append(start+","+path)
                            # if n in mapOfCaves.keys() and start in mapOfCaves[n]:
                            #     mapOfCaves[n].remove(start)
                        else:
                            print(solutions)
                            print("&&&&&&&&&& ended here &&&&&&&")
                            return [""]
                    else:
                        solutions.append(start+"."+path)
        else:
            print("boo")
            # return ""
        return solutions
        # start,A,b,A,c,A,end
        # start,A,b,A,end
        # start,A,b,end
        # start,A,c,A,b,A,end
        # start,A,c,A,b,end
        # start,b,A,c,A,end

        # start,b,A,end         'start,b,A.end'
        # start,A,c,A,end       'start,A.c,A.end'
        # start,A,end           'start,A.end'
        # start,b,end           'start,b,end'

        # ['start,A.c,A.b,A.end', 'start,b,A.end', 'start,b,end']

        # tart start nodes['A', 'b']


# caveMap {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start A nodes['c', 'b', 'end']
# caveMap {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start c nodes['A']
# caveMap {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start A nodes['b', 'end']
# caveMap {'start': ['A', 'b'], 'A': ['b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start b nodes['A', 'd', 'end']
# caveMap {'start': ['A', 'b'], 'A': ['b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start A nodes['end']
# returns  --> start,A.c,A.b,A.end

# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start end nodes['A']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start d nodes['b']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'end': ['A']}
# start b nodes['A', 'end']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start A nodes['end']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start end nodes['A']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start end nodes['A']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start b nodes['A', 'end']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start A nodes['end']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start end nodes['A']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
# start end nodes['A']
# caveMap {'start': ['A', 'b'], 'A': ['end'], 'c': ['A'], 'b': ['A', 'end'], 'end': ['A']}
    print(mapOfCaves["start"])
    pathSolutions = pathFinder("start", mapOfCaves["start"], mapOfCaves)
    print(pathSolutions)
    print(len(pathSolutions))  # 10


# Part One solution:
findCavePaths(input)
