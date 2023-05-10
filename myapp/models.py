from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True ,default="/profilepics/Default.png")
    
    address=models.CharField(max_length=200,null=True)
    dob=models.DateTimeField(null=True)
   
    created_date=models.DateTimeField(auto_now_add=True)
    cover_pic=models.ImageField(upload_to="coverpic",blank=True,default="/profilepics/coverpic.jpg")

    def __str__(self):
        return self.user.username
# from django.utils import timezone
# class Venue(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     venue_type = models.CharField(max_length=200)
#     capacity = models.IntegerField()
#     amenities = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     photo = models.ImageField(upload_to='venue_photos/')
#     available_dates = models.ManyToManyField('BookingDate')
#     def __str__(self):
#         return self.name
# class CateringService(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     photo = models.ImageField(upload_to='catering_photos/')
#     def __str__(self):
#         return self.name
# class PhotoVideoService(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     photo = models.ImageField(upload_to='photos/')
#     def __str__(self):
#         return self.name
# class BridalMakeoverService(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     photo = models.ImageField(upload_to='bridalmakeover_photos/')
#     def __str__(self):
#         return self.name
# class Booking(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
#     catering_service = models.ForeignKey(CateringService, on_delete=models.CASCADE)
#     photo_video_service = models.ForeignKey(PhotoVideoService, on_delete=models.CASCADE)
#     bridal_makeover_service = models.ForeignKey(BridalMakeoverService, on_delete=models.CASCADE)
#     guest_count = models.PositiveIntegerField(('guest count'))
#     booking_date = models.ForeignKey('BookingDate', on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=timezone.now)
# class Payment(models.Model):
#     booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
#     payment_date = models.DateTimeField(default=timezone.now)
#     amount = models.DecimalField(max_digits=8, decimal_places=2)
# class Chatbot(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     message = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
# class BookingDate(models.Model):
#     date = models.DateField()
#     is_available = models.BooleanField(default=True)




