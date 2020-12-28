# thedatacycle - the organization's very own data extraction api

With thedatacycle, you can extract an up-to-date dataframe from our extensive holdings of data tables.  It is an extremely easy tool to use- the functions only require a few arguments.  With just four lines of code one can request a dataframe and use it for personal use.  Provided below is a comprehensive guide on how to effectively manuever through the package.  

# Overview
thedatacycle Python package was written with fast use in mind. It provides the following key features:

  - Extract updated dataframes for hundreds of datasets. 
  - Look up definitions and details of the variables pertaining to each dataset.


## Usage

In the following paragraphs, I am going to describe how you can get and use thedatacycle for your own projects.

###  Getting it

To download thedatacycle, either fork this github repo or simply use PyPi via pip.
```sh
$ pip install thedatacycle
```

### Dependencies 

To use thedatacycle, one must install the pandas package through PyPi via pip.
```sh
$ pip install pandas
```
The package does not have to be imported.  It is already imported in the package.  It simply must be installed.  

### Using it

thedatacycle was programmed with ease-of-use in mind. First, import thedatacycle and assign a shortcut name for the module. 

```Python
import thedatacycle as tdc
```

One could import a particular individual function from the module but there are a multitude of functions that depend on each other.  It is important that one imports the entire module.

## State DataHubs

### State Codes

```Python
print(tdc.getStateCodes())
```

Since this organization will eventually create individualized datahubs for all fifty states, it is important to assign codes for each state so that data does not overlap or get lost in transition.  By executing this statement, one will print a dictionary with the codes assigned to each state.  In the event that you are familiar with state fips codes then there may be no need to execute this statement.  Fips codes are five digit numbers that contain information regarding the state and the county.  For example, the code 12086 refers to Florida (12) and Miami-Dade County (086).  By printing the dictionary located within this function one will observe that Florida is assigned the number 12.  


### Variable Codes

```Python
print(tdc.getStateVarCodes())
```

```Python
print(tdc.getUSVarCodes())
```

Upon selecting the state (using the getStateCodes() function) for which you will extract a dataframe, you will be required to select a variable for which to extract a time series dataset.  Such variables include unemployment rate, poverty rate, precipitation, et cetera.  These variables are split into state variables and country (United States) variables.  

The state variables primarily contain county data but may also include data points related to the state as a whole and the United States as a whole.  There are some variables underneath the state variables umbrella that only contain information regarding the state as a whole and the country, such as rental vacancy rate and nonperforming loans ratio.  Those variables underneath the US variables umbrella strictly contain information regarding the country as a whole, such as the federal funds rate, exchange rates, and treasury bond yield rates.

Just as with the getStateCodes() function, these two functions will print dictionary's with the variables assigned a unique code.  These codes will be used alongside the state code to extract the requested dataset, if the variable is located underneath the state variable umbrella.  For instance, the combination of state code 12 and state variable code 1 will yield the dataset for unemployment rate for the state of Florida.  If the variable desired is located underneath the US variable umbrella then no state code is needed.  


### Get Data 

Okay, now that one has selected the state code and the variable code, one can begin the simple and easy process of extracting the dataset and plugging it into a pandas dataframe. 

```Python
df = tdc.getStateData(state_code, state_var_code)
```

```Python
df = tdc.getUSData(us_var_code)
```

Touching upon the last paragraph of the previous section, it is true that the getStateData() function requires two arguments- state_code and state_var_code.  On the other hand, the getUSData() function only requires one argument- the US_var_code.  All of these codes can be acquired by calling the getStateCodes(), getStateVarCodes(), and getUSVarCodes() functions.  Once these codes are acquired they can then be plugged into the getStateData() and getUSData() functions.  These functions will return a pandas dataframe of the dataset requested.

##### Examples:

###### State Data

