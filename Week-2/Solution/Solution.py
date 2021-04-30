from pathlib import Path
import matplotlib.pyplot as plt
import csv

def ParseCsv(fileName:str):

    with open(fileName) as file:
        reader = csv.DictReader(file)
        data = []
        for line in reader:
            data.append(line)

    return data

def ChallengeOne(data):
    for line in data:
        print(f"{line['Name']:15} | {line['FavoriteLanguage']:>10} | {line['YearsExperience']:3}")

def ChallengeTwo(data):
    total = 0
    for item in data:
        total += int(item['YearsExperience'])
    
    average = total / len(data)
    
    print(f"Average Years Overall: {average:.2f}")


def ChallengeThree(data):
    aggregate = dict()
    for line in data:
        if line['FavoriteLanguage'] not in aggregate:
            aggregate[line['FavoriteLanguage']] = 1
        else:
            aggregate[line['FavoriteLanguage']] += 1
    
    for key, value in aggregate.items():
        print(f"{key:15} | {value}")

def ChallengeFour(data):
    average = sum(int(item['YearsExperience']) for item in data) / len(data)

    for line in data:
        for item in line.values():
            print(f"{item:15} | ", end="")
        print(f" {int(line['YearsExperience']) - average:>5.2f} Years From Average")

def ChallengeFive(data):
    aggregate = dict()
    for line in data:
        if line['FavoriteLanguage'] not in aggregate:
            aggregate[line['FavoriteLanguage']] = 1
        else:
            aggregate[line['FavoriteLanguage']] += 1
    
    keys = list(aggregate.keys())
    values = list(aggregate.values())

    plt.bar(keys, values)
    plt.title("Favorite Programming Languages")
    plt.xlabel("Language")
    plt.ylabel("Number of Favorites")
    plt.show()

if __name__ == "__main__":
    fileName = Path("Week-2/Users.csv")
    data = ParseCsv(fileName)
    
    print()
    print("\nChallenge 1")
    print(100 * "-")
    ChallengeOne(data)
    print("\nChallenge 2")
    print(100 * "-")
    ChallengeTwo(data)
    print("\nChallenge 3")
    print(100 * "-")
    ChallengeThree(data)
    print("\nChallenge 4")
    print(100 * "-")
    ChallengeFour(data)

    ChallengeFive(data)
