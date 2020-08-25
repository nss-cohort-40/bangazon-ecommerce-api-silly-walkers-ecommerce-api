from django.db import models
# from customer import Customer

class PaymentType(models.Model):
    merchant_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    expiration_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

class Meta:
    verbose_name = ("paymenttype")
    verbose_name_plural = ("paymenttypes")

def __str__(self):
    return self.merchant_name

