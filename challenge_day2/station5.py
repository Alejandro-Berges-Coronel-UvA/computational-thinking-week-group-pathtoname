import csv

def solution_station_5(students):
    learning_teams = {}
    with open('/path/to/learning_team.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            student = row[0]
            team = int(row[1])
            learning_teams[student] = team
    
    team_mapping = {}
    for student in students:
        if student in learning_teams:
            team_mapping[student] = learning_teams[student]
        else:
            team_mapping[student] = None
    
    return team_mapping