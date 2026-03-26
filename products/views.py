from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class productforsales(APIView):

    permission_classes=[IsAuthenticated]
    def get(self,request):
        all_prod=prodsales.objects.all()
        products=prodsales_serializer(all_prod,many=True).data
        return Response(products)

    def post(self,request):
        datas=prodsales_serializer(data=request.data)
        if datas.is_valid():
            datas.save()
            return Response("new product added")
        return Response(datas.errors)

class productforsalesbyid(APIView):
    def get(self,request,prod_id):
        db1=prodsales.objects.get(id=prod_id)
        iddata=prodsales_serializer(db1).data
        return Response(iddata)
       
    def patch(self,request,prod_id):
        db1=prodsales.objects.get(id=prod_id)
        update=prodsales_serializer(db1,data=request.data,partial=True)
        if update.is_valid():
            update.save()
            return Response("product updated")
        return Response(update.errors)

    def delete(self,request,prod_id):
        datas=prodsales.objects.get(id=prod_id)
        datas.delete()
        return Response("product deleted")

class cartbyview(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id=None):
        if id is None:
            datas=cart.objects.all()
            pr=cart_serializer(datas,many=True).data
            return Response(pr)
        else:
            data=cart.objects.get(id=id)
            pr1=cart_serializer(data).data
            return Response(pr1)
            
    def post(self,request):
        product=request.data['product']
        quantity=int(request.data['quantity'])
        proddb = prodsales.objects.get(id=product)
        total=proddb.price*quantity
        data=request.data.copy()
        data['product'] = product
        data['total_amount']=total
        serializer=cart_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("cart added")
        return Response(serializer.errors)


 






        


