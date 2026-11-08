from src.data_loader import load_dataset
from src.ocr_regex import run_ocr_and_regex
from src.fuzzy_matching import apply_fuzzy_matching

def main():
    print("Starting Invoice Processing Pipeline...")
    
    # Member 2: Load the dataset
    print("Loading dataset...")
    invoices = load_dataset("data/")
    
    # Member 3 (You): Run baseline OCR and Regex validation
    print("Running OCR and Regex validation...")
    ocr_results = run_ocr_and_regex(invoices)
    
    # Member 4: Apply fuzzy matching and layout rules
    print("Applying fuzzy matching and post-processing...")
    final_results = apply_fuzzy_matching(ocr_results)
    
    print("Pipeline execution complete. Check the outputs/ directory.")

if __name__ == "__main__":
    main()