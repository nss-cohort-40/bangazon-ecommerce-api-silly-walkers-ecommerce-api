from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from .payment_type import PaymentType
from .customer import Customer


class Order(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment_type = models.ForeignKey(
        PaymentType, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField()
