# Dependencies and Setup
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


#Player Count
player_df = purchase_data.drop_duplicates(subset=['SN'])
player_count = len(player_df)
print("Number of Players: " + str(player_count))


#Purchasing Analysis
print("------------------------------------------------------------------------------------------------------------------------")
print("PURCHASING ANALYSIS")
item_df = purchase_data.drop_duplicates(subset=['Item ID'])
unique_items = len(item_df)
print("Unique Items: " + str(unique_items))

average_price = round(purchase_data['Price'].mean(), 2)
print("Average Purchase Price: " + str(average_price))

total_purchases = len(purchase_data)
print("Total Number of Purchases: " + str(total_purchases))

total_revenue = round(sum(purchase_data['Price']), 2)
print("Total Revenue: " + str(total_revenue))


#Gender Demographics
gender_list = []
player_count_list = []
player_percentage_list = []

player_percentage_list.append

gender = "Male"
gender_list.append(gender)
male_players_df = player_df[player_df['Gender'] == 'Male']
male_player_count = len(male_players_df)
male_player_percentage = round(((male_player_count / player_count) * 100), 2)
player_count_list.append(male_player_count)
player_percentage_list.append(str(male_player_percentage)+"%")

gender = "Female"
gender_list.append(gender)
female_players_df = player_df[player_df['Gender'] == 'Female']
female_player_count = len(female_players_df)
female_player_percentage = round(((female_player_count / player_count) * 100), 2)
player_count_list.append(female_player_count)
player_percentage_list.append(str(female_player_percentage)+"%")

gender = "Other"
gender_list.append(gender)
other_players_df = player_df[player_df['Gender'] == 'Other / Non-Disclosed']
other_player_count = len(other_players_df)
other_player_percentage = round(((other_player_count / player_count) * 100), 2)
player_count_list.append(other_player_count)
player_percentage_list.append(str(other_player_percentage)+"%")


columns = ["Gender", "Player_Count", "Player_Percentage"]
gender_demographics_df = pd.DataFrame(list(zip(gender_list, player_count_list,
                                                 player_percentage_list)), columns = columns)

print("------------------------------------------------------------------------------------------------------------------------")
print("GENDER DEMOGRAPHICS")
print(gender_demographics_df)



#Purchasing Analysis (Gender)
gender_list = []
purchase_count_list = []
average_purchase_list = []
total_purchase_list = []
average_per_person_list = []


gender = "Male"
gender_list.append(gender)
male_purchase_df = purchase_data[purchase_data['Gender'] == 'Male']
male_dup_players_dropped = male_purchase_df.drop_duplicates(subset=['SN'])
male_purchase_count = len(male_dup_players_dropped)
purchase_count_list.append(male_purchase_count)
male_average_purchase = round(male_purchase_df['Price'].mean(), 2)
average_purchase_list.append(male_average_purchase)
male_total_purchase = round(sum(male_purchase_df['Price']), 2)
total_purchase_list.append(male_total_purchase)
male_total_per = round((male_total_purchase / male_player_count), 2)
average_per_person_list.append(male_total_per)

gender = "Female"
gender_list.append(gender)
female_purchase_df = purchase_data[purchase_data['Gender'] == 'Female']
female_dup_players_dropped = female_purchase_df.drop_duplicates(subset=['SN'])
female_purchase_count = len(female_dup_players_dropped)
purchase_count_list.append(female_purchase_count)
female_average_purchase = round(female_purchase_df['Price'].mean(), 2)
average_purchase_list.append(female_average_purchase)
female_total_purchase = round(sum(female_purchase_df['Price']), 2)
total_purchase_list.append(female_total_purchase)
female_total_per = round((female_total_purchase / female_player_count), 2)
average_per_person_list.append(female_total_per)


