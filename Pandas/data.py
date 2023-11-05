import pandas as pd

data = pd.read_csv("pandas_numpy_guide/data.csv")

data.dropna(inplace=True)



total=data[' Number of bytes'].sum()
print("the total number of bytes used", total)

average_number=total/data[' Number of bytes'].count()
print("the average number of bytes per request", average_number)

popular_country=data[' Country'].value_counts().idxmax()
print("the most popular country (by the number of requests)", popular_country)

third_place_user=data.sort_values(by=[' Number of bytes']).iloc[-3][' Username']
print("the user who is on the 3rd place by the number of bytes",third_place_user)


bytes_used_by_Ukraine=data.loc[data[' Country'] == ' Ukraine'][" Number of bytes"].sum()
print("the number of bytes used by users from Ukraine", bytes_used_by_Ukraine)

unique_users=data[' Username'].nunique()
print("number of unique users", unique_users)


bytes_used_by_Ukraine=data.loc[data[' Country'] == ' Ukraine'][" Number of bytes"].sum()
num_req_Ukraine=data.loc[data[' Country'] == ' Ukraine'][" Number of bytes"].count()
bytes_used_by_UK=data.loc[data[' Country'] == ' UK'][" Number of bytes"].sum()
num_req_UK=data.loc[data[' Country'] == ' UK'][" Number of bytes"].count()
difference=int((bytes_used_by_UK/num_req_UK)-(bytes_used_by_Ukraine/num_req_Ukraine))
print("the difference between the average number of bytes "
      "per request between users from Ukraine and the UK", difference)

num_unique_IP=data["IP"].nunique()
total_bytes=data[' Number of bytes'].sum()
ip_average_number=total_bytes/num_unique_IP
print('average number of bytes per IP address', ip_average_number)

users_from_Europe =data.loc[data[' Country'].isin([' UK',' France',' Germany',' Poland' ,' Ukraine'])][' Username'].nunique()
print('total number of users from Europe (UK, France, Germany, Poland and Ukraine)', users_from_Europe )

results=pd.DataFrame({"the total number of bytes used" : [total],
                        "the average number of bytes per request": [average_number],
                        "the most popular country (by the number of requests)": [popular_country],
                        "the user who is on the 3rd place by the number of bytes": [third_place_user],
                        "the number of bytes used by users from Ukraine": [bytes_used_by_Ukraine],
                        "number of unique users": [unique_users],
                        "the difference between the average number of bytes "
                              "per request between users from Ukraine and the UK": [difference],
                        'average number of bytes per IP address': [ip_average_number]
                    })
results.to_csv('results1.csv', index=False)


