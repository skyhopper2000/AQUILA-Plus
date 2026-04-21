import fromPyCompiler

# ── Configuration ──────────────────────────────────────────────────────────────
PROGRAM_NAME = "Aquila MK. 2"
MINI_CON = "assets\images\minicon.png"

QUESTION_DATA = fromPyCompiler.collectVariables("question_data", "QUESTIONS")

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
FPS           = 30

# Colors
COLOR_BACKGROUND    = (0, 0, 0)
COLOR_BUTTON_IDLE   = (70,  130, 70)
COLOR_BUTTON_HOVER  = (70, 160, 70)
COLOR_BUTTON_ACTIVE = (0,  90,  0)
COLOR_TEXT_BUTTON   = (0, 0, 0)
COLOR_TEXT          = (255, 255, 255)
COLOR_HINT          = (180, 180, 180)
COLOR_STATUS_IDLE   = (150, 150, 150)
COLOR_STATUS_SPEAK  = (100, 220, 120)

# Sprites
BUTTON1_IDLE = "assets\images\_button1_1.png"
BUTTON1_HOVER = "assets\images\_button1_1.png"
BUTTON1_ACTIVE = "assets\images\_button1_0.png"

BUTTON2_IDLE = "assets\images\_button2_1.png"
BUTTON2_HOVER = "assets\images\_button2_0.png"
BUTTON2_ACTIVE = "assets\images\_button2_2.png"

RIGHT_BUTTON_UP = "assets\images\_rightwrong_0.png"
RIGHT_BUTTON_DOWN = "assets\images\_rightwrong_1.png"
WRONG_BUTTON_UP = "assets\images\_rightwrong_1.png"
WRONG_BUTTON_DOWN = "assets\images\_rightwrong_3.png"
REVIEW_BUTTON_UP = "assets\images\_rightwrong_4.png"
REVIEW_BUTTON_UP = "assets\images\_rightwrong_5.png"

GREEN_LIGHT_OFF = "assets\images\_lights_0.png"
GREEN_LIGHT_ON = "assets\images\_lights_1.png"
RED_LIGHT_OFF = "assets\images\_lights_2.png"
RED_LIGHT_ON = "assets\images\_lights_3.png"

TSCREEN_SPRITE = "assets\images\_answerScreen.png"
QASCREEN_SPRITE = "assets\images\questionanswerBox.png"
STATSCREEN_SPRITE = "assets\images\_statsCol.png"

LOGO_SPRITE = "assets\images\AQUILA logo.png"

CORRECT_IDLE = "assets\images\_rightwrong_0.png"
CORRECT_ACTIVE = "assets\images\_rightwrong_1.png"

INCORRECT_IDLE = "assets\images\_rightwrong_2.png"
INCORRECT_ACTIVE = "assets\images\_rightwrong_3.png"

REVIEW_IDLE = "assets\images\_rightwrong_4.png"
REVIEW_ACTIVE = "assets\images\_rightwrong_5.png"

# Stats Screen
STATSCREEN_WIDTH = 300
STATSCREEN_HEIGHT = 450
STATSCREEN_X = WINDOW_WIDTH-STATSCREEN_WIDTH
STATSCREEN_Y = 0
STATSCREEN_BODY_Y = STATSCREEN_Y + 75
STATSCREEN_BODY_HEIGHT = 375
STATSCREEN_LABEL_HEIGHT = 75

# centering
CONTROL_CENTER_X = (WINDOW_WIDTH - STATSCREEN_WIDTH) // 2
BUFFER = 25

