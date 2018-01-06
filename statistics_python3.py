'''

Mean, Standard Deviation

'''

import statistics

example_list = [3, 5, 6, 53, 2, 1, 192, 24, 4]

x = statistics.mean(example_list)
print(x)


'''

statistics.mean(list)
          .median(list)
          .stdev(list)
          .variance(list)


          .harmonic_mean(list)
          .median_low(list)
          .median_high(list)
          .median_grouped(list)

          .mode(list) ---> also applies to non-numeric (nominal) data

          .pstdev(data, mu=None)
          .pvariance(list, mu=None)  ---> mu = mean

          .StatisticsError
'''
