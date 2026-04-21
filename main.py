import pygame
import pyttsx3
import random
import threading
from model import *
from aquila_utils import *

# ── Text-to-Speech helpers ─────────────────────────────────────────────────────

# A fresh engine is created for every speak call so that calling stop() on one
# session does not leave the engine in a broken state for future sessions.
class SpeechState:
    thread: threading.Thread | None = None
    engine: pyttsx3.Engine | None = None

speech = SpeechState()

def _speak_worker(text: str) -> None:
    """Run in a background thread with its own fresh TTS engine instance."""
    speech.engine = pyttsx3.init()
    word_rate = ((random.randint(120, 160) + random.randint(120, 160) + random.randint(120, 160)) // 3)
    speech.engine.setProperty('rate', word_rate)
    speech.engine.say(text)
    speech.engine.runAndWait()
    speech.engine = None  # Mark engine as inactive once finished naturally


def start_speaking(text: str) -> None:
    """Stop any ongoing speech, then start reading *text* in a background thread."""
    stop_speaking()
    speech.thread = threading.Thread(target=_speak_worker, args=(text,), daemon=True)
    speech.thread.start()


def stop_speaking() -> None:
    """Interrupt the active TTS engine and wait for the worker thread to finish."""
    if speech.engine is not None:
        speech.engine.stop()
    if speech.thread and speech.thread.is_alive():
        speech.thread.join(timeout=1.0)
    speech.thread = None
    speech.engine = None


def is_speaking() -> bool:
    return speech.thread is not None and speech.thread.is_alive()

# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:

    # On App Start
    pygame.init()
    screen = pygame.display.set_mode((app.width, app.height))
    pygame.display.set_caption(app.name)
    pygame.display.set_icon(app.icon)
    
    clock = pygame.time.Clock()
    buzzSW = Stopwatch()
    prevTime = 0.0
    dt = clock.get_time()

    mouseIsDown = False

    statTrack = StatisticsTracker()
    qCount = 0
    askingQuestion = False
    question = None

    season = 'season_26'


    for light in lightsGroup:
        light.turnOff()

    bag = [1, 2, 3, 4, 5, 6, 7, 8]

    running = True
    while running: # On Step
        mousePos = pygame.mouse.get_pos()
        
        dt = (clock.get_time() - prevTime) / 1000

        buzzSW.tick(dt)

        if not timer.paused:
            if (timer.getTime() > 0):
                timer.tick(dt)
            else:
                timeoutBuzzer.play_buzz()
                timer.reset()
                timer.pause()
                timeoutLight.turnOn()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT: # On App Quit
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # On Mouse Down
                mouseIsDown = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #On Mouse Up
                
                if askQuestionButton.isPressed and askQuestionButton.rect.collidepoint(mousePos): #On Read
                    
                    # reset view
                    questionBox.hideText()
                    answerBox.hideText()
                    buzzLight.turnOff()
                    statusLight.turnOn()
                    
                    # Prep timers
                    timer.reset()
                    buzzSW.reset()
                    buzzSW.unpause()

                    # Pick and read a random question
                    random.shuffle(bag)
                    weekIndex = bag.pop()
                    if len(bag) == 0:
                        bag = [1, 2, 3, 4, 5, 6, 7, 8]
                    week_questions = questionData[season].getWeekData(weekIndex)
                    question = week_questions.getRandomQuestion()
                    qCount += 1
                    questionBox.setText(question.getQuestion())
                    answerBox.setText(question.getAnswer())
                    full_question_phrase = "Question number " + str(qCount) + ". Question. " + question.getQuestion()
                    start_speaking(full_question_phrase)

                    # indicate status
                    askingQuestion = True

                if resetButton.isPressed and resetButton.rect.collidepoint(mousePos):
                    for light in lightsGroup:
                        light.turnOff()
                    questionBox.hideText()
                    answerBox.hideText()
                    timer.reset()
                    timer.pause()
                    buzzSW.pause()
                    askingQuestion = False

                if questionToggle.isPressed and questionToggle.rect.collidepoint(mousePos):
                    if questionBox.showingText:
                        questionBox.hideText()
                    else:
                        questionBox.showText()

                if answerToggle.isPressed and answerToggle.rect.collidepoint(mousePos):
                    if answerBox.showingText:
                        answerBox.hideText()
                    else:
                        answerBox.showText()

                if correctButton.isPressed and correctButton.rect.collidepoint(mousePos):
                    if not askingQuestion:
                        statTrack.logQuestion("CORRECT", question, buzzSW.getTime())

                if reviewButton.isPressed and reviewButton.rect.collidepoint(mousePos):
                    if not askingQuestion:
                        statTrack.logQuestion("REVIEW", question, buzzSW.getTime())

                if incorrectButton.isPressed and incorrectButton.rect.collidepoint(mousePos):
                    if not askingQuestion:
                        statTrack.logQuestion("INCORRECT", question, buzzSW.getTime())

                mouseIsDown = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                if timer.paused and not buzzLight.status: # on Buzz

                    timer.unpause()
                    buzzSW.pause()

                    buzzLight.turnOn()
                    stop_speaking()
                    statusLight.turnOff()
                    inBuzzer.play_buzz()
                    askingQuestion = False
        
        for button in buttonsGroup:
            button.update(mousePos, mouseIsDown)

        # Redraw All
        screen.fill(app.background)
        
        ### Drawing Body

        statsBox.setText(statTrack.generateStatText())

        for item in app.group:
            item.draw(screen)

        ###

        clock.get_time()
        pygame.display.flip()
        clock.tick(app.fps)

    stop_speaking()
    pygame.quit()

if __name__ == "__main__":
    main()