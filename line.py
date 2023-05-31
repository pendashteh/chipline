import os
import argparse
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv('API_KEY')

BASE_URL= 'http://localhost:3000'

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def make_url(path):
    return BASE_URL + path

def query_type_one():
    url = make_url('/one')
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

def query_type_two():
    url = make_url('/data/two')
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

def main():
    parser = argparse.ArgumentParser(description='Perform API queries.')
    parser.add_argument('query_type', help='The type of query to perform (one, two)')

    args = parser.parse_args()

    if args.query_type == 'one':
        query_type_one()
    elif args.query_type == 'two':
        query_type_two()
    else:
        print(f'Invalid query type: {args.query_type}')

if __name__ == '__main__':
    main()
