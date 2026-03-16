# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  
  - [x] When guess is too high like 99, expected hint "Go LOWER" but got "Go HIGHER."
  - [ ] When starting a new game, expected history to reset but previous guesses were kept
  - [ ] After winning, expected to be able to start a new game but the button did not work
  - [ ] When starting a new game, expected attempt count to reset to 0 but it kept the previous count
  - [ ] When entering a number outside 1–100, expected an error or rejection but any number was accepted
  - [ ] On the first attempt, expected the guess to appear in history but it was not recorded
  - [ ] On Normal difficulty, expected the same or more attempts than Easy but Normal gives 7 and Easy gives 5 (should be the other way around)
  - [x] On Hard difficulty, expected a larger range than Normal to make it harder, but the range was 1-50 which is easier than Normal.
  - [x] The guess prompt always said "between 1 and 100" regardless of difficulty, expected the message to reflect the actual range

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

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
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
