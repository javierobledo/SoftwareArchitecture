import sys
import scipy.cluster.hierarchy as hcluster
from file import *
import pylab

if(len(sys.argv) == 4):
    mat_name = sys.argv[1]
    mat_filename = sys.argv[2]
    k = int(sys.argv[3])
    data = load_sparse_mat(mat_name, store=mat_filename).A
    clusters = hcluster.fclusterdata(data,k,criterion='maxclust')
    pylab.scatter(*data[:,:], c=clusters)
    pylab.axis("equal")
    title = str(k)+" Clusters"
    print(title)
    pylab.title(title)
    pylab.draw()