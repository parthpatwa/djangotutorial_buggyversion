from django.db import models


class tagLine(models.Model):
    tagline = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200,default="test")
    #Create a IntegerFiled object 'numberOfVotes' with default value 0 here;
    
    #isPopular doesnt seem to be right.
    def isPopular(self):
        if(self.numberOfVotes > 5):
            return False
        else:
            return True
    def __str__(self):
        #This was not covered in the previous tutorial, but __str__(self) is used to 
        #specify what the object should return when called without any dereferencing.
        #   What do you think __str__() should return here for the tagLine object.