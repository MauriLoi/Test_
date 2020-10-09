import csv
import pandas as pd
import numpy as np
from datetime import date

df = pd.read_csv('London Listing Airbnb Row.csv')


print(df.dtypes)                                            #Is returning the types of values for each column
print(df.info())                                            #Is returning a summary of the DataFrame
print(df.get_dtype_counts())                                #Is returning the count of the data types for all the data frame

df['security_deposit'].fillna('0', inplace=True)
df['cleaning_fee'].fillna('0', inplace=True)
df.cleaning_fee.isnull().sum()
df.security_deposit.isnull().sum()


'''a=df.columns
b=list(a)
c=df.iloc[0:0,0:]
d=c.T
f=d.index
g=pd.Series(f)
h=g[:]'''


df1=df.iloc[:,:]

null=(df1.isnull().sum())
print(null)

df2=df1.iloc[:,[31,32,33]]  #df2=df1.iloc[:,9:12]        # All the colummns that 
print
(df2) 

z=df2.columns                                     #Is returning the count list of the unique value for each variables in df.
                                                  #With a for loop for all the column returning the list and the frequency of 
                                                  #evrey single value present in that column in  descending order and the finial sum of the overall frequency of observation for each column
def unique_value_Columns():                                  
      col=list(df2.columns)
      for i in col:
          z=df2[i].value_counts()
          print(pd.Series(z))
unique_value_Columns() 
null=(df2.isnull().sum())
print(null) 
print(df2.shape)      


df3= df.iloc[:,[2,8,10,11,12,13,14,15,          # The colummns that we will definetley* need to eliminate 
                16,18,25,26,27,29,31,34,          # [ 2 = scrape_id - same for all the records , 
                37,38,50,59,61,62,                #   8 = experiences_offered(contains only none value)]
                67,68,69,70,71,72,73,74,          # The colummns from 10 to 16 they do have more than 30.000 null values we do not accepted them.
                75,76,77,78,78,80,81,83,
                94,95,97,105]]                                
                                                  #[ 10 = notes(52444 null values),
                                                  #  11 = transit(31248 null values) ,                                29 = host_thumbnail_url(small face picture),
                                                  #  12 = access(39065 null values),                                  31 = host_neighbourhood(18861 null values),
                                                  #  13 = interaction(35706 null values) ,                            34 = host_verifications(phone number ,email),
                                                  #  14 = house_rules(36008 null values) ,                            37 = street(Borough, Ward, Street)
                                                  #  15 = thumbnail_url(85273 null values),                           38 = neighbourhood
                                                  #  16 = medium_url(85273 null values),                              40 = neighbourhood_group_cleansed 
                                                  #  18 = xl_picture_url(85273 null values),                          41 = city ( All London almost )
                                                  #  25 = host_response_time(24822 null values),                      42 = state (All England)
                                                  #  26 = host_response_rate(24822 null values) ,                     97 = is_business_travel_ready(f 85273)
                                                  #  27 = host_acceptance_rate (85273 null values) ,                  105 = reviews_per_month(we will re-calculate this field using our formula)
                                                  
                                                  #  44 = market (London 84417)                                       69 = minimum_minimum_nights
                                                  #  45 = smart_location                                              70 = maximum_minimum_nights
                                                  #  46 = country_code (GB 85270,FR 2,ES 1)                           71 = minimum_maximum_nights
                                                  #  47 = Country (United Kingdom 85270,France 2,Spain 1)             72 = maximum_maximum_nights 
                                                  #  50 = is_location_exact(unimportant inacurate up to 150 meters)   73 = minimum_nights_avg_ntm
                                                  #  59 = square_feet(84859 null values)                              74 = maximum_nights_avg_ntm
                                                  #  61 = weekly_price(78082 null values)                             75 = calendar_updated(we are not interested in future data that is a subject to daily updates)
                                                  #  62 = monthly_price(80144 null values)                            76 = has_availability(as above)
                                                  #  67 = minimum_nights                                              77 = availability_30(as above)
                                                  #  68 = maximum_nights                                              78 = availability_60(as above)
                                                  
                                                  #  79 = availability_90(as above)                                   
                                                  #  80 = availability_365(as above)                                 
                                                  #  81 = calendar_last_scraped(as above)  
                                                  #  83 = number_of_reviews_ltm                        
                                                  #  94 = license(85100)
                                                  #  95 = jurisdiction_names(85271)




