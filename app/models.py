from django.db import models


# Create your models here.
class SocialUserSearch(models.Model):
    username = models.CharField(max_length=255, unique=True, default=None, null=True, db_index=True)
    search_status = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_social_username'


class SocialUserFound(models.Model):
    username = models.ForeignKey(SocialUserSearch, to_field='id', on_delete=models.CASCADE)
    website_name = models.CharField(max_length=255, null=False)
    website_url = models.TextField(max_length=2000, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        unique_together = ('username', 'website_name')
        db_table = 'tbl_social_found_username'
