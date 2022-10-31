from django.db import models

"""
   here we are using filter model and storing the data of Filter_data.
"""

class Filter_data(models.Model):

    action = models.CharField(max_length=266,null=True,blank=True)
    timestamp_at = models.DateTimeField(max_length=266,null=True,blank=True)
    publisher_id = models.CharField(max_length=266,null=True,blank=True)
    shopper_id = models.CharField(max_length=266,null=True,blank=True)


""""
   here we are using Campaign model for storing the data of campaign.
"""
class Campaign(models.Model):

    campaign_id=models.CharField(max_length=266,null=True,blank=True)
    aff_medium=models.CharField(max_length=266,null=True,blank=True)
    aff_term=models.CharField(max_length=266,null=True,blank=True)
    aff_campaign=models.CharField(max_length=266,null=True,blank=True)
    aff_content=models.CharField(max_length=266,null=True,blank=True)
    parent_org=models.CharField(max_length=266,null=True,blank=True)

