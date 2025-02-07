from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.authentication.models import Printer
from apps.orders.models import Order
from apps.reviews.models import Review
from apps.reviews.requests import CreateReviewRequest, EditReviewRequest
from apps.reviews.responses import DeleteReviewResponse
from apps.reviews.serializers import ReviewSerializer
from . import services
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='post', request_body=CreateReviewRequest(many=False), operation_id='Create Review', responses={201: ReviewSerializer(many=False)}
)
@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request: Request, *args, **kwargs):
    review_request = request.data
    user = request.user
    printer_id = review_request['printer_id']
    try:
        printer = Printer.objects.get(id=printer_id)
    except:
        return Response({'error': 'Invalid Printer ID'})

    if Order.objects.filter(user=user, printer=printer).exists():
        if Review.objects.filter(user=user, printer=printer).exists():
            return Response({'message': 'You have already reviewed this vendor!', 'value': False})
        else:
            new_review = Review.objects.create(user=user, printer=printer, rating=review_request['rating'],
                                               comment=review_request['comment'])

        new_review.save()
    else:
        return Response({'message': 'You haven\'t made an order from this vendor! ', 'value': False})

    review_serializer = ReviewSerializer(instance=new_review)

    if printer.average_rating is None:
        printer.average_rating = new_review.rating
    else:
        services.calculate_average_rating(new_review)

    printer.save()

    return Response(data=review_serializer.data, status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    method='get', request_body=None, operation_id='Get Review By Id', responses={200: ReviewSerializer(many=False)}
)
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_review_by_id(request: Request, review_id: int):
    review = Review.objects.get(id=review_id)
    review_serializer = ReviewSerializer(instance=review)

    return Response(data=review_serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get', request_body=None, operation_id='Get Review For Me', responses={200: ReviewSerializer(many=True)}
)
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_reviews_for_me(request: Request):
    user = request.user

    if Printer.objects.filter(user=user).exists():
        printer = Printer.objects.get(user=user)

        reviews = Review.objects.filter(printer=printer)
    else:
        reviews = Review.objects.filter(user=user)

    review_serializer = ReviewSerializer(instance=reviews, many=True)

    return Response(data=review_serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get', request_body=None, operation_id='Get Reviews', responses={200: ReviewSerializer(many=True)}
)
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_reviews(request: Request):
    printer_id = request.query_params.get("printer", None)

    if printer_id:
        try:
            printer = Printer.objects.get(id=int(printer_id))
        except:
            return Response({'error': 'Printer does not exist!'})

        reviews = Review.objects.filter(printer=printer).order_by('-time_posted')
    else:
        reviews = Review.objects.all()

    review_serializer = ReviewSerializer(instance=reviews, many=True)

    return Response(data=review_serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='put', request_body=EditReviewRequest(many=False), operation_id='Edit Review', responses={200: ReviewSerializer(many=False)}
)
@api_view(["PUT"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_review(request: Request, review_id):
    user = request.user

    review_data = request.data

    try:
        review = Review.objects.get(id=review_id, user=user)
    except:
        return Response({'error': 'Review does not exist!'})

    old_rating = review.rating

    review.rating = review_data['rating']
    review.comment = review_data['comment']

    review.save()

    review_serializer = ReviewSerializer(instance=review)

    services.calculate_average_rating(review)

    return Response(data=review_serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='delete', request_body=None, operation_id='Delete Review', responses={200: DeleteReviewResponse(many=False)}
)
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_review(request: Request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except:
        return Response({'error': 'Invalid Review ID', 'value': False})

    review.delete()
    services.calculate_average_rating(review)

    return Response({'message': 'Review deleted successfully!', 'value': True})
