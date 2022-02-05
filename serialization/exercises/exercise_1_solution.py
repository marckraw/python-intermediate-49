with open(filepath) as file:
    reader = csv.reader(file)

    next(reader)

    counter = 0
    salary_sum = 0
    for row in reader:
        salary_sum += int(row[index])
        counter += 1

return salary_sum / counter