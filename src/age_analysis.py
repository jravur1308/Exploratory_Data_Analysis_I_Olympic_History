from src.olympic_history import data


# 1) youngest male and female participants of the 1996 Olympics
def get_min_age():
    df = data[data["Year"] == 1996]
    male_df = (df[df["Sex"] == "M"])["Age"]
    female_df = (df[df["Sex"] == "F"])["Age"]
    male_age = male_df.min()
    female_age = female_df.min()
    print("Male: " + str(male_age))
    print("Female: " + str(female_age))
