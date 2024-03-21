import os

import dotenv
import uvicorn

from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langserve import add_routes


def greet():
    print("ohai! 🦈")


def pre_flight_checks():
    env = dotenv.find_dotenv()
    print(f"dotenv file: >>{env}<<")
    dotenv.load_dotenv(env)


def build_chain():
    llama2 = Ollama(model=os.environ.get("OLLAMA_MODEL"))
    template = PromptTemplate.from_template("Tell me a joke about {topic}.")
    chain = template | llama2 | CommaSeparatedListOutputParser()
    return chain


def run(chain):
    app = FastAPI(
        title="LangChain",
        version="1.0",
        description=f"Local Langserve instance running {os.environ.get('OLLAMA_MODEL')}",
    )
    add_routes(app, chain, path="/chain")
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    greet()
    pre_flight_checks()
    run(build_chain())
