import os
import openai
import sys
import importlib
from proxy import proxy_function

prompt = sys.argv[2]
openai.api_key = os.getenv('OPENAI_API_KEY')
if openai.api_key is None:
    openai.api_key_path = os.getenv('OPENAI_API_KEY_PATH', 'key/openai.api_key')

def create(**kwargs):
    return proxy_function(openai.Completion.create, **kwargs)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        module_name = 'modules.' + sys.argv[1]
        imported_module = importlib.import_module(module_name)
        response = imported_module.response
        text_values = [choice.get('text') for choice in response.get('choices', [])]
        print('\n'.join(text_values)+'\n')