gender = "Other"
gender_list.append(gender)
other_purchase_df = purchase_data[purchase_data['Gender'] == 'Other / Non-Disclosed']
other_dup_players_dropped = other_purchase_df.drop_duplicates(subset=['SN'])
other_purchase_count = len(other_dup_players_dropped)
purchase_count_list.append(other_purchase_count)
other_average_purchase = round(other_purchase_df['Price'].mean(), 2)
average_purchase_list.append(other_average_purchase)
other_total_purchase = round(sum(other_purchase_df['Price']), 2)
total_purchase_list.append(other_total_purchase)
other_total_per = round((other_total_purchase / other_player_count), 2)
average_per_person_list.append(other_total_per)


columns = ["Gender", "Purchase_Count", "Average_Purchase", "Total_Purchase", "Average_Purchase"]
gender_demographics_df = pd.DataFrame(list(zip(gender_list, purchase_count_list,
                                                 average_purchase_list,total_purchase_list,
                                                 average_per_person_list)), columns = columns)

print("------------------------------------------------------------------------------------------------------------------------")
print("PURCHASING ANALYSIS (GENDER)")
print(gender_demographics_df)



#Age Demographics

year_list = []
purchase_count_list = []
average_purchase_list = []
total_purchase_list = []

#Years_9
years = "0-9"
year_list.append(years)
years_9 =
[purchase_data["Age"] < int(10)]
years_9_purchase_count = len(years_9)
purchase_count_list.append(years_9_purchase_count)
years_9_average_purchase = round(years_9['Price'].mean(), 2)
average_purchase_list.append(years_9_average_purchase)
years_9_total_purchase = years_9['Price'].sum()
total_purchase_list.append(years_9_total_purchase)


#years_10_14
years = "10-14"
year_list.append(years)
years_10_14 = purchase_data[(purchase_data["Age"] >= int(10)) & (purchase_data["Age"] <= int(14))]
years_10_14_purchase_count = len(years_10_14)
purchase_count_list.append(years_10_14_purchase_count)
years_10_14_average_purchase = round(years_10_14['Price'].mean(), 2)
average_purchase_list.append(years_10_14_average_purchase)
years_10_14_total_purchase = years_10_14['Price'].sum()
total_purchase_list.append(years_10_14_total_purchase)


#years_15_19
years = "15-19"
year_list.append(years)
years_15_19 = purchase_data[(purchase_data["Age"] >= int(15)) & (purchase_data["Age"] <= int(19))]
years_15_19_purchase_count = len(years_15_19)
purchase_count_list.append(years_15_19_purchase_count)
years_15_19_average_purchase = round(years_15_19['Price'].mean(), 2)
average_purchase_list.append(years_15_19_average_purchase)
years_15_19_total_purchase = years_15_19['Price'].sum()
total_purchase_list.append(years_15_19_total_purchase)


#years_20_24
years = "20-24"
year_list.append(years)
years_20_24 = purchase_data[(purchase_data["Age"] >= int(20)) & (purchase_data["Age"] <= int(24))]
years_20_24_purchase_count = len(years_20_24)
purchase_count_list.append(years_20_24_purchase_count)
years_20_24_average_purchase = round(years_20_24['Price'].mean(), 2)
average_purchase_list.append(years_20_24_average_purchase)
years_20_24_total_purchase = years_20_24['Price'].sum()
total_purchase_list.append(years_20_24_total_purchase)


#years_25_29
years = "25-29"
year_list.append(years)
years_25_29 = purchase_data[(purchase_data["Age"] >= int(25)) & (purchase_data["Age"] <= int(29))]
years_25_29_purchase_count = len(years_25_29)
purchase_count_list.append(years_25_29_purchase_count)
years_25_29_average_purchase = round(years_25_29['Price'].mean(), 2)
average_purchase_list.append(years_25_29_average_purchase)
years_25_29_total_purchase = round(years_25_29['Price'].sum(),2)
total_purchase_list.append(years_25_29_total_purchase)

#years_30_34
years = "30-34"
year_list.append(years)
years_30_34 = purchase_data[(purchase_data["Age"] >= int(30)) & (purchase_data["Age"] <= int(34))]
years_30_34_purchase_count = len(years_30_34)
purchase_count_list.append(years_30_34_purchase_count)
years_30_34_average_purchase = round(years_30_34['Price'].mean(), 2)
average_purchase_list.append(years_30_34_average_purchase)
years_30_34_total_purchase = round(years_30_34['Price'].sum(), 2)
total_purchase_list.append(years_30_34_total_purchase)


