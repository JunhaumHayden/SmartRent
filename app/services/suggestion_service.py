from ..models.schemas import PropertyFeatures, Suggestion
from typing import List

class SuggestionService:
    def __init__(self):
        pass # Não precisa de inicialização complexa

    def generate_suggestions(self, features: PropertyFeatures, predicted_price: float) -> List[Suggestion]:
        """
        Gera sugestões de otimização de preço baseadas em regras de negócio simples.
        """
        suggestions = []

        # REGRA 1: Imóvel pequeno com potencial de valorização por qualidade (menos de 60m² e cozinha não excelente)
        if features.area_first_floor_sqm < 60 and not features.kitchen_quality_excellent:
            suggestions.append(Suggestion(
                tip="Upgrade na Cozinha (Qualidade Excelente)",
                value_increase=round(predicted_price * 0.12, 2), 
                reason="Cozinha de qualidade Excelente é um diferencial em apartamentos menores. O seu modelo prevê um aumento de +12%."
            ))

        # REGRA 2: Sem segundo andar, sugere reforma se o preço for baixo
        if not features.has_second_floor and predicted_price < 2500:
            suggestions.append(Suggestion(
                tip="Aproveitar Potencial Vertical",
                value_increase=round(predicted_price * 0.20, 2), 
                reason="Adicionar um segundo andar ou mezanino (se possível) aumenta significativamente a área útil."
            ))
            
        # REGRA 3: Apenas 1 banheiro, sugere mais se a área for grande
        if features.bathrooms == 1 and features.area_first_floor_sqm > 80:
             suggestions.append(Suggestion(
                tip="Adicionar Banheiro/Lavabo",
                value_increase=450.00,
                reason="Um segundo banheiro ou lavabo melhora o conforto em imóveis espaçosos."
            ))

        return suggestions