from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline...")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )

            logger.info("Recommendation Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing Recommendation Pipeline: {e}")
            raise CustomException("Failed to initialize the recommendation pipeline.", e)
        
    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received a query {query}")
            recommendation = self.recommender.get_recommendations(query)
            logger.info("Recommendation generated successfully.")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation: {e}")
            raise CustomException("Failed to get recommendati", e)


