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

Just as with the getStateCodes() function, these two functions will print dictionary's with the variables assigned a unique code.  These codes will be used alongside the state code to extract the requested dataset, if the variable is located underneath the state variable umbrella.  For instance, the combination of state code 12 and state variable code 35 will yield the dataset for population for the state of Florida.  If the variable desired is located underneath the US variable umbrella then no state code is needed.  


### Get Data 

Okay, now that one has selected the state code and the variable code, one can begin the simple and easy process of extracting the dataset and plugging it into a pandas dataframe. 

```Python
df = tdc.getStateData(state_code, state_var_code)
```

```Python
df = tdc.getUSData(US_var_code)
```

Touching upon the last paragraph of the previous section, it is true that the getStateData() function requires two arguments- state_code and state_var_code.  On the other hand, the getUSData() function only requires one argument- the US_var_code.  All of these codes can be acquired by calling the getStateCodes(), getStateVarCodes(), and getUSVarCodes() functions.  Once these codes are acquired they can then be plugged into the getStateData() and getUSData() functions.  These functions will return a pandas dataframe of the dataset requested.


### Get Definitions 

Although the process for which requesting the dataset is quite simple, understanding the details and mechanics of the data can sometimes be difficult.  For example, not everyone knows about the meaning of allocated transfer risk reserves.  Not everyone is aware of the units level for the dataset.  However, this does not mean that the user has no need for this data.  On the contrary, it may be extremely useful for the user's individualized study or fact-finding process.  The user must simply be guided sometimes.  It is an incredibly useful tool that can fill any and all gaps in knowledge.  

```Python
print(tdc.getDefinitions(letter))
```

It is also extremely easy to use.  The user simply has to input a character (or series of characters) that belongs to the English alphabet.  Such characters compiled in this string can be lowercase or uppercase.  For example, the user can enter 'e' as the argument or 'abDk' as the argument.  Both are fully functional.  The latter will simply yield the definitions for all terms listed under the letters 'a', 'b', 'd', and 'k'.  All other characters that are not a part of the English alphabet will simply return an invalid message. 


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


Hire us: [Software Entwickler in Zürich](https://polygon-software.ch)!
