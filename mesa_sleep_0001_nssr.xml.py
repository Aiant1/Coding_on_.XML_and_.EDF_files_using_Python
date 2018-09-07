
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:34:44 2018

@author: ASUS
"""
import sys
import xml.etree.ElementTree as ET
import csv
import pandas as pd
Start=[]
Duration =[]
Eventtype=[]
Stages=[]
Input =[]
tree = ET.parse("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\mesa-sleep-0001-nsrr.xml")
root = tree.getroot()
for ele in root:
    if (ele.tag =='ScoredEvents'):
        for ele1 in ele:
            if ele1.tag == 'ScoredEvent':
                for ele2 in ele1:
                    if ele2.tag == "EventType":
                        Eventtype.append(ele2.text)
                    if ele2.tag == 'EventConcept':
                        Stages.append(ele2.text)
                    if ele2.tag =='Duration':
                        Duration.append(ele2.text)
                    if ele2.tag == 'Start':
                        Start.append(ele2.text)
data_frame = pd.DataFrame({"Duration":Duration,"Stages":Stages,"Start":Start,"Eventtype":Eventtype})

aa = data_frame.loc[data_frame["Eventtype"]== 'Stages|Stages']
aa.to_csv("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\mesa_sleep_0001_profusion_nssr_OUTPUT.xml.csv",index =None)
