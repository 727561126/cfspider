from django.shortcuts import render
from cfmodel.models import FhModel
import json

def hello(request):
    context          = {}
    res = FhModel.objects.filter(ProjectProgress='股东大会决议通过')
    for rs in res:
        print(rs.name,rs.ProjectProgress,rs.NOTICEDATE,rs.GQDJR,rs.CQCXR)
    context['hello'] = 'hello' 
    #fo = open("/home/admin/spider/cfqd/fh.txt","r+")
    #for line in fo.readlines():
    #    fh_data = json.loads(line)
    #    for fh_json in fh_data:
    #        fh = FhModel(MarketType=fh_json['MarketType'],code=fh_json['Code'],name=fh_json['Name'],SZZBL=fh_json['SZZBL'],SGBL=fh_json['SGBL'],ZGBL=fh_json['ZGBL'],XJFH=fh_json['XJFH'],GXL=fh_json['GXL'],YAGGR=fh_json['YAGGR'],GQDJR=fh_json['GQDJR'],CQCXR=fh_json['CQCXR'],ReportingPeriod=fh_json['ReportingPeriod'],ResultsbyDate=fh_json['ResultsbyDate'],ProjectProgress=fh_json['ProjectProgress'],AllocationPlan=fh_json['AllocationPlan'],NOTICEDATE=fh_json['NOTICEDATE'])
    #        fh.save()
    #fo.close() 
    #fh = FhModel(name='11')
    #fh.save() 
    return render(request, 'fh.html', context)
