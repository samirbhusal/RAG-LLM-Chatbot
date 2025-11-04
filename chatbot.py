from loadenv import get_openai_client

client = get_openai_client()

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
size="1024x1024",
quality="standard",
n=1,
)

image = response.data[0].url
print(image)

