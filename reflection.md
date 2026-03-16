# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    - Hints keep telling me to go higher when i went to 99 and lower when i typed 100, they seem to be backwards
    - The history is kept after starting a new game
    - The game doesnt let me start a new game after winning
    - The number of attempts is not reset after starting a new game
    - User can type any number, the program does not limits the input to 0-100
    - the first attempt is not recorded in the history
    - normal difficulty gives 7 attempts but easy only gives 5

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
  after testing on the web app and running the /tests
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
