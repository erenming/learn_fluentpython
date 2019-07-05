import gc
import objgraph

# gc.set_debug(gc.DEBUG_SAVEALL)
#
# print(gc.get_count())
#
# lst = []
# lst.append(lst)
# list_id = id(lst)
x = []
y = [x, [x], dict(x=x)]
objgraph.show_refs([y], filename='sample-graph.png')
# del lst
# gc.collect()
# for item in gc.garbage:
#     print(item)
#     assert list_id == id(item)

