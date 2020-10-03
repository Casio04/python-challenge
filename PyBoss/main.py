
import os
import csv
import datetime
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
def left(s, string):
    return s[:string]

employee_file = os.path.join("Resources", "employee_data.csv")
id_employee = []
first_name = []
last_name = []
new_date = []
new_SSN = []
new_state = []

with open(employee_file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        id_employee.append(row[0])
        name_list = row[1].split(" ",1)
        first_name.append(name_list[0])
        last_name.append(name_list[1])
        dt = datetime.datetime.strptime(str(row[2]),"%Y-%m-%d").strftime("%m/%d/%Y")
        new_date.append(dt)
        SSN = row[3].replace(row[3][0:6], "***-**")
        new_SSN.append(SSN)
        new_state.append(us_state_abbrev[row[4]])

    
new_csv = zip(id_employee,first_name, last_name, new_date, new_SSN, new_state)
output_file = os.path.join("Resources","employee_transformed.csv")

with open(output_file, "w", newline = "") as writefile:
    csvwriter = csv.writer(writefile)
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    csvwriter.writerows(new_csv)

