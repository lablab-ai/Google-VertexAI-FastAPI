import os
import openai
from flask import Flask
from flask_cors import CORS

openai.api_key = "sk-9zvTslc6JjVtr9gURn5IDgEcqRThMEWbZFUZ2kh4"


def alice_function(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': ['GET','POST'],
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': ['GET', 'POST'],
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600'
    }

    # list engines
    if request.args and 'engine' in request.args:
        engines = openai.Engine.list()

        return engines, 200, headers

    # list files
    if request.args and 'file' in request.args:
        files = openai.File.list()
        return files, 200, headers

    # query answers engine
    if request.args and 'query' in request.args:

        # params
        model = 'ada'
        search_model = 'ada'
        temp = 0
        max_rerank = 200
        tokens = 1000
        config = '1'

        # Args
        query = request.args.get('query')
        if request.args.get('model'):
            model = request.args.get('model')
        if request.args.get('search_model'):
            search_model = request.args.get('search_model')
        if request.args.get('max_rerank'):
            temp = request.args.get('temp')
        if request.args.get('max_rerank'):
            max_rerank = request.args.get('max_rerank')
        if request.args.get('tokens'):
            tokens = request.args.get('tokens')
        if request.args.get('config'):
            config = request.args.get('config')

        print(query, model, search_model, temp, max_rerank, tokens, config)

        # Configs
        if config == '1':  # Financial reports
            file = "file-oQDJdeZM3XwDINp4Os7FKegb"
            context = "The ERG Group is a major independent operator in the production of electricity from renewable sources such as wind,\nsolar, hydroelectric and high-efficiency, low environmental impact cogenerative thermoelectric power plants.\nManagement of the industrial and commercial processes of the ERG Group is entrusted to the subsidiary ERG Power\nGeneration S.p.A. which carries out:\n• centralised Energy Management activities for all the generation technologies in which the ERG Group operates;\n• the Operation and Maintenance activities of its Italian wind farms and part of the plants in France and Germany, as\nwell as the Terni Hydroelectric Complex and the Priolo CCGT plant. It provides technical and administrative services\nin France and Germany for both Group companies and third parties through its foreign subsidiaries."
            examples = [["EBTDA third quarter 2019?", "99 million"], ["What is the business of ERG?",
                                                                      "The ERG Group is a major independent operator in the production of electricity from renewable sources such as wind, solar, hydroelectric and high-efficiency, low environmental impact cogenerative thermoelectric power plants"],
                        ["What was the devation of the revenue between 2018-2019?",
                         "From 2018 and 2019 the revenue is decreased of 0,496%, passing from 1,026.7 milions to 1,021.6 (adjusted)"]]

        if config == '2':  # Artificial intelligence
            file = "file-jHcx2gRg1kIp2CKj0rsba84o"
            context_1 = "Number of AI journal publications grew by 34.5% from 2019 to 2020"
            context_2 = ""
            context_3 = ""

            example_1 = ["Growth of published AI journals 2018 to 2020?",
                         "19.6% 2018 - 2019 and increased to 34.5% from 2019 to 2020"]
            example_2 = ["",
                         ""]
            example_3 = ["",
                         ""]

            context = context_1 + " " + context_2 + " " + context_3
            examples = [example_1]

        if config == '3':  # something else
            file = "file-WxyUG1r8XHtboyUAODO85dam"
            context = "The ERG Group is a major independent operator in the production of electricity from renewable sources such as wind,\nsolar, hydroelectric and high-efficiency, low environmental impact cogenerative thermoelectric power plants.\nManagement of the industrial and commercial processes of the ERG Group is entrusted to the subsidiary ERG Power\nGeneration S.p.A. which carries out:\n• centralised Energy Management activities for all the generation technologies in which the ERG Group operates;\n• the Operation and Maintenance activities of its Italian wind farms and part of the plants in France and Germany, as\nwell as the Terni Hydroelectric Complex and the Priolo CCGT plant. It provides technical and administrative services\nin France and Germany for both Group companies and third parties through its foreign subsidiaries."
            examples = [["Which is the EBTDA in the third quarter of 2019?", "99 million"],["What is the business of ERG?",
                         "The ERG Group is a major independent operator in the production of electricity from renewable sources such as wind, solar, hydroelectric and high-efficiency, low environmental impact cogenerative thermoelectric power plants"],
                        ["What was the devation of the revenue between 2018-2019?",
                         "From 2018 and 2019 the revenue is decreased of 0,496%, passing from 1,026.7 milions to 1,021.6 (adjusted)"]]

        # models ada, babbage, curie, and davinci
        alice = openai.Answer.create(
            search_model=search_model,
            model=model,
            temperature=float(temp),
            return_metadata=True,
            return_prompt=True,
            max_rerank=int(max_rerank),
            n=1,
            question=query,
            file=file,
            examples_context=context,
            examples=examples,
            max_tokens=int(tokens),
            stop=["\n", "<|endoftext|>"],
        )

        responsdata = alice
        print(responsdata)
        return responsdata, 200, headers

    else:
        return 'error', 400, headers
