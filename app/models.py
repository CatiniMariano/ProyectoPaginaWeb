from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from ckeditor.fields import RichTextField

# Create your models here.



class Blog(models.Model):
    tittle = models.CharField('title', max_length=160, blank= False, null = False)
    descr = models.CharField('description', max_length=250, blank= False, null = False)
    relleno= RichTextField()
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    fecha= models.DateField('fecha', auto_now= False, auto_now_add= True)
    subtitle = models.CharField('subtitle', max_length=230, blank= False, null = False)
    imagen= models.URLField()
    

    class Meta:
        verbose_name= 'Post'
        verbose_name_plural= 'Posts'

class CrearBlogFormulario(ModelForm):
    class Meta:
            model = Blog
            fields = "__all__"



