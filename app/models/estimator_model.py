import joblib
import pandas as pd
from geopy.geocoders import Nominatim
from ..models.schemas import PropertyFeatures
import os

# Define o caminho para o modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'trained_model.pkl')

class EstimatorModel:
    def __init__(self):
        print(f"Carregando modelo de: {MODEL_PATH}")
        try:
            self.model = joblib.load(MODEL_PATH)
            # Nomes das features esperadas pelo modelo
            self.expected_features = ['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'qualidade_da_cozinha_Excelente']
            print(f"Modelo carregado com sucesso. Features esperadas: {self.expected_features}")
        except FileNotFoundError:
            print("ERRO: O arquivo do modelo NÃO foi encontrado. Usando previsão mockada.")
            self.model = None
            self.expected_features = [] # Sem features se mockado
        except Exception as e:
            print(f"ERRO ao carregar o modelo: {e}. Usando previsão mockada.")
            self.model = None
            self.expected_features = []

        # Inicializa o geocoder (manter para enriquecimento futuro)
        self.geolocator = Nominatim(user_agent="smartrent_estimator_app")

    def _geocode_and_enrich(self, features: PropertyFeatures) -> dict:
        """
        Pré-processa, enriquece e mapeia os dados para as features esperadas pelo modelo.
        """
        # 1. Preparação dos dados para o modelo
        data_for_model = {}

        # Adiciona a constante (Intercepto) - Fundamental para modelos OLS/statsmodels
        data_for_model['const'] = 1.0

        # Mapeamento e Feature Engineering
        data_for_model['area_primeiro_andar'] = features.area_first_floor_sqm
        # Converte booleano (True/False) para float (1.0/0.0)
        data_for_model['existe_segundo_andar'] = 1.0 if features.has_second_floor else 0.0
        data_for_model['quantidade_banheiros'] = features.bathrooms
        # Criação da Dummy Variable para qualidade_da_cozinha_Excelente
        data_for_model['qualidade_da_cozinha_Excelente'] = 1.0 if features.kitchen_quality_excellent else 0.0

        # 2. Enriquecimento de Dados (A ser implementado aqui, se necessário)

        return data_for_model

    def predict(self, features: PropertyFeatures) -> float:
        """
        Prepara os dados e realiza a previsão.
        """
        # 1. Enriquecimento/Pre-processamento
        processed_data = self._geocode_and_enrich(features)

        # 2. Converte para o formato de entrada do modelo (DataFrame)
        # É CRUCIAL passar `columns=self.expected_features` para manter a ordem correta
        df = pd.DataFrame([processed_data], columns=self.expected_features)

        # 3. Previsão
        if self.model:
            try:
                prediction = self.model.predict(df)[0]
            except Exception as e:
                print(f"Erro na previsão do modelo: {e}")
                prediction = -1.0
        else:
            # Previsão Mockada (fallback)
            prediction = (features.area_first_floor_sqm * 10) + (features.bathrooms * 500)

        # Garante que o valor é positivo e arredonda
        return round(max(0, prediction), 2)