#years_35_39
years = "35-39"
year_list.append(years)
years_35_39 = purchase_data[(purchase_data["Age"] >= int(35)) & (purchase_data["Age"] <= int(39))]
years_35_39_purchase_count = len(years_35_39)
purchase_count_list.append(years_35_39_purchase_count)
years_35_39_average_purchase = round(years_35_39['Price'].mean(), 2)
average_purchase_list.append(years_35_39_average_purchase)
years_35_39_total_purchase = years_35_39['Price'].sum()
total_purchase_list.append(years_35_39_total_purchase)



#years_40_44
years = "40-44"
year_list.append(years)
years_40_44 = purchase_data[(purchase_data["Age"] >= int(40)) & (purchase_data["Age"] <= int(44))]
years_40_44_purchase_count = len(years_40_44)
purchase_count_list.append(years_40_44_purchase_count)
years_40_44_average_purchase = round(years_40_44['Price'].mean(), 2)
average_purchase_list.append(years_40_44_average_purchase)
years_40_44_total_purchase = years_40_44['Price'].sum()
total_purchase_list.append(years_40_44_total_purchase)


#years_45_49
years = "45-49"
year_list.append(years)
years_45_49 = purchase_data[(purchase_data["Age"] >= int(45)) & (purchase_data["Age"] <= int(49))]
years_45_49_purchase_count = len(years_45_49)
purchase_count_list.append(years_45_49_purchase_count)
years_45_49_average_purchase = round(years_45_49['Price'].mean(), 2)
average_purchase_list.append(years_45_49_average_purchase)
years_45_49_total_purchase = years_45_49['Price'].sum()
total_purchase_list.append(years_45_49_total_purchase)




columns = ["Age Range", "Purchase_Count", "Average_Purchase", "Total_Purchase"]
age_demo_df = pd.DataFrame(list(zip(year_list, purchase_count_list,
                                    average_purchase_list,total_purchase_list)), columns = columns)


print("------------------------------------------------------------------------------------------------------------------------")
print("Age Demographics")
print(age_demo_df)

#Top_Spenders
player_list = []
purchase_list = []
for x in range(len(player_df)):
    player = player_df["SN"].iat[x]
    player_purchase_df = purchase_data[purchase_data["SN"] == str(player)]
    player_purchase_total = round(sum(player_purchase_df["Price"]),2)
    player_list.append(player)
    purchase_list.append(player_purchase_total)

columns = ["Player", "Purchase_Total"]
player_purchase_total_df = pd.DataFrame(list(zip(player_list, purchase_list)), columns = columns)
player_purchase_total_df = player_purchase_total_df.sort_values(['Purchase_Total'], ascending=False)
top_spenders_df = player_purchase_total_df[:5]


player_list = []
purchase_count_list = []
average_purchase_list = []
total_purchase_list = []

for y in range(len(top_spenders_df)):
    player = top_spenders_df["Player"].iat[y]
    player_list.append(player)
    player_purchase_df = purchase_data[purchase_data["SN"] == str(player)]
    purchase_count = len(player_purchase_df)
    purchase_count_list.append(purchase_count)
    average_purchase = player_purchase_df["Price"].mean()
    average_purchase_list.append(average_purchase)
    total_purchase = sum(player_purchase_df["Price"])
    total_purchase_list.append(total_purchase)
    
    
columns = ["Player", "Purchase_Count", "Average_Purchse", "Total_Spent"]
player_purchase_total_df = pd.DataFrame(list(zip(player_list, purchase_count_list,
                                                 average_purchase_list, total_purchase_list)), columns = columns)
player_purchase_total_df = player_purchase_total_df.sort_values(['Total_Spent'], ascending=False)
top_spenders_df = player_purchase_total_df[:5]
print("------------------------------------------------------------------------------------------------------------------------")
print("TOP SPENDERS")
print(top_spenders_df)


