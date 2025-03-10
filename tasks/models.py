from django.db import models


class User(models.Model):
 IMPORTANCE_OF_TASKS = [
     ("E", "easy"),
     ("N", "normal"),
     ("D", "difficult"),
     ]
 name = models.CharField(max_length=100)
 importance = models.CharField(choices=IMPORTANCE_OF_TASKS, default="E", max_length=1)





class Title(models.Model):
    task_name = models.CharField(max_length=100)

class Description(models.Model):
    task_description = models.CharField(max_length=100)

def main():
 pass
if __name__ == "__main__":
 main()
