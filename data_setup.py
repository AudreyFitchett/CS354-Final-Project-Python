import kagglehub
import pandas as pd
import os

def load_heart_data():
    """
    Downloads the Heart Disease dataset from Kaggle and finds the 
    correct CSV file regardless of nested folder structures.
    """
    print("--- Initializing Data Ingestion ---")
    
    try:
        # download dataset via Kagglehub
        # returns the local path where the files are stored
        path = kagglehub.dataset_download("kamilpytlak/personal-key-indicators-of-heart-disease")
        print(f"Source directory identified: {path}")
        
        # deep scan for CSV files using os.walk
        csv_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".csv"):
                    full_path = os.path.join(root, file)
                    csv_files.append(full_path)
        
        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {path}")

        # selection Logic
        file_path = next((f for f in csv_files if "2020" in f), csv_files[0])
        print(f"Targeting data file: {os.path.basename(file_path)}")
        
        # load into a Pandas DataFrame
        df = pd.read_csv(file_path)
        print(f"Data successfully ingested: {len(df)} rows detected.")
        
        return df

    except Exception as e:
        print(f"Error during data setup: {e}")
        raise

if __name__ == "__main__":
    heart_df = load_heart_data()
    
    # save the data locally so train_model.py can see it
    heart_df.to_csv("heart_2020_cleaned.csv", index=False)
    print("File saved to project directory: heart_2020_cleaned.csv")
    
    print("\n--- Quick Dataset Preview ---")
    print(heart_df.head())
