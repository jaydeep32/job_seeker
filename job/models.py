from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from user.models import Profile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


JOB_TIME = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
)
SALARY_TYPE = (
    ('yearly', 'Yearly'),
    ('monthly', 'Monthly'),
)


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    logo = models.CharField(max_length=50, default='tour')
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


@receiver(post_save, sender=Profile)
def save_profile(sender, instance, created, *args, **kwargs):
    if instance.is_company:
        c = Company(profile=instance)
        c.save()
    if not instance.is_company:
        instance.company_set.all().delete()

class Company(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    web = models.URLField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.profile} - {self.company_name}"


class Job(models.Model):
    job_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='job', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    location = models.CharField(max_length=200)
    vacancy = models.IntegerField(default=1)
    job_time = models.CharField(choices=JOB_TIME, max_length=10)
    salary_type = models.CharField(choices=SALARY_TYPE, max_length=10)
    max_salary = models.DecimalField(decimal_places=2, max_digits=6)
    min_salary = models.DecimalField(decimal_places=2, max_digits=6)
    last_date = models.DateField(default=timezone.now())
    posted_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.job_name


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)
    apply_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.job.job_name} - {self.profile.user.username}'

@receiver(pre_save, sender=Application)
def _post_save_receiver(sender, instance,  **kwargs):
    job = Job.objects.get(pk=instance.job.pk)
    if instance.selected:
        if job.vacancy > 0:
            job.vacancy -= 1
            job.save()
        else:
            instance.selected = False
    else:
        job.vacancy += 1
        job.save()

