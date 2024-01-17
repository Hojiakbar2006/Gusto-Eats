from rest_framework.permissions import IsAuthenticated,BasePermission, IsAdminUser, AllowAny


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Foydalanuvchiga faqat o'qish ruxsati
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Faqat adminlar uchun ruxsat
        return request.user and request.user.is_staff