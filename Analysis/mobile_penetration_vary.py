import numpy as np                # to load numpy library
import pandas as pd               # to load panda library
import matplotlib.pyplot as plt   # to load the matplotlib library only pyplot to ploy the graphs
%matplotlib inline                
%pylab inline

csv_data = "india-districts-census-2011.csv"
data_frame = pd.read_csv(csv_data)    # reading file and storing data to data_frame
data_frame_selected_colomns = data_frame[["State name","District name","Workers","Households","Agricultural_Workers","Households_with_Telephone_Mobile_Phone"]] # selecting required coloms names from data_frame here we are taking Ownership_Owned_Households as specific colom to compare values
#data_frame_selected_colomns            # checking wheather data getting in proper way or not for data frame selected coloms

high_agriculture = data_frame_selected_colomns[(data_frame_selected_colomns["Agricultural_Workers"]/data_frame_selected_colomns["Workers"]*100 > 50)] # assuming if the percentage of Agricultural_Workers based on workers is 50 above then high agriculture otherwise low
#high_agriculture    # checking data correctly getting or not for high agriculture

high_agriculture_sum_by_state_wise = high_agriculture.groupby("State name").sum()    # sum the coloms by grouping state wise
#high_agriculture_sum_by_state_wise # checking data correctly getting or not for high_agriculture_sum_by_state_wise

mobile_penetration = high_agriculture_sum_by_state_wise["Households_with_Telephone_Mobile_Phone"]/high_agriculture_sum_by_state_wise["Households"]*100  # getting percentage of mobile penetrations
#mobile_penetration     # checking data correctly getting or not for mobile_penetration

mobile_penetration.sort_values(inplace = True) # soring values in assending order
mobile_penetration.head(mobile_penetration.count()).plot(kind='bar') # taking a bar chat as plot
plt.show() # displaying chart
