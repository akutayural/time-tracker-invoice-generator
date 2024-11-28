import datetime
from mongoengine import Document, DateTimeField, StringField


class Base(Document):
    meta = {"abstract": True}  # Base is abstract and won't create its own collection

    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)
    deleted_at = DateTimeField(default=None, null=True)

    def save(self, *args, **kwargs):
        """Override save to update `updated_at` timestamp automatically."""
        self.updated_at = datetime.datetime.utcnow()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted_at = datetime.datetime.utcnow()
        return self.save(*args, **kwargs)

    def is_deleted(self) -> bool:
        """Check if the document is marked as deleted."""
        return self.deleted_at is not None
