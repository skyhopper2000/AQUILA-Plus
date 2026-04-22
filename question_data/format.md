Here is how to format questions such that Aquila can read them.
1. Create a folder inside `question_data` called `seasonXX` where XX is the last two digits of the year.
2. Add a file called `weekX.py` where X is the week number (1, 2 etc.)
3. Format the file as follows:
   ```python
   QUESTIONS = [
     ("question", "answer"),
     ("question", "answer")
     ]
   ```
