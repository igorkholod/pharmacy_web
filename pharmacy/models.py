from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=100, default="")
    adress = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', default='images/no_image.webp')

    def __str__(self):
        return self.name


class Description(models.Model):
    composition = models.TextField(default="")
    dosage_form = models.CharField(max_length=200, default="")
    weight = models.IntegerField(default=0)
    farma_group = models.TextField(default="")
    indication = models.TextField(default="")
    anti_indication = models.TextField(default="")
    appliance = models.TextField(default="")
    expiration_date = models.CharField(max_length=20, default="")
    conditions = models.TextField(default="")
    package = models.CharField(max_length=200, default="")

    def __str__(self):
        return "Description id " + str(self.id)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class Drug(models.Model):
    name = models.CharField(max_length=100, default="")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer_drugs')
    license = models.CharField(max_length=50, default="")
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING, related_name='description_drugs')
    pharmacy = models.ManyToManyField(Pharmacy, through='DrugPharmacy', related_name='pharmacy_drugs')
    image = models.ImageField(upload_to='images/', default='images/no_image.webp')

    def __str__(self):
        return self.name


class DrugPharmacy(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='drug_stocks')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='pharmacy_stocks')
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.drug.name + " in " + self.pharmacy.name + ". Amount: " + str(self.amount)
