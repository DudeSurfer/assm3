from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
  from_user = models.ForeignKey(User, related_name = "from")
  to_user = models.ForeignKey(User, related_name = "to")
  date_added = models.DateField()
  
  class Meta:
    unique_together = ("from_user", "to_user")
    
  def save (self, *args, **kwargs):
    if self.from_user.get_username() == self.to_user.get_username():
      return "Nope, not possible!"
    else:
      super(UserLink, self).save(*args, **kwargs)
    
  def __unicode__(self):
    return self.from_user.username + " is following " + self.to_user.username