import customtkinter
import requests 

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("green")  

class requestsAPP(customtkinter.CTk):
    
    user_input = ""
    api_result = ""
   
    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{580}")
        
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
        
        self.user_text = customtkinter.CTkEntry(master=self.text_frame, height=10, width=800)
        self.user_text.grid()
        
        
        # partie resultat 
        self.result_frame = customtkinter.CTkFrame(self, width=8000, corner_radius=0) 
        self.result_frame.grid(row=1, column=0)
        
        self.result_box = customtkinter.CTkTextbox(master=self.result_frame, height=400, width=800)
        self.result_box.configure(state="disabled")
        self.result_box.grid(sticky="nsew" )
       
    def update_user_input(self):
        
        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")    
        # récupere le texte de l'utilisateur
        t = self.user_text.get()
        self.user_input = t
        # appeler l'api pokemon 
        try:
            self.api_result = requests.get("https://pokeapi.co/api/v2/pokemon/" + self.user_input ).json()
            self.result_box.configure(state="normal")
            self.result_box.insert("0.0", self.api_result["abilities"])
            self.result_box.configure(state="disabled")
            print( self.api_result )
        except:
            self.result_box.configure(state="normal")
            self.result_box.insert("0.0", "Erreur lors de la requete")
            self.result_box.configure(state="disabled")
        


if __name__ == "__main__":
    mon_instance = requestsAPP()    
    mon_instance.mainloop()