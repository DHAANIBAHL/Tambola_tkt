# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 06:45:32 2023

@author: dhaani
"""

import random

def tambola_ticket():
    tkt = []
    
    sample_space = random.sample(range(1, 90), 15)

    for i in range(3):
        ss = sample_space[i*5:(i*5)+5]
        ss.sort()
        tkt.append(ss)

    print(tkt)

ticket = tambola_ticket()
