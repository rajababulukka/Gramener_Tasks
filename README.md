# Gramener_Tasks

**This repository consists of the following :**

1. README.txt (this file) 
2. "india-districts-census-2011.csv" file 
3. 3 Ipython notebooks


### Step 1 : IMPORTING LIBRARIES

numpy, pandas, matplotlib 
from collections import OrderedDict  
from operator import itemgetter 
related libraies are imported

### Step 2 : LOADING THE DATA

india-districts-census-2011.csv file is loaded in pandas dataframe

The following questions have been answered :
#### Q1. Create a geographic map of states with low literacy rates.

Note: in given data there are no lattitude and longitude so unable to implement it. But tried to answer this with bar chart.

**Step 1.** Grouped all values statewise with required coloms

**Step 2.** Getting literacy rate by using this formula
            Literacy rate = (total literate population / total population) * 100

**Step 3.** Store the results for each state

**Step 4.** Plot the results into bar chart
            Sorted values in assending order to represet data in good way in bar chart.
            
            
#### Q2. Find out most similar districts in Bihar and Tamil Nadu. Similarity can be based on any of the columns from the data.

**Step 1.** Grouped all values statewise with required coloms

**Step 2.** Getting bihar state data and tamilnadu state data
            
**Step 3.** Iterate through all coloms data in both states to calculate degree of diffrence and checking the matched values for                     districts, put them in dictiornaries. 

**Step 4.** Oredering the data with the help of collections and operator
            
**Step 5.** Plot the results into bar chart with two bars represent aqua color is tamilnadu and black is bihar state

#### Q3. How does the mobile penetration vary in regions (districts or states) with high or low agricultural workers?

**Step 1.** Grouped all values statewise with required coloms

**Step 2.** Calculating high agriculture rate with this formula
            agriculture rate = (total Agricultural_Workers / total populWorkersation) * 100 > 50
            
**Step 3.** Grouped all values statewise 

**Step 4.** Calculating high mobile penetration with this formula
            mobile penetration = (total Households_with_Telephone_Mobile_Phone/ total Households) * 100
            
**Step 5.** Sort the values in assending order.Plot the results into bar chart.
            
