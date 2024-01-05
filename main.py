# openai package
from openai import OpenAI
from time import time
from PIL import Image
# api key of it
API_KEY = "YOUR_API_KEY"


client = OpenAI(
    api_key=API_KEY
)


def ask_to_gpt(question):
    """It will take question as STRING argument and print the response from chatGPT-3.5"""
    # create a question to ask "content" as text generation
    text = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": question}
        ]
    )

    # to see the output of your question
    data2 = text.choices[0].message.content

    print(data2)


def generate_img(prompt: str):
    """It will take prompt as STRING argument and return the link for image, and time taken to do so"""
    # to generate an image, it will return a link to image which is 3MB large and PNG
    before = time()
    img_response = client.images.generate(
        model="dall-e-3",
        size="1024x1024",
        quality="hd",
        prompt=prompt,
        n=1,
        style="natural"
    )

    print(img_response.data[0].url)
    print("Seconds to generate an image : " + str(time() - before))

generate_img("A cute dog with cute black cat with red eyes, in morden looking house,")
