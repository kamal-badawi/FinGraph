
# Wichtiger Hinweis:
# footer_translations wurde durch ChatGpt generiert

def run_footer(language_index):
    import streamlit as st

    footer_translations = [
        "Created by Kamal Badawi, Yelda Öztürk, Hannah Andres and Aysenur Tekin",  # Englisch
        "Erstellt von Kamal Badawi, Yelda Öztürk, Hannah Andres und Aysenur Tekin",  # Deutsch
        "Creato da Kamal Badawi, Yelda Öztürk, Hannah Andres e Aysenur Tekin",  # Italienisch
        "Créé par Kamal Badawi, Yelda Öztürk, Hannah Andres et Aysenur Tekin",  # Französisch
        "Creado por Kamal Badawi, Yelda Öztürk, Hannah Andres y Aysenur Tekin",  # Spanisch
        "Criado por Kamal Badawi, Yelda Öztürk, Hannah Andres e Aysenur Tekin",  # Portugiesisch
        "Skapad av Kamal Badawi, Yelda Öztürk, Hannah Andres och Aysenur Tekin",  # Schwedisch
        "Opprettet av Kamal Badawi, Yelda Öztürk, Hannah Andres og Aysenur Tekin",  # Norwegisch
        "Oprettet af Kamal Badawi, Yelda Öztürk, Hannah Andres og Aysenur Tekin",  # Dänisch
        "Utworzone przez Kamal Badawi, Yelda Öztürk, Hannah Andres i Aysenur Tekin",  # Polnisch
        "Создано Камалем Бадави, Йельдой Озтюрк, Ханной Андрес и Айсенур Тэкин",  # Russisch
        "Створено Камалем Бадаві, Йельдою Озтюрк, Ганною Андрес і Айсенур Текін"  # Ukrainisch
    ]


    st.write('')
    st.write('')


    # Created by Kamal Badawi, Yelda Öztürk, Hannah Andres and Aysenur Tekin
    st.write(f'**{footer_translations[language_index]} ©**')