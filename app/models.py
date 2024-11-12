from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.TextField(max_length=32)
    email = models.TextField(max_length=32)
    phone = models.TextField(max_length=32)
    is_favorite = models.BooleanField()

def create_contact(name, email, phone, is_favorite):
    contact = Contact(name = name, email = email, phone = phone, is_favorite = is_favorite)
    contact.save()
    return contact


def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(name):
    for item in Contact.objects.all():
        if item.name == name:
            return item
        else:
            continue

def favorite_contacts():
    return Contact.objects.filter(is_favorite = True)

def update_contact_email(name, new_email):
    Contact.objects.filter(name=name).update(email=new_email)
    

def delete_contact(name):
    try:
        obj = Contact.objects.get(name = name) 
        obj.delete()
    except:
        print("error")