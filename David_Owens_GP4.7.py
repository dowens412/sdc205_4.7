print("davowe9952")

import pandas as pd
import matplotlib.pyplot as plt

# create arrays for student names and subjects
students = [['John', 'John', 'Mary', 'Mary', 'David', 'David', 'Sarah', 'Sarah', 'Chris', 'Chris',
             'Emma', 'Emma', 'Michael', 'Michael', 'Ashley', 'Ashley', 'Daniel', 'Daniel', 'Sophia', 'Sophia'],
            ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science',
             'Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science']]

# create a multiindex using student and subject
index = pd.MultiIndex.from_arrays(students, names=('Student', 'Subject'))

# create a dataframe with grades for each student and subject
df = pd.DataFrame({'Grade': [90, 85, 88, 92, 95, 89, 84, 90, 91, 86,
                             87, 93, 94, 88, 89, 91, 92, 84, 90, 87]}, index=index)

# group the data by subject and find the mean grade
averageGrade = df.groupby(by=["Subject"]).mean()

print(averageGrade)

# create a vertical bar graph from the grouped data
averageGrade['Grade'].plot(kind='bar')

plt.xlabel("Average Grade by Subject")
plt.title("Average Grade by Subject")
plt.xticks(rotation=0)

plt.show()