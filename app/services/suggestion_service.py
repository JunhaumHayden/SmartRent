# app/services/suggestion_service.py (CONTEÚDO FINAL)

from ..models.schemas import PropertyFeatures, Suggestion
from typing import List
from .gemini_service import GeminiService # <--- Nova Importação

class SuggestionService:
    def __init__(self):
        # Inicializa o serviço Gemini
        self.gemini_service = GeminiService()

    def generate_suggestions(self, features: PropertyFeatures, predicted_price: float) -> List[Suggestion]:
        """
        Gera sugestões de otimização de preço baseadas em regras de negócio simples,
        com justificativas geradas pelo Gemini.
        """
        suggestions = []

        # Variáveis de Localização para o Gemini
        city = features.city
        neighborhood = features.neighborhood

        # --- REGRA 1: Upgrade na Cozinha ---
        if features.area_first_floor_sqm < 60 and not features.kitchen_quality_excellent:
            tip = "Upgrade na Cozinha (Qualidade Excelente)"
            reason = self.gemini_service.generate_reason(tip, city, neighborhood) # <--- Chamada ao Gemini
            suggestions.append(Suggestion(
                tip=tip,
                value_increase=round(predicted_price * 0.12, 2), 
                reason=reason
            ))

        # --- REGRA 2: Aproveitar Potencial Vertical ---
        if not features.has_second_floor and predicted_price < 2500:
            tip = "Aproveitar Potencial Vertical (Mezanino/Segundo Andar)"
            reason = self.gemini_service.generate_reason(tip, city, neighborhood) # <--- Chamada ao Gemini
            suggestions.append(Suggestion(
                tip=tip,
                value_increase=round(predicted_price * 0.20, 2), 
                reason=reason
            ))
            
        # --- REGRA 3: Adicionar Banheiro/Lavabo ---
        if features.bathrooms == 1 and features.area_first_floor_sqm > 80:
             tip = "Adicionar Banheiro/Lavabo"
             reason = self.gemini_service.generate_reason(tip, city, neighborhood) # <--- Chamada ao Gemini
             suggestions.append(Suggestion(
                tip=tip,
                value_increase=450.00,
                reason=reason
            ))

        return suggestions