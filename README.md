# Pipeline de Données d'Assurance en Temps Réel

[![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat&logo=dbt&logoColor=white)](https://www.getdbt.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Airbyte](https://img.shields.io/badge/Airbyte-615EFF?style=flat&logo=airbyte&logoColor=white)](https://airbyte.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)

## 📋 Table des Matières

- [Vue d'Ensemble](#-vue-densemble)
- [Architecture](#-architecture)
- [Stack Technique](#-stack-technique)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du Projet](#-structure-du-projet)
- [Installation](#-installation)
- [Guide Pas à Pas](#-guide-pas-à-pas)
- [Résultats](#-résultats)
- [Améliorations Futures](#-améliorations-futures)
- [Contact](#-contact)

## 🎯 Vue d'Ensemble

Ce projet démontre la construction d'un **pipeline de données en temps réel** pour le traitement des réclamations d'assurance. Il simule un environnement de production réaliste où les données de clients et de réclamations sont générées, ingérées, transformées et visualisées de manière automatisée.

### Objectifs

- **Éducatif** : Fournir un exemple concret d'architecture de données moderne
- **Pratique** : Utiliser des outils de niveau production
- **Complet** : Couvrir l'ensemble du cycle de vie des données
- **Réaliste** : Simuler des cas d'usage du secteur de l'assurance

### Cas d'Usage

- 📊 Suivi des réclamations d'assurance en temps réel
- 🔍 Détection des patterns de fraude potentielle
- 📈 Analyse des tendances par type de réclamation
- 💰 Calcul des montants moyens des sinistres
- 📅 Génération de rapports mensuels automatisés

## 🏗️ Architecture

### Flux de Données
```
┌─────────────┐       ┌──────────┐       ┌─────────────┐       ┌──────────┐
│   MongoDB   │──────▶│ Airbyte  │──────▶│  Snowflake  │──────▶│ Power BI │
│   (OLTP)    │       │  (ETL)   │       │   (OLAP)    │       │  (BI)    │
└─────────────┘       └──────────┘       └──────┬──────┘       └──────────┘
                                                 │
                                                 │
                                          ┌──────▼──────┐
                                          │     DBT     │
                                          │    (SQL)    │
                                          └─────────────┘
```

### Architecture OLTP vs OLAP

- **OLTP (MongoDB)** : Transactions en temps réel, opérations CRUD
- **Transfer (Airbyte)** : Ingestion et synchronisation automatique
- **OLAP (Snowflake)** : Entrepôt analytique, requêtes complexes
- **Transformation (DBT)** : Nettoyage et modélisation des données
- **Visualisation (Power BI)** : Dashboards et rapports interactifs

## 🛠️ Stack Technique

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| **Base OLTP** | MongoDB | Stockage transactionnel NoSQL |
| **ETL/ELT** | Airbyte | Ingestion et synchronisation |
| **Data Warehouse** | Snowflake | Entrepôt de données cloud |
| **Transformation** | DBT | Transformations SQL |
| **Visualisation** | Power BI | Tableaux de bord |
| **Génération** | Python (Faker) | Simulation de données |

## ✨ Fonctionnalités

### Génération de Données
- ✅ Création automatique de clients fictifs réalistes
- ✅ Génération de réclamations avec montants cohérents
- ✅ Types variés : automobile, santé, habitation
- ✅ Indicateurs de fraude potentielle

### Pipeline ETL
- ✅ Synchronisation automatique MongoDB → Snowflake
- ✅ Détection des changements incrémentaux
- ✅ Gestion des erreurs avec retry automatique
- ✅ Logs détaillés pour monitoring

### Transformations
- ✅ Modèles staging : nettoyage des données brutes
- ✅ Modèles analytics : agrégations et KPIs
- ✅ Tests de qualité de données
- ✅ Documentation automatique

### Visualisations
- ✅ Dashboard réclamations en temps réel
- ✅ Analyse des fraudes
- ✅ Tendances mensuelles
- ✅ KPIs interactifs

## 📁 Structure du Projet
```
insurance-pipeline/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── data_generation/              # Scripts Python
│   ├── simulator.py              # Générateur de données
│   └── requirements.txt
│
├── dbt/                          # Projet DBT
│   └── models/
│       ├── staging/              # Modèles de nettoyage
│       │   ├── stg_customers.sql
│       │   ├── stg_claims.sql
│       │   └── source.yml
│       └── analytics/            # Modèles d'agrégation
│           └── claims_summary.sql
│
├── snowflake/                    # Scripts SQL
│   └── setup.sql
│
└── powerbi/                      # Dashboards
    └── insurance_dashboard.pbix
```

## 🚀 Installation

### Prérequis

- **MongoDB Atlas** : Compte gratuit (M0)
- **Snowflake** : Trial 30 jours gratuit
- **Airbyte** : Installation locale ou cloud
- **Power BI Desktop** : Gratuit
- **Python 3.8+**
- **DBT CLI**

### Étape 1 : MongoDB Setup
```bash
# 1. Créer un cluster sur MongoDB Atlas
# 2. Récupérer la connection string
# 3. Installer les dépendances Python

cd data_generation
pip install -r requirements.txt

# 4. Générer les données
python simulator.py --customers 1000 --claims 5000
```

### Étape 2 : Configuration Snowflake
```sql
-- Créer la database
CREATE DATABASE INSURANCE_DB;

-- Créer les schemas
CREATE SCHEMA INSURANCE_DB.RAW;
CREATE SCHEMA INSURANCE_DB.STAGING;
CREATE SCHEMA INSURANCE_DB.ANALYTICS;

-- Créer le warehouse
CREATE WAREHOUSE COMPUTE_WH 
WITH WAREHOUSE_SIZE = 'XSMALL';
```

### Étape 3 : Configuration Airbyte

1. Installer Airbyte localement :
```bash
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
docker-compose up
```

2. Accéder à l'interface : http://localhost:8000
3. Créer la connexion MongoDB → Snowflake
4. Configurer la synchronisation (fréquence : 1 heure)

### Étape 4 : DBT Setup
```bash
# Installer DBT
pip install dbt-snowflake

# Configurer profiles.yml avec vos credentials

# Lancer les transformations
dbt run

# Tester la qualité des données
dbt test
```

### Étape 5 : Power BI

1. Ouvrir Power BI Desktop
2. Se connecter à Snowflake
3. Importer les tables analytics
4. Créer les visualisations

## 📚 Guide Pas à Pas

### 1. Génération de Données (15 min)

Le script Python génère des données JSON réalistes :
```python
# Exemple de données générées
{
  "customer_id": "c_001",
  "name": "Jean Dupont",
  "email": "jean.dupont@email.com",
  "registration_date": "2024-01-15"
}

{
  "claim_id": "cl_001",
  "customer_id": "c_001",
  "claim_type": "automobile",
  "amount": 2500.00,
  "status": "approved",
  "is_fraud": false,
  "claim_date": "2024-10-20"
}
```

### 2. Modèles DBT Créés

#### Staging : `stg_claims.sql`
```sql
SELECT
    _id AS claim_id,
    customer_id,
    claim_type,
    amount::DECIMAL(10,2) AS amount,
    status,
    is_fraud,
    claim_date::DATE AS claim_date,
    DATE_TRUNC('month', claim_date) AS claim_month
FROM {{ source('raw', 'claims') }}
WHERE amount > 0
```

#### Analytics : `claims_summary.sql`
```sql
SELECT
    claim_month,
    claim_type,
    COUNT(*) AS total_claims,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount,
    SUM(CASE WHEN is_fraud THEN 1 ELSE 0 END) AS fraud_count,
    ROUND(SUM(CASE WHEN is_fraud THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100, 2) AS fraud_rate_pct
FROM {{ ref('stg_claims') }}
GROUP BY claim_month, claim_type
ORDER BY claim_month DESC
```

## 📊 Résultats

### Métriques Clés

| Métrique | Description |
|----------|-------------|
| **Total Claims** | Nombre total de réclamations |
| **Average Amount** | Montant moyen par réclamation |
| **Fraud Rate** | Taux de fraude détecté |
| **Claims by Type** | Répartition par catégorie |
| **Monthly Trend** | Évolution mensuelle |

### Dashboard Power BI

Le dashboard inclut :
- 📈 KPI Cards (Total, Moyenne, Fraude)
- 📊 Line Chart (Évolution temporelle)
- 📊 Bar Chart (Réclamations par type)
- 🔍 Table de détection de fraude

## 🔮 Améliorations Futures

### Version 2.0

- [ ] **Streaming Temps Réel** avec Apache Kafka
- [ ] **Machine Learning** pour prédiction de fraude
- [ ] **Orchestration** avec Apache Airflow
- [ ] **CI/CD** avec GitHub Actions
- [ ] **Data Quality** avec Great Expectations
- [ ] **API REST** pour accès aux données

### Idées Supplémentaires

- Notifications Slack sur événements critiques
- Support multi-tenant
- Intégration Tableau/Looker
- Version containerisée complète

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📧 Contact

**Venceslas Osée Ngassam Kate** - Data Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/venceslas-osee-ngassam-kate-data-engineer)

**Lien du Projet** : [https://github.com/ngassamven/Projet-d-ing-nierie-des-donn-es-en-assurance-pour-d-butants-Pipeline-r-el-avec-Snowflake-et-DBT](https://github.com/ngassamven/Projet-d-ing-nierie-des-donn-es-en-assurance-pour-d-butants-Pipeline-r-el-avec-Snowflake-et-DBT)

## 🙏 Remerciements

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Snowflake](https://www.snowflake.com/)
- [Airbyte](https://airbyte.com/)
- [DBT Labs](https://www.getdbt.com/)
- [Faker](https://faker.readthedocs.io/)
- La communauté Data Engineering

---

**⭐ Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile !**

*Fait avec ❤️ pour la communauté Data Engineering*
