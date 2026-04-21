import pygame
import aquila_graphics
from buzzer import Buzzer
from globals import *
from aquila_utils import *

pygame.init()

# ---------- Loading Fonts ---------- #
fontDict = {
    'button' : pygame.font.SysFont(FONT_TYPEFACE, FONT_SIZE_BUTTON),
    'hint'   : pygame.font.SysFont(FONT_TYPEFACE, FONT_SIZE_HINT),
    'status' : pygame.font.SysFont(FONT_TYPEFACE, FONT_SIZE_STATUS),
    'statLabel' : pygame.font.SysFont(FONT_TYPEFACE, FONT_SIZE_STATISTICS),
    'qaLabel' : pygame.font.SysFont(FONT_TYPEFACE, FONT_SIZE_QALABEL),
    'body' : pygame.font.SysFont(FONT_TYPEFACE, FONT_SIZE_ANSWER),
    'timer' : pygame.font.SysFont(TIMER_TYPEFACE, FONT_SIZE_TIMER),
    'logo1' : pygame.font.SysFont(LOGO_TYPEFACE, FONT_LOGO_SIZE)
}

# ---------- App Object ----------- #

app = aquila_graphics.App(lilLoad(MINI_CON), PROGRAM_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)

# ---------- All Text Boxes ---------- #

textBoxGroup = pygame.sprite.Group()


statsBox = aquila_graphics.TextBox(STATSCREEN_X, STATSCREEN_Y, STATSCREEN_WIDTH, STATSCREEN_HEIGHT,
                                   lilLoad(STATSCREEN_SPRITE), "", fontDict['body'],
                                   label = "STATISTICS", labelFont = fontDict['statLabel'], labelHeight = STATSCREEN_LABEL_HEIGHT,
                                   mode = 'formatted')

questionBox = aquila_graphics.TextBox(QSCREEN_X, QSCREEN_Y, QABODY_WIDTH, QABODY_HEIGHT,
                                   lilLoad(QASCREEN_SPRITE), "", fontDict['body'],
                                   label = "Question", labelFont = fontDict['qaLabel'], labelHeight = QALABEL_HEIGHT,
                                   mode = 'autowrap')
questionBox.setLabelWidth(QALABEL_WIDTH)

answerBox = aquila_graphics.TextBox(ASCREEN_X, ASCREEN_Y, QABODY_WIDTH, QABODY_HEIGHT,
                                   lilLoad(QASCREEN_SPRITE), "", fontDict['body'],
                                   label = "Answer", labelFont = fontDict['qaLabel'], labelHeight = QALABEL_HEIGHT,
                                   mode = 'autowrap')
answerBox.setLabelWidth(QALABEL_WIDTH)

textBoxGroup.add(statsBox, questionBox, answerBox)
for item in textBoxGroup:
    app.group.add(item)

# ---------- All Buttons ---------- #

buttonsGroup = pygame.sprite.Group()

askQuestionButton = aquila_graphics.Button(BUTTON1_X, BUTTON1_Y, BUTTON1_WIDTH, BUTTON1_HEIGHT,
                           (lilLoad(BUTTON1_IDLE), lilLoad(BUTTON1_HOVER), lilLoad(BUTTON1_ACTIVE)), label =  "ASK QUESTION", font = fontDict['button'])

resetButton = aquila_graphics.Button(BUTTON2_X, BUTTON2_Y, BUTTON2_WIDTH, BUTTON2_HEIGHT,
                           (lilLoad(BUTTON1_IDLE), lilLoad(BUTTON1_HOVER), lilLoad(BUTTON1_ACTIVE)), label = "RESET", font = fontDict['button'])

questionToggle = aquila_graphics.Button(QBUTTON_X, QBUTTON_Y, QABUTTON_WIDTH, QABUTTON_HEIGHT, 
                                        (lilLoad(BUTTON2_IDLE), lilLoad(BUTTON2_HOVER), lilLoad(BUTTON2_ACTIVE)), label = "Show", font = fontDict['button'])

answerToggle = aquila_graphics.Button(ABUTTON_X, ABUTTON_Y, QABUTTON_WIDTH, QABUTTON_HEIGHT, 
                                        (lilLoad(BUTTON2_IDLE), lilLoad(BUTTON2_HOVER), lilLoad(BUTTON2_ACTIVE)), label = "Show", font = fontDict['button'])

correctButton = aquila_graphics.Button(RWBUTTON1_X, RWBUTTON1_Y, RWBUTTON1_WIDTH, RWBUTTON1_HEIGHT,
                           (lilLoad(CORRECT_IDLE), lilLoad(CORRECT_IDLE), lilLoad(CORRECT_ACTIVE)))

reviewButton = aquila_graphics.Button(RWBUTTON2_X, RWBUTTON2_Y, RWBUTTON1_WIDTH, RWBUTTON2_HEIGHT,
                           (lilLoad(REVIEW_IDLE), lilLoad(REVIEW_IDLE), lilLoad(REVIEW_ACTIVE)))

incorrectButton = aquila_graphics.Button(RWBUTTON3_X, RWBUTTON3_Y, RWBUTTON3_WIDTH, RWBUTTON3_HEIGHT,
                           (lilLoad(INCORRECT_IDLE), lilLoad(INCORRECT_IDLE), lilLoad(INCORRECT_ACTIVE)))

# optionsButton = 

# printoutButton =

buttonsGroup.add(askQuestionButton, resetButton, questionToggle, answerToggle, correctButton, reviewButton, incorrectButton)
for item in buttonsGroup:
    app.group.add(item)

# ---------- All Indicator Lights ---------- #

lightsGroup = pygame.sprite.Group()

statusLight = aquila_graphics.Light(LIGHT1_X, LIGHT1_Y, LIGHT1_WIDTH, LIGHT1_HEIGHT, 
                                     (lilLoad(GREEN_LIGHT_OFF), lilLoad(GREEN_LIGHT_ON)))

buzzLight = aquila_graphics.Light(LIGHT2_X, LIGHT2_Y, LIGHT2_WIDTH, LIGHT2_HEIGHT, 
                                     (lilLoad(GREEN_LIGHT_OFF), lilLoad(GREEN_LIGHT_ON)))

timeoutLight = aquila_graphics.Light(LIGHT3_X, LIGHT3_Y, LIGHT3_WIDTH, LIGHT3_HEIGHT, 
                                     (lilLoad(RED_LIGHT_OFF), lilLoad(RED_LIGHT_ON)))

# bonusButton = 

lightsGroup.add(statusLight, buzzLight, timeoutLight)
for item in lightsGroup:
    app.group.add(item)

# ---------- Misc ---------- #

logo = aquila_graphics.Graphic(LOGO_X, LOGO_Y, LOGO_WIDTH, LOGO_HEIGHT, lilLoad(LOGO_SPRITE))
app.group.add(logo)

inBuzzer = Buzzer(BUZZ_FREQ, BUZZ_TIME, BUZZ_VOL)
timeoutBuzzer = Buzzer(TIMEOUT_TONE, BUZZ_TIME, BUZZ_VOL)

timer = aquila_graphics.Timer(TIMER_X, TIMER_Y, TIMER_WIDTH, TIMER_HEIGHT, 30.0, fontDict['timer'], (255, 255, 255))
app.group.add(timer)

questionData = {season.getName() : season for season in QUESTION_DATA}