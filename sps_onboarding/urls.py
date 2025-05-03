from django.urls import path
from sps_onboarding.api.views import OnboardingView

urlpatterns = [
    path("", OnboardingView.as_view(), name="onboarding")
]
