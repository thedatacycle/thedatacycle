"""
@alexandercuneo
@thedatacycle
"""

import pandas as pd


def getDefinitions(letter):
    
    try: 
    
        letter = letter.lower()
    
    except: 
        
        print('Letter entered is not readable')
    
    

    a = '''
    
        Active Listings: the count of active single-family and condo/townhome listings for a given market during the specified month (excludes pending listings).  Frequency: Monthly Units: Level Field Size: 43.0  
    
        Alcoholic Sales Taxes: estimated tax revenue stemming from the sale of alcoholic beverages or products.  Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Allocated Transfer Risk Reserves: an allowance for bad debts that a bank keeps in order to protect against country risk. For example, a bank may keep an ATRR in case a country renders its currency inconvertible, which would prevent a foreign borrower in that country from making payments.  Frequency: Quarterly Units: Thousands USD Field Size: 2.0  
         
        Asian - Hispanic: a native of Asia or a person of by others to have African ancestry; and are of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin.  Frequency: Annual Units: Persons Field Size: 67.0
         
         
        Asian – Not Hispanic: a native of Asia or a person of by others to have African ancestry; and who is not of Hispanic origin.
         Frequency: Annual Units: Persons Field Size: 67.0  
         
        Average House Prices: calculated by adding up all of the house prices and dividing them by the number of houses in that region.  
        Frequency: Monthly Units: USD Field Size: 43.0
         
         
        Average Weekly Hours Worked: the mean number of hours worked by employees on a weekly basis.
        Frequency: Monthly Units: Number Field Size: 2.0
         
         
        Average Hourly Earnings: the mean number of hourly earnings achieved by a collective group of employees.
        Frequency: Monthly Units: USD Field Size: 2.0
         
         
        Average Temperature: average temperature that we know of according to the standard model of particle physics.  Frequency: Monthly Units: Fahrenheit Field Size: 67.0
        '''
    
    b = '''
        Bachelor’s Degree: percent of individuals that have received an bachelor’s degree. 
         Frequency: Annual Units: Percent Field Size: 67.0 
         
        Bank Assets: the items that the bank owns. This includes loans, securities, and reserves. Liabilities are items that the bank owes to someone else, including deposits and bank borrowing from other institutions.
        Frequency: Quarterly Units: Billions USD Field Size: 2.0
         
         
        Bank Deposits: consists of money placed into banking institutions for safekeeping. These deposits are made to deposit accounts such as savings accounts, checking accounts and money market accounts. The account holder has the right to withdraw deposited funds, as set forth in the terms and conditions governing the account agreement.
        Frequency: Quarterly Units: Billions USD Field Size: 2.0
         
         
        Bank Liabilities: what the bank owes to others. Specifically, the bank owes any deposits made in the bank to those who have made them.
        Frequency: Quarterly Units: Billions USD Field Size: 2.0
         
         
        Bank Prime Rate: the interest rate that commercial banks charge their most creditworthy customers, generally large corporations. The prime interest rate, or prime lending rate, is largely determined by the federal funds rate, which is the overnight rate that banks use to lend to one another.
        Frequency: Daily Units: Percent Field Size: 1.0
         
         
        Bitcoin: a digital currency created in January 2009 following the housing market crash. It follows the ideas set out in a whitepaper by the mysterious and pseudonymous Satoshi Nakamoto. The identity of the person or persons who created the technology is still a mystery. Bitcoin offers the promise of lower transaction fees than traditional online payment mechanisms and is operated by a decentralized authority, unlike government-issued currencies.
        Frequency: Daily Units: USD Field Size: 1.0
         
         
        Black - Hispanic: an individual with total or partial ancestry from any of the black racial groups of Africa; and who is of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin.  Frequency: Annual Units: Persons Field Size: 67.0
         
        Black – Not Hispanic: an individual with total or partial ancestry from any of the black racial groups of Africa; and who is not of Hispanic origin.
         Frequency: Annual Units: Persons Field Size: 67.0 
         
        Burdened Households: the percentage of households in a particular region who pay more than 30 percent of their income towards rent or mortgage expenses  Frequency: Annual Units: Percent Field Size: 67.0  
         
        Business Applications: all applications for an EIN (Employer Identification Number), except for applications for tax liens, estates, trusts, or certain financial filings, applications with no state-county geocodes, applications from certain agricultural, public entities, and applications in certain industries (e.g. private households, civic and social organizations).  Frequency: Weekly Units: Number Field Size: 2.0  
         '''
    c = '''
        Civilian Labor Force: people age 16 and older who are classified as either employed or unemployed.  Frequency: Monthly Units: Persons Field Size: 67.0  
         
        Clothing Sales: measurement of sales from clothing outlets and stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Commercial Banks: the number of financial institutions that accept deposits, offer checking account services, make various loans, and offer basic financial products like certificates of deposit (CDs) and savings accounts to individuals and small businesses.  Frequency: Quarterly Units: Number Field Size: 2.0 
        
        Commercial Paper: the amount of short-term unsecured promissory notes issued by companies.  Frequency: Weekly Units: Billions USD Field Size: 1.0
          
        Continued Claims: also referred to as insured unemployment, is the number of people who have already filed an initial claim and who have experienced a week of unemployment and then filed a continued claim to claim benefits for that week of unemployment.  Frequency: Weekly Units: Number Field Size: 2.0  
         
        Coronavirus Cases: the number of confirmed cases stemming from the coronavirus (SARS-CoV-2).  Frequency: Daily Units: Number Field Size: 69.0  
         
        Coronavirus Deaths: the number of confirmed deaths stemming from the coronavirus (SARS-CoV-2).  Frequency: Daily Units: Number Field Size: 69.0  
         
        Coronavirus Recoveries: the number of confirmed recoveries stemming from the coronavirus (SARS-CoV-2).  Frequency: Daily Units: Number Field Size: 69.0  
         
        Corporate License Taxes: estimated tax revenue stemming from the money paid to the government for the privilege of being licensed to do something, such as selling liquor or practicing medicine.  Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Consumer Price Index: measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services.  Frequency: Monthly Units: Index Field Size: 8.0  
         '''
    d = '''
        Department Store Sales: measurement of sales from department stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Diabetes Rate: percent of people in the population diagnosed with diabetes I, diabetes II, pre-diabetes, or gestational diabetes.  Frequency: Annual Units: Percent Field Size: 1.0 
        
        Diesel Gas Price Per Gallon: weighted average price per gallon for diesel gas based on the sampling of approximately 350 retail outlets.  Frequency: Weekly Units: USD per Gallon Field Size: 1.0  
         
        Disconnected Youth: the percentage of youth in a particular region who are between the ages of 16 and 19, who are not enrolled in school and who are unemployed or not in the labor force.  Frequency: Annual Units: Percent Field Size: 67.0  
         
        Discount Rate: the interest rate set by central banks - the Federal Reserve in the U.S. - on loans extended by the central bank to commercial banks or other depository institutions.  Frequency: Monthly Units: Percent Field Size: 1.0  
         
        Discouraged Workers: persons who, discouraged about their prospects of finding work, have given up their job searches and are therefore no longer officially counted as unemployed.  Frequency: Quarterly Units: Persons Field Size: 1.0  
         
        Documentary & Stock Transfer Taxes: estimated tax revenue stemming from the transfer of the title of real property from one person (or entity) to another within the jurisdiction. It is based on the property’s sale price and is paid by the buyer, seller, or both parties upon transfer of real property.  Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Dow Jones Industrial: stock market index that measures the stock performance of 30 large companies listed on stock exchanges in the United States.  Frequency: Daily Units: USD Index Field Size: 1.0  
         '''
    e = '''
        Electronics Sales: measurement of sales from electronic stores and electronic media sites / downloads.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Employment Cost Index: a BLS survey of employer payrolls conducted that measures the change in total employee compensation each quarter.  Frequency: Quarterly Units: Index Field Size: 1.0  
         
        Employed Persons: number of people who are currently employed under the definition of the most recent legislation.  Frequency: Monthly Units: Persons Field Size: 67.0  
         
        Estimated Median Household Income: the median income of the householder and all other people 15 years and older in the household, whether or not they are related to the householder.  Frequency: Annual Units: USD Field Size: 67.0  
         
        Ethereum: the second-largest cryptocurrency platform by market capitalization. It is a decentralized open source blockchain featuring smart contract functionality.  Frequency: Daily Units: USD Field Size: 1.0  
         
        Excessive Drinking Rate: percent of people in the population with excessive alcohol use, either in the form of binge drinking (drinking 5 or more drinks on an occasion for men or 4 or more drinks on an occasion for women) or heavy drinking (drinking 15 or more drinks per week for men or 8 or more drinks per week for women).  Frequency: Annual Units: Percent Field Size: 68.0  
         '''
        
    f = '''
        Fair / Poor Health Rate: the percentage of adults in a particular region who consider themselves to be in poor or fair health.  Frequency: Annual Units: Percent Field Size: 68.0  
         
        Federal Funds Rate: the interest rate at which depository institutions trade federal funds (balances held at Federal Reserve Banks) with each other overnight.  Frequency: Daily Units: Percent Field Size: 1.0  
         
        Fifteen Year Fixed Mortgage Rate: the average price of a mortgage loan charging an interest rate that remains the same throughout the 15-year term of the loan.  Frequency: Weekly Units: Percent Field Size: 1.0 
        
        Financial Stress Index: measures the degree of financial stress in the markets and is constructed from 18 weekly data series, all of which are weekly averages of daily data series: seven interest rates, six yield spreads, and five other indicators. Each of these variables captures some aspect of financial stress. Accordingly, as the level of financial stress in the economy changes, the data series are likely to move together.  Frequency: Weekly Units: Index Field Size: 1.0  
         
        Five / One Year Ajustable Mortgage Rate: a mortgage loan with the interest rate on the note periodically adjusted based on an index which reflects the cost to the lender of borrowing on the credit markets.  Frequency: Weekly Units: Percent Field Size: 1.0
         
         
        Foreign Exchange Rate: the value of one currency for the purpose of conversion to another.  Frequency: Daily Units: Foreign to USD (or USD to Foreign) Field Size: 1.0  
         
        Furniture Sales: measurement of sales from furniture stores and retailers.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         '''
        
    g = '''
        Gas Station Sales: measurement of sales from gas stations, including all other non-gasoline sales.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        General Merchandise Sales: measurement of sales from general merchandise stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        General Sales Taxes: estimated tax revenue stemming from a sales tax applied to all goods and services sold in a jurisdiction that are not specifically exempted.  Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Government Employees: people who work in a variety of fields such as teaching, sanitation, health care, management, and administration for the federal, state, or local government. Legislatures establish basic prerequisites for employment such as compliance with minimal age and educational requirements and residency laws.  Frequency: Monthly Units: Thousands of Persons Field Size: 2.0  
         
        Grocery Sales: measurement of sales from grocery stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         '''
        
    h = '''
        Health Care Assistance Earnings: monetary earnings collected by those employed in the health care and social assistance industry.
        Frequency: Quarterly Units: Thousands USD Field Size: 1.0
         
         
        Health Care Costs & Expenses: the actual costs of providing services related to the delivery of health care, including the costs of procedures, therapies, and medications.
        Frequency: Annual Units: USD Field Size: 68.0
         
         
        High School Graduation Rate: percent of students who graduate with a regular high school diploma within four years.
        Frequency: Annual Units: Percent Field Size: 67.0
         
         
        Hispanic: of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin.
        Frequency: Annual Units: Persons Field Size: 67.0
         
         
        High Quality Corporate Bond Spot Rates: secondary market interest rates paired with corporate bonds that are categorized as high quality.
        Frequency: Weekly Units: Percent Field Size: 1.0
         
         
        HIV Rate: the estimated number of adults and children that have been diagnosed with human immunodeficiency virus (HIV) in a specific year, expressed per 100K.
        Frequency: Annual Units: Persons per 100K Field Size: 68.0
         
         
        Home Ownership Rate: the percentage of U.S. homes that are owner-occupied. The rate is calculated by dividing the number of homes that are owner-occupied by the total number of occupied households.
        Frequency: Annual Units: Percent Field Size: 43.0
         
         
        Home Vacancy Rate: the percentage of all available units in a rental property, such as a hotel or apartment complex, that are vacant or unoccupied at a particular time. A vacancy rate is the opposite of the occupancy rate, which is the percentage of units in a rental property that are occupied.
        Frequency: Annual Units: Percent Field Size: 2.0
         
         
        Home Delinquency Rate: the percentage of home loans for which the borrower has failed to make payments as required in the loan documents. A mortgage is considered delinquent or late when a scheduled payment is not made on or before the due date. If the borrower cannot bring the payments on a delinquent mortgage current within a certain time period, the lender may begin foreclosure proceedings.
        Frequency: Quarterly Units: Percent Field Size: 1.0
        '''
    
    i = '''
        ICE BofA High Yield Index: tracks the performance of US dollar denominated below investment grade rated corporate debt publicly issued in the US domestic market.
        Frequency: Daily Units: Index Field Size: 1.0
         
         
        Income Inequality: this data represents the ratio of the mean income for the highest quintile (top 20 percent) of earners divided by the mean income of the lowest quintile (bottom 20 percent) of earners in a particular county.
        Frequency: Annual Units: Ratio Field Size: 67.0
         
         
        Inflation Rate: quantitative measure of the rate at which the average price level of a basket of selected goods services in an economy increases over some period of time. It is the rise in the general level of prices where a unit of currency effectively buys less than it did in prior periods. Often expressed as a percentage, inflation thus indicates a decrease in the purchasing power of a nation’s currency.
        Frequency: Annual Units: Percent Field Size: 1.0
         
         
        Initial Claims: claim filed by an unemployed individual after a separation from an employer. The claim requests a determination of basic eligibility for the Unemployment Insurance program.
        Frequency: Weekly Units: Number Field Size: 2.0
         
         
        Insurance Premiums Taxes: estimated tax revenue stemming from a tax on insurance premiums.
        Frequency: Quarterly  Units: Millions USD Field Size: 1.0
         
         
        Insured Unemployment Rate: continued claims (also called insured unemployment) divided by Covered Employment.
        Frequency: Weekly  Units: Percent Field Size: 2.0
         '''
    j = '''
        No terms under this letter. 
        '''
        
    k = '''
        No terms under this letter. 
        '''
       
    l = '''
        Labor Force Rate: the section of working population in the age group of 16-64 in the economy currently employed or seeking employment.
        Frequency: Monthly  Units: Percent Field Size: 2.0
         
         
        Libor Rate: the global reference rate for unsecured short-term borrowing in the interbank market. It acts as a benchmark for short-term interest rates. It is used for pricing of interest rate swaps, currency rate swaps as well as mortgages.
        Frequency: Daily Units: Percent Field Size: 1.0
         
         
        Litecoin: open-source global payment network that is not controlled by any central authority. Litecoin differs from Bitcoins in aspects like faster block generation rate and use of script as a proof of work scheme. 
        Frequency: Daily  Units: USD Field Size: 1.0
         
         
        Low Birthweight Rate: percent of newborns born weighing less than 5 pounds, 8 ounces
        Frequency: Annual  Units: Percent Field Size: 1.0
         '''
      
    m = '''
        M1 Money Stock: consists of: (1) currency outside the U.S. Treasury, Federal Reserve Banks, and the vaults of depository institutions; (2) traveler's checks of nonbank issuers; (3) demand deposits; and (4) other checkable deposits (OCDs), which consist primarily of negotiable order of withdrawal (NOW) accounts at depository institutions and credit union share draft accounts.
        Frequency: Weekly Units: Billions USD Field Size: 1.0  
         
        M2 Money Stock: includes a broader set of financial assets held principally by households. M2 consists of M1 plus: (1) savings deposits (which include money market deposit accounts, or MMDAs); (2) small-denomination time deposits (time deposits in amounts of less than $100,000); and (3) balances in retail money market mutual funds (MMMFs).  Frequency: Weekly Units: Billions USD Field Size: 1.0  
         
        Mammogram Screening Rate: percent of women aged 40 and over who had a mammogram within the past 2 years.  Frequency: Annual Units: Percent Field Size: 68.0  
         
        Market Hotness Rank: exposes how local areas are experiencing fast moving supply and rising demand. Using proprietary insights on buyer activity and the most comprehensive data on active inventory, the analysis breaks down demand and supply dynamics to rank metro areas, counties and zip codes relative to the rest of the country. Realtor.com examines listing views by market as an indicator of demand and median days on market as an indicator of supply.  
        Frequency: Monthly Units: Rank Field Size: 41.0  
         
        Maximum Temperature: highest temperature that we know of according to the standard model of particle physics.  Frequency: Monthly Units: Fahrenheit Field Size: 67.0 
        
        Mean Commuting Time: calculated by dividing the aggregate travel time to work for all workers by the total number of workers, 16-years old and older, who commute.
         Frequency: Annual Units: Minutes Field Size: 67.0 
        
        Median Days on the Market: the median number of days on market of listings in a given geography during the specified month.  Frequency: Monthly Units: Days Field Size: 69.0  
         
        Median House Prices: the sale price of the middle home in a list of properties ranked from highest sale price to lowest over a set period of time.
         Frequency: Monthly Units: USD Field Size: 43.0  
         
        Median Price Per Square Foot: the price where exactly half of homes listed have a price per square foot higher than this price and exactly half are lower than this price.
         Frequency: Monthly Units: USD Field Size: 43.0  
         
        Median Square Footage: the square footage where exactly half of the homes listed have a square footage higher than this square footage and exactly half are lower than this square footage.
         Frequency: Monthly Units: Level Field Size: 43.0  
         
        Mental Health Professional Rate (per 100K): the capita rate of professionals who diagnose mental health conditions and provide treatment. Most have at least a master's degree or more-advanced education, training, and credentials.  Frequency: Annual Units: Persons per 100K Field Size: 68.0   
         
        Minimum Temperature: this is the lowest temperature that we know of according to the standard model of particle physics  Frequency: Monthly Units: Fahrenheit  Field Size: 67.0
         
         
        Mobility Concentration: the percent change in the concentration of people moving to or out of certain types of areas within a generalized region.  These areas include transit stations, residential areas, workplaces, retail and recreation, parks, and grocery stores.
        Frequency: Weekly Units: Percent Change Field Size: 67.0  
         
        Minimum Wage: the lowest wage permitted by law or by a special agreement (such as one with a labor union).
         Frequency: Annual Units: USD per Hour Field Size: 1.0  
         
        Miscellaneous Store Sales: sales from establishments that include stores with unique characteristics like florists, used merchandise stores, and pet and pet supply stores as well as other store retailers.
         Frequency: Monthly Units: Millions USD Field Size: 1.0
         
         
        Motor Vehicle Mortality Rate: the rate of people per 100K who suffer fatal motor vehicle accidents in a given region.  Frequency: Annual Units: Persons per 100K Field Size: 68.0  
         
        Motor Fuel Taxes: sales tax that is imposed on the sale of fuels such as gasoline, jet fuel, and diesel. Motor fuel tax rates are higher for fuel consumed for the purposes of transportation. Agricultural and heating fuels are taxed at a lower rate than motor fuels.
         Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Motor License Taxes: estimated tax revenue stemming from taxes paid to the government for the privilege of being licensed to operate a motor vehicle.   Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Municipal Bond Yield Rates: the rate of return collected by holders of bonds distributed by the local government in the primary market.   Frequency: Daily Units: Percent Field Size: 1.0  
         '''
        
    n = '''
        NASDAQ: market capitalization weighted index with more than 3000 common equities listed on the NASDAQ Stock Market. The types of securities in the index include American depositary receipts (ADRs), common stocks, real estate investment trusts (REITs), and tracking stocks.  Frequency: Daily Units: Index Field Size: 1.0  
         
        Native Indian or Alaskan – Hispanic: people having origin in any of the original people of North America and who maintains cultural identification through tribal affiliation; and who are of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race.  Frequency: Annual Units: Persons Field Size: 67.0  
         
        Native Indian or Alaskan - Not Hispanic: people having origin in any of the original people of North America and who maintains cultural identification through tribal affiliation; and who are not of Hispanic origin.   Frequency: Annual Units: Persons Field Size: 67.0  
         
        Native Hawaiian – Hispanic: the Aboriginal Polynesian people of the Hawaiian Islands or their descendants; and who are of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race.  Frequency: Annual Units: Persons Field Size: 67.0  
         
        Native Hawaiian - Not Hispanic: the Aboriginal Polynesian people of the Hawaiian Islands or their descendants; and who are not of Hispanic origin.   Frequency: Annual Units: Persons Field Size: 67.0  
        Natural Gas Consumption: the amount of natural gas consumed.  Frequency: Monthly Units: Billions Cubic Feet Field Size: 1.0  
         
        Net Corporation Taxes: measurement of tax imposed on the net profit of a corporation that are taxed at the entity level in a particular jurisdiction.  Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Net Bank Income: the balance between bank operating revenues and expenses.  Frequency: Quarterly Units: Thousands USD Field Size: 2.0  
         
        Net Loan Losses Rate: the difference of Charge-offs on Allowance for Loan and Lease Losses and Recoveries on Allowance for Loan and Lease Losses to the Total Loans and Leases.
        Frequency: Quarterly Units: Ratio Field Size: 2.0  
         
        New Authorized House Building Permits: the number of new privately-owned housing units authorized by building permits.  A housing unit, as defined for purposes of this report, is a house, an apartment, a group of rooms or a single room intended for occupancy as separate living quarters.
         Frequency: Annual Units: Number (Florida & Counties), Thousands (United States) Field Size: 43.0 
         
         
        New Listings: the count of new listings added to the market in a given geography during the month.   Frequency: Monthly Units: Number Field Size: 43.0  
         
        NIKKEI 225: major stock market index comprising of 225 highly liquid stocks of the Tokyo Stock Exchange.
         Frequency: Daily Units: Index Field Size: 1.0  
         
        Nominal Gross Domestic Product: an assessment of economic production in an economy that includes current prices in its calculation. In other words, it does not strip out inflation or the pace of rising prices, which can inflate the growth figure. All goods and services counted in nominal GDP are valued at the prices that are sold for in that year.
         Frequency: Annual Units: Thousands (Counties), Millions USD (Florida), Billions (United States) Field Size: 69.0  
         
        Nominal Government Gross Domestic Product: a subsection of nominal gross domestic product that only includes government expenditures.
         Frequency: Annual Units: Thousands USD Field Size: 67.0  
         
        Nominal Private Goods Gross Domestic Product: a subsection of nominal gross domestic product that only includes private goods-producing industries.
         Frequency: Annual Units: Thousands USD Field Size: 67.0  
         
        Nominal Private Services Gross Domestic Product: a subsection of nominal gross domestic product that only includes private services-producing industries.
         Frequency: Annual Units: Thousands USD Field Size: 67.0  
         
        Non-performing Loans Ratio: the ratio of the amount of nonperforming loans in a bank's loan portfolio to the total amount of outstanding loans the bank holds. The NPL ratio measures the effectiveness of a bank in receiving repayments on its loans. The odds of loan repayment decrease significantly after 90 days, which is why the nonperforming loan designation uses this standard. Loans can be classified as nonperforming if the borrower defaults on the loan, declares bankruptcy or loses the income she needs to repay the debt. Because nonperforming loans can hurt a bank's standing as a borrower, the bank may choose to sell these loans to collection agencies or other businesses to recover its losses.
        Frequency: Quarterly Units: Ratio Field Size: 2.0  
         
        Non-store Retail Sales: the sales accrued from the selling of goods and services outside the confines of a retail facility. It is a generic term describing retailing taking place outside of shops and stores (that is, off the premises of fixed retail locations and of markets stands).
        Frequency: Monthly Units: Millions USD Field Size: 1.0
         
         
        Not Hispanic: not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin.
        Frequency: Annual Units: Persons Field Size: 67.0
         '''
       
    o = '''
        Obesity Rate: percent of the total population of a specific region who are obese.  A person has traditionally been considered to be obese if they are more than 20% over their ideal weight. Obesity has been more precisely defined by the National Institutes of Health (the NIH) as a BMI (Body Mass Index) of 30 and above.
        Frequency: Annual Units: Percent Field Size: 68.0
         
         
        Other Race – Hispanic: used to refer to a person or thing that is different or distinct from one already mentioned or known about; and is a person who is of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin.
        Frequency: Annual Units: Persons Field Size: 67.0
         
         
        Other Race – Not Hispanic: used to refer to a person or thing that is different or distinct from one already mentioned or known about; and is not of Hispanic origin.
        Frequency: Annual Units: Persons Field Size: 67.0
         
         
        Overnight Bank Funding Rate: a measure of wholesale, unsecured, overnight bank funding costs. It is calculated using federal funds transactions, certain Eurodollar transactions, and certain domestic deposit transactions, all as reported in the FR 2420 Report of Selected Money Market Rates. The federal funds market consists of domestic unsecured borrowings in U.S. dollars by depository institutions from other depository institutions and certain other entities, primarily government-sponsored enterprises. The Eurodollar market consists of unsecured U.S. dollar deposits held at banks or bank branches outside of the United States. U.S.-based banks can also take Eurodollar deposits domestically through international banking facilities (IBFs). Also included in the calculation of the OBFR are U.S. dollar deposits with a fixed overnight term and a negotiated interest rate that are booked in U.S. offices of banks.
        Frequency: Daily Units: Percent Field Size: 1.0
         '''
    p = '''
        Primary Care Physician Rate: the ratio of the population to primary care physicians.
        Frequency: Annual Units: Persons per 100K Field Size: 68.0
         
         
        Poverty Rate: corresponds to the proportion of individuals (or households) whose standard of living is lower in a given year than a set threshold, called the poverty line.
        Frequency: Annual Units: Percent Field Size: 69.0
         
         
        Percent of Children in Poverty: corresponds to the proportion of children whose standard of living is lower in a given year than a set threshold, called the poverty line.
        Frequency: Annual Units: Percent Field Size: 69.0
         
         
        Percent of Related Children in Poverty: corresponds to the proportion of related children whose standard of living is lower in a given year than a set threshold, called the poverty line.
        Frequency: Annual Units: Percent Field Size: 69.0
        
         
        Pending Listings: the count of pending listings in a given market during the specified month, if a pending definition is available for that geography. When a property is marked as pending, an offer has been accepted by the seller and all contingencies have been satisfactorily addressed or waived. Pending deals are no longer considered active listings. A home will remain in the pending state until all legal work has been processed.  Frequency: Monthly Units: Number Field Size: 43.0  
         
        Per Capita Personal Income: an area's personal income divided by its population. 
        Frequency: Annual Units: USD Field Size: 69.0  
         
        Percent Medically Uninsured: rate of individuals who have no health insurance.  Frequency: Annual Units: Percent Field Size: 68.0  
         
        Percent Physically Inactive: percent of people who do not get the recommended level of regular physical activity. The American Heart Association recommends 30-60 minutes of aerobic exercise three to four times per week to promote cardiovascular fitness.  Frequency: Annual Units: Percent Field Size: 68.0  
         
        Personal Care Sales: measurement of sales from cosmetics and personal care stores.  Products that fall underneath this umbrella include skin moisturizers, perfumes, lipsticks, fingernail polishes, shampoos, hair colors, toothpastes, and deodorants, among others.
         Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Personal Income: refers to all income collectively received by all individuals or households in a specific region. Personal income includes compensation from a number of sources, including salaries, wages, and bonuses received from employment or self-employment, dividends and distributions received from investments, rental receipts from real estate investments, and profit sharing from businesses.
         Frequency: Annual Units: USD Field Size: 67.0  
         
        Population: all the inhabitants of a particular region.
         Frequency: Annual Units: Thousands of Persons (Florida & Counties), Persons (United States) Field Size: 69.0  
         
        Precipitation: the amount of precipitation (i.e. rain, snow, hail) that a specific region experiences during a given month.  Frequency: Monthly Units: Inches Field Size: 67.0 
         
         
        Premature Death Rate: the ratio of all deaths according to the population where the deceased is younger than 75 years of age. 75 years of age is the standard consideration of a premature death according to the CDC's definition of Years of Potential Life Loss.  Frequency: Annual Units: Deaths per 100K Field Size: 67.0  
         
        Preventable Hospital Rate: the discharges for ambulatory care sensitive conditions from short-stay acute care hospitals per 1,000 medicare enrollees.
         Frequency: Annual Units: Persons per 1K Field Size: 67.0  
         
        Primary Credit Rate: the basic interest rate charged to most banks.  Frequency: Daily Units: Percent Field Size: 1.0  
         '''
    
    q = '''
        No terms under this letter. 
        '''
        
    r = '''
        Real Estate Earnings: collective earnings accrued from real estate, rental, and leasing entanglements.
         Frequency: Quarterly Units: Thousands USD Field Size: 1.0 
        
        Real Gross Domestic Product: an inflation-adjusted measure that reflects the value of all goods and services produced by an economy in a given year (expressed in base-year prices) and is often referred to as constant-price GDP, inflation-corrected GDP, or constant dollar GDP.
         Frequency: Annual Units: Thousands (Counties), Millions USD (Florida), Billions (United States) Field Size: 69.0  
         
        Real Government Gross Domestic Product: an inflation-adjusted measure that reflects the value of all government expenditures in an economy in a given year (expressed in base-year prices) and is often referred to as constant-price GDP, inflation-corrected GDP, or constant dollar GDP.
         Frequency: Annual Units: Thousands USD Field Size: 67.0  
         
        Real Private Goods Gross Domestic Product: an inflation-adjusted measure that reflects the value of all private goods produced by an economy in a given year (expressed in base-year prices) and is often referred to as constant-price GDP, inflation-corrected GDP, or constant dollar GDP.
         Frequency: Annual Units: Thousands USD Field Size: 67.0  
         
        Real Private Services Gross Domestic Product: an inflation-adjusted measure that reflects the value of all private services produced by an economy in a given year (expressed in base-year prices) and is often referred to as constant-price GDP, inflation-corrected GDP, or constant dollar GDP.
         Frequency: Annual Units: Thousands USD Field Size: 67.0  
         
        Recreation Sales: measurement of sales from sports equipment and recreation stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0 
         
         
        Regular Gas Price Per Gallon: weighted average price per gallon for regular gas based on the sampling of approximately 350 retail outlets.  Frequency: Weekly Units: USD per Gallon Field Size: 1.0  
         
        Rental Vacancy Rate: the percentage of all available units in a rental property, such as a hotel or apartment complex, that are vacant or unoccupied at a particular time.  Frequency: Annual Units: Percent Field Size: 2.0  
         
        Restaurants Sales: measurement of sales from restaurants.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Return on Average Bank Equity: refers to the performance of a company over a financial year. This ratio is an adjusted version of the return of equity that measures the profitability of a bank.  Frequency: Quarterly  Units: Percent Field Size: 2.0 
        '''
    s = '''
        Severance Taxes: estimated tax revenue stemming from the extraction of non-renewable natural resources that are intended for consumption in other states. These natural resources include such as crude oil, condensate and natural gas, coalbed methane, timber, uranium, and carbon dioxide.
        Frequency: Quarterly Units: Millions USD Field Size: 1.0 
         
         
        Smoking Rate: the percent of individuals in a given region that smoke on a regular basis.
        Frequency: Annual Units: Percent Field Size: 68.0
         
         
        SNAP Benefits Recipients: number of individuals provided nutrition benefits to supplement the food budget of needy families so they can purchase healthy food and move towards self-sufficiency.
        Frequency: Annual Units: Number Field Size: 67.0
         
         
        Secured Overnight Financing Rate: a benchmark interest rate for dollar-denominated derivatives and loans that is replacing the London interbank offered rate
        Frequency: Daily Units: Percent Field Size: 1.0
         
         
        Standard & Poor’s 500 Index (S&P 500): a market-capitalization-weighted index of 500 of the largest publicly traded companies in the U.S.
         Frequency: Daily Units: Index Field Size: 1.0
         
         
        Subprime Credit Population Rate: the percent of individuals in a given region that are registered as having a subprime credit score, which is any value logged within the range of 580 and 619.
        Frequency: Quarterly Units: Percent Field Size: 67.0
         
         
        Supplies Sales: measurement of sales from supplies outlets and stores.  Frequency: Monthly Units: Millions USD Field Size: 1.0  
         '''
        
    t = '''
        Teen Birth Rate: rate of teenagers aged 15 – 19 that gave birth to a child.   Frequency: Annual Units: Persons per 1K Field Size: 68.0  
         
        Thirty Year Fixed Mortgage Rate: the average price of a mortgage loan charging an interest rate that remains the same throughout the 30-year term of the loan.  Frequency: Weekly Units: Percent Field Size: 1.0 
        
        Tobacco Sales Taxes: estimated tax revenue stemming from the sales of tobacco products.
         Frequency: Quarterly Units: Millions USD Field Size: 1.0  
         
        Total Business Sales: measurement of sales from all business ventures in a given region.
         Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Total Held-To-Maturity Securities: total dollar value of securities that are purchased to be owned until maturity.
         Frequency: Quarterly Units: Thousands USD Field Size: 2.0  
         
        Total Retail Food Sales: measurement of sales from food retail outlets.
         Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Total Taxes: estimated tax revenue stemming from all sources of taxable products and services.
         Frequency: Quarterly Units: Millions USD Field Size: 1.0
         
         
        Treasury Bill & Bond Yield Rate: the return on investment, expressed as a percentage, on the U.S. government's debt obligations. In essence, the Treasury yield is the effective interest rate that the U.S. government pays to borrow money for different lengths of time.
        Frequency: Daily Units: Percent Field Size: 1.0  
         
         
        Twenty-Five & Up Associate's Degree: percent of individuals aged 25 and up that have received an associate’s degree. 
         Frequency: Annual Units: Percent Field Size: 67.0  
         
        Two Or More Races - Hispanic : people who identify with more than just one of the five major races; and who are of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race.  Frequency: Annual Units: Persons Field Size: 67.0  
         nbsp;
        Two Or More Races - Not Hispanic: people who identify with more than just one of the five major races; and who is not of Hispanic origin.   Frequency: Annual Units: Persons Field Size: 67.0 
        
        Two Races Including Some Other Race – Hispanic: people who identify with more than just one of all the available races; and who are of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race.  Frequency: Annual Units: Persons Field Size: 67.0  
         
        Two Races Including Some Other Race - Not Hispanic : people who identify with more than just one of all the available races; and who is not of Hispanic origin.   Frequency: Annual Units: Persons Field Size: 67.0  
         '''
        
    u = '''
        Unemployment Rate: the percentage of unemployed workers in the total labor force. Workers are considered unemployed if they currently do not work, even though they are able and willing to do so.
         Frequency: Monthly Units: Percent Field Size: 69.0  
         
        Utilities Taxes: estimated tax revenue stemming from public service businesses, including businesses that engage in transportation, communications, and the supply of energy, natural gas, and water.
         Frequency: Quarterly Units: Millions USD Field Size: 1.0 
        '''
    
    v = '''
        Vehicle Sales: measurement of sales from vehicles.
         Frequency: Monthly Units: Millions USD Field Size: 1.0  
         
        Velocity of Money Stock: measurement of the rate at which money is exchanged in an economy. It is the number of times that money moves from one entity to another. It also refers to how much a unit of currency is used in a given period of time. Simply put, it's the rate at which consumers and businesses in an economy collectively spend money.
         Frequency: Annual Units: Ratio Field Size: 1.0  
         
        Violent / Property Crimes: the combined number of violent and property crime offenses within a given region during a specified time.
         Frequency: Annual Units: Number Field Size: 67.0  
         '''
        
    w = '''
        Wages: the average of fixed regular payments, typically paid on a daily or weekly basis, made by an employer to an employee, especially to a manual or unskilled worker, in a given region.
         Frequency: Annual Units: USD Field Size: 41.0  
         
        White – Hispanic: a racial classification and skin color specifier, used mostly and exclusively for people of European and (more technically) Western Eurasian descent; and who are of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race.  Frequency: Annual Units: Persons Field Size: 67.0  
         
        White - Not Hispanic: a racial classification and skin color specifier, used mostly and exclusively for people of European and (more technically) Western Eurasian descent; and who is not of Hispanic origin.   Frequency: Annual Units: Persons Field Size: 67.0  
         
        Wilshire 5000: a market-capitalization-weighted index of the market value of all US-stocks actively traded in the United States.  Frequency: Daily Units: Index Field Size: 1.0
        '''
    x = '''
        No terms under this letter. 
        '''
    y = '''
        No terms under this letter. 
        '''
    z = '''
        No terms under this letter. 
        '''
    
    switcher={
       'a':a,
       'b':b,
       'c':c,
       'd':d,
       'e':e,
       'f':f,
       'g':g,
       'h':h,
       'i':i, 
       'j':j,
       'k':k, 
       'l':l, 
       'm':m, 
       'n':n, 
       'o':o, 
       'p':p, 
       'q':q, 
       'r':r, 
       's':s, 
       't':t, 
       'u':u, 
       'v':v, 
       'w':w, 
       'x':x, 
       'y':y, 
       'z':z
       
     }
    
    return switcher.get(letter,"Invalid")


