from sqlalchemy import create_engine

def get_conn():
    engine = create_engine("cockroachdb://admin100:t3OlQVK3l2L5J9WNkk2wOA@ecloud-16053.8nj.gcp-europe-west1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full" )
    print("Connection created")
    return engine
