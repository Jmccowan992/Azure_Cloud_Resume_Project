# Import Function Libary for Azure Function
import azure.functions as func

# No Authentication is needed to use this Function App
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# HTTP trigger Creation
@app.route(route="http_trigger")

def main(req: func.HttpRequest) -> func.HttpResponse:
 
# Importing Libaries used to talk to Cosmos DB Table API 
    import logging
    from azure.data.tables import TableClient, UpdateMode
    import os

# Logging that our proccess has started successfully 
    logging.info('Python HTTP trigger function processed a request.')
    
# Python Code itself 
    conn_str = os.getenv("CosmosDbConnectionSetting")
    table_client = TableClient.from_connection_string(conn_str=conn_str, table_name="Visitors")
    entity = table_client.get_entity(partition_key="PageViewCount", row_key='1')
    entity['Count'] += 1
    table_client.update_entity(mode=UpdateMode.REPLACE, entity=entity)

# HTTP Response
    return func.HttpResponse(f"{entity['Count']}")

    
