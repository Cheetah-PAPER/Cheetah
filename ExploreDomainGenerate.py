from disjoint_set import DisjointSet
import networkx as nx
import openpyxl
import pandas as pd


list_s = set()
ds = DisjointSet()
result_dic = {}


def neighborhood(e, G):
    global i
    edges = []
    for vex in e:
        s = G._node[vex]['times']
        s = s + 1
        G._node[vex]['times'] = s
    edges1 = G.edges(e)
    for edge in edges1:
        edges.append(edge[1])
    return edges


def mining(G, c):
    global list_s
    if len(c) == 4:
        return
    else:
        V = set(neighborhood(c, G))
        list_s |= V
        for v in V:
            if v not in c:
                c.append(v)
                # LOG.debug('%s' % str(c))
                # LOG.debug('%s %s' % (str(c), 'F'))
                mining(G, c)
                c.pop()


def process_set():
    global list_s
    global ds
    list_l = list(list_s)
    begin_v = list_l[0]
    for v in list_l[1:]:
        ds.union(begin_v, v)


    # print(list_ds[1])
    # print(list_ds[1][0])


G = nx.Graph()
i = 0
file_path = 'D:/study/codes/python/workongraph/wiki-talk-temporal-static.txt'
for line in open(file_path):
    # i = i + 1
    # if i < 10000 and (i % 1000 == 0) or i % 100000 == 0:
    #     print(i)
    [u, v] = line.split()
    if not G.has_node(u):
        G.add_node(u, domain='0', times=0)
    if not G.has_node(v):
        G.add_node(v, domain='0', times=0)
    G.add_edge(u, v)


update_file_path = 'D:/study/codes/python/workongraph/wiki-talk-temporal-static.txt'
updates = []
for line in open(update_file_path):
    [u, v] = line.split()
    updates.append([u, v])

# updates = [['1', '3'], ['4', '5']]
for i, update in enumerate(updates):
    G.add_node(update[0], domain='0', times=0)
    G.add_node(update[1], domain='0', times=0)
    G.add_edge(update[0], update[1])
    if i == 1000:
        break
    list_s.clear()
    list_s.add(update[0])
    list_s.add(update[1])
    mining(G, update)
    process_set()

list_ds = list(ds)
print(list_ds)
for vec in list_ds:
    if vec[1] in result_dic:
        reset = result_dic.get(vec[1]) + 1
        result_dic[vec[1]] = reset
    else:
        result_dic[vec[1]] = 1

print('domain size is \n')
print(result_dic)

times_dic = {}
for vertex in G.nodes:
    domain = ds.find(vertex)
    if domain in times_dic:
        reset = times_dic.get(domain)
        reset = reset + G._node[vertex]['times']
        times_dic[domain] = reset
    else:
        if G._node[vertex]['times'] != 0:
            times_dic[domain] = G._node[vertex]['times']

print('times is \n')
print(times_dic)


df = pd.DataFrame(list(times_dic.items()))
df.to_excel('times.xlsx')

df = pd.DataFrame(list(result_dic.items()))
df.to_excel('domain_size.xlsx')

