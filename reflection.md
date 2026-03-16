# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
    - [x] When guess is too high like 99, expected hint "Go LOWER" but got "Go HIGHER."
        - #FIXED: Moved check_guess out of app.py, fixed swapped high/low hints, and removed string casting of secret in app.py using claude.
    - [x] When starting a new game, expected history and attempts to reset but previous guesses were kept
        - #Fixed: New game now clears history, resets attempts to 0, resets status to "playing", and uses difficulty-based range instead of hardcoded 1-100.
    - [x] After winning, expected to be able to start a new game but the button did not work
        - #Fixed: New game now resets status to "playing", allowing a new game after a win or loss.
    - [x] When entering a number outside 1–100, expected an error or rejection but any number was accepted
        - #Fixed: Added range validation in app.py after parse_guess; shows an error if guess is outside the difficulty range.
    - [x] After submitting the guess, expected the guess to appear in history immediately but it was not updated
        - #Fixed: Moved the debug expander to after the submit block so history reflects the current guess on the same rerun.
    - [x] On Normal difficulty, expected the same or more attempts than Easy but Normal gives 7 and Easy gives 5 (should be the other way around)
        - #Fixed: Changed Easy attempts from 6 to 10 so Easy (10) > Normal (8) > Hard (5).
    - [x] On Hard difficulty, expected a larger range than Normal to make it harder, but the range was 1-50 which is easier than Normal.
        - #Fixed: Display correct range and attempts left based on difficulty settings.
    - [x] The guess prompt always said "between 1 and 100" regardless of difficulty, expected the message to reflect the actual range
        - #Fixed: Display correct range and attempts left based on difficulty settings.
    - [x] When guessing too high on an even attempt, expected score to decrease but it increases by 5 (wrong guesses should never reward points)
        - #FIXED: Updated scoring logic to keep penalties consistent for wrong guesses.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - The AI was able to fix the bug where the new game button did not work. The AI explained that if the user won or lost, the app checks status calls the stop() function, so the new game never ran. Then, it updated the state status and the button work as intended.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    - The AI fixed the high and lower problem but added a work around to the string-casting bug in the code instead or pointing out the bug or give possible solutions on the bug. The AI also remove everything from the logic utils when moving the logic to the file.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    - I decided the bug was fixed after testing on the web app and running the /tests
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    - I ran pytest to called check_guess(60, 50) and check_guess(40, 50) and checked that the hint messages returned "LOWER" and "HIGHER" respectively. The test showed the swapped hints bug was fixed.
    - The previous test were not working for me and had to fix them. I was returning a tuple and the test were only checking for a string.
- Did AI help you design or understand any tests? How?
    - AI help me to design the test to verify if the swapped bug was fixed and check the message text.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    - This never happen on the app. The number was always the same during the game session
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Every time the user interact with a Streamlit app, like clicking a button or typing in a box, the entire Python script runs again from top to bottom. That's would be a "rerun."

- What change did you make that finally gave the game a stable secret number?
    - This was not a bug on this version

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    - This could be a testing habit, a prompting strategy, or a way you used Git.
    - Multiple chats: One chat for each bug fix was useful because it allow me to be more organized with my prompts and prevent the AI to get confused with different bugs.
    - The tests were useful to check if the code actually work
- What is one thing you would do differently next time you work with AI on a coding task?
    - Make sure that the generated code is actually fixing the bugs instead of creating workarounds to avoid triggering the bugs

- In one or two sentences, describe how this project changed the way you think about AI generated code.
    - This project showed me that AI can be very powerful in approaching bugs and allow me to quickly fix them, but AI can also create new bugs or create workarounds for some bugs instead of fixing them.
