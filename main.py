import json
import random

elements = ['360_scene', 'image', 'video', 'audio', 'text', 'character']


def generate_prompt():
    # some common phrases
    templates = [
        "create an {element}",
        "make a {element} with {element2}",
        "add a {element} and a {element2}"
    ]
    template = random.choice(templates)
    element1 = random.choice(elements)
    element2 = random.choice(elements)
    prompt = template.format(element=element1, element2=element2)
    return prompt


def generate_completion(prompt):
    return list(filter(lambda element: element in prompt, elements))


# Generate 1000 prompts and completions
dataset = []
for i in range(1000):
    prompt = generate_prompt()
    completion = generate_completion(prompt)
    data = {"prompt": prompt, "completion": completion}
    dataset.append(data)

# Save the dataset to a JSON file
with open("generated_dataset.json", "w") as f:
    json.dump(dataset, f)