def getStateCodes():
    
    states = {'Florida': 12, 'New York': 36, 'California': 6, 'Texas': 48, 'Pennsylvania': 42}
    
    return states



def getStateVarCodes(): 
    
    var_list = ['Unemployment Rate', 'Nominal Gdp', 'Real Gdp', 'Nominal Private Goods Gdp', 
                'Real Private Goods Gdp', 'Nominal Private Services Gdp', 'Real Private Services Gdp', 
                'Nominal Govt Gdp', 'Real Govt Gdp', 'Est Median Hh', 'Wages', 'Income Inequality', 
                'Personal Income', 'Per Capita Personal Income', 'Median House Prices', 
                'Average House Prices', 'Median Price Per Sq Foot', 'Median Sq Footage', 
                'New Listing', 'Active Listing', 'Pending Listing', 'New House Building Permits', 
                'Home Ownership Rate', 'Market Hotness Rank', 'Snap Benefits Recipients', 
                'Pct All Ages Poverty', 'Subprime Credit Population', 'Pct Children Poverty', 
                'Pct Related Children Poverty', 'Burdened Households', 'High School Grad', 
                'Bachelor Degree', 'Twenty Five Up Associate Degree', 'Disconnected Youth', 
                'Population', 'Initial Claims', 'Rental Vacancy Rate', 'Home Vacancy Rate', 
                'Continued Claims', 'Minimum Wage', 'Labor Force Rate', 'Insured Unemployment Rate', 
                'Avg Hourly Earnings', 'Nonperforming Loans Ratio', 'Commercial Banks', 
                'Real Estate Earnings', 'Bank Assets', 'Govt Employees', 'Net Loan Losses Rate', 
                'Rtn Avg Bank Equity', 'Allocated Transfer Risk Reserves', 'Discouraged Workers', 
                'Median Days Market', 'Total Held To Maturity Securities', 'Net Income Banks', 
                'Business Applications', 'Average Weekly Hours Worked', 'Employment Cost Index', 
                'Mean Commuting Time', 'Premature Death Rate', 'Violent Property Crimes', 
                'Preventable Hospital Rate', 'Total Taxes', 'Net Corporation Taxes', 'Motor Fuel Taxes', 
                'Severance Taxes', 'General Sales Taxes', 'Utilities Taxes', 'Alcoholic Sales Taxes', 
                'Insurance Premiums Taxes', 'Documentary Stock Taxes', 'Motor License Taxes', 
                'Tobacco Sales Taxes', 'Corporate License Taxes', 'Fair Poor Health', 'Med Uninsured', 
                'Smokers', 'Obesity Rate', 'Excessive Drinking', 'Mv Mortality Rate', 'Teen Birth Rate', 
                'Pcp Rate', 'Mammogram Rate', 'Low Birthweight Rate', 'Mhp Rate', 'Pct Diabetes', 
                'Pct Physically Inactive', 'Hiv Rate', 'Hispanic', 'Not Hispanic', 'Health Care Assistance Earnings', 
                'Employment Level', 'Civilian Labor Force', 'White Not Hispanic', 'Black Not Hispanic', 
                'Indian Or Alaska Not Hispanic', 'Asian Not Hispanic', 'Native Hawaiian Not Hispanic', 
                'Other Not Hispanic', 'Two Or More Races Not Hispanic', 'Two Races Including Some Other Race Not Hispanic', 
                'White Hispanic', 'Black Hispanic', 'Indian Or Alaska Hispanic', 'Asian Hispanic', 
                'Native Hawaiian Hispanic', 'Other Hispanic', 'Two Or More Races Hispanic', 
                'Two Races Including Some Other Race Hispanic', 'Precipitation', 'Avg Temp', 
                'Max Temp', 'Min Temp', 'Retail And Recreation', 'Grocery And Pharmacy', 'Parks', 
                'Transit Stations', 'Workplaces', 'Residential', 'Current Municipal Bond Yield', 
                'Current Plus One Municipal Bond Yield', 'Current Plus Two Municipal Bond Yield', 
                'Current Plus Five Municipal Bond Yield', 'Current Plus Ten Municipal Bond Yield', 
                'Current Plus Fifteen Municipal Bond Yield', 'Current Plus Twenty Municipal Bond Yield', 
                'Current Plus Twenty Five Municipal Bond Yield', 'Covid Cases', 'Covid Deaths']
    
    var_code_list = list(range(1, len(var_list) + 1, 1))
                            
    d = dict(zip(var_list, var_code_list))
    
    return d
    
    

