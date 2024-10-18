from django.db import models
from django.conf import settings


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    verified_purchase = models.BooleanField(default=False)
    helpful_count = models.PositiveIntegerField(default=0)
    unhelpful_count = models.PositiveIntegerField(default=0)
    helpful_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='helpful_reviews', blank=True)
    unhelpful_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unhelpful_reviews', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"

    @classmethod
    def create_review(cls, user, product, rating, text, image=None):
        verified = cls.verify_purchase(user, product)
        return cls.objects.create(
            user=user, 
            product=product, 
            rating=rating, 
            text=text, 
            image=image, 
            verified_purchase=verified
        )

    @staticmethod
    def verify_purchase(user, product):
        # 이 메서드는 나중에 실제 구매 확인 로직으로 대체.
        return Purchase.objects.filter(user=user, product=product).exists()
