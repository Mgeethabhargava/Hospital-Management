from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Appointment, Hospital
from .serializers import AppointmentSerializer, HospitalSerializer
from appointments.utils import generate_token

class AppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['token'] = generate_token()
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        appointments = Appointment.objects.filter(user=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        analytics = {
            "total_appointments": Appointment.objects.count(),
            "total_users": CustomUser.objects.count(),
            "appointments_per_hospital": {
                hospital.name: Appointment.objects.filter(hospital=hospital).count()
                for hospital in Hospital.objects.all()
            },
        }
        return Response(analytics)
