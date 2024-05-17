import customtkinter
import requests 
from openai import OpenAI

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("green") 

client = OpenAI(api_key="udsbdfb")

class requestsAPP(customtkinter.CTk):
    
    user_input = ""
    api_result = "" 
    sliderValue = ""
    content_system = ""
    temperature = 1
    historique_rep = [{'role': "system", 'content': 'Répond à chacune de mes questions comme si tu étais un monarque du 10ème siecle'}]

    
    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{680}")
                
        #créer une grille de 3 lignes et 3 colonnes
        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)
    
    
        # partie bouton
        self.buton_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0) 
        self.buton_frame.grid(row=0, column=1)
        
        self.button = customtkinter.CTkButton(master=self.buton_frame, text="Cliquez ici", command=self.update_user_input)
        self.button.grid()
        
        # partie champs texte
        self.text_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0) 
        self.text_frame.grid(row=0, column=0)

        self.system_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0) 
        self.system_frame.grid(row=1, column=0)
        
        self.user_text = customtkinter.CTkEntry(master=self.text_frame, height=10, width=800)
        self.user_text.grid()
        
        self.system_text = customtkinter.CTkEntry(master=self.system_frame, height=100, width=800)
        self.system_text.grid()
        
        # partie slider temperature
        self.temperature_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0) 
        self.temperature_frame.grid(row=2, column=1)

        self.labelSystem = customtkinter.CTkLabel(master=self.system_frame, text='Modification du systeme de réponse', width=200, corner_radius=0)
        self.labelSystem.grid()

        self.labelQuestion = customtkinter.CTkLabel(master=self.text_frame, text="Veuillez posé votre question", width=200, corner_radius=0)
        self.labelQuestion.grid()

        self.label = customtkinter.CTkLabel(master=self.temperature_frame, text=self.temperature, width=200, corner_radius=0)
        self.label.grid()
        
        self.slider = customtkinter.CTkSlider(master=self.temperature_frame, from_=0, to=2, number_of_steps=10, command=self.slider_event)
        self.slider.set(self.temperature)
        self.slider.grid()

        # partie resultat 
        self.result_frame = customtkinter.CTkFrame(self, width=8000, corner_radius=0) 
        self.result_frame.grid(row=2, column=0)
        
        self.result_box = customtkinter.CTkTextbox(master=self.result_frame, height=400, width=800)
        self.result_box.configure(state="disabled")
        self.result_box.grid(sticky="nsew" )

    def slider_event(self, value):
        self.temperature = round(value, 1)
        self.label.configure(text=self.temperature)
        

    def update_user_input(self):
        
        # self.result_box.configure(state="normal")
        # self.result_box.delete("0.0", "end")    
        # récupere le texte de l'utilisateur
        t = self.user_text.get()
        self.user_input = t
        self.historique_rep += [{'role': "user", 'content': self.user_input}]

        value_system = self.system_text.get()
        content_system = value_system
        # appeler l'api pokemon 
        try:
            if content_system != '' :
                self.historique_rep[0]['content'] = content_system
            else :
                self.historique_rep[0]['content'] = self.historique_rep[0]['content']
            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.historique_rep,
                temperature= self.temperature
            )
            resultat = completion.choices[0].message.content
            
            self.historique_rep += [{'role': "assistant", 'content': resultat}]
            self.result_box.configure(state="normal")
            self.result_box.insert("end", f'Moi : {self.user_input}\nOpenAI : {resultat}\n\n')
            self.result_box.configure(state="disabled")
            print( self.historique_rep[0]['content'] )
        except Exception as e:
            print(e)
            self.result_box.configure(state="normal")
            self.result_box.insert("0.0", "Erreur lors de la requete")
            self.result_box.configure(state="disabled")
        


if __name__ == "__main__":
    mon_instance = requestsAPP()    
    mon_instance.mainloop()