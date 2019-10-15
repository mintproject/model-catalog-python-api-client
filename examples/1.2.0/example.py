#!/usr/bin/env python
# coding: utf-8

# ## MINT Model Catalog API client
#
# This notebook shows how interact with the MINT Model catalog using the MINT Model Catalog API client.
#
# For more information about this client: https://github.com/mintproject/MINT-ModelCatalogAPI-client
# You can submit issues at https://github.com/mintproject/MINT-ModelCatalogIngestionAPI/issues

# ### First steps
#
# You must import the required modules and obtain the default configuration to interact with the API

# In[7]:


from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
import json
import ast

configuration = modelcatalog.Configuration()


# ## Authentication
# ### Why do you need authentication?
#
# You have your own workspace to store your models. So, you must authenticate to modify your models.

# ### Log in
#
# After, we must login in to the system. We can login using the method `api_instance.login_user(username, password)`. This method returns the access token and you must save the token in the configuration variable
# ```
#     configuration.access_token = api_instance.login_user(username, password)
# ```

# In[36]:


# create an instance of the API class
api_instance = modelcatalog.DefaultApi()
username = 'mint@isi.edu' # str | The user name for login
password = 'mint123' # str | The password for login in clear text

try:
    api_response = api_instance.user_login_get(username, password)
    data = json.dumps(ast.literal_eval(api_response))
    access_token = json.loads(data)["access_token"]
    configuration.access_token = access_token
    print("Access token: {} ".format(access_token))

except ApiException as e:
    print("Exception when calling DefaultApi->user_login_get: %s\n" % e)


# ### Yay!
# Congrats! You can create new models!

# ## Model Configuration
#
# A model may be configured in different ways depending on the data that is avaialble. For example, if topological information is available, a groundwater model may use it to produce a better estimation of the water budget of an aquifer. A model configuration represents a unique setting of inputs and outputs of a given model designed for a particular functionality.
#
# https://mintproject.github.io/Mint-ModelCatalog-Ontology/modelCatalog/release/0.4.0/index-en.html#ModelConfiguration|
#
#

# ### Get model configuration
#
# You can get a model configuration by the name.

# In[37]:


api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))


# In[38]:


resource_id='cycles'
try:
    # Get modelconfiguration
    api_response = api_instance.modelconfigurations_id_get(resource_id, username=username)
    new_model_configuration = api_response
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_model_configuraton: %s\n" % e)


# ### Create a Model Configuration
#
# Lets create a new model configuration.

# In[44]:



# In[ ]:


try:
    # Update a ModelConfiguration
    api_instance.modelconfigurations_post(username, model_configuration=new_model_configuration)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_put: %s\n" % e)



