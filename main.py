# openai package
from openai import OpenAI
from time import time
from PIL import Image
# api key of it
API_KEY = "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"


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


def edit_img(img_path,mask_path, prompt: str, n: int = 1):

    """It will take image path as STRING,prompt as STRING, number of variation as INT as argument and will return the links of those"""

    # to edi any image it should be under 4MB, PNG and in "rb"
    # to make more images N=

    img_edit = client.images.edit(
        image=open(img_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt=prompt,
        size="1024x1024",
        n=n
    )

    # # for 1st image's link
    # print(img_edit.data[0].url)

    # to get all the links
    links = [img_edit.data[i].url for i in range(n)]
    print(links)


im = "2.png"
img = Image.open(im, formats=["png"])
img_rgba = img
img_rgba.putalpha(255)
img_rgba.save(im)

mask = "mask.png"
# mas = Image.open(mask, formats=["png"])
# mas.resize((1024, 1024))
# mas.save(mask)

prom = "add 'JAY' in background colorfully"
# edit_img(im, mask, prom)


generate_img("A cute dog with cute black cat with red eyes, in morden looking house,")