from file_organizer.watcher import start_watching


INPUT_FOLDER = "data/input"
OUTPUT_FOLDER = "data/output"


start_watching(
    INPUT_FOLDER,
    OUTPUT_FOLDER
)