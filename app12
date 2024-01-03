import random
from google.cloud import firestore

# Replace 'your-project-id' with your Google Cloud project ID
project_id = 'your-project-id'

# Initialize Firestore client
db = firestore.Client(project=project_id)

def generate_random_machine_data():
    data = {
        'machine_name': f'A1Textile_Machine_{random.randint(1, 100)}',
        'production_capacity': random.randint(100, 1000),
        'location': f'A1Textile_Location_{random.randint(1, 10)}',
        'maintenance_score': random.uniform(0, 100),
        'category': f'Category_{random.choice(["Weaving", "Spinning", "Knitting"])}',
        'manufacturer': f'Manufacturer_{random.choice(["A1Machines", "TechTextile", "FabricMaster"])}'
    }
    return data

def upload_to_firestore(collection_name):
    # Reference to the Firestore collection
    collection_ref = db.collection(collection_name)

    # Generate a random number of documents (between 1 and 10)
    num_documents = random.randint(1, 10)

    for _ in range(num_documents):
        # Generate random machine data
        document_data = generate_random_machine_data()

        # Add the document to the collection
        collection_ref.add(document_data)

if __name__ == "__main__":
    # Set the collection name
    collection_name = 'A1Textile_machines'

    # Upload random machine data to Firestore each time the script is executed
    upload_to_firestore(collection_name)
