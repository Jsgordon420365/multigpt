import argparse
from transformers import pipeline

# Define the available models
models = {
    'a': 'model_a_identifier',
    'b': 'model_b_identifier',
    'c': 'model_c_identifier',
    'd': 'model_d_identifier',
    'e': 'model_e_identifier',
    'f': 'model_f_identifier'
}

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Generate text using specified GPT models.')
# Add arguments for each model
for model in models:
    parser.add_argument(f'-{model}', action='store_true', help=f'Use model {model.upper()}')

# Add argument for the prompt
parser.add_argument('prompt', type=str, help='The prompt to generate text for')

# Parse the arguments
args = vars(parser.parse_args())

# Function to generate text
def generate_text(model_identifier, prompt):
    generator = pipeline('text-generation', model=model_identifier)
    return generator(prompt, max_length=50, num_return_sequences=1)

# Main execution
if __name__ == '__main__':
    # Generate text for each specified model
    for model, identifier in models.items():
        if args[model]:
            response = generate_text(identifier, args['prompt'])
            print(f'Model {model.upper()} response:')
            print(response[0]['generated_text'])

