import pygame
import os
import sys
from fromPyCompiler import Question

def lilLoad(relative_path: str) -> pygame.Surface:
    """Does pygame.image.load but smaller and also
       returns correct path for dev and PyInstaller builds."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    path =  os.path.join(base_path, relative_path)
    return pygame.image.load(path)

def timeout(timer : float) -> bool:
    return (timer == 0.0)

class StatisticsTracker:

    def __init__(self):
        self.questionsAsked = 0
        self.correctQs = []
        self.reviewQs = []
        self.incorrectQs = []
        self.allQs = []
        self.buzzSpeeds = []
        self.buzzSpeedsOnCorrect = []
    
    def logQuestion(self, correctness : str, question : Question, buzzSpeed : float):
        if question not in self.allQs:
            self.allQs.append(question)
            self.questionsAsked += 1
            self.buzzSpeeds.append(buzzSpeed)
            if correctness == "CORRECT":
                self.correctQs.append(question)
                self.buzzSpeedsOnCorrect.append(buzzSpeed)
            elif correctness == "REVIEW":
                self.reviewQs.append(question)
            elif correctness == "INCORRECT":
                self.incorrectQs.append(question)
    
    def getAverageBuzzSpeed(self) -> float:
        try:
            return sum(self.buzzSpeeds)/len(self.buzzSpeeds)
        except (ZeroDivisionError):
            return 0.0
    
    def getAverageBuzzSpeedOnCorrect(self) -> float:
        try:
            return sum(self.buzzSpeedsOnCorrect)/len(self.buzzSpeedsOnCorrect)
        except (ZeroDivisionError):
            return 0.0
    
    def generateStatText(self) -> str:
        outString = f"""
Questions Logged: 
{self.questionsAsked}
Right/Wrong/Review: 
{len(self.correctQs)}/{len(self.incorrectQs)}/{len(self.reviewQs)}
Average Time to Buzz: 
{round(self.getAverageBuzzSpeed(), 2)} seconds
Average Time to Correct Buzz: 
{round(self.getAverageBuzzSpeedOnCorrect(), 2)} seconds
"""
        return outString
        
class Stopwatch:

    def __init__(self):
            self.time = 0
            self.paused = False
    
    def tick(self, dt : float) -> None:
        if not self.paused:
            self.time += dt
    
    def getTime(self) -> float:
        return self.time
    
    def pause(self) -> None:
        self.paused = True
    
    def unpause(self) -> None:
        self.paused = False
    
    def reset(self) -> None:
        self.time = 0