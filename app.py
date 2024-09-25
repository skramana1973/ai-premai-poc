from dotenv import load_dotenv
from premai import Prem
import os

load_dotenv()

# Set API key
os.environ["PREMAI_API"] = os.getenv("PREMAI_API")

client = Prem(api_key=os.environ["TOOL_HOUSE_KEY"])

project_id = 6075

client = Prem(api_key=os.environ["PREMAI_API"])

project_id = 6075

system_prompt = "You're an helpful assistant"
messages = [
    {"role": "user", "content": "Who won the world series in 2020?"},
]
project_id = 6075


# # Create completion
# response = client.chat.completions.create(
#     project_id=project_id,
#     system_prompt=system_prompt,
#     messages=messages,
# )

# print("Choises : ")
# print(response.choices)


# # Create completion with stream
# response = client.chat.completions.create(
#     project_id=project_id,
#     messages=messages,
#     stream=True,
# )

# print("Choise Content : ")
# for chunk in response:
#     if chunk.choices[0].delta["content"]:
#         print(chunk.choices[0].delta["content"], end="")


# # Text you want to summarize
# text_to_summarize = "This is the great tale of ... "
# # Construct the message with the template
# messages = [
#     {
#         "role": "user",
#         "template_id": "4e3d5a6e-a7a0-4638-89da-08606544cf3e",  # Your template's ID
#         "params": {"text": text_to_summarize},
#     }
# ]

# response = client.chat.completions.create(project_id=project_id, messages=messages)

# print("Choise Content By Template : ")

# print(response.choices)


model = "gpt-3.5-turbo"
system_prompt = "You are a helpful assistant."
session_id = "my-session"
temperature = 0.7
messages = [
    {"role": "user", "content": "Who won the world series in 2020?"},
]

# print("Choise Content gpt-3.5-turbo : ")


# response = client.chat.completions.create(
#     project_id=project_id,
#     messages=messages,
#     model=model,
#     system_prompt=system_prompt,
#     session_id=session_id,
#     temperature=temperature,
# )

# print(response)

messages = [
    {"role": "user", "content": "What is Kafka?"},
]

repositories = dict(ids=[2739], similarity_threshold=0.65, limit=3)

# response = client.repositories.create(
#     name="Raman_repository",
#     description="Raman Repository",
#     organization="org-test@premai.io",
# )

FILE_PATH = "repo/kafka.pdf"
# Content: "My friend Jack has a beautiful pet, he gave it the name Sparky, [...]"

# response = client.repository.document.create(repository_id=2739, file=FILE_PATH)

# print(response)
# E.g., DocumentOutput(repository_id=4, document_id=14, name="pets_and_their_owners.txt", type="text", status="UPLOADED", chunk_count=0, error=None)


# Create completion
response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
    model=model,
    repositories=repositories,
    system_prompt=system_prompt,
    session_id=session_id,
    temperature=temperature,
    stream=False,
)

# print(response.choices[0])

# print(response.choices[0].message)

print(response.choices[0].message.content)
