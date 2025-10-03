# app/services/gemini_service.py

import os
from google import genai
from google.genai.errors import APIError

class GeminiService:
    def __init__(self):
        # A chave de API será lida automaticamente da variável de ambiente GEMINI_API_KEY
        try:
            self.client = genai.Client()
            self.model_name = 'gemini-2.5-flash'
        except Exception as e:
            print(f"AVISO: Gemini Client não pôde ser inicializado. Verifique a GEMINI_API_KEY. Erro: {e}")
            self.client = None

    def generate_reason(self, tip: str, city: str, neighborhood: str) -> str:
        """Gera uma justificativa criativa e persuasiva usando o Gemini."""
        if not self.client:
            return "Análise de mercado não disponível (Erro de conexão com a IA)."

        prompt = (
            f"Você é um consultor imobiliário de elite. "
            f"Gere uma justificativa de 1 a 2 frases para a seguinte sugestão de otimização "
            f"em um imóvel em {neighborhood}, {city}. "
            f"Foco no impacto financeiro e na atratividade para locatários modernos. "
            f"Sugestão: '{tip}'. Apenas a justificativa."
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config={"temperature": 0.5} 
            )
            return response.text.strip().replace('\n', ' ')
        except APIError as e:
            return f"Erro na API Gemini: Falha ao gerar análise ({e})."
        except Exception:
            return "Erro desconhecido ao processar a resposta da IA."