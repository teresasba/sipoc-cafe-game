
import streamlit as st
import pandas as pd
from datetime import datetime

def sipoc_metrics_game():
    st.set_page_config(page_title="Jeu Lean SIPOC & Indicateurs", layout="centered")
    st.title("🚀 Jeu Lean SIPOC & Indicateurs – Pensée Lean")

    with st.expander("🌟 Pourquoi le SIPOC est important – Cliquez pour être inspiré"):
        st.markdown("""
        En une seule page simple, un diagramme SIPOC vous offre une vue complète et structurée de votre processus :

        - **Il identifie tous vos Clients** — internes et externes — et vous rappelle que chaque action que vous entreprenez impacte l'expérience de quelqu'un.
        - **Il cartographie le vrai début et la vraie fin de votre travail** — en vous montrant que vous faites partie d'une chaîne de valeur plus grande.
        - **Il met en évidence les Entrées et les Sorties** qui soutiennent la qualité.
        - **Il vous connecte aux bons Indicateurs** — pour guider la performance de manière proactive.

        💡 Vous ne réalisez pas seulement des tâches — vous **créez de la valeur** pour vos collègues, vos clients, votre équipe, et votre organisation.

        💡 En comprenant le flux, les besoins et les indicateurs, vous êtes habilité à **construire de meilleurs résultats**, aujourd'hui et demain.

        **Le SIPOC n'est pas juste un outil.**  
        C'est une nouvelle façon de voir **le but derrière le processus, et les personnes derrière le but**.
        """)

    st.header("🎯 Votre Mission :")
    st.markdown("""
Comprendre le flux complet de votre processus.
Classer correctement les éléments dans le SIPOC.
Identifier les bons types d'indicateurs.
Reconnaître les Indicateurs Avancés (Leading) et Retardés (Lagging).
Découvrir l'impact réel de votre travail sur vos Clients et vos Collègues.
    """)

    player_name = st.text_input("👤 Entrez votre nom ou équipe :", key="player_name")

    with st.expander("📘 Glossaire – Cliquez pour ouvrir"):
        st.markdown("""
        ### 🧩 Éléments SIPOC
        - **Fournisseur (Supplier):** Personne, groupe ou organisation fournissant des entrées (interne ou externe).
        - **Entrée (Input):** Ressources nécessaires pour démarrer le processus (matériaux, informations, données).
        - **Processus (Process):** Actions qui transforment les entrées en sorties.
        - **Sortie (Output):** Produit ou service résultant du processus.
        - **Client (Customer):** Personne, groupe ou organisation recevant la sortie (interne ou externe).

        ### 📊 Types d'Indicateurs
        - **Indicateurs d'Entrée:** Mesurent la qualité ou la disponibilité des entrées.
        - **Indicateurs de Processus:** Mesurent les activités à l'intérieur du processus.
        - **Indicateurs de Sortie:** Mesurent les résultats immédiats du processus.
        - **Indicateurs de Résultat:** Mesurent l'impact final sur les clients.

        ### ⚡ Indicateurs Avancés (Leading) vs Retardés (Lagging)
        - **Indicateurs Avancés (Leading):** Basés sur les Entrées et Processus. Permettent une action proactive.
        - **Indicateurs Retardés (Lagging):** Basés sur les Sorties et Résultats. Mesurent les résultats après coup.

        ---
        Souvenez-vous :
        - Leading = Avertissement anticipé → Vous pouvez agir MAINTENANT.
        - Lagging = Après coup → Seulement des corrections réactives.
        """)

    scenario = st.radio("Sélectionnez votre scénario :", ["☕ Préparer un Café", "📞 Gérer un Appel Client"])

    if scenario == "☕ Préparer un Café":
        elements = {
            "Café moulu": "Entrée",
            "Eau": "Entrée",
            "Barista": "Fournisseur",
            "Tasse propre": "Entrée",
            "Mettre la moka sur le feu": "Processus",
            "Faire bouillir l'eau": "Processus",
            "Café chaud dans une tasse": "Sortie",
            "Client": "Client",
            "Moulin à café": "Fournisseur",
            "Allumer le feu": "Processus"
        }
    else:
        elements = {
            "Numéro de téléphone du client": "Entrée",
            "Données CRM client": "Entrée",
            "Équipe de saisie CRM interne": "Fournisseur",
            "Demande d'information du client": "Entrée",
            "Accéder au système CRM": "Processus",
            "Répondre à l'appel et vérifier le client": "Processus",
            "Problème résolu": "Sortie",
            "Mise à jour du ticket CRM": "Sortie",
            "Client (appelant)": "Client"
        }

    st.subheader("🧩 Classifiez chaque élément dans le SIPOC")
    total_score = 0
    results = []

    for item, correct_category in elements.items():
        guess = st.selectbox(f"Que représente '{item}' ?", ["Fournisseur", "Entrée", "Processus", "Sortie", "Client"], key=item)
        results.append({
            "Joueur": player_name,
            "Élément": item,
            "Votre Choix": guess,
            "Catégorie Correcte": correct_category,
            "Correct": guess == correct_category
        })
        if guess == correct_category:
            total_score += 2

    st.markdown("---")
    st.subheader("📊 Défi des Indicateurs : Avancé ou Retardé ?")

    metrics = {
        "Stabilité de la température de l'eau": "Avancé",
        "Note finale du goût du café": "Retardé",
        "Temps d'accès au CRM": "Avancé",
        "Taux de Résolution au Premier Appel": "Retardé",
        "Satisfaction Client (CSAT)": "Retardé",
        "Temps moyen de traitement (AHT)": "Avancé"
    }

    for metric, correct_type in metrics.items():
        guess_metric = st.radio(f"Classifiez l'indicateur : {metric}", ["Avancé", "Retardé"], key=metric)
        results.append({
            "Joueur": player_name,
            "Élément": metric,
            "Votre Choix": guess_metric,
            "Catégorie Correcte": correct_type,
            "Correct": guess_metric == correct_type
        })
        if guess_metric == correct_type:
            total_score += 1

    st.markdown("---")
    st.subheader("🏁 Score Final")
    st.markdown(f"### 🎯 Votre score total est : **{total_score}** points!")

    if player_name.strip():
        df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sipoc_metrics_results_{player_name}_{timestamp}.csv"
        st.success("📥 Vos résultats ont été enregistrés !")
        st.download_button("⬇ Télécharger vos résultats", data=df.to_csv(index=False), file_name=filename, mime="text/csv")

    st.markdown("---")
    st.subheader("🌟 Réflexion Finale : Votre Impact")
    st.markdown("""
    ✨ Maintenant, posez-vous la question :

    > **Connaissez-vous tous vos Clients ?**  
    > **Connaissez-vous vraiment l'impact de votre travail sur eux ?**

    ➡️ Commencez à poser ces questions.  
    ➡️ Commencez à voir au-delà des tâches.  
    ➡️ Commencez à construire de la valeur — avec conscience, avec but, avec cœur. 💖
    """)

sipoc_metrics_game()
