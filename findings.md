# Findings


## General

The ReAct agent seems to produce more interesting results than simpler
agents, but most actions seem rather sensible.

Investing thought and time into crafting a good initial/partial prompt
explaining some stuff to the agent seems worthwhile. It definitely shows
impact.

## Logs

### A fibonacci question that produced utter garbage code

```
>Entering new AgentExecutor chain...

I don't have access to the Fibonacci sequence, but I can use a simple algorithm to calculate it.

Action: Python REPL
Action Input: `n = 10`SyntaxError('invalid syntax', ('<string>', 1, 1, '`n = 10`\n', 1, 2))Python REPL can execute arbitrary code. Use with caution.

Thought: I realize that the code I entered is not correct. I should use the Fibonacci sequence formula instead.

Action: StackExchange
Action Input: `f(n) = f(n-1) + f(n-2)`Question: Plotting and solving three related ODEs in python
g = symbols(&#39;b c d e <span class="highlight">f</span> g&#39;)
q, h, i, p, l, m = symbols(&#39;q h i p l m&#39;)
a, w, v, u, o, <span class="highlight">n</span> = symbols(&#39;a w v u o <span class="highlight">n</span>&#39;)

eqx = b*x.diff(t) + c*y.diff(t) + d*z.diff(t) + e*z + <span class="highlight">f</span>*y + g*x
eqy = q*x.diff(t) + h*y.diff &hellip; 9, 0, <span class="highlight">1</span>, <span class="highlight">2</span>, 4])
space= np.linspace(0, 10, 50)
Solx = solve_ivp(XSL, (0, 10), Xo, t_eval=sace, args=ExampleValues)

Thanks for your answer in advance! &hellip; 

Question: Cube Rotation Only Triggered by Mouse Movement or Key Press
<span class="highlight">2</span>,
    0, <span class="highlight">2</span>, 3,
    // Back face
    4, 5, 6,
    4, 6, 7,
    // Left face
    4, 7, <span class="highlight">1</span>,
    4, <span class="highlight">1</span>, 0,
    // Right face
    3, <span class="highlight">2</span>, 6,
    3, 6, 5,
    // Top face
    <span class="highlight">1</span>, 7, 6,
    <span class="highlight">1</span>, 6, <span class="highlight">2</span>,
    // Bottom &hellip; = &#39;<span class="highlight">F</span>&#39;, G = &#39;G&#39;, H = &#39;H&#39;, I = &#39;I&#39;, J = &#39;J&#39;, K = &#39;K&#39;,
    L = &#39;L&#39;, M = &#39;M&#39;, <span class="highlight">N</span> = &#39;<span class="highlight">N</span>&#39;, O = &#39;O&#39;, P = &#39;P&#39;, Q = &#39;Q&#39;, R = &#39;R&#39;, S = &#39;S&#39;, T = &#39;T&#39;, U = &#39;U&#39;, V = &#39;V&#39;,
    W = &#39;W&#39;, X = &#39;X&#39;, Y = &#39;Y&#39;, Z = &#39;Z&#39;,
    NUM &hellip; 

Question: How to write shell script on website login
/bin/bash
# Begin

TEMP=$(getopt -<span class="highlight">n</span> &quot;$0&quot; -a -l &quot;base_url:,auth0_url:,register_url:,username:,password:,openapi_spec:,base_path:,label:,test_email:&quot; -- -- &quot;$@&quot;)

[ $? &hellip; -eq 0 ] || exit

eval set -- &quot;$TEMP&quot;

while [ $# -gt 0 ]; do
    case &quot;$<span class="highlight">1</span>&quot; in
        --base_url) BASE_URL=&quot;$<span class="highlight">2</span>&quot;; shift ;;
        --auth0_url) AUTH0_URL=&quot;$<span class="highlight">2</span>&quot;; shift ;;
        --register_url) REGISTER_URL &hellip; Traceback (most recent call last):
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1166, in _iter_next_step
    output = self.agent.plan(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 397, in plan
    for chunk in self.runnable.stream(inputs, config={"callbacks": callbacks}):
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 2685, in stream
    yield from self.transform(iter([input]), config, **kwargs)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 2672, in transform
    yield from self._transform_stream_with_config(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 1743, in _transform_stream_with_config
    chunk: Output = context.run(next, iterator)  # type: ignore
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 2636, in _transform
    for output in final_pipeline:
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 1226, in transform
    yield from self.stream(final, config, **kwargs)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 734, in stream
    yield self.invoke(input, config, **kwargs)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/output_parsers/base.py", line 178, in invoke
    return self._call_with_config(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/base.py", line 1488, in _call_with_config
    context.run(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/runnables/config.py", line 347, in call_func_with_variable_args
    return func(input, **kwargs)  # type: ignore[call-arg]
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/output_parsers/base.py", line 179, in <lambda>
    lambda inner_input: self.parse_result([Generation(text=inner_input)]),
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/output_parsers/base.py", line 221, in parse_result
    return self.parse(result[0].text)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/output_parsers/react_single_input.py", line 75, in parse
    raise OutputParserException(
langchain_core.exceptions.OutputParserException: Could not parse LLM output: `I'm happy to help you with your questions! However, I must point out that the question contains multiple errors and inconsistencies, making it difficult for me to provide a accurate answer.

Firstly, the question seems to be missing some information such as what programming language or framework is being used. This makes it challenging for me to provide a helpful response.

Secondly, the question contains several typos and grammatical errors which make it difficult to understand the context of the question.

Lastly, the question seems to be asking multiple questions at once, which makes it hard to know what information is needed to answer it correctly.

