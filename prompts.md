# Prompts

### prompt 1 - Summarisation

Summarize the following text in in 2–3 sentences: 

Transformer-based language models use self-attention mechanisms to model contextual relationships between tokens in an input sequence, allowing them to capture both local and long-range dependencies effectively. Unlike recurrent or convolutional neural networks, transformers process entire sequences in parallel rather than step-by-step, which leads to significantly faster training times on modern hardware. This architectural design has enabled the scaling of language models to billions of parameters and massive training datasets. However, the self-attention mechanism has a computational and memory complexity that grows quadratically with sequence length, making long-context processing expensive. As a result, various optimizations such as sparse attention, sliding windows, and low-rank approximations have been proposed to reduce resource usage while preserving model performance.


----------------------

### prompt 2 - Code Help

Explain what this Python function does in simple terms:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

### prompt 3 - Code Help

Refactor this JavaScript function to make it more readable and efficient:

function addNumbers(arr) {
    let sum = 0;
    for(let i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    return sum;
}

### prompt 4 - Code Help

Write unit tests in Python using pytest for this function:

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

### prompt 5 - Code Help

Suggest an improvement or optimization for this Python snippet: 

numbers = [1,2,3,4,5]
squared = []
for n in numbers:
    squared.append(n**2)


-----------------------

### prompt 6 - Structured Output (JSON)

Extract the key details from this text as JSON:

'John Smith, 32, lives in New York and works as a data scientist at Google.'  
Format: `{ "name": ..., "age": ..., "city": ..., "occupation": ... }`

### prompt 7 - Structured Output (JSON)

Convert the following requirements into test cases in JSON:

'The login page should allow users to enter a username and password. Invalid credentials should display an error. Successful login redirects to the dashboard.'  
Format: `[ { "test_case": ..., "expected_result": ... } ]`