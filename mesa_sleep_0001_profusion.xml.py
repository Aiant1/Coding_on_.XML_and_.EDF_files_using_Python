# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:34:44 2018

@author: ASUS
"""

import xml.etree.ElementTree as ET
import csv
import pandas as pd
Start=[]
Duration =[]
Name =[]
Input =[]
tree = ET.parse("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\mesa_sleep_0001_profusion.xml")
root = tree.getroot()
for ele in root:
    if (ele.tag =='ScoredEvents'):
        for ele1 in ele:
            if ele1.tag == 'ScoredEvent':
                
                for ele2 in ele1:
                    if ele2.tag == "Name":
                        Name.append(ele2.text)
                    if ele2.tag == 'Start':
                        Start.append(ele2.text)
                    if ele2.tag =='Duration':
                        Duration.append(ele2.text)
                    if ele2.tag == 'Input':
                        Input.append(ele2.text)
print (len(Input))
print (len(Name))
print (len(Duration))
print (len(Start))

data_frame = pd.DataFrame({"Duration":Duration,"Name":Name,"start":Start,"Input":Input})

data_frame.to_csv("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\mesa_sleep_0001_profusion_OUTPUT.xml.csv",index =None)
                       
            