def getUSVarCodes():
    
    var_list = ['Federal Funds Rate', 'Ice Bofa High Yield Index', 'US / Euro Exchange Rate', 
                'S&P 500', 'Dow Jones', 'China Us Ex Rate', 'Japan Us Ex Rate', 'Bank Prime Rate', 
                'Primary Credit Rate', 'Bank Deposits', 'Bank Liabilities', 'Inflation', 
                'Financial Stress Index', 'Discount Rate', 'Three Month Libor', 'One Year Libor', 
                'Overnight Bank Funding Rate', 'Sofr', 'M1', 'M2', 'Commercial Paper', 
                'Velocity Money Stock', 'Litecoin', 'Nikkei225', 'Wilshire 5000', 'Nasdaq', 
                'Bitcoin', 'Ethereum', 'Six Month Hqm Spot', 'One Year Hqm Spot', 'Two Year Hqm Spot', 
                'Five Year Hqm Spot', 'Ten Year Hqm Spot', 'Thirty Year Hqm Spot', 'Fifty Year Hqm Spot', 
                'One Hundred Year Hqm Spot', 'One Month Tbill Rate', 'Three Month Tbill Rate', 
                'Six Month Tbill Rate', 'One Year Tbill Rate', 'Two Year Tbill Rate', 
                'Three Year Tbill Rate', 'Five Year Tbill Rate', 'Seven Year Tbill Rate', 
                'Ten Year Tbill Rate', 'Twenty Year Tbill Rate', 'Thirty Year Tbill Rate', 
                'Venezuela Us Ex Rate', 'Southafrica Us Ex Rate', 'South Korea Us Ex Rate', 
                'Sweden Us Ex Rate', 'Switzerland Us Ex Rate', 'Hong Kong Us Ex Rate', 
                'Mexico Us Ex Rate', 'Canada Us Ex Rate', 'Us Australia Ex Rate', 'Us Uk Ex Rate', 
                'Singapore Us Ex Rate', 'India Us Ex Rate', 'Brazil Us Ex Rate', 'Diesel Gas Gallon Price', 
                'Reg Gas Gallon Price', 'Natural Gas Consumption', 'Fifteen Year Fixed Mortgage', 
                'Thirty Year Fixed Mortgage', 'House Delinquency Rate', 'Five One Year Ajustable Mortgage', 
                'Total Business Sales', 'Total Retail Food Sales', 'Restaurants Sales', 'Clothing Sales', 
                'Supplies Sales', 'Furniture Sales', 'Grocery Sales', 'Gas Station Sales', 
                'Electronics Sales', 'Vehicle Sales', 'Department Store Sales', 'Personal Care Sales', 
                'Recreation Sales', 'General Merch Sales', 'Misc Store Sales', 'Nonstore Retail Sales', 
                'One Week Libor', 'Covid Recoveries']

        
    var_code_list = list(range(1, len(var_list) + 1, 1))
                            
    d = dict(zip(var_list, var_code_list))
    
    return d
    


