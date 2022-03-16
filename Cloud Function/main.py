import functions_framework
from google.cloud import aiplatform
from typing import Dict, Text, Any, Tuple, List
import tensorflow as tf
import os
import base64
import pandas as pd

PRODUCTS_FILE_NAME = os.environ.get('PRODUCTS_FILE_NAME')
#PRODUCTS_FILE_NAME = 'prods.csv'
products_df = pd.read_csv(PRODUCTS_FILE_NAME)

USER_FILE_NAME = os.environ.get('USER_FILE_NAME')
#USER_FILE_NAME = 'users.csv'
users_df = pd.read_csv(USER_FILE_NAME)

PROJECT_ID = os.environ.get('PROJECT_ID')
LOCATION = os.environ.get('LOCATION')

PREDICT_ENDPOINT_ID = os.environ.get('PREDICT_ENDPOINT_ID')
#PREDICT_ENDPOINT_ID = "6519734516804747264"

RECOMM_ENDPOINT_ID = os.environ.get('RECOMM_ENDPOINT_ID')
#RECOMM_ENDPOINT_ID="913878880635322368"

aiplatform.init(project=PROJECT_ID, location=LOCATION)
aiplatform_predict_endpoint = aiplatform.Endpoint(PREDICT_ENDPOINT_ID)
aiplatform_recomm_endpoint = aiplatform.Endpoint(RECOMM_ENDPOINT_ID)

def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _float_feature(value):
  """Returns a float_list from a float / double."""
  return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def _int64_feature(value):
  """Returns an int64_list from a bool / enum / int / uint."""
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def serialize_example(Product_ID, Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, Marital_Status, Product_Category_1, Product_Category_2):
  """
  Creates a tf.train.Example message ready to be written to a file or transmitted as Base64.
  """

  feature = {
      'Product_ID': _bytes_feature(bytes(Product_ID, 'utf-8')),
      'Gender': _bytes_feature(bytes(Gender, 'utf-8')),
      'Age': _bytes_feature(bytes(Age, 'utf-8')),
      'Occupation': _int64_feature(Occupation),
      'City_Category': _bytes_feature(bytes(City_Category, 'utf-8')),
      'Stay_In_Current_City_Years': _bytes_feature(bytes(Stay_In_Current_City_Years, 'utf-8')),
      'Marital_Status': _int64_feature(Marital_Status),
      'Product_Category_1': _int64_feature(Product_Category_1),
      'Product_Category_2': _int64_feature(Product_Category_2),
  }

  # Create a Features message using tf.train.Example.

  example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
  return example_proto.SerializeToString()

def get_product_row(product_id: str) -> Dict[Text, Any]:
  """
  Retreives the product category data associated with the product id.

  :returns: Product data as a dictionary.
  """
  row = products_df[products_df['Product_ID'] == product_id]

  ret_dict = {
    'Product_ID': row['Product_ID'].values[0],
    'Product_Category_1': row['Product_Category_1'].values[0],
    'Product_Category_2': row['Product_Category_2'].values[0],
  }

  return ret_dict

def get_user_row(user_id: int) -> Dict[Text, Any]:
  """
  Retreives the user data associated with the user id.

  :returns: User data as a dictionary.
  """

  row = users_df[users_df['User_ID'] == user_id].iloc[0].tolist()

  ret_dict = {
    'User_ID': row[0],
    'Gender': row[1],
    'Age': row[2],
    'Occupation': row[3],
    'City_Category': row[4],
    'Stay_In_Current_City_Years': row[5],
    'Marital_Status': row[6]
  }

  return ret_dict

def get_recomm_products(user_id: str) -> List[Text]:
  """
  Gets the top 10 products the user is most likely to purchase.

  :returns: List of product ids.
  """
  instances_packet = {
    "instances": [user_id]
  }

  prediction = aiplatform_recomm_endpoint.predict(instances=instances_packet)

  return prediction[0][0]["output_2"]


def get_purchase_prediction(packet: Dict[Text, Any]) -> int:
  """
  Gets the purchase prediction for a product using the features: 
  [Gender,
   Age,
   Occupation, 
   City_Category, 
   Stay_In_Current_City_Years, 
   Marital_Status, 
   Product_Category_1, 
   Product_Category_2]
  
  :returns: Monthly spending prediction.
  """

  serialized_example = serialize_example(**packet)
  b64_example = base64.b64encode(serialized_example).decode("utf-8")

  instances_packet = {
    "examples": {
      "b64": b64_example
    }
  }

  return instances_packet  

  #return prediction_value

def validate_packet(packet: Dict[Text, Any]) -> Tuple[bool, Text]:
  """ 
  Check that the schema is correct and contains valid data.
  """

  # Check that the packet is a dict. Can be expanded.
  prediction_keys = ['User_ID']

  for key in prediction_keys:
    if key not in packet:
      return False, f"Could not find {key} in packet."

  # Check that the user exists.
  user_id = packet['User_ID']
  if user_id not in users_df['User_ID'].values:
    return False, f"User {user_id} does not exist."

  # Packet structure ok.
  return True, "OK"

def inference(request):
  """Responds to any HTTP request.
  Args:
      request (flask.Request): HTTP request object.
  Returns:
      The response text or any set of values that can be turned into a
      Response object using
      `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
  """
  request_json = request.get_json(silent=True)

  valid_packet, message = validate_packet(request_json)
  if not valid_packet:
    return message

  user_id = request_json['User_ID']
  recommendations = get_recomm_products(user_id)
  
  print(recommendations)

  # Get all recommendation values
  del request_json['User_ID']

  # Array to store results
  results = []
  instances_packet = []

  # Get purchase predictions
  for product_id in recommendations:
    # Build purchase packet
    packet = request_json.copy()
    
    # Get correct product categories
    product_row = get_product_row(product_id)
    packet['Product_ID'] = product_id
    packet['Product_Category_1'] = int(product_row['Product_Category_1'])
    packet['Product_Category_2'] = int(product_row['Product_Category_2'])

    # Get User Details
    user_row = get_user_row(user_id)
    packet['Gender'] = user_row['Gender']
    packet['Age'] = user_row['Age']
    packet['Occupation'] = user_row['Occupation']
    packet['City_Category'] = user_row['City_Category']
    packet['Stay_In_Current_City_Years'] = user_row['Stay_In_Current_City_Years']
    packet['Marital_Status'] = user_row['Marital_Status']

    # Get prediction
    prediction_packet = get_purchase_prediction(packet)
    instances_packet.append(prediction_packet)

    # Add prediction to results
    #results.append(prediction_value)


  prediction = aiplatform_predict_endpoint.predict(instances=instances_packet)
  print(prediction)
  prediction_values = prediction[0][0]
  
  results_sum = sum(prediction_values)
  print(f"Sum: {results_sum}")
    
  return { 
    "status": "OK", 
    "output": results_sum
  }



    