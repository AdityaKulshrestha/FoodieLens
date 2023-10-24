import replicate
from config import MODEL
from typing import BinaryIO


def generate_recipe(img: BinaryIO, prompt: str):
    output = replicate.run(
        MODEL,
        input={"image": img, "prompt": prompt}
    )
    recipe = ""
    print(output)
    for item in output:
        recipe += item
    return recipe
