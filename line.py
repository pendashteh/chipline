#!/usr/bin/env python

import argparse
import requests
import yaml

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
}

def query_type_one(config, extra_arg):
    url = construct_url(config['BASE_URL'], '/data/one', extra_arg)
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

def query_type_two(config, extra_arg):
    url = construct_url(config['BASE_URL'], '/data/two', extra_arg)
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

def construct_url(base_url, endpoint, extra_arg):
    return base_url + endpoint + '/' + extra_arg

def get_query_functions():
    functions = {name: func for name, func in globals().items() if callable(func) and name.startswith('query_type_')}
    return functions

def main():
    parser = argparse.ArgumentParser(description='Perform API queries.')
    parser.add_argument('query_type', nargs='?', help='The type of query to perform')
    parser.add_argument('extra_arg', nargs='?', help='An extra argument for the query')

    args = parser.parse_args()

    # Load configuration from YAML file
    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    query_functions = get_query_functions()

    if args.query_type:
        query_func = query_functions.get(f'query_type_{args.query_type}')
        if query_func and args.extra_arg:
            query_func(config, args.extra_arg)
        elif not query_func:
            print(f'Invalid query type: {args.query_type}')
        else:
            print(f'Missing extra argument for query type: {args.query_type}')
    else:
        print('Available query types:')
        for name in query_functions:
            print(name.replace('query_type_', ''))

if __name__ == '__main__':
    main()
