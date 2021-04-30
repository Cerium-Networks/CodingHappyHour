from pathlib import Path
import csv


def ParseCsv(fileName):
    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)

        data = []
        for line in reader:
            data.append(line)

    return data


def ChallengeOne(data):
    for line in data:
        print(f"{line['Name']:15} | {line['FavoriteLanguage']:>10} | {line['YearsExperience']:>3}")



if __name__ == "__main__":
    fileName = Path("Week-2/Users.csv")
    csvData = ParseCsv(fileName)

    ChallengeOne(csvData)
