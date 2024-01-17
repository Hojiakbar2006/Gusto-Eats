from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from products.models import Product, Review, Category
from rest_framework.decorators import action
from rest_framework import status
from ..permissions import IsAdminOrReadOnly
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.serializers import ProductSerializer, ReviewSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def list(self, request):
        query = request.query_params.get('keyword')
        if query == None:
            query = ''
        products = Product.objects.filter(name__icontains=query)

        page = request.query_params.get('page')
        paginator = Paginator(products, 30)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        if page == None:
            page = 1

        page = int(page)

        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})

    @action(
        detail=True, methods=['post'],
        permission_classes=[IsAdminUser]
    )
    def create_review(self, request, pk=None):
        product = self.get_object()
        user = request.user
        data = {'product': product.id, 'user': user.id, **request.data}
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'])
    def recommended(self, request):
        recommended_products = Product.get_recommended_products()
        serializer = ProductSerializer(recommended_products, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create_review':
            return [AllowAny()]
        elif self.action == 'recommended':
            return [AllowAny()]
        return super().get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]  # Bu orqali faqat adminlarga mumkin

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Faqat ko'rib chiqish uchun ruxsat
        return super().get_permissions()

    @action(detail=True, methods=['GET'], permission_classes=[IsAdminUser])
    def get_category_details(self, request, pk=None):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def recommended(self, request):
        recommended_products = Product.get_recommended_products()
        serializer = ProductSerializer(recommended_products, many=True)
        return Response(serializer.data)
