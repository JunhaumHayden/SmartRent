from fastapi import FastAPI, HTTPException
from .models.schemas import PropertyFeatures, PredictionResponse
from .models.estimator_model import EstimatorModel
from .services.suggestion_service import SuggestionService

# Inicialização do FastAPI
app = FastAPI(title="SmartRent Estimator API")

# Inicialização dos serviços (o modelo será carregado apenas uma vez)
try:
    estimator = EstimatorModel()
    suggester = SuggestionService()
except Exception as e:
    # Se o modelo não carregar, a API deve indicar o erro
    print(f"ERRO: Não foi possível carregar o modelo ou serviços: {e}")
    # Nota: Em um ambiente de produção, você pararia o app. Aqui, vamos permitir que continue com o modelo mockado.


@app.post("/predict", response_model=PredictionResponse)
def predict_rent_price(features: PropertyFeatures):
    """
    Recebe as características do imóvel, retorna a previsão de preço e sugestões.
    """
    try:
        # 1. Previsão do Preço (o modelo lida com o enriquecimento)
        predicted_price = estimator.predict(features)
        
        # 2. Geração das Sugestões
        suggestions = suggester.generate_suggestions(features, predicted_price)
        
        # 3. Retorno da Resposta Formatada
        return PredictionResponse(
            price_prediction=predicted_price,
            suggestions=suggestions
        )
        
    except Exception as e:
        # Captura de erro genérica e retorna um erro 500
        raise HTTPException(status_code=500, detail=f"Erro interno no processamento: {e}")