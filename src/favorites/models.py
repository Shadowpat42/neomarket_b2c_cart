import uuid
from django.db import models


class FavoriteItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(db_index=True)
    product_id = models.UUIDField(db_index=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favorite_items'
        unique_together = ('user_id', 'product_id')
        ordering = ['-added_at']

    def __str__(self):
        return f'{self.user_id} -> {self.product_id}'