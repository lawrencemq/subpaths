from pprint import pprint
from subpaths.subpaths import find_all_subpath_occurrences

path_a = [1, 2, 3, 4, 5]

pprint(find_all_subpath_occurrences(path_a))

path_b = [3, 4, 5, 7]
path_c = [2, 3, 4, 8, 9, 7]

pprint(find_all_subpath_occurrences(path_a, path_b, path_c))