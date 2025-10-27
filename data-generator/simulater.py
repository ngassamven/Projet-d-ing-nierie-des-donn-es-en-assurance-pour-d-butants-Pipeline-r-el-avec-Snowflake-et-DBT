from faker import Faker
import random
import time
from pymongo import MongoClient
import urllib.parse

# Identifiants MongoDB Atlas
username = "datengineer79_db_user"
password = urllib.parse.quote_plus("t085XLGOM471KeEv")  # encode les caractères spéciaux
cluster_url = "insurance.7hauqof.mongodb.net"  # Nom exact du cluster

# Connexion au cluster MongoDB Atlas
uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=insurance"
client = MongoClient(uri)

# Sélection de la base de données et des collections
db = client["insurance"]
customers_col = db["customers"]
claims_col = db["claims"]

print("✅ Connexion réussie à MongoDB Atlas ! Insertion des données en cours...\n")

fake = Faker()

while True:
    # Génération d'un client
    customer = {
        "customer_id": f"CUST-{random.randint(100, 999)}",
        "name": fake.name(),
        "state": fake.state_abbr(),
        "policy_type": random.choice(["Auto", "Home", "Health"])
    }

    # Génération d'une réclamation
    claim = {
        "claim_id": f"CLM-{random.randint(1000, 9999)}",
        "customer_id": customer["customer_id"],
        "date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
        "amount": round(random.uniform(100, 20000), 2),
        "claim_type": random.choice(["Accident", "Theft", "Fire"]),
        "is_fraud": random.random() < 0.05
    }

    # Insertion dans MongoDB
    customers_col.insert_one(customer)
    claims_col.insert_one(claim)

    print(f"✅ Claim {claim['claim_id']} ajouté pour le client {customer['customer_id']}")
    time.sleep(2)