#Most Popular Items
item_id_list = []
item_total_list = []
for z in range(len(item_df)):
    item_id = item_df["Item ID"].iat[z]
    item_id_list.append(item_id)
    item_df_filtered = purchase_data[purchase_data["Item ID"] == item_id]
    item_total = len(item_df_filtered)
    item_total_list.append(item_total)


columns = ["Item_ID", "Item_Total"]
item_purchase_total_df = pd.DataFrame(list(zip(item_id_list, item_total_list)), columns = columns)
item_purchase_total_df = item_purchase_total_df.sort_values(['Item_Total'], ascending=False)
top_items_df = item_purchase_total_df[:5]



item_id_list = []
item_name_list = []
purchase_count_list = []
item_price_list = []
item_total_list = []
for a in range(len(top_items_df)):
    item_id = top_items_df["Item_ID"].iat[a]
    item_id_list.append(str(item_id))
    item_df_filtered = purchase_data[purchase_data["Item ID"] == item_id]
    item_name = str(item_df_filtered["Item Name"].iat[0])
    item_name_list.append(item_name)
    purchase_count = len(item_df_filtered)
    purchase_count_list.append(str(purchase_count))
    item_price = item_df_filtered["Price"].mode()
    item_price_list.append(item_price)
    item_total = round(top_items_df["Item_Total"].iat[a], 2)
    item_total_list.append(item_total)
    
columns = ["Item_ID", "Item_Name", "Purchase_Count", "Item_Price", "Total_Purchase_Value"]
item_purchase_total_df = pd.DataFrame(list(zip(item_id_list, item_name_list,
                                               purchase_count_list, item_price_list,
                                               item_total_list)), columns = columns)
print("------------------------------------------------------------------------------------------------------------------------")
print("MOST POPULAR ITEMS")
print(item_purchase_total_df) 

#Identify the 5 most popular items by purchase count, then list (in a table):
##tem ID
##Item Name
##Purchase Count
##Item Price
##Total Purchase Value




#Most Profitable Items
item_id_list = []
item_total_list = []
for z in range(len(item_df)):
    item_id = item_df["Item ID"].iat[z]
    item_id_list.append(item_id)
    item_df_filtered = purchase_data[purchase_data["Item ID"] == item_id]
    item_total = sum(item_df_filtered["Price"])
    item_total_list.append(item_total)


columns = ["Item_ID", "Item_Total"]
item_purchase_total_df = pd.DataFrame(list(zip(item_id_list, item_total_list)), columns = columns)
item_purchase_total_df = item_purchase_total_df.sort_values(['Item_Total'], ascending=False)
top_items_df = item_purchase_total_df[:5]


item_id_list = []
item_name_list = []
purchase_count_list = []
item_price_list = []
item_total_list = []
for a in range(len(top_items_df)):
    item_id = top_items_df["Item_ID"].iat[a]
    item_id_list.append(str(item_id))
    item_df_filtered = purchase_data[purchase_data["Item ID"] == item_id]
    item_name = str(item_df_filtered["Item Name"].iat[0])
    item_name_list.append(item_name)
    purchase_count = len(item_df_filtered)
    purchase_count_list.append(str(purchase_count))
    item_price = item_df_filtered["Price"].mode()
    item_price_list.append(item_price)
    item_total = round(top_items_df["Item_Total"].iat[a], 2)
    item_total_list.append(item_total)
    
columns = ["Item_ID", "Item_Name", "Purchase_Count", "Item_Price", "Total_Purchase_Value"]
item_purchase_total_df = pd.DataFrame(list(zip(item_id_list, item_name_list,
                                               purchase_count_list, item_price_list,
                                               item_total_list)), columns = columns)
print("------------------------------------------------------------------------------------------------------------------------")
print("MOST PROFITABLE ITEMS")
print(item_purchase_total_df) 

print("------------------------------------------------------------------------------------------------------------------------")
print("ANALYSIS")
analysis = ("After observing the data I have discovered a few trends:\n\n 1) An overwhelming majority (84%) of players are male\n 2) Most of the purchases are made by people between the ages of 20-24\n 3) The most popular items are also the most profitable  ")
            
            

print(analysis)
    
               





