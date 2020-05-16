def sparsify(adj_dict):
    """
    This function takes in an adjacency dictionary(adj_dict) and returns the corresponding sparse matrix as a list of lists. For example if we have: adj_dict= {"A": {"B":1}, "B":{"C":2}, "C":{"A":1,"D":1}, "D":{}}, the sparse matrix would be represented by: [ [0, 0, 1, 0], [1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 1, 0] ] 
    """
    for k, v in adj_dict.items():
        assert type(k) == str and k.isupper(), "Error"
        for l, u in v.items():
            assert type(l) == str and l.isupper(), "Error"
            assert type(u) == int, "Error"
    
    x = len(adj_dict)
    indices, val = {}, 0
    for _ in sorted(adj_dict):
        indices[_] = val
        val += 1
    matrix = [[0 for i in range(x)] for i in range(x)]
    n_adj_dict = {}
    for j in sorted(adj_dict):
        n_adj_dict[j] = adj_dict.get(j)
    a = 0
    for node, pair in n_adj_dict.items():
        for m, t in pair.items():
            temp = indices.get(m)
            matrix[temp][a] = t
        a += 1
    return matrix
    
print(sparsify({"A" :{"B": 2,"D":4}, "D": {"B": 1}, "C": {"A": 3, "D": 1},  "B": {"C": 1}}))

print("\n")

print(sparsify({"A" : {"B": 1}, "B":{"C":2}, "C":{"A":1,"D":1}, "D":{}, "E": {"C": 8}}))

print(sparsify({}))