def getStateData(state_code, var_code):
    
    states = {'subfolder': 12, 'nydatahub': 36, 'calidatahub': 6, 'txdatahub': 48, 'penndatahub': 42}
    
    key_list = list(states.keys())
    val_list = list(states.values())
     
    position = val_list.index(state_code)
    folder = key_list[position]
    
    
    var_dict = {'UNEMPLOYMENT_RATE': 1, 'NOMINAL_GDP': 2, 'REAL_GDP': 3, 'NOMINAL_PRIVATE_GOODS_GDP': 4, 
                'REAL_PRIVATE_GOODS_GDP': 5, 'NOMINAL_PRIVATE_SERVICES_GDP': 6, 
                'REAL_PRIVATE_SERVICES_GDP': 7, 'NOMINAL_GOVT_GDP': 8, 'REAL_GOVT_GDP': 9, 
                'EST_MEDIAN_HH': 10, 'WAGES': 11, 'INCOME_INEQUALITY': 12, 'PERSONAL_INCOME': 13, 
                'PER_CAPITA_PERSONAL_INCOME': 14, 'MEDIAN_HOUSE_PRICES': 15, 'AVERAGE_HOUSE_PRICES': 16, 
                'MEDIAN_PRICE_PER_SQ_FOOT': 17, 'MEDIAN_SQ_FOOTAGE': 18, 'NEW_LISTING': 19, 
                'ACTIVE_LISTING': 20, 'PENDING_LISTING': 21, 'NEW_HOUSE_BUILDING_PERMITS': 22, 
                'HOME_OWNERSHIP_RATE': 23, 'MARKET_HOTNESS_RANK': 24, 'SNAP_BENEFITS_RECIPIENTS': 25, 
                'PCT_ALL_AGES_POVERTY': 26, 'SUBPRIME_CREDIT_POPULATION': 27, 'PCT_CHILDREN_POVERTY': 28, 
                'PCT_RELATED_CHILDREN_POVERTY': 29, 'BURDENED_HOUSEHOLDS': 30, 'HIGH_SCHOOL_GRAD': 31, 
                'BACHELOR_DEGREE': 32, 'TWENTY_FIVE_UP_ASSOCIATE_DEGREE': 33, 'DISCONNECTED_YOUTH': 34, 
                'POPULATION': 35, 'INITIAL_CLAIMS': 36, 'RENTAL_VACANCY_RATE': 37, 'HOME_VACANCY_RATE': 38, 
                'CONTINUED_CLAIMS': 39, 'MINIMUM_WAGE': 40, 'LABOR_FORCE_RATE': 41, 
                'INSURED_UNEMPLOYMENT_RATE': 42, 'AVG_HOURLY_EARNINGS': 43, 
                'NONPERFORMING_LOANS_RATIO': 44, 'COMMERCIAL_BANKS': 45, 'REAL_ESTATE_EARNINGS': 46, 
                'BANK_ASSETS': 47, 'GOVT_EMPLOYEES': 48, 'NET_LOAN_LOSSES_RATE': 49, 
                'RTN_AVG_BANK_EQUITY': 50, 'ALLOCATED_TRANSFER_RISK_RESERVES': 51, 
                'DISCOURAGED_WORKERS': 52, 'MEDIAN_DAYS_MARKET': 53, 'TOTAL_HELD_TO_MATURITY_SECURITIES': 54, 
                'NET_INCOME_BANKS': 55, 'BUSINESS_APPLICATIONS': 56, 'AVERAGE_WEEKLY_HOURS_WORKED': 57, 
                'EMPLOYMENT_COST_INDEX': 58, 'MEAN_COMMUTING_TIME': 59, 'PREMATURE_DEATH_RATE': 60, 
                'VIOLENT_PROPERTY_CRIMES': 61, 'PREVENTABLE_HOSPITAL_RATE': 62, 'TOTAL_TAXES': 63, 
                'NET_CORPORATION_TAXES': 64, 'MOTOR_FUEL_TAXES': 65, 'SEVERANCE_TAXES': 66, 
                'GENERAL_SALES_TAXES': 67, 'UTILITIES_TAXES': 68, 'ALCOHOLIC_SALES_TAXES': 69, 
                'INSURANCE_PREMIUMS_TAXES': 70, 'DOCUMENTARY_STOCK_TAXES': 71, 'MOTOR_LICENSE_TAXES': 72, 
                'TOBACCO_SALES_TAXES': 73, 'CORPORATE_LICENSE_TAXES': 74, 'FAIR_POOR_HEALTH': 75, 
                'MED_UNINSURED': 76, 'SMOKERS': 77, 'OBESITY_RATE': 78, 'EXCESSIVE_DRINKING': 79, 
                'MV_MORTALITY_RATE': 80, 'TEEN_BIRTH_RATE': 81, 'PCP_RATE': 82, 'MAMMOGRAM_RATE': 83, 
                'LOW_BIRTHWEIGHT_RATE': 84, 'MHP_RATE': 85, 'PCT_DIABETES': 86, 'PCT_PHYSICALLY_INACTIVE': 87, 
                'HIV_RATE': 88, 'HISPANIC': 89, 'NOT_HISPANIC': 90, 'HEALTH_CARE_ASSISTANCE_EARNINGS': 91, 
                'EMPLOYMENT_LEVEL': 92, 'CIVILIAN_LABOR_FORCE': 93, 'WHITE_NOT_HISPANIC': 94, 
                'BLACK_NOT_HISPANIC': 95, 'INDIAN_OR_ALASKA_NOT_HISPANIC': 96, 'ASIAN_NOT_HISPANIC': 97, 
                'NATIVE_HAWAIIAN_NOT_HISPANIC': 98, 'OTHER_NOT_HISPANIC': 99, 'TWO_OR_MORE_RACES_NOT_HISPANIC': 100, 
                'TWO_RACES_INCLUDING_SOME_OTHER_RACE_NOT_HISPANIC': 101, 'WHITE_HISPANIC': 102, 
                'BLACK_HISPANIC': 103, 'INDIAN_OR_ALASKA_HISPANIC': 104, 'ASIAN_HISPANIC': 105, 
                'NATIVE_HAWAIIAN_HISPANIC': 106, 'OTHER_HISPANIC': 107, 'TWO_OR_MORE_RACES_HISPANIC': 108, 
                'TWO_RACES_INCLUDING_SOME_OTHER_RACE_HISPANIC': 109, 'PRECIPITATION': 110, 'AVG_TEMP': 111, 
                'MAX_TEMP': 112, 'MIN_TEMP': 113, 'RETAIL_AND_RECREATION': 114, 'GROCERY_AND_PHARMACY': 115, 
                'PARKS': 116, 'TRANSIT_STATIONS': 117, 'WORKPLACES': 118, 'RESIDENTIAL': 119, 
                'CURRENT_MUNICIPAL_BOND_YIELD': 120, 'CURRENT_PLUS_ONE_MUNICIPAL_BOND_YIELD': 121, 
                'CURRENT_PLUS_TWO_MUNICIPAL_BOND_YIELD': 122, 'CURRENT_PLUS_FIVE_MUNICIPAL_BOND_YIELD': 123, 
                'CURRENT_PLUS_TEN_MUNICIPAL_BOND_YIELD': 124, 'CURRENT_PLUS_FIFTEEN_MUNICIPAL_BOND_YIELD': 125, 
                'CURRENT_PLUS_TWENTY_MUNICIPAL_BOND_YIELD': 126, 'CURRENT_PLUS_TWENTY_FIVE_MUNICIPAL_BOND_YIELD': 127, 
                'COVID_CASES': 128, 'COVID_DEATHS': 129}
    
    key_list = list(var_dict.keys())
    val_list = list(var_dict.values())
     
    position = val_list.index(var_code)
    var = key_list[position]
    
    
    df = pd.read_excel('https://thedatacycle.com/{}/ExcelTables/{}.xlsx'.format(folder, var))
    
    df.drop(['Unnamed: 0'], axis = 1, inplace=True)
    
    return df


