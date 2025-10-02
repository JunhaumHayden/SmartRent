from pydantic import BaseModel
from typing import List, Optional

# --- Estrutura da Entrada de Dados do Formulário (Request Body) ---
# ATENÇÃO: Os campos foram ajustados para corresponder às features do modelo ML!
class PropertyFeatures(BaseModel):
    """Estrutura dos dados de entrada do Frontend, ajustada para o modelo ML."""
    city: str                       # Para futuro enriquecimento de dados (geocodificação)
    neighborhood: str               # Para futuro enriquecimento de dados (geocodificação)
    area_first_floor_sqm: float     # Corresponde à feature 'area_primeiro_andar'
    has_second_floor: bool          # Corresponde à feature 'existe_segundo_andar' (0 ou 1)
    bathrooms: int                  # Corresponde à feature 'quantidade_banheiros'
    kitchen_quality_excellent: bool # Corresponde à feature 'qualidade_da_cozinha_Excelente' (0 ou 1)

# --- Estrutura para uma Sugestão de Otimização ---
class Suggestion(BaseModel):
    """Detalhes de uma sugestão de otimização."""
    tip: str
    value_increase: float
    reason: Optional[str] = None

# --- Estrutura da Resposta Final da API (Response Body) ---
class PredictionResponse(BaseModel):
    """Estrutura da resposta JSON final para o Frontend."""
    price_prediction: float
    suggestions: List[Suggestion]