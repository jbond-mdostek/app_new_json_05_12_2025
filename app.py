from flask import Flask, app, jsonify, request
import os
import datetime
from pymongo import MongoClient
import uuid

#Adecuación para desplegar en Render crear_app()/return app     
def crear_app():

    app = Flask(__name__)
    #port = 5000

    users = [
        {
            "id": "8a169ade-2d06-4508-b5ba-57e730bef4af",
            "name": "Blanca Estela",
            "ap_paterno": "Silva",
            "ap_materno": "Pita",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position":"Directora de Modernización Aduanera 2",
            "phone": "123-456-7890",
            "street": "123 Main St",
            "city": "Ciudad de México",
        },
        {
            "id": "8a169ade-2d06-4508-b5ba-57e730bef4af",
            "name": "Rocio",
            "ap_paterno": "Acosta",
            "ap_materno": "González",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "123-456-7890",
            "street": "123 Main St",
            "city": "Ciudad de México",
        },
        {
            "id": "ef3347db-d6f3-46ac-84aa-36f4c6076cc3",
            "name": "Dulce María",
            "ap_paterno": "Ramírez",
            "ap_materno": "Gómez",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "334-159-2123",
            "street": "123 Hook St",
            "city": "Ciudad de México",
        },
        {
            "id": "8a169ade-2d06-4508-b5ba-57e730bef4af",
            "name": "Yanet",
            "ap_paterno": "Ramírez",
            "ap_materno": "Flores",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "123-456-7890",
            "street": "123 Main St",
            "city": "Ciudad de México",
        },
        {
            "id": "ef3347db-d6f3-46ac-84aa-36f4c6076cc3",
            "name": "Emmanuel",
            "ap_paterno": "Garcia",
            "ap_materno": "Hernández",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "334-159-2123",
            "street": "123 Hook St",
            "city": "Ciudad de México",
        },
        {
            "id": "8a169ade-2d06-4508-b5ba-57e730bef4af",
            "name": "Graciela",
            "ap_paterno": "Luna",
            "ap_materno": "Avendaño",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "123-456-7890",
            "street": "123 Main St",
            "city": "Ciudad de México",
        },
        {
            "id": "ef3347db-d6f3-46ac-84aa-36f4c6076cc3",
            "name": "Enrique",
            "ap_paterno": "Tenorio",
            "ap_materno": "Buendía",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "334-159-2123",
            "street": "123 Hook St",
            "city": "Ciudad de México",
        },
        {
            "id": "8a169ade-2d06-4508-b5ba-57e730bef4af",
            "name": "Ramses",
            "ap_paterno": "Rojas",
            "ap_materno": "Hernández",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Enlace de Negocio",
            "phone": "123-456-7890",
            "street": "123 Main St",
            "city": "Ciudad de México",
        },
        {
            "id": "ef3347db-d6f3-46ac-84aa-36f4c6076cc3",
            "name": "Cristian Alejandro",
            "ap_paterno": "López",
            "ap_materno": "Salazar",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Subdirector",
            "phone": "334-159-2123",
            "street": "123 Hook St",
            "city": "Ciudad de México",
        },
        {
            "id": "ef3347db-d6f3-46ac-84aa-36f4c6076cc3",
            "name": "Jaime",
            "ap_paterno": "Mojica",
            "ap_materno": "Rodríguez",
            "age": 28,
            "Company": "Agencia Nacional de Aduanas de México, ANAM",
            "Position": "Subdirector",
            "phone": "334-159-2123",
            "street": "123 Hook St",
            "city": "Ciudad de México",
        },   
    ]

    @app.route("/")
    def hello_world():
        return 'Hello world!'

    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(users), 200
    
    #@app.route('/mapa')
    #def get_mapa():
    #     exec(python mapa_aduanas.py run)

    return app

if __name__ == '__main__':
    app = crear_app()
    app.run()
