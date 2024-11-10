from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().capitalize()
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="brands/", null=True, blank=True)
    category = models.ForeignKey(
        Category, related_name="brands", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    category = models.ForeignKey(
        Category, related_name="tags", on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower().capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    emballage = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    description = models.TextField(db_index=True)
    image = models.ImageField(upload_to="products/")
    quantity_in_stock = models.PositiveIntegerField(null=True, blank=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)

    def save(self, *args, **kwargs):
        self.title = self.title.lower().capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled"),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"Order {self.id}"


class TeamMember(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to="team_photos/", blank=True, null=True)
    priority = models.IntegerField(
        help_text="Définissez la priorité d'affichage. Par exemple : Directeur = 1 ..., etc. Les valeurs les plus basses sont affichées en premier."
    )

    class Meta:
        ordering = ["priority", "name"]
        verbose_name = "Membre de l'équipe"
        verbose_name_plural = "Membres de l'équipe"

    def __str__(self):
        return f"{self.name} - {self.role}"


# just for delete the images from the directory
@receiver(pre_delete, sender=Category)
@receiver(pre_delete, sender=Brand)
@receiver(pre_delete, sender=Product)
@receiver(pre_delete, sender=Tag)
@receiver(pre_delete, sender=TeamMember)
def delete_image(sender, instance, **kwargs):
    """Supprimer l'image associée à l'instance avant la suppression."""
    if hasattr(instance, "image") and instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
