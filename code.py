import pandas as pd
import math

def set_level(df):
    for i in range(0, df.shape[0]):
        code = df.loc[i, "code"].strip().replace(" ", "")
        if (code[2] == "1"):
            df.loc[i, "level"] = "100"
        elif (code[2] == "2"):
            df.loc[i, "level"] = "200"
        elif (code[2] == "3"):
            df.loc[i, "level"] = "300"
        elif (code[2] == "4"):
            df.loc[i, "level"] = "400"

# Add additional course codes as required
def set_subjects(df):
    for i in range(0, df.shape[0]):
        sub = df.loc[i, "code"].strip().replace(" ", "")[0:2]
        switcher = {
            "CS": "Computer Science",
            "ST": "Statistics",
            "CH": "Chemistry",
            "MT": "Mathematics",
            "EN": "ENGLISH",
            "GL": "Geology"
        }

        df.loc[i, "subject"] = switcher.get(sub, "Subject X")

def set_grade_points(df):
    for i in range(0, df.shape[0]):
        grade = df.loc[i, "grade"]
        switcher = {
            "A+": 4.0,
            "B+": 3.3,
            "C+": 2.3,
            "D+": 1.3,
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "A-": 3.7,
            "B-": 2.7,
            "C-": 1.7,
            "E": 0
        }
        df.loc[i, "grade_point"] = switcher.get(grade, -1)

def cal_gpa(level, df):
    df_selected = df[df['level'] == level].copy()
    df_selected.reset_index(drop=True, inplace=True)
    credit_grade_product_sum = 0
    total_credits = 0

    for i in range(0, df_selected.shape[0]):
        grade_point = df_selected.loc[i, 'grade_point']

        if grade_point != -1.0:
            credits = df_selected.loc[i, 'credits']
            credit_grade_product_sum = credit_grade_product_sum + (credits * grade_point)
            total_credits = total_credits + credits

    if total_credits == 0:
        return 0  # or return a default value

    return credit_grade_product_sum / total_credits





def cal_final_gpa(df):
    gpa_100L = cal_gpa("100", df)
    gpa_200L = cal_gpa("200", df)
    gpa_300L = cal_gpa("300", df)
    gpa_400L = cal_gpa("400", df)

    gpa = (0.2 * gpa_100L) + (0.2 * gpa_200L) + (0.3 * gpa_300L) + (0.3 * gpa_400L)

    return round(gpa, 3)

# Add courses to be removed into a list (Add course code)
remove_courses = ['coursecode1', 'coursecode2']

# import data
grades = pd.read_csv('grades.csv')
grades = grades.loc[:, ['code', 'course', 'year', 'sem', 'credits', 'grade']]

set_subjects(grades)
set_level(grades)
set_grade_points(grades)

grades_gpa = grades.copy()

for rm_course in remove_courses:
    grades_gpa = grades_gpa.drop(grades_gpa[grades_gpa['code'] == rm_course].index)


# overall gpa
final_gpa = cal_final_gpa(grades_gpa)
total_credits = grades_gpa['credits'].sum()

print(f'GPA: {final_gpa}\nTotal credits: {total_credits}')




# credits per level
credits_100 = grades_gpa[grades_gpa['level'] == "100"]['credits'].sum()
credits_200 = grades_gpa[grades_gpa['level'] == "200"]['credits'].sum()
credits_300 = grades_gpa[grades_gpa['level'] == "300"]['credits'].sum()
credits_400 = grades_gpa[grades_gpa['level'] == "400"]['credits'].sum()

print(f"100L: {credits_100}\n200L: {credits_200}\n300L: {credits_300}\n400L: {credits_400}")

# credits per year
grades_gpa.groupby("year")['credits'].sum()

# credits per subject
grades_gpa.groupby("subject")['credits'].sum()

total_300L_400L = grades_gpa[((grades_gpa['level'] == "400") | (grades_gpa['level'] == "300"))]['credits'].sum()
total_A_300L_400L = grades_gpa[((grades_gpa['level'] == "400") | (grades_gpa['level'] == "300")) & ((grades_gpa['grade'] == "A+") | (grades_gpa['grade'] == "A"))]['credits'].sum()

print(f'Total number of credits in 300L + 400L: {total_300L_400L}')
print(f'Number of credits with A and A+: {total_A_300L_400L}')
if total_300L_400L != 0:
    percentage = (total_A_300L_400L / total_300L_400L) * 100
    print(f'Percentage of A and A+ of all 300L + 400L credits: {round(percentage, 2)} %')
else:
    print("No 300L + 400L credits found.")

