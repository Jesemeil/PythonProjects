def displaySummaryTable(scores, numStudents, numSubjects):
    print("=======================================================")
    print(f"%-20s" % "STUDENT", end="")
    for sub in range(numSubjects):
        print(f"%-8s" % ("SUB" + str(sub + 1)), end="")
    print(f"%-8s%-12s%-15s" % ("TOT", "AVE", "POS"))
    print("=======================================================")

    totals = [0] * numStudents

    for i in range(numStudents):
        total = 0
        for j in range(numSubjects):
            total += scores[i][j]
        totals[i] = total

    sortedIndices = sorted(range(numStudents), key=lambda i: totals[i], reverse=True)

    for pos, i in enumerate(sortedIndices):
        studentIndex = i
        average = totals[i] / numSubjects
        print(f"%-20s" % ("Student " + str(studentIndex + 1)), end="")
        for j in range(numSubjects):
            print(f"%-8d" % scores[studentIndex][j], end="")
        print(f"%-8d%-12.2f%-15d" % (totals[studentIndex], average, (pos + 1)))

    print("=======================================================")
    print("=======================================================")



def displaySubjectSummary(scores, numStudents, numSubjects):
    print("\nSUBJECT SUMMARY\n")

    for sub in range(numSubjects):
        highestScore = float("-inf")
        lowestScore = float("inf")
        totalScore = 0
        numPasses = 0
        numFails = 0

        for i in range(numStudents):
            score = scores[i][sub]
            totalScore += score

            if score > highestScore:
                highestScore = score

            if score < lowestScore:
                lowestScore = score

            if score >= 50:
                numPasses += 1
            else:
                numFails += 1

        averageScore = totalScore / numStudents

        print("Subject " + str(sub + 1))
        print("Highest scoring student is: Student " + str(findStudentWithScore(scores, numStudents, numSubjects, sub, highestScore) + 1) + " scoring " + str(highestScore))
        print("Lowest scoring student is: Student " + str(findStudentWithScore(scores, numStudents, numSubjects, sub, lowestScore) + 1) + " scoring " + str(lowestScore))
        print("Total score is: " + str(totalScore))
        print("Average score is: %.2f" % averageScore)
        print("Number of passes: " + str(numPasses))
        print("Number of fails: " + str(numFails))
        print()

    hardestSubject = findHardestSubject(scores, numStudents, numSubjects)
    easiestSubject = findEasiestSubject(scores, numStudents, numSubjects)

    print("The hardest subject is subject " + str(hardestSubject + 1) + " with " + str(countFails(scores, numStudents, numSubjects, hardestSubject)) + " failures")
    print("The easiest subject is subject " + str(easiestSubject + 1) + " with " + str(countPasses(scores, numStudents, numSubjects, easiestSubject)) + " passes.")
    print("=============================================")

def findStudentWithScore(scores, numStudents, numSubjects, subjectIndex, score):
    for i in range(numStudents):
        if scores[i][subjectIndex] == score:
            return i
    return -1

def findHardestSubject(scores, numStudents, numSubjects):
    hardestSubject = -1
    mostFails = -1

    for sub in range(numSubjects):
        numFails = countFails(scores, numStudents, numSubjects, sub)
        if numFails > mostFails:
            hardestSubject = sub
            mostFails = numFails

    return hardestSubject

def findEasiestSubject(scores, numStudents, numSubjects):
    easiestSubject = -1
    mostPasses = -1

    for sub in range(numSubjects):
        numPasses = countPasses(scores, numStudents, numSubjects, sub)
        if numPasses > mostPasses:
            easiestSubject = sub
            mostPasses = numPasses

    return easiestSubject

def findOverallHighest(scores, numStudents, numSubjects):
    highestScore = float("-inf")
    studentIndex = -1
    subjectIndex = -1

    for i in range(numStudents):
        for j in range(numSubjects):
            if scores[i][j] > highestScore:
                highestScore = scores[i][j]
                studentIndex = i
                subjectIndex = j

    print("The overall highest score is scored by Student " + str(studentIndex + 1) +
          " in subject " + str(subjectIndex + 1) + " scoring " + str(highestScore))

