def calc_average(scores):
    average = sum(scores) / len(scores)
    return average

def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

def main():
    scores = []
    for i in range(5):
        score = float(input(f"Enter test score {i + 1}: "))
        scores.append(score)
 
    for i, score in enumerate(scores):
        grade = determine_grade(score)
        print(f"Test score {i + 1}: {score} - Grade: {grade}")

    average_score = calc_average(scores)
    print(f"Average test score: {average_score:.2f}")

if __name__ == "__main__":
    main()