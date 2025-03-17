from django.db import models
from django.urls import reverse 

#jméno kočky
class Cat(models.Model):
 cat_name = models.CharField(max_length=30, help_text = "Insert cats name", null= 'False')
 add_date = models.DateTimeField(help_text = "Insert date of ad", null = 'False')

#věk kočky
 age = models.IntegerField(null = False)

#obrázek kočky
 image = models.ImageField(upload_to='cat_images/', height_field=None, width_field=None, max_length=100)

#popis kočky
 description = models.TextField(max_length=2000, null = True)

 id = models.CharField('ID', max_length=5, unique= True, primary_key='True', default='1')

#plemeno kočky
 breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null= True)

#kastrace
 neutered_choice = (
   ('yes', 'yes'),
   ('no', 'no'),
 )
 neutered = models.CharField(choices = neutered_choice, max_length=10, default='yes')
 
 #vakcinace
 vaccination_choice = (
   ('yes', 'yes'),
   ('no', 'no'),
 )
 vaccination = models.CharField(choices = vaccination_choice, max_length=10, default='yes')

#odčervení
 deworming_choice = (
   ('yes', 'yes'),
   ('no', 'no'),
 )
 deworming = models.CharField(choices = deworming_choice, max_length=10, default='yes')
 #pohlaví kočky
 genders = (
   ('female', 'female'),
   ('male', 'male'),
  )
 
 sex = models.CharField(choices= genders, max_length=10, default='female')
#status adopce - zda je kočka dostupná
 adoption_status = (
   ('free', 'Free to adoption'),
   ('unadoptable', 'curretnly unadoptable'),
   ('reserved', 'reserved'),
 )

 adopt_status = models.CharField(
   max_length=15,
    choices = adoption_status,
    help_text = 'Cats availability',
    default = 'free',
 )

#uspořádání dle jména koček
 class Meta:
  ordering = ['-cat_name']

 def get_absolute_url(self):
        return reverse('cat_detail', args=[str(self.id)])
  
 def __str__(self):
   return self.cat_name
 
 #model pro plemeno kočky
 
class Breed(models.Model):
 breed = models.CharField(max_length=30, null = True, unique= True)
 
 #seřazení podle plemena
 class Meta:
   ordering = ['-breed']

#id plemena
 def get_absolute_url(self):
     return reverse(args =
                  [str(self.id)])
  
  #zobrazení v lidské podobě jména plemena
 def __str__(self):
   return self.breed
  