from rest_framework.views import APIView
from sps_onboarding.api.serializers import OnboardingCreateReadSerializer
from rest_framework.response import Response
from rest_framework import status
from sps_onboarding.models import SchoolOnboarding


class OnboardingView(APIView):
    """would use this to capture basic onboarding information on the public form section for the landing page"""
    serializer_class = OnboardingCreateReadSerializer

    def get(self, request):
        schools = SchoolOnboarding.objects.all()
        data = self.serializer_class(schools, many=True).data
        return Response(data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
