import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data['temp'])
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# # total_temp = 0
# # for temp in temp_list:
# #     total_temp += temp
# # avarage_temp = total_temp / len(temp_list)
# avarage_temp = sum(temp_list) / len(temp_list)
# print(avarage_temp)
#
# print(data["temp"].mean())
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
#
# def f(x):
#     x = x * 1.8 + 32
#     return float(x)
#
#
# print(data["temp"].apply(f))
#
#
# # creating data frame
#
# data_dict = {
#     "Students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirrel_data["Primary Fur Color"]

all_colors = fur_color.value_counts()
data = pandas.DataFrame(all_colors)
data.to_csv("Fur_Color_Data.csv")
