
from station1 import solution_station_1
from station_2 import solution_station_2
from station3 import solution_station_3
from station4 import solution_station_4
from station5 import get_learning_team
from station6 import solution_station_6
from station7 import solution_station_7

print('imports done')

# List three observations of all inputs (not sample inputs) observed at the same time
# Format: (time: str, station1_input: int, station2_input: str, station3_input: int, station4_input: int, station5_input: str, station6_input: int, station7_input: str)
# Example: ('12:30:00', 1, '1990-01-01', 2, 3, "John", 4, "e=mc^2")
observation1 = ("50:30", 47, "2024-05-01", 20660, 2066, "Brendan", 20, "b*e+a*d")
observation2 = ("53:00", 51, "2024-03-16", 28700, 2870, "Felicia", 28, "e+c*b")
observation3 = ("54:20", 97, "2024-02-27", 63443, 6344, "Lucas", 63, "d+b*a")

def combined_algorithm(observations: tuple) -> int:
    output1 = solution_station_1(observations[1])
    print("output1")
    output2 = solution_station_2(observations[2])
    print("output2")
    output3 = solution_station_3(observations[3])
    print("output3")
    output4 = solution_station_4(observations[4])
    print("output4")
    output5 = get_learning_team(observations[5])
    print("output5")
    output6 = solution_station_6(observations[6])
    print("output6")
    output7 = solution_station_7(observations[7])
    print("output7")
    assert isinstance(output1, int)
    assert isinstance(output2, str)
    assert isinstance(output3, bool)
    assert isinstance(output4, bool)
    assert isinstance(output5, int)
    assert isinstance(output6, float)
    assert isinstance(output7, float)
    return output1 * int.from_bytes(output2[0].encode("unicode_escape"), byteorder='big') * (3 if output3 else 2) * (5 if output4 else 4) * output5 * output6 * output7

FINAL_OUTPUT1 = combined_algorithm(observation1)
FINAL_OUTPUT2 = combined_algorithm(observation2)
FINAL_OUTPUT3 = combined_algorithm(observation3)
print(f"Final Output 1: {FINAL_OUTPUT1}")
print(f"Final Output 2: {FINAL_OUTPUT2}")
print(f"Final Output 3: {FINAL_OUTPUT3}")
#tests.Test_Exercise(combined_algorithm)