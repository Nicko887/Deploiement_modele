from shiny import App, render, ui

# Définition de la fonction serveur
def server(input, session):

    # Fonction pour afficher le texte de sortie
    @render.text
    def output_text():
        return f"Le prénom de l'utilisateur est: {input.prenom}"

    # Fonction pour afficher une image
    @render.image
    def output_image():
        # Charger l'image en fonction de la sélection de l'utilisateur
        if input.choix_image == "1":
            image_path = "image1.jpg"
        elif input.choix_image == "2":
            image_path = "image2.jpg"
        else:
            image_path = "image3.jpg"
        return read_image(image_path)

# Définition de l'interface utilisateur
app_ui = ui.page_fluid(
    # Titre de la page
    ui.panel_title("Application Shiny"),

    # En-tête de niveau 1
    ui.h1("Ceci est un titre de niveau 1"),

    # Champ de saisie pour le prénom
    ui.input_text("prenom", "Quel est votre prénom ?"),

    # Texte de sortie
    ui.output_text("output_text"),

    # Saut de ligne
    ui.br(),

    # Choix de l'image
    ui.select_input("choix_image", "Choisissez une image:",
                    choices=[("1", "Image 1"), ("2", "Image 2"), ("3", "Image 3")],
                    selected="1"),

    # Affichage de l'image
    ui.output_image("output_image")
)

# Création de l'application
app = App(app_ui, server)

# Exécution de l'application
app.run()
