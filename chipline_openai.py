import openai
import sys
import importlib
from proxy import proxy_function

prompt = sys.argv[2]
openai.api_key_path = 'key'

def create(**kwargs):
    return proxy_function(openai.Completion.create, **kwargs)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        module_name = 'modules.' + sys.argv[1]
        imported_module = importlib.import_module(module_name)
        response = imported_module.response
        text_values = [choice.get('text') for choice in response.get('choices', [])]
        print('\n'.join(text_values)+'\n')
