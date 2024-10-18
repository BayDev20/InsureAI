import pandas as pd
from app import create_app, db
from app.models import InsuranceRecord

def import_csv_to_db(csv_file):
    """
    Imports data from a CSV file into the database.
    
    :param csv_file: Path to the CSV file containing insurance data.
    """
    app = create_app()
    with app.app_context():
        # Read the CSV file
        df = pd.read_csv(csv_file)
        # Iterate through each row and create InsuranceRecord objects
        for _, row in df.iterrows():
            record = InsuranceRecord(
                age=row['age'],
                sex=row['sex'],
                bmi=row['bmi'],
                children=row['children'],
                smoker=row['smoker'],
                region=row['region'],
                charges=row['charges']
            )
            db.session.add(record)
        # Commit all records to the database
        db.session.commit()
    print("Data import completed.")

if __name__ == "__main__":
    import_csv_to_db('data/insurance.csv')
