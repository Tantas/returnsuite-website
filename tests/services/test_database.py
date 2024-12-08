from sqlalchemy import inspect

from returnsuite_website.services import database


def test_database_schema():
    database.create_all()
    inspector = inspect(database.engine)
    assert inspector.get_table_names() == [
        "contact_document_review",
        "contact_newsletter_subscription",
        "contact_request",
        "contact_waitlist",
    ]
    database.drop_all()
    inspector = inspect(database.engine)
    assert inspector.get_table_names() == []
