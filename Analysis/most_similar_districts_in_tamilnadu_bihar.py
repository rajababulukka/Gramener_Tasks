import numpy as np                # to load numpy library
import pandas as pd               # to load panda library
import matplotlib.pyplot as plt   # to load the matplotlib library only pyplot to ploy the graphs
%matplotlib inline                
%pylab inline

csv_data = "india-districts-census-2011.csv"
data_frame = pd.read_csv(csv_data)     # reading file and storing data to data_frame
data_frame_selected_colomns = data_frame[["State name","District name","Ownership_Owned_Households"]] # selecting required coloms names from data_frame here we are taking Ownership_Owned_Households as specific colom to compare values
#data_frame_selected_colomns            # checking wheather data getting in proper way or not for data frame selected coloms

bihar_data_frame = data_frame_selected_colomns[(data_frame_selected_colomns['State name'] == 'BIHAR')] #Getting bihar state data
#bihar_data_frame # checking wheather data getting in proper way or not for data frame selected coloms

tamilnadu_data_frame = data_frame_selected_colomns[(data_frame_selected_colomns['State name'] == 'TAMIL NADU')]#Getting tamilnadu state data
#tamilnadu_data_frame # checking wheather data getting in proper way or not for data frame selected coloms

dev = 0.004                                                         #assuming 0.4% of degree change in original values
bihar_d = {}                                                        # to store the bihar districts in dictionary
tamilnadu_d = {}                                                    # to store the tamil nadu districts in dictionary
for i,tn_state,tn_dist,tn_ooh in tamilnadu_data_frame.itertuples(): # to iterate all coloms with tamilnadu state data 
    start_value_tn = tn_ooh-dev*tn_ooh                              # calculating ooh value with degree of change for start value for TN
    #print(start_value_tn)                                          # printing start value
    end_value_tn = tn_ooh+dev*tn_ooh                                # calculating ooh value with degree of change for end value
    #print(end_value_tn)                                            # printing end value
    for i,bh_state,bh_dist,bh_ooh in bihar_data_frame.itertuples(): # to iterate all coloms with bihar state data 
        start_value_bh = bh_ooh-dev*bh_ooh                          # calculating ooh value with degree of change for start value for Bihar 
        #print(start_value_bh)                                      # printing start value
        end_value_bh = bh_ooh+dev*bh_ooh                            # calculating ooh value with degree of change for end value for Bihar 
        #print(end_value_bh)                                        # printing start value
        if ((start_value_tn<=bh_ooh) and (bh_ooh<=end_value_tn))or((start_value_bh<=tn_ooh) and (tn_ooh<=end_value_bh)):#checking bihar values wtih tamilnadu values and vice versa
            bihar_d[bh_dist] = bh_ooh                               # if true then insert calculated bihar degree value to bihar dictionary
            tamilnadu_d[tn_dist] = tn_ooh                           # if true then insert calculated tamilnadu degree value to tamilnadu dictionary  
            
#print(bihar_d)                                                     # printing bihar dictionary values
#print(tamilnadu_d)                                                 # printing tamilnadu dictionary values

from collections import OrderedDict # importing OrderedDict from collections 
from operator import itemgetter     # importing itemgetter from operator

bihar_d_ordered = OrderedDict(sorted(bihar_d.items(), key=itemgetter(1)))          # sorting in assending order of bihar dictionary values
tamilnadu_d_ordered = OrderedDict(sorted(tamilnadu_d.items(), key=itemgetter(1)))  # sorting in assending order of tamilnadu dictionary values

#bihar_d_ordered
#tamilnadu_d_ordered
#print(bihar_d_ordered)     #  printing bihar dictionary values to check ordered or not
#print(tamilnadu_d_ordered) #  printing tamilnadu dictionary values to check ordered or not

no_of_things = len(bihar_d_ordered) # getting length or bihar dictionary values
fig, ax = plt.subplots()            # creating plot with fig and axis
index = np.arange(no_of_things)     # getting index of the no_of_things using numpy arrange

bar_width = 0.2                     # defining bar width
opacity = 0.5                       # defining opacity for bar visibility

tamilnadu_bar = plt.bar(index, tamilnadu_d_ordered.values(), bar_width,alpha=opacity,color='aqua',label='Tamilnadu')  # tamilnadu bar properties and values 
bihar_bar = plt.bar(index + bar_width, bihar_d_ordered.values(), bar_width,alpha=opacity,color='black',label='Bihar') # bihar bar properties and values

plt.xticks(rotation=90)             # rotating by 90 degree and set the location
combine_value_list = []             # taking empty list for combined values                
for (key_1,value_1), (key_2,value_2) in zip(tamilnadu_d_ordered.items(), bihar_d_ordered.items()): # making tuple from each dictionary values
    combine_value_list.append(key_1 +"\n"+ key_2)      # appending key values to list
    
plt.xticks(index + bar_width , combine_value_list)     # setting tick location and lable
plt.tight_layout()                                     # to automatically adjust subplot parameters  
plt.show()                                             # displaying chart
