
import streamlit as st


st.set_page_config(page_title="Portfolio | Seydou Badji", page_icon="🌐", layout="wide")

with st.sidebar:
    st.image ("a.png" ,width=400)
    st.title("Seydou Badji")
    st.write("📍 **lac rose , Dakar, Sénégal**")
    st.write("📧 Email (badjiseydou8070@gmail.com)")
    st.write("📱 **+221 77 845 92 38**")


col_title, col_logo = st.columns([3, 1])
with col_title:
    st.title("Géomaticien & Développeur Web")
    st.markdown("##### *Fusionner l'intelligence spatiale et le développement moderne.*")


with st.container():
    st.write("---")
    st.subheader("🎯 Profil")
    st.info("""
    Experte en devenir alliant la précision de la **Géomatique** à la flexibilité du **Développement Web**. 
    Spécialisée en **Télédétection** et analyse de données spatiales, j'accompagne la transformation digitale 
    du territoire par la création de solutions cartographiques innovantes.
    """)



st.subheader("Formation")
    

st.markdown("### **BTS en Géomatique**")
st.caption("📍 CEDT G15 Dakar ")
st.write("""
        * Cartographie numérique avancée.
        * Systèmes d'Information Géographique (SIG).
        * Levés topographiques et traitement GNSS.
        """)


st.markdown("### **Bachelor Développement Web**")
st.caption("📍 UNSHK ")
st.write("""
        * Architecture MVC et intégration front-end.
        * Programmation Python pour le Web.
        * Gestion de bases de données spatiales.
        """)


st.subheader("Expertise Technique")
    

st.markdown("#### 🌍 SIG & Géo")
st.write("- QGIS / ArcGIS Pro")
st.write("- Télédétection (Sentinel/Landsat)")
st.write("- KoboToolbox / ODK")
        
    
st.markdown("#### 💻 Tech & Code")
st.write("- Python (Pandas, GeoPandas)")
st.write("- HTML / CSS / JS")
st.write("- Streamlit & Dashboards")
        
   
st.markdown("#### ⚙️ Outils")
st.write("- Suite Office (Expert)")
st.write("- Git / GitHub")
st.write("- Google Earth Engine")


st.subheader("Spécialisation : Télédétection")
st.success("""
    Analyse IA de l’occupation du sol : Dakar et périphérie
L’urbanisation fulgurante de Dakar et l’émergence du pôle de Diamniadio imposent un suivi automatisé par intelligence artificielle. Grâce au Deep Learning (notamment l'architecture U-Net), l'analyse d'images satellitaires (Sentinel ou Pléiades) permet de cartographier l'évolution du bâti avec une précision impossible à atteindre manuellement.

Ces outils traitent des volumes massifs de données pour distinguer les types d'habitats, suivre la disparition des zones agricoles (Niayes) et identifier les constructions en zones inondables. Malgré les défis locaux, comme la confusion spectrale entre le sable et les infrastructures, l'IA transforme la gestion urbaine : elle permet de passer d'un simple constat à une planification prédictive. C'est un levier stratégique pour adapter les services publics et renforcer la résilience de la capitale face aux enjeux environnementaux..
    """)
st.write("---")
st.write("✨ *Intéressé(e) par une collaboration ? N'hésitez pas à me contacter via la barre latérale.*")
