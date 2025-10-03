<h1 align="center">  SmartRent Estimator API </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=Em%20Desenvolvimento&color=GREEN&style=for-the-badge"/>
</p>

<p align="center">
  <em>✨ Porque precificar aluguel deveria ser mais <strong>ciência de dados</strong> e menos <strong>bola de cristal</strong> 🔮</em>
</p>

---

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-1.10%2B-blue?logo=pydantic)](https://pydantic.dev/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.1%2B-F7931E?logo=scikit-learn)](https://scikit-learn.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.22%2B-purple?logo=python)](https://www.uvicorn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/mit/)
[![Made with Love](https://img.shields.io/badge/Made%20with-💖-red)]()
[![Magic](https://img.shields.io/badge/Magic-Math%20%26%20Code-purple)](https://www.youtube.com/watch?v=3o1_1zGQ9K4)

[![GitHub Repo stars](https://img.shields.io/github/stars/JunhaumHayden/SmartRent?style=social)](https://github.com/JunhaumHayden/SmartRent)
[![GitHub forks](https://img.shields.io/github/forks/JunhaumHayden/SmartRent?style=social)](https://github.com/JunhaumHayden/SmartRent/fork)
[![GitHub watchers](https://img.shields.io/github/watchers/JunhaumHayden/SmartRent?style=social)](https://github.com/JunhaumHayden/SmartRent/watchers)

</div>

---

## 🏗️ Sobre o Projeto

Imagine um corretor de imóveis que:
- lê os dados da casa 🏡  
- roda um modelo de machine learning 🤖  
- e cospe um preço justo em milissegundos 💸⚡

É isso que a **SmartRent Estimator API** faz.  

> Proprietários param de subvalorizar imóveis.  
> Inquilinos encontram custo-benefício real.  
> E todo mundo economiza tempo, dinheiro e neurônios. 🧠✨

---
## ✨ Features

- 📈 **Predição inteligente** do preço de aluguel com base nas características do imóvel  
- 🛠️ **Sugestões automáticas** para valorizar propriedades  
- 🚀 API RESTful turbinada com FastAPI

---

## 🧰 Requisitos

- 🐍 Python 3.11+
- 📦 pip

---
## Instalação

```bash
pip install -r requirements.txt
``` 
###  Ambiente Local
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
### Docker
Build and run the container:
```bash
docker build -t smartrent-backend .
docker run -p 8000:8000 smartrent-backend
```

## Uso
Endpoint
```bash
POST /predict
```
Exemplo de Endpoint local:
```bash
http://127.0.0.1:8000/predict
```

Request Body
```json
{
  "city": "São Paulo",
  "neighborhood": "Pinheiros",
  "area_first_floor_sqm": 75.5,
  "has_second_floor": true,
  "bathrooms": 2,
  "kitchen_quality_excellent": true
}
````
Response
```json
{
    "price_prediction": 1755.0,
    "suggestions": []
}
```
```json
{
    "price_prediction": 1755.0,
    "suggestions": [
        {
            "tip": "Aproveitar Potencial Vertical",
            "value_increase": 351.0,
            "reason": "Adicionar um segundo andar ou mezanino (se possível) aumenta significativamente a área útil."
        }
    ]
}
```
---

## Estrutura do Projeto
```bash
📂 app/
 ├── main.py          # Ponto de entrada FastAPI
 ├── models/          # Schemas & Estimator
 └── services/        # Sugestões inteligentes
📝 requirements.txt   # Dependências Python
🐳 Dockerfile         # Configuração do container
```
---

##  Licença

MIT — ou seja: use, quebre, refaça, mas me cite se for ficar famoso com isso 😎

---

🧙‍♂️ Autores
<table> <tr> <td align="center"> <a href="https://github.com/JunhaumHayden"> <img src="https://avatars.githubusercontent.com/u/183040803?v=4" width="115"/><br> <sub><b>Lucas Marisco</b></sub> </a> </td> <td align="center"> <a href="https://github.com/JunhaumHayden"> <img src="https://avatars.githubusercontent.com/u/79289647?v=4" width="115"/><br> <sub><b>Carlos Hayden</b></sub> </a> </td> </tr> </table>
<p align="center"> <em>🧠💻 Built with data, code & caffeine.<br> May the <strong>rent</strong> be ever in your favor.</em> ☕✨ </p>
