import wikipedia

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
# ANSI escape codes for colors

def get_wikipedia_info(topic):
    try:
        # Set the language to English
        wikipedia.set_lang("en")
        sen = RED+"---|["+BLUE+"no of sentence"+ RED+"]|--|:"
        sentences = int(input(sen+YELLOW))
        # Get the page summary for the specified topic
        summary = wikipedia.summary(topic, sentences=sentences)

        # Get the full page content for the specified topic
        page = wikipedia.page(topic)

        # Extract information
        title = page.title
        full_text = page.content

        # Return the extracted information
        return {
            "title": title,
            "summary": summary,
            "full_text": full_text
        }

    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found for topic: {topic}")
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {topic} may refer to multiple topics. Options: {e.options}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    import os
    os.system("clear")
    # Topic to search
    top = RED+"----|["+ BLUE+"wiki search"+RED+" ]|---|:"
    topic = str(input(top+YELLOW))

    # Get Wikipedia info
    info = get_wikipedia_info(topic)

    # Print the information if available
    if info:
        print(RED+"\n----|[",BLUE+"Title",RED+"]|-- : ", GREEN+info["title"])
        print(RED+"\n----|[",BLUE+"Summary",RED+"]|-- : ",GREEN+info["summary"])
        # Uncomment the following line if you want to print the full content
        # print("Full content: ", info["full_text"])
    ask = input(YELLOW+"do you want to search again (y|n) :"+RED)
    if ask == "y":
      main()
    else :
      print(RED+"bye")
      exit()
if __name__ == "__main__":
    main()