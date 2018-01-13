import numpy as np                # to load numpy library
import pandas as pd               # to load panda library
import matplotlib.pyplot as plt   # to load the matplotlib library only pyplot to ploy the graphs
%matplotlib inline                
%pylab inline

csv_data = "india-districts-census-2011.csv"
data_frame = pd.read_csv(csv_data)     # reading file and storing data to data_frame
data_frame_selected_colomns = data_frame[["State name","Literate","Population"]] # selecting required colom names from data_frame
#data_frame_selected_colomns            # checking wheather data getting in proper way or not for data frame selected coloms


sum_coloms_by_state_name = data_frame_selected_colomns.groupby('State name').sum()    # sum all the coloms data based on group of states
literacy_rate =  sum_coloms_by_state_name["Literate"]/sum_coloms_by_state_name["Population"]*100     # calculating literacy for statewise
#literacy_rate                                                                          # checking wheather data getting in proper way or not for literacy rate
                                                                         # checking wheather data getting in proper way or not for literacy rate

literacy_rate.sort_values(inplace = True) # soring values in assending order
literacy_rate.plot(kind='bar')            # geographic map is not possible so taken bar chart to display data 
plt.show()                                # showing chart with 