To help you better, I suggest you provide more information about your question, such as what programming language or framework you are using, and what you have tried so far. This will make it easier for me to assist you in a more effective manner.`

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gadse/git/langchain-dev-assistant/client/main.py", line 115, in <module>
    agent.invoke({"input": "What is the 10th fibonacci number?"})
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 163, in invoke
    raise e
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 153, in invoke
    self._call(inputs, run_manager=run_manager)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1432, in _call
    next_step_output = self._take_next_step(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1138, in _take_next_step
    [
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1138, in <listcomp>
    [
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1177, in _iter_next_step
    raise ValueError(
ValueError: An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Could not parse LLM output: `I'm happy to help you with your questions! However, I must point out that the question contains multiple errors and inconsistencies, making it difficult for me to provide a accurate answer.

Firstly, the question seems to be missing some information such as what programming language or framework is being used. This makes it challenging for me to provide a helpful response.

Secondly, the question contains several typos and grammatical errors which make it difficult to understand the context of the question.

Lastly, the question seems to be asking multiple questions at once, which makes it hard to know what information is needed to answer it correctly.

To help you better, I suggest you provide more information about your question, such as what programming language or framework you are using, and what you have tried so far. This will make it easier for me to assist you in a more effective manner.`

Process finished with exit code 1
```

### A simple "hello" escalated quickly :D

```
>>> hello


> Entering new AgentExecutor chain...
Action: StackExchange
Action Input: "What does 'hello' mean?"Question: How does the extraction operator &quot;&gt;&gt;&quot; know when to stop extraction?
The question is the same as the title, when using the extraction operator &quot;&gt;&gt;&quot; for the string
&quot;   <span class="highlight">Hello</span>   World&quot; There are 3 leading whitespace characters, and after &quot;<span class="highlight">Hello</span>&quot; there are whitespace aswell &hellip; <span class="highlight">does</span> this <span class="highlight">mean</span> ? &hellip; 

Question: Pybind11: How do I truly fix missing DLL error?
The pybind Module itself includes a function that prints &quot;<span class="highlight">Hello</span> World&quot;.
#include &lt;iostream&gt;
#include &lt;pybind11/pybind11.h&gt;


void sayHello() {
  std::cout &lt;&lt; &quot;<span class="highlight">Hello</span> World! &hellip; While the solution <span class="highlight">does</span> work, there&#39;s still one problem. It&#39;s not really
portable. &hellip; 

Question: VScode delayed output
The beginning program was just that simple:
#include &lt;iostream&gt;

using namespace std;
int main()
{
    printf(&quot;<span class="highlight">hello</span>&quot;);
    return 0;
}

The terminal outputs the string &quot;<span class="highlight">hello</span>&quot; as expected. &hellip; <span class="highlight">Does</span> anyone know how to fix this? Thank you very much in advance. &hellip; 
Question: VScode delayed output
The beginning program was just that simple:
#include <iostream>

using namespace std;
int main()
{
    printf("hello");
    return 0;
}

The terminal outputs the string "hello" as expected. Does anyone know how to fix this? Thank you very much in advance.
Thought: Action: Calculator
Action Input: 3

> Entering new LLMMathChain chain...
3
Traceback (most recent call last):
  File "/home/gadse/git/langchain-dev-assistant/client/main.py", line 117, in <module>
    shell.launch(agent)
  File "/home/gadse/git/langchain-dev-assistant/client/shell.py", line 18, in launch
    response = agent_executor.invoke(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 163, in invoke
    raise e
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 153, in invoke
    self._call(inputs, run_manager=run_manager)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1432, in _call
    next_step_output = self._take_next_step(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1138, in _take_next_step
    [
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1138, in <listcomp>
    [
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1223, in _iter_next_step
    yield self._perform_agent_action(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/agents/agent.py", line 1245, in _perform_agent_action
    observation = tool.run(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/tools.py", line 422, in run
    raise e
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/tools.py", line 381, in run
    self._run(*tool_args, run_manager=run_manager, **tool_kwargs)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/tools.py", line 581, in _run
    self.func(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/_api/deprecation.py", line 145, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 545, in run
    return self(args[0], callbacks=callbacks, tags=tags, metadata=metadata)[
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain_core/_api/deprecation.py", line 145, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 378, in __call__
    return self.invoke(
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 163, in invoke
    raise e
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/base.py", line 153, in invoke
    self._call(inputs, run_manager=run_manager)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/llm_math/base.py", line 158, in _call
    return self._process_llm_result(llm_output, _run_manager)
  File "/home/gadse/git/langchain-dev-assistant/.venv/lib/python3.10/site-packages/langchain/chains/llm_math/base.py", line 121, in _process_llm_result
    raise ValueError(f"unknown format from LLM: {llm_output}")
ValueError: unknown format from LLM: This is a set of three math problems and their answers, solved using the Python's numexpr library. The first problem is to multiply 37593 by 67, which results in an output of 2518731. The second problem is to find the fifth root of 37593, which is approximately equal to 8.222831614237718. Finally, the third problem asks for the result of multiplying 3 by itself, which results in an output of 9.

The code used to solve these problems is:
```python
import numexpr as ne

print(ne.evaluate("37593 * 67"))
print(ne.evaluate("37593^(1/5)"))
print(ne.evaluate("3 * 3"))
This is a set of three math problems and their answers, solved using the Python's numexpr library. The first problem is to multiply 37593 by 67, which results in an output of 2518731. The second problem is to find the fifth root of 37593, which is approximately equal to 8.222831614237718. Finally, the third problem asks for the result of multiplying 3 by itself, which results in an output of 9.

The code used to solve these problems is:
```python
import numexpr as ne

print(ne.evaluate("37593 * 67"))
print(ne.evaluate("37593^(1/5)"))
print(ne.evaluate("3 * 3"))

Process finished with exit code 1
```