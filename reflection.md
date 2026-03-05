# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually
happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    - There's no obvious UI/UX bug. Game renders appropriately.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    - can guess > 100
    - 100 says higher. 101 -> says lower
    - accepts floats, ie. 101.1 -> says go higher
    - enter key doesn't work
    - allows to enter 0 -> says go lower.
    - gives incorrect hint. when number was 24, hint says go lower for 0.
      Summary: there are bounds and type errors

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - I will use Gemini and Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested
  and how you verified the result).
    - I'm experimenting with setting up a monorepo for codepath projects. It helped me
      learn and troubleshoot using my local parameters and learning git flow.
- Give one example of an AI suggestion that was incorrect or misleading (including what
  the AI suggested and how you verified the result).
    - In this exercise, I did not get a misleading/incorrect LLM suggestion -- only
      that Claude agent was not working in Pycharm for whatever reason.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    - I ran the LLM generated tests after verifying the tests.
    - I ran the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    - The tests targetted the main areas of logic error: bounds, types
- Did AI help you design or understand any tests? How?
    - I followed directions and all tests were llm generated. it also fixed the
      provided ones.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    - The secret number is generated using the random module but fixed to 1-100
      range for all levels. I fixed this by passing low and high from
      get_range_for_difficulty into init_session_state and using them in the new game
      handler as well.
- How would you explain Streamlit "reruns" and session state to a friend who has never
  used Streamlit?
    - Every widget interaction is a stop and rerun of the entire app.py script from
      top to bottom. So variables get reset to their initial value. Session state
      helps persist state across reruns.
    - See: https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun
      and https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
- What change did you make that finally gave the game a stable secret number?
    - What's meant by stable here? The original app already used st.session_state to
      guard the secret from regenerating on every rerun, so the secret number was not
      technically unstable between guesses

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs
  or projects?
    - This could be a testing habit, a prompting strategy, or a way you used Git.
    - Good to start with small practice. But we need more guidance on how to use
      harnesses and other agentic coding best practices to work on larger codebases.
      I'm saying this for a field where changes occur in weeks or months.
- What is one thing you would do differently next time you work with AI on a coding
  task?
    - Parse the entire file first and refactor to a point where it's easier to trace
      bugs. This assignment sequenced refactoring after bug detecetion, but that
      doesn't work for my brain.
- In one or two sentences, describe how this project changed the way you think about AI
  generated code.
    - First, I don't call it AI. It's a LLM model. While it's under the umbrella of AI,
      AI has taken on a cultural definition that is not accurate. So I use LLM. LLM
      have gotten more powerful, but it's so easy to default to it. My own learning
      and tolerance for learning does not get stronger.
