from rest_framework import serializers

from sps_onboarding.models import SchoolOnboarding

class OnboardingCreateReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolOnboarding
        fields = [
            "name",
            "contact_information",
            # "logo",
            "address",
            "reason"
        ]
