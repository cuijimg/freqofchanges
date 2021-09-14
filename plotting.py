import matplotlib.pyplot as plt
import datetime as dt
# dict1 = {'2012-01-01': 0, '2012-04-01': 351, '2012-07-01': 248, '2012-10-01': 224, '2013-01-01': 299, '2013-04-01': 294, '2013-07-01': 375, '2013-10-01': 385, '2014-01-01': 332, '2014-04-01': 332, '2014-07-01': 415, '2014-10-01': 473, '2015-01-01': 740, '2015-04-01': 502, '2015-07-01': 617, '2015-10-01': 544, '2016-01-01': 1313, '2016-04-01': 1104, '2016-07-01': 749, '2016-10-01': 1074, '2017-01-01': 644, '2017-04-01': 572, '2017-07-01': 619, '2017-10-01': 477, '2018-01-01': 382, '2018-04-01': 888, '2018-07-01': 5611, '2018-10-01': 1328, '2019-01-01': 1552, '2019-04-01': 1904, '2019-07-01': 880, '2019-10-01': 1848, '2020-01-01': 1966, '2020-04-01': 610, '2020-07-01': 9718, '2020-10-01': 2763}
# print(dt.date(list(dict1.keys())))
# plt.hist(date(dict1.keys()), dict1.values(), color='g', label = "histgram")
# plt.show()

import os
from collections import Counter
import numpy as np
import xlrd
import pandas as pd
import time
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

sdate = dt.date(2012,1,1)
edate = dt.date(2020,12,31)
timeline =pd.date_range(sdate,edate,freq='qs')
timeline=list(timeline)

dict1 = {'2012-01-01': 0, '2012-04-01': 30, '2012-07-01': 17, '2012-10-01': 15, '2013-01-01': 22, '2013-04-01': 28, '2013-07-01': 20, '2013-10-01': 34, '2014-01-01': 30, '2014-04-01': 23, '2014-07-01': 34, '2014-10-01': 33, '2015-01-01': 46, '2015-04-01': 28, '2015-07-01': 26, '2015-10-01': 34, '2016-01-01': 51, '2016-04-01': 61, '2016-07-01': 48, '2016-10-01': 37, '2017-01-01': 46, '2017-04-01': 33, '2017-07-01': 37, '2017-10-01': 31, '2018-01-01': 34, '2018-04-01': 67, '2018-07-01': 292, '2018-10-01': 178, '2019-01-01': 86, '2019-04-01': 133, '2019-07-01': 93, '2019-10-01': 116, '2020-01-01': 152, '2020-04-01': 72, '2020-07-01': 604, '2020-10-01': 296}
print(timeline)
plt.plot(timeline, dict1.values(), color='g', label = "histgram")
plt.show()


# timeline = [1,2,3]
# a = [34,56,23]
# plt.bar(timeline, a, color='g', label = "histgram")
# plt.show()
plt.savefig(r'C:\Users\f-cui\Desktop\mostchanges\hist.jpg')


######################################################################
# ~ x = pd.date_range(start='2003-1',periods=198,freq='1M')

# ~ fig, ax1 = plt.subplots()
# ~ ax2 = ax1.twinx()

# ~ ax1.plot(x,comm,'--',label='MP',color='r')
# ~ ax2.plot(x,AI_t,label='AI',color='b')


# ~ plt.title('compare')
# ~ ax1.set_ylabel('MP')
# ~ ax2.set_ylabel('AI')

# ~ ax1.legend(loc=2)
# ~ ax2.legend(loc=1)
# ~ plt.show()