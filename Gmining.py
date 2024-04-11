import networkx as nx
from timeit import default_timer as timer

nodes_dic = {}
nodes = set()
neighbor_table = {}
all_time = 0
matches_num = 0


def neighborhood(v, G):
    return {edge[1] for edge in G.edges(v)}


# fu = [1,2,3,4] 1 is the common vertex
def updates_neighborhood(fu, G):
    global neighbor_table
    adjacent_list = []
    for node in fu:
        if node in neighbor_table:
            print('success found in neighbor_table')
        else:
            a = neighborhood(node, G)
            neighbor_table.setdefault(node, a)
            adjacent_list.extend(a)
    return adjacent_list


def G1(v_list, fu, sub_updates):
    sub_update = [fu[0]]
    sub_update.extend(v_list)
    sub_updates.append(sub_update)
    # print(v_list)
    # patterns_num = 4
    if len(v_list) == (4 - 2):
        return

    else:
        for vertex in fu[1:]:
            if vertex > v_list[-1]:
                v_list.append(vertex)
                G1(v_list, fu, sub_updates)
                v_list.pop()

    return


def generate(fu):
    sub_updates = []
    # 除去common vertex
    for vertex in fu[1:]:
        G1([vertex], fu, sub_updates)
    return sub_updates


def filter(extended, G):
    global matches_num
    if len(extended) == 4:
        print(extended)
        matches_num = matches_num + 1


def exploring(sub_u, v_list, ad_list, G):
    if len(v_list) > (4-2):
        return
    global neighbor_table
    if len(v_list) == 1:
        v = v_list[0]
        parent_list = neighbor_table[v]
        if len(parent_list) == 1:
            key = parent_list[0]
            for update in sub_u:
                if len(update) == 3 and key in update:
                    update.append(v)
                    filter(update, G)
                    update.pop()
        elif fu[0] in parent_list:
            key = fu[0]
            for update in sub_u:
                if len(update) == 3 and key in update:
                    update.append(v)
                    filter(update, G)
                    update.pop()
                    neighbor_list = neighborhood(v, G)
                    ad_list.update(neighbor_list)
        else:
            # contains_flag = False 需要限制一下2 3 4 5都与顶点为邻居的情况
            for ver in parent_list:
                for update in sub_u:
                    if len(update) == 3 and ver in update:
                        update.append(v)
                        filter(update, G)
                        update.pop()

    for ad in ad_list:
        if ad > ad_list[-1]:
            v_list.append(ad)
            exploring(sub_u, v_list, ad_list, G)
            v_list.pop()


def explore(fu, G):
    global neighbor_table
    global matches_num
    adjacent_list = updates_neighborhood(fu, G)

    neighbor_table = {'1': ['8', '10', '15', '17', '19'], '2': ['11'], '3': ['16'], '4': ['14'], '5': ['15'],
                      '8': ['1'], '10': ['1'], '11': ['2'], '14': ['4'], '15': ['1', '5'], '16': ['3'],
                      '17': ['1'], '19': ['1']}
    adjacent_list = ['8', '10', '15', '17', '19', '11', '16', '14', '15']
    adjacent_vertices = set(adjacent_list)
    print("adjacent_vertices is ", adjacent_vertices)

    # 生成挖掘子结构
    sub_updates = generate(fu)
    print("sub updates are ", sub_updates)

    for v in adjacent_vertices:
        exploring(sub_updates, [v], adjacent_vertices, G)


def fuse(updates):
    update_G = nx.Graph()

    for line in updates:
        [u, v] = line.split()
        if not update_G.has_node(u):
            update_G.add_node(u)
        if not update_G.has_node(v):
            update_G.add_node(v)
        update_G.add_edge(u, v)

    common_vertices = sorted(update_G.degree, key=lambda x: x[1], reverse=True)
    print(common_vertices)
    fusion_updates = []
    for line in common_vertices:
        # line[0] is vertex  line[1] is the degree
        v = line[0]
        if update_G.has_node(v) and update_G.degree(v) > 1:
            fu = [v]
            neighbors = update_G.edges(v)
            for vs in neighbors:
                fu.append(vs[1])
            fusion_updates.append(fu)
            update_G.remove_node(v)

    return fusion_updates



def set_all_time(alltime):
    global all_time
    all_time = all_time + alltime


def get_all_time():
    return all_time


updates = ['1 2', '1 3', '1 4', '1 5', '2 5', '2 8']
G = nx.Graph()
start = timer()
fusion_updates_list = fuse(updates)
for fu in fusion_updates_list:
    explore(fu, G)
end = timer()
set_all_time((end - start))
print(' all_time is %0.6f seconds' % get_all_time())
print('matches_num is %d' % matches_num)
