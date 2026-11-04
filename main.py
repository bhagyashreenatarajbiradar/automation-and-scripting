from file_organizer.organizer import FileOrganizer
from utils.logger import setup_logger


logger = setup_logger()


INPUT_FOLDER = "data/input"
OUTPUT_FOLDER = "data/output"


logger.info("File Organizer started")


organizer = FileOrganizer(
    INPUT_FOLDER,
    OUTPUT_FOLDER
)

organizer.organize_files()


logger.info("File Organizer completed")