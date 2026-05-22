import os
from google import genai
from dotenv import load_dotenv
from google.genai import types
import gradio as gr
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=GEMINI_API_KEY)
languages = {
    "Afrikaans": "Translate the given sentence into Afrikaans language",
    "Amharic": "Translate the given sentence into Amharic language",
    "Arabic": "Translate the given sentence into Arabic language",
    "Assamese": "Translate the given sentence into Assamese language",
    "Basque": "Translate the given sentence into Basque language",
    "Bengali": "Translate the given sentence into Bengali language",
    "Bodo": "Translate the given sentence into Bodo language",
    "Bulgarian": "Translate the given sentence into Bulgarian language",
    "Burmese": "Translate the given sentence into Burmese language",
    "Catalan": "Translate the given sentence into Catalan language",
    "Chinese": "Translate the given sentence into Chinese language",
    "Croatian": "Translate the given sentence into Croatian language",
    "Czech": "Translate the given sentence into Czech language",
    "Danish": "Translate the given sentence into Danish language",
    "Dogri": "Translate the given sentence into Dogri language",
    "Dutch": "Translate the given sentence into Dutch language",
    "English": "Translate the given sentence into English language",
    "Esperanto": "Translate the given sentence into Esperanto language",
    "Estonian": "Translate the given sentence into Estonian language",
    "Filipino": "Translate the given sentence into Filipino language",
    "Finnish": "Translate the given sentence into Finnish language",
    "French": "Translate the given sentence into French language",
    "Galician": "Translate the given sentence into Galician language",
    "German": "Translate the given sentence into German language",
    "Greek": "Translate the given sentence into Greek language",
    "Gujarati": "Translate the given sentence into Gujarati language",
    "Haitian Creole": "Translate the given sentence into Haitian Creole language",
    "Hebrew": "Translate the given sentence into Hebrew language",
    "Hindi": "Translate the given sentence into Hindi language",
    "Hungarian": "Translate the given sentence into Hungarian language",
    "Icelandic": "Translate the given sentence into Icelandic language",
    "Indonesian": "Translate the given sentence into Indonesian language",
    "Irish": "Translate the given sentence into Irish language",
    "Italian": "Translate the given sentence into Italian language",
    "Japanese": "Translate the given sentence into Japanese language",
    "Kannada": "Translate the given sentence into Kannada language",
    "Kashmiri": "Translate the given sentence into Kashmiri language",
    "Kazakh": "Translate the given sentence into Kazakh language",
    "Konkani": "Translate the given sentence into Konkani language",
    "Korean": "Translate the given sentence into Korean language",
    "Latin": "Translate the given sentence into Latin language",
    "Latvian": "Translate the given sentence into Latvian language",
    "Lithuanian": "Translate the given sentence into Lithuanian language",
    "Maithili": "Translate the given sentence into Maithili language",
    "Malay": "Translate the given sentence into Malay language",
    "Malayalam": "Translate the given sentence into Malayalam language",
    "Manipuri": "Translate the given sentence into Manipuri language",
    "Marathi": "Translate the given sentence into Marathi language",
    "Mongolian": "Translate the given sentence into Mongolian language",
    "Nepali": "Translate the given sentence into Nepali language",
    "Norwegian": "Translate the given sentence into Norwegian language",
    "Odia": "Translate the given sentence into Odia language",
    "Pashto": "Translate the given sentence into Pashto language",
    "Persian": "Translate the given sentence into Persian language",
    "Polish": "Translate the given sentence into Polish language",
    "Portuguese": "Translate the given sentence into Portuguese language",
    "Punjabi": "Translate the given sentence into Punjabi language",
    "Romanian": "Translate the given sentence into Romanian language",
    "Russian": "Translate the given sentence into Russian language",
    "Santali": "Translate the given sentence into Santali language",
    "Sanskrit": "Translate the given sentence into Sanskrit language",
    "Scottish Gaelic": "Translate the given sentence into Scottish Gaelic language",
    "Serbian": "Translate the given sentence into Serbian language",
    "Sindhi": "Translate the given sentence into Sindhi language",
    "Sinhala": "Translate the given sentence into Sinhala language",
    "Slovak": "Translate the given sentence into Slovak language",
    "Slovenian": "Translate the given sentence into Slovenian language",
    "Spanish": "Translate the given sentence into Spanish language",
    "Swahili": "Translate the given sentence into Swahili language",
    "Swedish": "Translate the given sentence into Swedish language",
    "Tamil": "Translate the given sentence into Tamil language",
    "Telugu": "Translate the given sentence into Telugu language",
    "Thai": "Translate the given sentence into Thai language",
    "Turkish": "Translate the given sentence into Turkish language",
    "Ukrainian": "Translate the given sentence into Ukrainian language",
    "Urdu": "Translate the given sentence into Urdu language",
    "Uzbek": "Translate the given sentence into Uzbek language",
    "Vietnamese": "Translate the given sentence into Vietnamese language",
    "Welsh": "Translate the given sentence into Welsh language",
    "Zulu": "Translate the given sentence into Zulu language"
}
def language_translator(user_prompt,language):
    system_prompt=languages[language]
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=user_prompt
    )
    return response.text

demo=gr.Interface(
    fn=language_translator,
    inputs=[gr.Textbox(lines=4,placeholder="Enter the Sentence...",label="Translate Sentence"),
            gr.Dropdown(choices=list(languages.keys()),label="Select Language",value="English")],
    outputs=gr.Textbox(lines=10,label="Response"),
    title="Language Translator",
    description="Here you can translate the sentance with other languages"
)
demo.launch(debug=True)

# user_prompt="କୁକୁର ମାନେ ଇଂରାଜୀ ଭାଷାରେ କନ"
# language="English"
# output=language_translator(user_prompt,language)
# print(output)