```Python
df = tdc.getStateData(12, 1)
print(df)
```
```
Unemployment Rate

       index         COUNTY                 DATE  MEASURE  CHANGE  PCT_CHANGE
0          0        Alachua  1990-01-01 00:00:00      3.8     NaN         NaN
1          1        Alachua  1990-02-01 00:00:00      3.5    -0.3    -7.89474
2          2        Alachua  1990-03-01 00:00:00      3.2    -0.3    -8.57143
3          3        Alachua  1990-04-01 00:00:00      3.3     0.1     3.12500
4          4        Alachua  1990-05-01 00:00:00      3.5     0.2     6.06061
     ...            ...                  ...      ...     ...         ...
26199    870  United States  2020-07-01 00:00:00     10.2    -0.9    -8.10811
26200    871  United States  2020-08-01 00:00:00      8.4    -1.8   -17.64706
26201    872  United States  2020-09-01 00:00:00      7.9    -0.5    -5.95238
26202    873  United States  2020-10-01 00:00:00      6.9    -1.0   -12.65823
26203    874  United States  2020-11-01 00:00:00      6.7    -0.2    -2.89855

[26204 rows x 6 columns]
```

###### US Data

```Python
df = tdc.getUSData(1)
print(df)
```
```
Federal Funds Rate

       index         COUNTY                 DATE  MEASURE  CHANGE  PCT_CHANGE
0          0  United States  1954-07-01 00:00:00     1.13     NaN         NaN
1          1  United States  1954-07-02 00:00:00     1.25    0.12    10.61947
2          2  United States  1954-07-03 00:00:00     1.25    0.00     0.00000
3          3  United States  1954-07-04 00:00:00     1.25    0.00     0.00000
4          4  United States  1954-07-05 00:00:00     0.88   -0.37   -29.60000
     ...            ...                  ...      ...     ...         ...
24273  24273  United States  2020-12-14 00:00:00     0.09    0.00     0.00000
24274  24274  United States  2020-12-15 00:00:00     0.09    0.00     0.00000
24275  24275  United States  2020-12-16 00:00:00     0.09    0.00     0.00000
24276  24276  United States  2020-12-17 00:00:00     0.09    0.00     0.00000
24277  24277  United States  2020-12-18 00:00:00     0.09    0.00     0.00000

[24278 rows x 6 columns]
```



### Get Definitions 

Although the process for which requesting the dataset is quite simple, understanding the details and mechanics of the data can sometimes be difficult.  For example, not everyone knows about the meaning of allocated transfer risk reserves.  Not everyone is aware of the units level for the dataset.  However, this does not mean that the user has no need for this data.  On the contrary, it may be extremely useful for the user's individualized study or fact-finding process.  The user must simply be guided sometimes.  It is an incredibly useful tool that can fill any and all gaps in knowledge.  

```Python
print(tdc.getDefinitions(character))
```

It is also extremely easy to use.  The user simply has to input a character (or series of characters) that belongs to the English alphabet.  Such characters compiled in this string can be lowercase or uppercase.  For example, the user can enter 'e' as the argument or 'abDk' as the argument.  Both are fully functional.  The latter will simply yield the definitions for all terms listed under the letters 'a', 'b', 'D', and 'k'.  All other characters that are not a part of the English alphabet will simply return an invalid message. 

##### Examples: 

###### One Character 

```Python
print(tdc.getDefinitions('e'))
```
```
E: 
                
Electronics Sales: measurement of sales from electronic stores and electronic media sites / downloads.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
             
Employment Cost Index: a BLS survey of employer payrolls conducted that measures the change in total employee compensation each quarter.  Frequency: Quarterly Units: Index Field Size: 1.0  
             
Employed Persons: number of people who are currently employed under the definition of the most recent legislation.  Frequency: Monthly Units: Persons Field Size: 67.0  
             
Estimated Median Household Income: the median income of the householder and all other people 15 years and older in the household, whether or not they are related to the householder.  Frequency: Annual Units: USD Field Size: 67.0  
             
Ethereum: the second-largest cryptocurrency platform by market capitalization. It is a decentralized open source blockchain featuring smart contract functionality.  Frequency: Daily Units: USD Field Size: 1.0  
             
Excessive Drinking Rate: percent of people in the population with excessive alcohol use, either in the form of binge drinking (drinking 5 or more drinks on an occasion for men or 4 or more drinks on an occasion for women) or heavy drinking (drinking 15 or more drinks per week for men or 8 or more drinks per week for women).  Frequency: Annual Units: Percent Field Size: 68.0  
```

###### Multiple Characters 

