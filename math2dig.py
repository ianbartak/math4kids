import streamlit as st
import random

def generate_math_problems(n_addition=10, n_subtraction=10):
    """
    Generate a specified number of addition and subtraction math problems 
    with two-digit numbers.
    
    Parameters:
    - n_addition (int): The number of addition problems to generate.
    - n_subtraction (int): The number of subtraction problems to generate.
    
    Returns:
    - problems (list of str): List of generated problem strings.
    - answers (list of int): List of answers to the generated problems.
    """
    problems = []
    answers = []
    
    # Generate addition problems
    for _ in range(n_addition):
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        problems.append(f"{a} + {b} = ?")
        answers.append(a + b)
        
    # Generate subtraction problems
    for _ in range(n_subtraction):
        a = random.randint(10, 99)
        b = random.randint(10, a)
        problems.append(f"{a} - {b} = ?")
        answers.append(a - b)
    
    return problems, answers

# Streamlit UI
st.title("Math Practice for Kids")
st.write("Practice addition and subtraction with two-digit numbers!")

# Input: Number of problems
n_addition = st.number_input("Number of addition problems:", min_value=0, max_value=100, value=10, step=5)
n_subtraction = st.number_input("Number of subtraction problems:", min_value=0, max_value=100, value=10, step=5)

# Generate problems and answers
problems, answers = generate_math_problems(n_addition, n_subtraction)

# Button to display problems
if st.button("Generate Math Problems"):
    st.subheader("Problems")
    for i, problem in enumerate(problems):
        st.write(f"Problem {i+1}:   {problem}")

# Button to display answers
if st.button("Show Answers"):
    st.subheader("Answers")
    for i, answer in enumerate(answers):
        st.write(f"Answer {i+1}:   {answer}")
