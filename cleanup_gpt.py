import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt(messages, max_new_tokens):
    # Generate a response from ChatGPT model
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",  # choose the engine for the chat-based model
        #gpt-4-0125-preview
        max_tokens=max_new_tokens,
        temperature=0.0000001,
        messages=messages,
    )

    # Get the assistant's response from the API response
    assistant_response = response.choices[0].message.content

    # Write the conversation to a log file
    with open('log.txt', "a") as file:
        for msg in messages:
            file.write(msg["role"] + ": " + msg["content"]+"\n")
        file.write("assistant: " + assistant_response+"\n\n\n")

    # Return the assistant's response
    return assistant_response

class ChatML:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def complete(self, max_new_tokens=4096):
        response = chatgpt(self.messages, max_new_tokens)
        self.add_message("assistant", response)
        return response

INCOMPLETE = ["ace", "ambitious", "america", "angelinvesting", "avg", "startupfunding", "fr", "road", "siliconvalley", "better", "bubble", "cities", "college", "convince", "ds", "essay", "foundersatwork", "gap", "gh", "greatwork", "growth", "guidetoinvestors", "hiring", "hp", "hs", "hundred", "icad", "ideas", "laundry", "lesson", "lies", "love", "marginal", "mit", "nerds", "notnot", "opensource", "philosophy", "popular", "re", "really", "road", "say", "siliconvalley", "softwarepatents", "spam", "start", "startupideas", "startuplessons", "startupmistakes", "superangels", "superlinear", "taste", "wealth", "worked"]
INCOMPLETE_2 = ["startupfunding", "fr", "road", "greatwork", "lies", "popular", "re", "start", "startupideas", "wealth", "worked"]
INCOMPLETE_3 = ["greatwork", "lies", "road", "worked"]
INCOMPLETE_4 = ["road"]

# get all ./articles_text/articles/*.txt
import glob
import os
glob_files = glob.glob("./articles_text/articles/*.txt")

total = len(glob_files)

prompt = "Copy this article, word by word, and remove any unnecessary tags and characters. Use Markdown to format it. Preserve links within text (use markdown format), but remove links that surround the article and are not part of it. For quote lines, use '> ' symbol. Integrate things like bold, italics, code block and so on, when needed based on common sense. If headings are present, format them as such. Start with the title of the article."

# i = 0
# for file in glob_files:
#     with open(file, "r") as f:
#         out_filename = file.replace("articles_text/articles", "cleaned").replace(".html.txt", ".md")
        
#         i += 1

#         # check if exists, skip
#         if os.path.exists(out_filename):
#             continue

#         print(f"{i}/{total} {file}")

#         text = f.read()
#         # create chat
#         chat = ChatML()

#         chat.add_message("system", prompt)

#         chat.add_message("system", "ARTICLE:")
#         chat.add_message("user", text)
#         chat.add_message("system", "CLEANED:")

#         # process
#         response = chat.complete()

#         with open(out_filename, "w") as f:
#             f.write(response.strip())

#             # print(response.strip())

#     # exit()
            
# for file in INCOMPLETE:
#     file_in = f"./articles_text/articles/{file}.html.txt"
#     out_filename = file_in.replace("articles_text/articles", "cleaned").replace(".html.txt", ".md")
#     with open(file_in, "r") as f:
#         # if exists, continue
#         if os.path.exists(out_filename + ".1.md"):
#             continue

#         with open(out_filename, "r") as f2:
#             t2 = f2.read()

#             print(f"COMPLETING: {file_in}")

#             text = f.read()
#             # create chat
#             chat = ChatML()

#             chat.add_message("system", prompt + " If you get interrupted, simply continue from where you stopped.")

#             chat.add_message("system", "ARTICLE:")
#             chat.add_message("user", text)
#             chat.add_message("system", "CLEANED:")
#             chat.add_message("user", t2)

#             # process
#             response = chat.complete()

#             with open(out_filename + ".1.md", "w") as f:
#                 f.write(t2)
#                 f.write("\n")
#                 f.write(response.strip())

#                 # print(response.strip())


# for file in INCOMPLETE_2:
#     file_in = f"./articles_text/articles/{file}.html.txt"
#     out_filename = file_in.replace("articles_text/articles", "cleaned").replace(".html.txt", ".md")
#     with open(file_in, "r") as f:
#         # if exists, continue
#         if os.path.exists(out_filename + ".2.md"):
#             continue

#         with open(out_filename, "r") as f2:
#             t2 = f2.read()

#             with open(out_filename + '.1.md', "r") as f3:
#                 t3 = f3.read()

#                 print(f"COMPLETING: {file_in}")

#                 text = f.read()
#                 # create chat
#                 chat = ChatML()

#                 chat.add_message("system", prompt + " If you get interrupted, simply continue from where you stopped.")

#                 chat.add_message("system", "ARTICLE:")
#                 chat.add_message("user", text)
#                 chat.add_message("system", "CLEANED:")
#                 chat.add_message("user", t2)
#                 chat.add_message("user", t3)

#                 # process
#                 response = chat.complete()

#                 with open(out_filename + ".2.md", "w") as f:
#                     f.write(t2)
#                     f.write("\n")
#                     f.write(t3)
#                     f.write("\n")
#                     f.write(response.strip())

#                     # print(response.strip())



# for file in INCOMPLETE_3:
#     file_in = f"./articles_text/articles/{file}.html.txt"
#     out_filename = file_in.replace("articles_text/articles", "cleaned").replace(".html.txt", ".md")
#     with open(file_in, "r") as f:
#         # if exists, continue
#         if os.path.exists(out_filename + ".3.md"):
#             continue

#         with open(out_filename, "r") as f2:
#             t2 = f2.read()

#             with open(out_filename + '.2.md', "r") as f3:
#                 t3 = f3.read()

#                 print(f"COMPLETING: {file_in}")

#                 text = f.read()
#                 # create chat
#                 chat = ChatML()

#                 chat.add_message("system", prompt + " If you get interrupted, simply continue from where you stopped.")

#                 chat.add_message("system", "ARTICLE:")
#                 chat.add_message("user", text)
#                 chat.add_message("system", "CLEANED:")
#                 chat.add_message("user", t3)

#                 # process
#                 response = chat.complete()

#                 with open(out_filename + ".3.md", "w") as f:
#                     f.write(t3)
#                     f.write("\n")
#                     f.write(response.strip())

#                     # print(response.strip())


for file in INCOMPLETE_4:
    file_in = f"./articles_text/articles/{file}.html.txt"
    out_filename = file_in.replace("articles_text/articles", "cleaned").replace(".html.txt", ".md")
    with open(file_in, "r") as f:
        # if exists, continue
        if os.path.exists(out_filename + ".4.md"):
            continue

        with open(out_filename, "r") as f2:
            t2 = f2.read()

            with open(out_filename + '.3.md', "r") as f3:
                t3 = f3.read()

                print(f"COMPLETING: {file_in}")

                text = f.read()
                # create chat
                chat = ChatML()

                chat.add_message("system", prompt + " If you get interrupted, simply continue from where you stopped.")

                chat.add_message("system", "ARTICLE:")
                chat.add_message("user", text)
                chat.add_message("system", "CLEANED:")
                chat.add_message("user", t3)

                # process
                response = chat.complete()

                with open(out_filename + ".4.md", "w") as f:
                    f.write(t3)
                    f.write("\n")
                    f.write(response.strip())

                    # print(response.strip())






# for file in *.html.txt; do
#     mv -- "$file" "${file%.html.txt}.md"
# done