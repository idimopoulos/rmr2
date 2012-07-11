import hadoopy
import hadoopy_hbase
import time
import logging
logging.basicConfig(level=logging.DEBUG)

st = time.time()

out = 'out-%f/0' % st
hadoopy_hbase.launch_frozen('testtable', out, 'hbase_test_job.py', columns=['colfam1:'])
results = hadoopy.readtb(out)
print([results.next() for x in range(2)])

out = 'out-%f/1' % st
hadoopy_hbase.launch_frozen('testtable', out, 'hbase_test_job.py')
results = hadoopy.readtb(out)
print([results.next() for x in range(2)])

out = 'out-%f/2' % st
hadoopy_hbase.launch_frozen('testtable', out, 'hbase_test_job2.py')
results = hadoopy.readtb(out)
print([results.next() for x in range(2)])
