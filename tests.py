import os
import openai
from openai.error import InvalidRequestError
from fastapi import Depends, BackgroundTasks, status
from fastapi.responses import JSONResponse

openai.api_key = "sk-9zvTslc6JjVtr9gURn5IDgEcqRThMEWbZFUZ2kh4"


# response = openai.Answer.create(
#   search_model="curie",
#   model="davinci",
#   question="africA?",
#   file="file-2FLzlUNzq2KcFl6gnS0MSbN5",
#   examples_context="In 2017, U.S. life expectancy was 78 years.",
#   examples=[["What is human life expectancy in the United States?","78 years."]],
#   max_tokens=1500,
#   temperature=1,
#   stop=["\n", "<|endoftext|>"],
# )
#
# print(response)


def answers():
  try:
    response = openai.Answer.create(
      search_model="curie",
      model="davinci",
      question="africA?",
      file="file-2FLzlUNzq2KcFl6gnS0MSbN5",
      examples_context="In 2017, U.S. life expectancy was 78 years.",
      examples=[["What is human life expectancy in the United States?", "78 years."]],
      max_tokens=1500,
      temperature=1,
      stop=["\n", "<|endoftext|>"],
    )
    print(response)
  except InvalidRequestError:
    return JSONResponse({}, status_code=status.HTTP_204_NO_CONTENT)


answers()
