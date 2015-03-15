# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:00:09 2015

@author: Ying
"""
from explore_data import load_data
train, test=load_data()
feature_cols = [col for col in train.columns if col not in train.columns[11:55] and col  not in ['Cover_Type','Id']]

def r(x):
    if x+180>360:
        return x-180
    else:
        return x+180


def add_feature():
    train['Aspect2']=train.Aspect.map(r)
    test['Aspect2']=test.Aspect.map(r)
    
    train['Ele_minus_VDtHyd'] = train.Elevation-train.Vertical_Distance_To_Hydrology
    test['Ele_minus_VDtHyd'] = test.Elevation-test.Vertical_Distance_To_Hydrology
         
    train['Ele_plus_VDtHyd'] = train.Elevation+train.Vertical_Distance_To_Hydrology
    test['Ele_plus_VDtHyd'] = test.Elevation+test.Vertical_Distance_To_Hydrology
     
    train['Distanse_to_Hydrolody'] = (train['Horizontal_Distance_To_Hydrology']**2+train['Vertical_Distance_To_Hydrology']**2)**0.5
    test['Distanse_to_Hydrolody'] = (test['Horizontal_Distance_To_Hydrology']**2+test['Vertical_Distance_To_Hydrology']**2)**0.5
     
    train['Hydro_plus_Fire'] = train['Horizontal_Distance_To_Hydrology']+train['Horizontal_Distance_To_Fire_Points']
    test['Hydro_plus_Fire_plus'] = test['Horizontal_Distance_To_Hydrology']+test['Horizontal_Distance_To_Fire_Points']
     
    train['Hydro_minus_Fire'] = train['Horizontal_Distance_To_Hydrology']-train['Horizontal_Distance_To_Fire_Points']
    test['Hydro_minus_Fire'] = test['Horizontal_Distance_To_Hydrology']-test['Horizontal_Distance_To_Fire_Points']
     
    train['Hydro_plus_Road'] = train['Horizontal_Distance_To_Hydrology']+train['Horizontal_Distance_To_Roadways']
    test['Hydro_plus_Road'] = test['Horizontal_Distance_To_Hydrology']+test['Horizontal_Distance_To_Roadways']
     
    train['Hydro_minus_Road'] = train['Horizontal_Distance_To_Hydrology']-train['Horizontal_Distance_To_Roadways']
    test['Hydro_minus_Road'] = test['Horizontal_Distance_To_Hydrology']-test['Horizontal_Distance_To_Roadways']
     
    train['Fire_plus_Road'] = train['Horizontal_Distance_To_Fire_Points']+train['Horizontal_Distance_To_Roadways']
    test['Fire_plus_Road'] = test['Horizontal_Distance_To_Fire_Points']+test['Horizontal_Distance_To_Roadways']
     
    train['Fire_minus_Road'] = train['Horizontal_Distance_To_Fire_Points']-train['Horizontal_Distance_To_Roadways']
    test['Fire_minus_Road'] = test['Horizontal_Distance_To_Fire_Points']-test['Horizontal_Distance_To_Roadways']
    
    
    train['Soil']=0
    for i in range(1,41):
        train['Soil']=train['Soil']+i*train['Soil_Type'+str(i)]
     
    test['Soil']=0
    for i in range(1,41):
        test['Soil']=test['Soil']+i*test['Soil_Type'+str(i)]
     
    train['Wilderness_Area']=0
    for i in range(1,5):
         train['Wilderness_Area']=train['Wilderness_Area']+i*train['Wilderness_Area'+str(i)]
      
    test['Wilderness_Area']=0
    for i in range(1,5):
         test['Wilderness_Area']=test['Wilderness_Area']+i*test['Wilderness_Area'+str(i)]

