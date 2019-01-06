import os
from django.shortcuts import render
from hexbytes import HexBytes
from django.http import HttpResponse
import json
import ipfsapi
from django.views.decorators.csrf import csrf_exempt
from web3.auto import w3
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import requests
import base64
from Crypto.PublicKey import RSA
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from .models import ipfs_details

## WALLET CREATION
## INPUT - USER ID AND PASSWORD
## OUTPUT - WALLET WITH PUBLIC KEY AND PRIVATE KEY ENCRYPTED BY PASSWORD

@csrf_exempt
def wallet(request):
    if request.method == 'POST':
        user_id = request.POST.get('User_Id', None)
        password = request.POST.get('password',None)
        acct = w3.eth.account.create(user_id)
        secret_key = password
        cipher = AES.new(secret_key.encode("utf8"),AES.MODE_ECB)
        public_key = acct.address
        private_key = acct.privateKey.hex()
        private_key = private_key.rjust(32) + '00000000000000'
        private_key = private_key.encode("utf8")
        encoded_private_key = base64.b64encode(cipher.encrypt(private_key))
        json_response = json.dumps({"user_id":user_id,"public_key":str(public_key),"encoded_private_key":str(encoded_private_key)})
        return HttpResponse(json_response)
    return HttpResponse("Not a post request")

## CLIENT VALIDATION
@csrf_exempt
def validation(request):
    if request.method == 'POST':
        user_id = request.POST.get('User_Id', None)
        Api_Key = request.POST.get('Api_Key',None)
        url = 'http://34.231.20.51/authentication/'
        post_fields = {'User_Id':user_id,'API_Key':Api_Key}
        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()
        return HttpResponse(json)
    return HttpResponse("Not a post request")

##FILE UPLOAD
@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        user_id = request.POST.get('User_Id', None)
        api_key = request.POST.get('api_key', None)
	file_type = request.POST.get('file_type', None)
	file_title = request.POST.get('User_Id', None)
	file_name = request.POST.get('file_name', None)
	file_extension = request.POST.get('file_extension', None)	
        file = request.FILES['File']
	post_fields = {'User_Id':user_id,'API_Key':api_key}
	

        request = Request('http://34.231.20.51/authentication/', urlencode(post_fields).encode())
        json = urlopen(request).read().decode()
	if json['valid'] is not True:
            return "acccount not validated"
        api = ipfsapi.connect('0.0.0.0', 5001)
        res = api.add(file)
        hash = res['Hash']
        size = res['Size']
        status = os.system('ipfs pin add ' + hash)
        URL = "https://gateway.ipfs.io/ipfs/" + hash + "/"
        if status == 0:
            Pin_Status = "Added"
        else:
            Pin_Status = "Not added"
        os.system('ipfs swarm peers|wc -l > ' + hash)
        file = open(hash, "r")
        for line in file:
            peers = line[:-1]
            break  
        os.remove(hash)
        ipfs_entry = ipfs_details()
        ipfs_entry.Hash = hash
        ipfs_entry.save()
        print(ipfs_entry.Host_Count)
        json_data = json.dumps({'ipfs user id':user_id,'file name':file_name,file_extension:'file_extension',api_key:'api_key','file type':file_extension,file_title:'file_title','hash':hash,'size':size,'pin status':Pin_Status,'url':URL,'peers':peers})
        return HttpResponse(json_data)
    return HttpResponse("not a post request")

## FILE HOST COUNT
@csrf_exempt
def file_host_count(request):
    if request.method == 'POST':
        hash_id = request.POST.get('Hash_Id', None)
        try:
            ipfs_entry = ipfs_details.objects.get(Hash = hash_id)
            ipfs_entry.Host_Count = ipfs_entry.Host_Count + 1
            ipfs_entry.save()
            print(ipfs_entry.Host_Count)
            if ipfs_entry.Host_Count > 5:
                os.system('ipfs pin rm ' + hash_id) 
                ipfs_entry.delete()               
            return HttpResponse(ipfs_entry.Host_Count)
        except Exception as e:
            return HttpResponse("No longer exists in system")
    return HttpResponse("not a post request")
    