```Python
print(tdc.getDefinitions('bDk'))
```
```
B: 
                
Bachelor’s Degree: percent of individuals that have received an bachelor’s degree. 
Frequency: Annual Units: Percent Field Size: 67.0 
             
Bank Assets: the items that the bank owns. This includes loans, securities, and reserves. Liabilities are items that the bank owes to someone else, including deposits and bank borrowing from other institutions.
Frequency: Quarterly Units: Billions USD Field Size: 2.0

Bank Deposits: consists of money placed into banking institutions for safekeeping. These deposits are made to deposit accounts such as savings accounts, checking accounts and money market accounts. The account holder has the right to withdraw deposited funds, as set forth in the terms and conditions governing the account agreement.
Frequency: Quarterly Units: Billions USD Field Size: 2.0
                
Bank Liabilities: what the bank owes to others. Specifically, the bank owes any deposits made in the bank to those who have made them.
Frequency: Quarterly Units: Billions USD Field Size: 2.0
                
Bank Prime Rate: the interest rate that commercial banks charge their most creditworthy customers, generally large corporations. The prime interest rate, or prime lending rate, is largely determined by the federal funds rate, which is the overnight rate that banks use to lend to one another.
Frequency: Daily Units: Percent Field Size: 1.0
             
Bitcoin: a digital currency created in January 2009 following the housing market crash. It follows the ideas set out in a whitepaper by the mysterious and pseudonymous Satoshi Nakamoto. The identity of the person or persons who created the technology is still a mystery. Bitcoin offers the promise of lower transaction fees than traditional online payment mechanisms and is operated by a decentralized authority, unlike government-issued currencies.
Frequency: Daily Units: USD Field Size: 1.0
             
Black - Hispanic: an individual with total or partial ancestry from any of the black racial groups of Africa; and who is of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin.  Frequency: Annual Units: Persons Field Size: 67.0
             
Black – Not Hispanic: an individual with total or partial ancestry from any of the black racial groups of Africa; and who is not of Hispanic origin.
Frequency: Annual Units: Persons Field Size: 67.0 
             
Burdened Households: the percentage of households in a particular region who pay more than 30 percent of their income towards rent or mortgage expenses  Frequency: Annual Units: Percent Field Size: 67.0  
             
Business Applications: all applications for an EIN (Employer Identification Number), except for applications for tax liens, estates, trusts, or certain financial filings, applications with no state-county geocodes, applications from certain agricultural, public entities, and applications in certain industries (e.g. private households, civic and social organizations).  Frequency: Weekly Units: Number Field Size: 2.0  
             

D: 
                
Department Store Sales: measurement of sales from department stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
             
Diabetes Rate: percent of people in the population diagnosed with diabetes I, diabetes II, pre-diabetes, or gestational diabetes.  Frequency: Annual Units: Percent Field Size: 1.0 
            
Diesel Gas Price Per Gallon: weighted average price per gallon for diesel gas based on the sampling of approximately 350 retail outlets.  Frequency: Weekly Units: USD per Gallon Field Size: 1.0  
             
Disconnected Youth: the percentage of youth in a particular region who are between the ages of 16 and 19, who are not enrolled in school and who are unemployed or not in the labor force.  Frequency: Annual Units: Percent Field Size: 67.0  
             
Discount Rate: the interest rate set by central banks - the Federal Reserve in the U.S. - on loans extended by the central bank to commercial banks or other depository institutions.  Frequency: Monthly Units: Percent Field Size: 1.0  
             
Discouraged Workers: persons who, discouraged about their prospects of finding work, have given up their job searches and are therefore no longer officially counted as unemployed.  Frequency: Quarterly Units: Persons Field Size: 1.0  
             
Documentary & Stock Transfer Taxes: estimated tax revenue stemming from the transfer of the title of real property from one person (or entity) to another within the jurisdiction. It is based on the property’s sale price and is paid by the buyer, seller, or both parties upon transfer of real property.  Frequency: Quarterly Units: Millions USD Field Size: 1.0  
             
Dow Jones Industrial: stock market index that measures the stock performance of 30 large companies listed on stock exchanges in the United States.  Frequency: Daily Units: USD Index Field Size: 1.0  


K: 
                
No terms under this letter - k. 
```

License
----

MIT License

Copyright (c) 2020 The Data Cycle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Hire us: [The Data Cycle](https://thedatacycle.com/#service)
