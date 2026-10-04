# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start?
  - The hints were backwards
  - Difficulty levels did not work as expected

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                            | Expected Behavior                                                         | Actual Behavior                                     | Console Output / Error | Suspected Code Location |
| -------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------- | ----------------------- |
| Click on New Game button         | Start a new game, clear the guess input and Game Over message             | Did not clear the input field and Game Over message | none                   | `app.py`                |
| Wrong hint for the secret number | If the secret is higher than guess, it should say _Go higher_, vice versa | Give the opposite hint                              | none                   | `app.py`                |
| Click on Difficulty dropdown     | Level Hard should show range 1-100                                        | Range 1-100 is shown for _Difficulty: Normal_       | none                   | `app.py`                |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Gemini
- Give one example of an AI suggestion that was correct: Gemini correctly suggested swapping the hint strings in `logic_utils.py`, which I verified by testing guesses in the running game.
- Give one example of an AI suggestion you did not accept as written: Gemini initially suggested completely rewriting the `check_guess` function, which I rejected as over-engineered in favor of a simple string swap.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I decided a bug was fixed when the game worked correctly in the browser and all automated tests passed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code. I ran a pytest case simulating a "New Game" button click, which proved that the game properly erased old data.
- Did AI help you design or understand any tests? How? Yes, the AI wrote the test code that automatically simulated user clicks on the app.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Every time you click a button, Streamlit redraws the entire page from top to bottom. "Session state" is just a special memory box to save your game's progress between those redraws.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? I want to build a habit of writing automated tests right after I fix a bug to ensure it doesn't break again.
- What is one thing you would do differently next time you work with AI on a coding task? Next time, I will give the AI more specific details about how my project folders are set up to avoid simple errors.
- In one or two sentences, describe how this project changed the way you think about AI generated code. This project taught me that AI code is rarely perfect on the first try. It always needs a human to review and thoroughly test it.
