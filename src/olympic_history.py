import pandas as pd
import src.player_analysis as player_analysis

PATH = "../data/athlete_events.csv"
data = pd.read_csv(PATH)


# 2) percentage of male gymnasts among all the male participants of the 2000 Olympics
def get_male_gymnasts():
    male_participants = data[(data["Year"] == 2000) & (data["Sex"] == "M")]
    male_participants_count = male_participants.Name.unique().shape
    male_gymnasts = male_participants[male_participants["Sport"] == "Gymnastics"]
    male_gymnasts_count = male_gymnasts.Name.unique().shape
    print("Male Participants: " + str(male_participants_count))
    print("Male Gymnasts: " + str(male_gymnasts_count))


# 3) What are the mean and standard deviation of height for female basketball players participated in the 2000
# Olympics? Round the answer to the first decimal.
def get_girls_data():
    df = (data[(data["Sex"] == "F") & (data["Year"] == 2000) & (data["Sport"] == "Basketball")])["Height"]
    print("Mean: " + str(df.mean().round(1)))
    print("Standard Deviation: " + str(df.std().round(1)))


# 4) Find a sportsperson participated in the 2002 Olympics, with the highest weight among other participants of the
# same Olympics. What sport did he or she do?
def highest_weight_person():
    weight_value = (data[data["Year"] == 2002])["Weight"].max()
    print(data[(data["Year"] == 2002) & (data["Weight"] == weight_value)])


# 5) How many times did Pawe Abratkiewicz participate in the Olympics held in different years?
def get_pawe_participation():
    df = (data[data["Name"] == "Pawe Abratkiewicz"]).groupby(["Year"]).mean()
    print("No. of times: " + str(len(df.index)))


# 6) How many silver medals in tennis did Australia win at the 2000 Olympics?
def silver_medal_australia():
    df = data[
        (data["Medal"] == "Silver") & (data["Year"] == 2000) & (data["NOC"] == "AUS") & (data["Sport"] == "Tennis")]
    print("Silver Medals: " + str(len(df.index)))


# 7) Is it true that Switzerland won fewer medals than Serbia at the 2016 Olympics? Do not consider NaN values in
# Medal column.
def fewer_medals():
    olympics_2016 = data[data["Year"] == 2016]
    switzerland = olympics_2016[olympics_2016["Team"] == "Switzerland"]
    serbia = olympics_2016[olympics_2016["Team"] == "Serbia"]
    print("Switzerland: " + str(len(switzerland.dropna().index)))
    print("Serbia: " + str(len(serbia.dropna().index)))


# 8) What age category did the fewest and the most participants of the 2014 Olympics belong to?
def get_range():
    olympics_2014 = data[(data['Year'] == 2014)]
    olympics_2014 = olympics_2014[['Name', 'Age']].drop_duplicates()
    # print(len(olympics_2014))
    bins = pd.cut(olympics_2014['Age'], [14, 24, 34, 44, 55])
    print(olympics_2014.groupby(bins)['Age'].agg('count'))


# 9) Is it true that there were Summer Olympics held in Lake Placid? Is it true that there were Winter Olympics held
# in Sankt Moritz?
def get_city_season():
    lake_placid_records = data[(data["Season"] == "Summer") & (data["City"] == "Lake Placid")]
    sankt_moritz_records = data[(data["Season"] == "Winter") & (data["City"] == "Sankt Moritz")]
    print("Held in Lake Placid: " + str(not lake_placid_records.empty))
    print("Held in Sankt Moritz: " + str(not sankt_moritz_records.empty))


# 10) What is the absolute difference between the number of unique sports at the 1995 Olympics and 2016 Olympics?
def get_difference():
    sports_1995 = data[data["Year"] == 1995]
    sports_2016 = data[data["Year"] == 2016]
    count_1995 = sports_1995.Sport.unique().shape
    count_2016 = sports_2016.Sport.unique().shape
    print("In 1995: " + str(count_1995))
    print("In 2016: " + str(count_2016))


if __name__ == '__main__':
    player_analysis.most_medals(data)
    # get_male_gymnasts()
    # get_girls_data()
    # highest_weight_person()
    # get_pawe_participation()
    # silver_medal_australia()
    # fewer_medals()
    # get_range()
    # get_city_season()
    # get_difference()