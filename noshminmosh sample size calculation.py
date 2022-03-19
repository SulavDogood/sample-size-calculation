# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:12:03 2022

@author: Sulav
"""

import noshmishmosh as nm
import numpy as np

# list of all noshmishmosh visitors
all_visitors = nm.customer_visits

#list of visitors who make a purchase in  a week
paying_visitors = nm.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# percentage of visitors who purchase in a week
baseline_percent = (paying_visitor_count/total_visitor_count)*100
print(baseline_percent)

# list of money spent by each customer in a week
payment_history = nm.money_spent
average_payment = np.mean(payment_history)
print(average_payment)

# no. of new customers needed to make extra $1240 a week
new_customers_needed = np.ceil(1240/average_payment)
# additional percent of customers needed to make extra 1240 a week
percentage_point_increase = (new_customers_needed/total_visitor_count)*100
print(percentage_point_increase)

# desired lift percentage
mde = (percentage_point_increase/baseline_percent)*100
print(mde)

# given significance threshold of 0.10 resulting sample size = 500