# Logo
LOGO_WIDTH = 250
LOGO_HEIGHT = 66
LOGO_X = CONTROL_CENTER_X - (LOGO_WIDTH // 2)
LOGO_Y = 10

# Timer
TIMER_WIDTH = 200
TIMER_HEIGHT = 75
TIMER_X = CONTROL_CENTER_X - (TIMER_WIDTH // 2)
TIMER_Y = LOGO_Y + LOGO_HEIGHT + BUFFER

# Button 1
BUTTON1_WIDTH  = 175 
BUTTON1_HEIGHT = 50
BUTTON1_RADIUS = 0
BUTTON1_X = CONTROL_CENTER_X - BUFFER - BUTTON1_WIDTH 
BUTTON1_Y = 300

# Button 2
BUTTON2_WIDTH  = 175
BUTTON2_HEIGHT = 50
BUTTON2_RADIUS = 0
BUTTON2_X = CONTROL_CENTER_X + BUFFER 
BUTTON2_Y = 300



# 'Review' Button
RWBUTTON2_WIDTH = 50
RWBUTTON2_HEIGHT = 50
RWBUTTON2_X = CONTROL_CENTER_X - (RWBUTTON2_WIDTH // 2)
RWBUTTON2_Y = 375

# 'Correct' Button
RWBUTTON1_WIDTH = 50
RWBUTTON1_HEIGHT = 50
RWBUTTON1_X = RWBUTTON2_X - BUFFER - RWBUTTON1_WIDTH
RWBUTTON1_Y = 375

# 'Incorrect' Button
RWBUTTON3_WIDTH = 50
RWBUTTON3_HEIGHT = 50
RWBUTTON3_X = CONTROL_CENTER_X + BUFFER + (RWBUTTON2_WIDTH// 2)
RWBUTTON3_Y = 375


# Answer Screen
ASCREEN_X = 400
ASCREEN_Y = 450
ABODY_Y = ASCREEN_Y + 50

# Question Screen
QSCREEN_X = 0
QSCREEN_Y = 450
QBODY_Y = QSCREEN_Y + 50

# QA Shared Stats
QASCREEN_WIDTH = 400
QASCREEN_HEIGHT = 150
QABODY_WIDTH = 400
QABODY_HEIGHT = 100
QALABEL_WIDTH = 150
QALABEL_HEIGHT = 50

# QA Button Shared Stats
QABUTTON_WIDTH = 125
QABUTTON_HEIGHT = 50

# Answer Button
ABUTTON_X = ASCREEN_X + QABODY_WIDTH - QABUTTON_WIDTH
ABUTTON_Y = ASCREEN_Y

# Question Button
QBUTTON_X = QSCREEN_X + QABODY_WIDTH - QABUTTON_WIDTH
QBUTTON_Y = QSCREEN_Y



# Timer Screen
TSCREEN_WIDTH = 200
TSCREEN_HEIGHT = 100
TSCREEN_X = CONTROL_CENTER_X - (TSCREEN_WIDTH // 2)
TSCREEN_Y = 75

# Buzz Light
LIGHT2_WIDTH = 50
LIGHT2_HEIGHT = 50
LIGHT2_X = CONTROL_CENTER_X - BUFFER - LIGHT2_WIDTH
LIGHT2_Y = 175

# Status Light
LIGHT1_WIDTH = 50
LIGHT1_HEIGHT = 50
LIGHT1_X = LIGHT2_X - BUFFER - LIGHT1_WIDTH
LIGHT1_Y = 175

# Timeout Light
LIGHT3_WIDTH = 50
LIGHT3_HEIGHT = 50
LIGHT3_X = CONTROL_CENTER_X + BUFFER + LIGHT3_WIDTH
LIGHT3_Y = 175

# Font Info
FONT_TYPEFACE = "lucidaconsole"
LOGO_TYPEFACE = "algerian"
TIMER_TYPEFACE = "cursedtimerulil"

FONT_SIZE_TIMER = 48
FONT_SIZE_BUTTON = 16
FONT_SIZE_HINT   = 16
FONT_SIZE_STATUS = 16
FONT_SIZE_ANSWER = 12
FONT_SIZE_STATISTICS = 32
FONT_SIZE_QALABEL = 28
FONT_LOGO_SIZE = 48

# Buzzer sound
BUZZ_FREQ = 698.46
BUZZ_TIME = 0.75
BUZZ_VOL = 0.75
TIMEOUT_TONE = 554.37