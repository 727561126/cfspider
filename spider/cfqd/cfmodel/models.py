from django.db import models

# Create your models here.
class FhModel(models.Model):
    MarketType = models.CharField(max_length=50,default="")
    code = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=50,default="")
    SZZBL = models.CharField(max_length=50,default="")
    SGBL = models.CharField(max_length=50,default="")
    ZGBL = models.CharField(max_length=50,default="")
    XJFH = models.CharField(max_length=50,default="")
    GXL = models.CharField(max_length=50,default="")
    YAGGR = models.CharField(max_length=50,default="")
    GQDJR = models.CharField(max_length=50,default="")
    CQCXR = models.CharField(max_length=50,default="")
    ReportingPeriod = models.CharField(max_length=50,default="")
    ResultsbyDate = models.CharField(max_length=50,default="")
    ProjectProgress = models.CharField(max_length=50,default="")
    AllocationPlan = models.CharField(max_length=50,default="")
    NOTICEDATE = models.CharField(max_length=50,default="")
