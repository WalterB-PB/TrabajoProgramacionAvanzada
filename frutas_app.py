import streamlit as st
import math

st.title("🍎 ¿Qué fruta es más parecida?")
st.write("Introduce las características de una fruta.")


peso = st.number_input("Peso (gramos)", value=180)
diametro = st.number_input("Diámetro (cm)", value=7.0)
dulzor = st.number_input("Dulzor (0 - 10)", value=8.0)


fruta_usuario = [peso, diametro, dulzor]
st.write("Vector de tu fruta:", fruta_usuario)

# Frutas conocidas          peso  diámetro  dulzor
manzana = [170, 7.0, 7]
banano  = [120, 5.0, 9]
naranja = [200, 8.0, 6]
pera    = [160, 6.5, 7.5]   # <-- nueva fruta

# Calculamos las distancias
distancia_manzana = math.sqrt(
    (fruta_usuario[0] - manzana[0])**2 +
    (fruta_usuario[1] - manzana[1])**2 +
    (fruta_usuario[2] - manzana[2])**2
)

distancia_banano = math.sqrt(
    (fruta_usuario[0] - banano[0])**2 +
    (fruta_usuario[1] - banano[1])**2 +
    (fruta_usuario[2] - banano[2])**2
)

distancia_naranja = math.sqrt(
    (fruta_usuario[0] - naranja[0])**2 +
    (fruta_usuario[1] - naranja[1])**2 +
    (fruta_usuario[2] - naranja[2])**2
)

distancia_pera = math.sqrt(
    (fruta_usuario[0] - pera[0])**2 +
    (fruta_usuario[1] - pera[1])**2 +
    (fruta_usuario[2] - pera[2])**2
)


st.subheader("Distancias")
st.write("🍎 Manzana:", distancia_manzana)
st.write("🍌 Banano:", distancia_banano)
st.write("🍊 Naranja:", distancia_naranja)
st.write("🍐 Pera:", distancia_pera)


distancias = {
    "🍎 Manzana": distancia_manzana,
    "🍌 Banano": distancia_banano,
    "🍊 Naranja": distancia_naranja,
    "🍐 Pera": distancia_pera
}

fruta_mas_parecida = min(distancias, key=distancias.get)

st.subheader("Resultado")
st.success(f"La fruta más parecida es: {fruta_mas_parecida}")
