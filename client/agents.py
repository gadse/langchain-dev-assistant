"""
See Also:
    https://python.langchain.com/docs/modules/agents/
"""

import requests

from langchain import LLMMathChain
from langchain import hub
from langchain.agents import AgentType, initialize_agent, create_react_agent, AgentExecutor
from langchain.tools import (
    BaseTool,
    StructuredTool,
    Tool,
    tool,
    DuckDuckGoSearchRun,
    StackExchangeTool,
)
from langchain.llms.base import LLM
from langchain_community.utilities import StackExchangeAPIWrapper
from langchain_experimental.utilities import PythonREPL

from typing import Optional, List, Mapping, Any


HOST = "localhost:5000"
URI = f"http://{HOST}/api/v1/generate"


class AlpacaLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if isinstance(stop, list):
            stop = stop + ["\n###", "\nObservation:"]

        response = requests.post(
            URI,
            json={
                "prompt": prompt,
                "temperature": 0.7,
                "max_new_tokens": 256,
                "early_stopping": True,
                "stopping_strings": stop,
                "do_sample": True,
                "top_p": 0.1,
                "typical_p": 1,
                "repetition_penalty": 1.18,
                "top_k": 40,
                "min_length": 0,
                "no_repeat_ngram_size": 0,
                "num_beams": 1,
                "penalty_alpha": 0,
                "length_penalty": 1,
                "seed": -1,
                "add_bos_token": True,
                "truncation_length": 2048,
                "ban_eos_token": False,
                "skip_special_tokens": True,
            },
        )
        response.raise_for_status()
        return response.json()["results"][0]["text"]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {}


llm = AlpacaLLM()


def build_tooled_agent(llm):
    """
    Used https://www.comet.com/site/blog/enhancing-langchain-agents-with-custom-tools/
    """
    stack_exchange = StackExchangeAPIWrapper()
    stack_exchange_tool = Tool.from_function(
        func=stack_exchange.run,
        name="StackExchange",
        description="You coding and programming related search engine for StackExchange. Useful for when you need to search"
                    "the internet for coding, programming, or computer related information.",
    )

    # duck_duck_go = DuckDuckGoSearchRun()
    # search_tool = Tool.from_function(
    #     func=duck_duck_go.run,
    #     name="Internet Search",
    #     description="Your internet search engine. Useful for when you need to search the internet for general"
    #                 "information on people, places, history, etc.",
    # )

    llm_math_chain = LLMMathChain(llm=llm, verbose=True)
    math_tool = Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="Your handy calculator. Useful for when you are asked to perform math calculations",
    )

    python_repl = PythonREPL()
    repl_tool = Tool(
        name="Python REPL",
        description="A Python shell. Use this to execute python commands. Input should be a valid python"
                    "command. If you want to see the output of a value, you should print it out with"
                    "`print(...)`.",
        func=python_repl.run,
    )

    instructions = """
    You are an agent designed to help a developer write code, reason about code,
    and to look up information about programming concepts.
    """

    instructions += """
    You can use your StackExchange tool to search specifically for coding, programming, or computer
    related information.
    """

    # instructions += """
    # You can also use your internet search tool to search for general information.
    # """

    instructions += """
    You can also use your handy calculator tool for performing math calculations.
    """

    instructions += """
    You can also use your Python REPL too to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    You can use the output of your code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """
    # base_prompt = hub.pull("langchain-ai/react-agent-template")
    base_prompt = hub.pull("hwchase17/react")
    prompt = base_prompt.partial(instructions=instructions)

    tools = [
        stack_exchange_tool,
        #search_tool,
        math_tool,
        repl_tool
    ]
    agent = create_react_agent(
        llm,
        tools,
        prompt
    )

    return AgentExecutor(agent=agent, tools=tools, verbose=True)
