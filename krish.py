from google import genai

client = genai.Client(api_key="AIzaSyDThhS39JbKDp8eraCFhSbk6qAeQo1jgOc")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="",
)

print(response.text)