df4=df.iloc[:,[0,19,22,28,35,36,48,49,51,52,53,54,
               55,56,57,60,63,64,65,66,67,82
               ,93,96,98,99]]                    #All the colummns that do contain int[possible numerical value] for numerical analysis 
                                                  #   0 =  Id , 19 = host_id                           63 = security_deposit(29652 null values)      
                                                  #   22 = host_since(date)                            64 = cleaning_fee(21529 null values) 
                                                  #   28 = host_is_superhost(t,f boelean value),       65 = guests_included(descrete value which we will use to evaluate the cost per person)
                                                  #   51 = property_type                               66 = extra_people(cost of additional person per night)
                                                  #   48 = latitude                                    67 = minimum_nights
                                                  #   49 = longitude                                   82 = number_of_reviews
                                                  #   53 = room_type                                   93 = requires_license                           
                                                  #   54 = accommodates                                96 = instant_bookable(f 48093,t 37180)
                                                  #   55 = bathrooms                                   98 = cancellation_policy(flexible,moderate,strict )
                                                  #   56 = bedrooms                                    99 = require_guest_profile_picture(f 84414,t 859)
                                                  #   57 = beds                                        100 = require_guest_phone_verification(f 83844,t 1429)
                                                  #   57 = beds                                        101 = calculated_host_listings_count(continious value,number of host listings
                                                  #   58 = bed_type                                          #another metric to measure host experience or to distinguish buisness from individual)
                                                  #   60 = price                                       35 = host_has_profile_pic(f 230,t 85027)
                                                  #   36 = host_identity_verified(f 54698 ,t 30559)
                                                                                       
                                                                                                             
df5=df.iloc[:,[1,4,5,6,7,17,20,30,
               32,33]]                    # All the colummns that do contain string[verbal] value for further text analyis
                                                  # [ 1 = listing_url , 
                                                  #   4 = name(Title of the adds) ,
                                                  #   5 = summary , 
                                                  #   6 = space , 
                                                  #   7 = description ,
                                                  #  17 = picture_url ,
                                                  #  20 = host_url (Host web page we all the adds) , 
                                                  #  21 = host_name(name of the host),
                                                  #  30 = host_picture_url ,
                                                  #  32 = host_listings_count , 
                                                  #  33 = host_total_listings_count ]
                                                  #  48 = latitude
                                                  #  49 = longitude
df6=df.iloc[:,[3,9,21,23,24,37,39,43,
                58,84,85,86,87,88,89,
                90,91,92,93,102,103,104]]        # This will be the dataframe with all the not defined colummns 
                                                  # [ 3 = last_scraped(we will use it to calculate reviews_per_month)        84 = first_review(21003 null values )
                                                  #   9 = neighborhood_overview                                              85 = last_review(21003 null values)
                                                  #   21 = host_name                                                         86 = review_scores_rating(22682 null values )
                                                  #   23 = host_location(London, England, United Kingdom)                    87 = review_scores_accuracy(22733)
                                                  #   24 = host_about                                                        88 = review_scores_cleanliness(22720)
                                                  #   39 = neighbourhood_cleansed( Ward)                                     89 = review_scores_checkin(22781)
                                                  #   43 = zipcode                                                           90 = review_scores_communication(22726)
                                                  #   58 = amenities                                                         91 = review_scores_location(22780)
                                                  #  102 = calculated_host_listings_count_entire_homes                       92 = review_scores_value(22781)
                                                  #  103 = calculated_host_listings_count_private_rooms                      93 = requires_license
                                                  #  104 = calculated_host_listings_count_shared_rooms

dfListing_Duration=df6.iloc[:,[9,10]] 
dfListing_Duration.dropna()  

                  
df7=df.iloc[:,[0,19,22,28,51,52,53,54,55,56,
                57,60,65,66,67,82,93,96,98,99,
                1,4,5,6,7,17,20,30,32,33,48,
                49,3,9,21,23,24,37,39,43,
                58,63,64,84,85,86,87,88,
                89,90,91,92,93,102,103,104]]


df4= pd.concat([df4,df.last_review], axis=1)
df4= pd.concat([df4,df.first_review], axis=1)
df4= pd.concat([df4,df.number_of_reviews], axis=1)

df4.columns


df3.to_csv('LondonAirbnb_Removed_colummns.csv',index=False)
df4.to_csv('LondonAirbnb_Numerical_colummns.csv',index=False)
df5.to_csv('LondonAirbnb_String_colummns.csv',index=False)
df6.to_csv('LondonAirbnb_Maybe_colummns.csv',index=False)

df7.to_csv('LondonAirbnb_Total_colummns.csv',index=False)

null=(df7.isnull().sum())
print(null) 

df4.isnull().sum()

