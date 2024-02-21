from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import EmployeesSerializer, AccountsSerializer
from .models import Employees, Accounts
from rest_framework import permissions


class IsAdminPermissions(permissions.BasePermission):
    """
    Custom permission to allow access only to admin users.
    """
    def has_permission(self, request, view):
        """
        Check if the requesting user is an admin.

        Args:
            request (HttpRequest): The request object.
            view (APIView): The view that's being accessed.

        Returns:
            bool: True if the user is an admin, False otherwise.
        """
        return request.user.is_admin==True


class Logout(APIView):
    """
    View to handle user logout.

    Only accepts POST requests and allows any user to access it.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        """
        Handle user logout by blacklisting the provided refresh token.

        Args:
            request (HttpRequest): The request object containing the refresh token.

        Returns:
            Response: A response indicating the success or failure of the logout operation.
        """
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AccountsView(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Accounts model.

    Only allows access to admin users.
    """
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [IsAdminPermissions]


class EmployeeView(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Employees model.

    Only allows access to admin users.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAdminPermissions]
        

