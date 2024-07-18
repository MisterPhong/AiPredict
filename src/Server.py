import grpc
# from concurrent import futures
# import time
# from proto import ProtoType
# from pymongo import MongoClient
# import datetime
# import predict_pb2_grpc

# class PredictService(predict_pb2_grpc.PredictService):
#     def __init__(self):
#         self.client = MongoClient("mongodb://root:example@localhost:27017/")
#         self.db = self.client["crypto_predictions"]
#         self.collection = self.db["crypto_predict"]

#     def predict(self, request, context):
#         predictions = []
#         for doc in self.collection.find():
#             # convert datetime to timestamp
#             timestamp = int(doc["Date"].timestamp()) if isinstance(doc["Date"], datetime.datetime) else doc["Date"]
#             
#             prediction = predict_pb2.Predict(
#                 symbol=doc["Symbol"],
#                 date=timestamp,
#                 current_price=doc["Current Price"],
#                 predicted_price=doc["Predicted Price"]
#             )
#             predictions.append(prediction)
#         return predict_pb2.PredictResponse(predict=predictions)

# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     predict_pb2_grpc.add_PredictServiceServicer_to_server(PredictServiceServicer(), server)
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     print("Server started on port 50051")
#     try:
#         while True:
#             time.sleep(86400)
#     except KeyboardInterrupt:
#         server.stop(0)
