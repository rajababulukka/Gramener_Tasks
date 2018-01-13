# Gramener_Tasks

**This repository consists of the following :**

1. README.txt (this file) 
2. Analysis folder for Analysis related tasks
3. JavaScript_Tasks folder for javascript related taks
4. Python_Tasks folder for python related tasks

**Analysis folder consists of the following :**
1. "india-districts-census-2011.csv" file  
2. Canopy Ipython notebooks
3. Canopy Ipython notebooks checkpoints
4. Python files

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
  
  
  
**JavaScript_Tasks folder consists of the following :**
1. javascript_task.html   
2. remove_zeros_frm_arr.js

The following questions have been answered :
#### Q1. Write a Javascript function or expression that returns an array with just the zeroes removed.

**Step 1.** Created a function name with array_without_zero and parameters as array and element

**Step 2.** Looping through array and checking if element is matched or not. if matched splice the array with indexed element

**Step 3.** Displaying the returned output in javascript_task.html page


**Python_Tasks folder consists of the following :**
1. Common_elements_inList1.py  
2. no_of_Thursdays.py

The following questions have been answered :
#### Q1. Given two lists L1 = ['a', 'b', 'c'], L2 = ['b', 'd'], find common elements, find elements present in L1 and not in L2?

**Step 1.** Created a function name with common_elements_in_list1 and parameters as list1 and list2

**Step 2.** Taking empty list and Looping through list1 and checking if element is in list2 or not. if there append list1 element to empty list and return that appended values list.

#### Q1. How many Thursdays were there between 1990 - 2000?

**Step 1.** Created a function name with no_of_Thursdays and parameters as from year and to year

**Step 2.** Converting from year to start date of the from year and to year to end date of the to year

**Step 3.** Specifying datetime format and taking count as 0

**Step 4.** Iterate from start date day in range of all days from end date and start date difference

**Step 5.** Get the weekday from calender and check if the weekday is Thursday then increment count by 1 and return the count.

