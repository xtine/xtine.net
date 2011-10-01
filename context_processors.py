from django.conf import settings

def googleAnalytics(request):
    return {"googleAnalyticsID": settings.GOOGLE_ANALYTICS_ID}
