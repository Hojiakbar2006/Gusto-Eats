from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
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

    def list(self, request,):
        queryset = self.filter_queryset(self.get_queryset())
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

        serializer = self.get_serializer(queryset, many=True)
        return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})

    @action(
        detail=True, methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    def create_review(self, request, pk=None):
        user = request.user
        product = get_object_or_404(Product, pk=pk)

        existing_review = Review.objects.filter(
            product=product, user=user).first()
        if existing_review:
            return Response({'detail': 'You have already reviewed this product'}, status=status.HTTP_400_BAD_REQUEST)

        data = {'product': product.id, 'user': user.id, **request.data}
        serializer = ReviewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def recommended(self, request):
        recommended_products = Product.get_recommended_products()
        serializer = ProductSerializer(recommended_products, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create_review':
            return [IsAuthenticated()]
        elif self.action == 'recommended':
            return [AllowAny()]
        return super().get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
