from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the Anime Recommendation Pipeline...")

        # Load the anime data
        data_loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = data_loader.load_and_process()

        # Build and save the vector store
        vector_store_builder = VectorStoreBuilder(
            csv_path=processed_csv,
            persist_dir="chroma_db"
        )
        vector_store_builder.build_and_save_vector_store()

        logger.info("Vectore store built successfully.")
    except Exception as e:
            logger.error(f"Error executing Recommendation Pipeline: {e}")
            raise CustomException("Failed to executing the recommendation pipeline.", e)
    
if __name__ == "__main__":
    main()