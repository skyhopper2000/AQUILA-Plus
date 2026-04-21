
import os
import importlib.util
import random

class Question:

    def __init__(self, question : str, answer : str, weekNum : int, location : str):
        """
        Basic type for question storage

        :param question: the string of the question
        :param weekData: the string of the corresponding answer
        :param weekNum: the integer value of the week being added
        :param weekData: the scripture reference, format
        """
        self.question = question
        self.answer = answer
        self.weekNum = weekNum
        self.location = location
    
    def getQuestion(self) -> str:
        return self.question

    def getAnswer(self) -> str:
        return self.answer
    
    def getWeek(self) -> int:
        return self.week
    
    def getLocation(self) -> str:
        return self.location
    
    def getQuestionLike(self) -> tuple[str, str, int, str]:
        """
        Returns a tuple form of the question object.
        Format: (question, answer, week, location)
        """
        return (self.question, self.answer, self.week, self.location)

class weekQuestions:
    def __init__(self, weekNum : int, weekData):
        """
        Compile a week's set of questions

        :param weekNum: the integer value of the week being added
        :param weekData: the list of question-answer tuples in for that week
        """
        self.weekNum = weekNum
        self.weekData = weekData
        self.questionData = []
        for qaTuple in self.weekData:
            question = qaTuple[0]
            answer = qaTuple[1]
            location = answer[answer.rfind("(") : answer.rfind(")")]
            questionItem = Question(question, answer, weekNum, location)
            self.questionData.append(questionItem)

    def getNum(self) -> int:
        "Returns the week's number"
        return self.weekNum
    
    def getData(self):
        "Returns the list of question-answer tuples"
        return self.weekData
    
    def getRandomQuestion(self) -> Question:
        "returns a true random question-answer tuple from the week's material"
        return self.questionData[random.randint(0, len(self.weekData) - 1)]


class seasonQuestions:
    def __init__(self, allWeeks, name = ""):
        self.name = name

        self.weeksData = allWeeks
        

    def setName(self, name : str) -> None:
        """
        Sets the name of the season.
        Preferred format, 'season' + last two digits of year.
        (i.e. 'season26')
        """
        self.name = name
    
    def getName(self) -> str:
        "Return the name of the season"
        return self.name

    def getAllWeekData(self) -> list[weekQuestions]:
        "Returns the list of weekQuestions objects"
        return self.weeksData
    
    def getWeekData(self, weekNum : int) -> weekQuestions:
        "Returns a particular weekQuestions object"
        for week in self.weeksData:
            if week.getNum() == weekNum:
                return week
        print("Week not Found, " + str(weekNum))
        return self.weeksData[0]

def collectVariables(folder, variable_name):
    allSeasons = []
    for secondaryFolder in sorted(os.listdir(folder)):
        secondaryFolderPath = os.path.join(folder, secondaryFolder)
        allWeeks = []
        for filename in sorted(os.listdir(secondaryFolderPath)):
            if filename.endswith(".py") and not filename.startswith("__"):
                path = os.path.join(secondaryFolderPath, filename)
                spec = importlib.util.spec_from_file_location(filename[:-3], path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, variable_name):
                    subQuestions = getattr(module, variable_name)
                    weekNumber = int(filename[4:filename.rfind(".")])
                    allWeeks.append(weekQuestions(weekNumber, subQuestions))
        seasonData = seasonQuestions(allWeeks, secondaryFolder)
        allSeasons.append(seasonData)
                        
    return allSeasons