def getUSData(var_code):
    

    var_dict = {'FED_FUNDS_RATE': 1, 'ICE_BOFA_HIGH_YIELD_INDEX': 2, 'US_EURO_EX_RATE': 3, 'SP500': 4, 
                'DOW_JONES': 5, 'CHINA_US_EX_RATE': 6, 'JAPAN_US_EX_RATE': 7, 'BANK_PRIME_RATE': 8, 
                'PRIMARY_CREDIT_RATE': 9, 'BANK_DEPOSITS': 10, 'BANK_LIABILITIES': 11, 'INFLATION': 12, 
                'FINANCIAL_STRESS_INDEX': 13, 'DISCOUNT_RATE': 14, 'THREE_MONTH_LIBOR': 15, 
                'ONE_YEAR_LIBOR': 16, 'OVERNIGHT_BANK_FUNDING_RATE': 17, 'SOFR': 18, 'M1': 19, 'M2': 20, 
                'COMMERCIAL_PAPER': 21, 'VELOCITY_MONEY_STOCK': 22, 'LITECOIN': 23, 'NIKKEI225': 24, 
                'WILSHIRE_5000': 25, 'NASDAQ': 26, 'BITCOIN': 27, 'ETHEREUM': 28, 'SIX_MONTH_HQM_SPOT': 29, 
                'ONE_YEAR_HQM_SPOT': 30, 'TWO_YEAR_HQM_SPOT': 31, 'FIVE_YEAR_HQM_SPOT': 32, 
                'TEN_YEAR_HQM_SPOT': 33, 'THIRTY_YEAR_HQM_SPOT': 34, 'FIFTY_YEAR_HQM_SPOT': 35, 
                'ONE_HUNDRED_YEAR_HQM_SPOT': 36, 'ONE_MONTH_TBILL_RATE': 37, 'THREE_MONTH_TBILL_RATE': 38, 
                'SIX_MONTH_TBILL_RATE': 39, 'ONE_YEAR_TBILL_RATE': 40, 'TWO_YEAR_TBILL_RATE': 41, 
                'THREE_YEAR_TBILL_RATE': 42, 'FIVE_YEAR_TBILL_RATE': 43, 'SEVEN_YEAR_TBILL_RATE': 44, 
                'TEN_YEAR_TBILL_RATE': 45, 'TWENTY_YEAR_TBILL_RATE': 46, 'THIRTY_YEAR_TBILL_RATE': 47, 
                'VENEZUELA_US_EX_RATE': 48, 'SOUTHAFRICA_US_EX_RATE': 49, 'SOUTH_KOREA_US_EX_RATE': 50, 
                'SWEDEN_US_EX_RATE': 51, 'SWITZERLAND_US_EX_RATE': 52, 'HONG_KONG_US_EX_RATE': 53, 
                'MEXICO_US_EX_RATE': 54, 'CANADA_US_EX_RATE': 55, 'US_AUSTRALIA_EX_RATE': 56, 
                'US_UK_EX_RATE': 57, 'SINGAPORE_US_EX_RATE': 58, 'INDIA_US_EX_RATE': 59, 
                'BRAZIL_US_EX_RATE': 60, 'DIESEL_GAS_GALLON_PRICE': 61, 'REG_GAS_GALLON_PRICE': 62, 
                'NATURAL_GAS_CONSUMPTION': 63, 'FIFTEEN_YEAR_FIXED_MORTGAGE': 64, 
                'THIRTY_YEAR_FIXED_MORTGAGE': 65, 'HOUSE_DELINQUENCY_RATE': 66, 
                'FIVE_ONE_YEAR_AJUSTABLE_MORTGAGE': 67, 'TOTAL_BUSINESS_SALES': 68, 
                'TOTAL_RETAIL_FOOD_SALES': 69, 'RESTAURANTS_SALES': 70, 'CLOTHING_SALES': 71, 
                'SUPPLIES_SALES': 72, 'FURNITURE_SALES': 73, 'GROCERY_SALES': 74, 'GAS_STATION_SALES': 75, 
                'ELECTRONICS_SALES': 76, 'VEHICLE_SALES': 77, 'DEPARTMENT_STORE_SALES': 78, 
                'PERSONAL_CARE_SALES': 79, 'RECREATION_SALES': 80, 'GENERAL_MERCH_SALES': 81, 
                'MISC_STORE_SALES': 82, 'NONSTORE_RETAIL_SALES': 83, 'ONE_WEEK_LIBOR': 84, 
                'COVID_RECOVERIES': 85}
    
    key_list = list(var_dict.keys())
    val_list = list(var_dict.values())
     
    position = val_list.index(var_code)
    var = key_list[position]
    
    
    df = pd.read_excel('https://thedatacycle.com/subfolder/ExcelTables/{}.xlsx'.format(var))
    
    df.drop(['Unnamed: 0'], axis = 1, inplace=True)

    return df
    









