from scipy.sparse import csr_matrix, rand
import tables_test as tb

a = rand(2000, 2000, format='csr')  # imagine that many values are stored in this matrix and that sparsity is low
b = a.T
l, m, n = a.shape[0], a.shape[1], b.shape[1]

f = tb.open_file('dot.h5', 'w')
filters = tb.Filters(complevel=5, complib='blosc')
out = f.create_carray(f.root, 'data', tb.Float32Atom(), shape=(l, n), filters=filters)

bl = 1000  # this is the number of rows we calculate each loop
# this may not the most efficient value
# look into buffersize usage in PyTables and adopt the buffersite of the
# carray accordingly to improve specifically fetching performance

b = b.tocsc()  # we slice b on columns, csc improves performance

# this can also be changed to slice on rows instead of columns
for i in range(0, l, bl):
    out[:, i:min(i + bl, l)] = (a.dot(b[:, i:min(i + bl, l)])).toarray()

f.close()