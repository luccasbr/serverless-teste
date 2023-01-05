#!/usr/bin/env python

import runpod
import requests

## Load models into VRAM here so they can be warm between requests

def handler(event):
    print(event)

    URL = "http://52.70.161.84:3000/"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
      print("Erro ao fazer a requisição:", response.text)
      return "Erro ao fazer a requisição" + response.text


runpod.serverless.start({"handler": handler})