def findOverallLowest(scores, numStudents, numSubjects):
    lowestScore = float("inf")
    studentIndex = -1
    subjectIndex = -1

    for i in range(numStudents):
        for j in range(numSubjects):
            if scores[i][j] < lowestScore:
                lowestScore = scores[i][j]
                studentIndex = i
                subjectIndex = j

    print("The overall lowest score is scored by Student " + str(studentIndex + 1) +
          " in subject " + str(subjectIndex + 1) + " scoring " + str(lowestScore))

def countPasses(scores, numStudents, numSubjects, subjectIndex):
    numPasses = 0
    for i in range(numStudents):
        if scores[i][subjectIndex] >= 50:
            numPasses += 1
    return numPasses

def countFails(scores, numStudents, numSubjects, subjectIndex):
    numFails = 0
    for i in range(numStudents):
        if scores[i][subjectIndex] < 50:
            numFails += 1
    return numFails

def displayClassSummary(scores, numStudents, numSubjects):
    print("\nCLASS SUMMARY")
    bestStudentIndex = findBestStudent(scores, numStudents, numSubjects)
    worstStudentIndex = findWorstStudent(scores, numStudents, numSubjects)

    print("=========================================")
    print("Best Graduating Student is: Student " + str(bestStudentIndex + 1) + " scoring " + str(calculateTotal(scores[bestStudentIndex])))
    print("=========================================")

    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Worst Graduating Student is: Student " + str(worstStudentIndex + 1) + " scoring " + str(calculateTotal(scores[worstStudentIndex])) + " ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    classTotal = calculateClassTotal(scores, numStudents, numSubjects)
    classAverage = classTotal / (numStudents * numSubjects)

    print("\n=========================================")
    print("Class total score is: " + str(classTotal))
    print("Class Average score is: " + str(classAverage))
    print("=========================================")

def findBestStudent(scores, numStudents, numSubjects):
    bestStudentIndex = 0
    highestTotal = calculateTotal(scores[0])

    for i in range(1, numStudents):
        total = calculateTotal(scores[i])
        if total > highestTotal:
            bestStudentIndex = i
            highestTotal = total

    return bestStudentIndex

def findWorstStudent(scores, numStudents, numSubjects):
    worstStudentIndex = 0
    lowestTotal = calculateTotal(scores[0])

    for i in range(1, numStudents):
        total = calculateTotal(scores[i])
        if total < lowestTotal:
            worstStudentIndex = i
            lowestTotal = total

    return worstStudentIndex

def calculateTotal(scores):
    total = 0
    for score in scores:
        total += score
    return total

def calculateClassTotal(scores, numStudents, numSubjects):
    classTotal = 0
    for i in range(numStudents):
        classTotal += calculateTotal(scores[i])
    return classTotal

def main():
    numStudents = int(input("How many students do you have? "))
    numSubjects = int(input("How many subjects do you have? "))

    scores = [[0] * numSubjects for _ in range(numStudents)]

    for index in range(numStudents):
        print("\nEntering score for student " + str(index + 1) + ": ")
        for index1 in range(numSubjects):
            score = int(input("Enter score for subject " + str(index1 + 1) + ": "))
            while score < 0 or score > 100:
                print("Score must be between 0 and 100. Re-enter score: ")
                score = int(input())
            scores[index][index1] = score
            print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("Saved successfully.\n")

    displaySummaryTable(scores, numStudents, numSubjects)
    displaySubjectSummary(scores, numStudents, numSubjects)
    displayClassSummary(scores, numStudents, numSubjects)
    findOverallHighest(scores, numStudents, numSubjects)
    findOverallLowest(scores, numStudents, numSubjects)

if __name__ == "__main__":
    main()
