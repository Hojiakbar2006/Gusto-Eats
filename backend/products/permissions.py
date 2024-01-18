from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Foydalanuvchiga faqat o'qish ruxsati
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Faqat adminlar uchun ruxsat
        return request.user and request.user.is_staff
    

class IsOwner(BasePermission):
    """
    Permission to check if the user is the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        # Agar foydalanuvchi admin bo'lsa, ruxsat berish
        if request.user.is_staff:
            return True

        # Foydalanuvchi faqat o'ziga tegishli obyektlarni o'qish, o'zgartirish yoki o'chirish huquqiga ega bo'lishi mumkin
        return obj.user == request.user
