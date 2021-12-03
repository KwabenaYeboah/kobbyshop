from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=150, db_index=True),
        slug = models.SlugField(max_length=150, db_index=True, unique=True)
    )
    
    class Meta:
        #ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=150, db_index=True),
        slug = models.SlugField(max_length=150, db_index=True),
        description = models.TextField(blank=True)
    )   
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    #class Meta:
    #    ordering = ('name',)
    #    index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug, self.pk])