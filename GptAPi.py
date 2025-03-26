from openai import OpenAI
from dotenv.main import load_dotenv
import os
import random

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class GPT:
    def __init__(self, design_data):
        self.client = OpenAI()
        self.services = design_data.get("service").split(", ")
        self.service = random.choice(self.services)
        self.campaign = design_data.get("campaign")
        self.lang = design_data.get("lang")
        self.SYSTEM_MESSAGE = f"As a system, you can generate eye-catching content for social networks. Always respond in {self.lang}"
        self.ASSISTANT_MESSAGE = "As an assistant, you'll be a community manager and help me generate engaging content for social media. Don't comment, just follow the instructions. And don't forget: DON'T COMMENT."

    def create_message(self, role, content):
        return {"role": role, "content": content}

    def generate_response(self, model, messages, temperature=1):
        response = self.client.chat.completions.create(
            model=model, messages=messages, temperature=temperature
        )
        res = response.choices[0].message.content
        clean_response = (
            res.replace("'", " ")
            .replace("\n", " ")
            .replace("```html", " ")
            .replace("```", " ")
        )
        return clean_response

    # ============================= OSCEOLA METHODS ==============================


    def copy_osceola(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create compelling text for {theme}. The text should be compelling for the company's social media channels, focusing on the service's benefits and inviting people to take advantage of the service with two strategic emojis at the end. Also, create eight viral and engaging hashtags with the information in the text. The text should be {characters} long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def theme_osceola(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def document_title_osceola(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Based on this: {theme}, provide a short, impactful word that summarizes the benefit of the service.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def firts_comment_osceola(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create a short and engaging first comment on {theme}. The comment should sound natural and authentic, as if it's coming from a real person, without seeming spammy. It's important to keep in mind that the comment is coming directly from the company, so it should be engaging to encourage people to comment. You should subtly encourage interaction with a question or a friendly comment. Avoid repetitive phrases and make it feel personal. Use only an emoji at the end if appropriate. The comment should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")



    # ============================= QUICK CLEANING METHODS ==============================

    def copy_quick_cleaning(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create compelling text for {theme}. The text should be compelling for the company's social media channels, focusing on the service's benefits and inviting people to take advantage of the service with two strategic emojis at the end. Also, create eight viral and engaging hashtags with the information in the text. The text should be {characters} long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def theme_quick_cleaning(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def document_title_quick_cleaning(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Based on this: {theme}, provide a short, impactful word that summarizes the benefit of the service.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def firts_comment_quick_cleaning(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create a short and engaging first comment on {theme}. The comment should sound natural and authentic, as if it's coming from a real person, without seeming spammy. It's important to keep in mind that the comment is coming directly from the company, so it should be engaging to encourage people to comment. You should subtly encourage interaction with a question or a friendly comment. Avoid repetitive phrases and make it feel personal. Use only an emoji at the end if appropriate. The comment should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    # # ============================= ELITE SPA METHODS ==============================
    
    def copy_elite_spa(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create compelling copy for {theme}. The copy should be compelling for the company's social media, focusing on the key benefits of the service, with a clear call to action, and two strategic emojis at the end. Also, create eight viral and engaging hashtags with the information in the text. The text should be {characters} long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def theme_elite_spa(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def document_title_elite_spa(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Based on this: {theme}, provide a short, impactful word that summarizes the benefit of the service.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
        
    def firts_comment_elite_spa(self, theme, characters=30):        
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create a short and engaging first comment on {theme}. The comment should sound natural and authentic, as if it's coming from a real person, without seeming spammy. It's important to keep in mind that the comment is coming directly from the company, so it should be engaging to encourage people to comment. You should subtly encourage interaction with a question or a friendly comment. Avoid repetitive phrases and make it feel personal. Use only an emoji at the end if appropriate. The comment should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        

    # ============================= LOPEZ & LOPEZ ABOGADOS  ==============================
    
    def copy_lopez_abogados(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE) 
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Write professional and concise copy about {theme} related to the firm López & López Abogados (it's not necessary to mention the firm, just for context). The text should highlight the legal benefits of the service, convey trust and expertise, and conclude with two relevant emojis that maintain a formal tone. Focus on the specific topic of legal services, ensuring the copy reflects the firm's legal expertise. Also, include eight relevant hashtags relevant to the content. The text should not exceed {characters} characters.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        )
        
    def theme_lopez_abogados(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should evoke trust, seriousness, and professionalism.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    
    def document_title_lopez_abogados(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Based on this: {theme}, provide a short, impactful word that summarizes the benefit of the service. In accordance with **professional legal language**.",
        )        
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")


    def firts_comment_lopez_abogados(self, theme, characters=90):
        
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create a formal and authoritative first comment about {theme}. The comment should reflect the seriousness of a professional law firm, express respect, and subtly invite interaction through a thoughtful legal comment or question. Avoid informal phrases. Conclude with an appropriate legal emoji. Maximum {characters} characters."
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

        
    # ============================= BOTÁNICAS MÉTODOS ==============================
    

    def theme_botanica(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Dado el siguiente servicio: {self.service}, proporcione un tema que capture la esencia del servicio. El tema debe ser atractivo, relevante e impactante.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def copy_botanica(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Crea un texto llamativo y persuasivo sobre {theme}, diseñado específicamente para redes sociales dentro del mundo esotérico y espiritual(los servicios se conectan con la santeria, brujos, amarres, etc). Resalta los beneficios místicos y transformadores de este servicio o producto con un tono envolvente que conecte con la audiencia. Incluye una llamada a la acción clara y poderosa que invite a la interacción. Usa dos emojis estratégicos al final del texto, justo antes de los hashtags. Además, genera ocho hashtags virales y atractivos alineados con la temática. El texto debe tener {characters} caracteres.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def document_title_botanica(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"En base a este servicio esotérico {theme}, proporciona una sola palabra corta e impactante que resuma su beneficio principal. Sin emojis",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def firts_comment_botanica(self, theme, characters=30):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera un comentario breve y auténtico sobre {theme}, diseñado para incentivar la interacción en redes sociales. El comentario debe sonar natural y cercano, evitando frases repetitivas o genéricas. Debe reflejar el tono espiritual y místico del negocio, invitando a los seguidores a dejar sus inquietudes, compartir sus experiencias o etiquetar a un amigo. No debe parecer spam, sino un mensaje atractivo que motive la conversación (sin hashtags). Usa solo un emoji si es necesario y asegúrate de que el comentario tenga {characters} caracteres.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")

