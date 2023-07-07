from os import environ

from google.cloud import firestore

environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../app/serviceAccount.json"

db = firestore.Client()

ADDED_USER_PROPERTIES = {
    'queries': 0,
    'quota': 10,
    'active': True,
}
DB_BATCH_LIMIT = 500


def enable_counting_queries():
    db_batch = db.batch()
    users = db.collection('users').limit(DB_BATCH_LIMIT).stream()
    counter = 0
    for user in users:
        db_batch.update(user.reference, ADDED_USER_PROPERTIES)
        counter += 1
    db_batch.commit()
    if counter >= DB_BATCH_LIMIT:
        enable_counting_queries()


enable_counting_queries()
