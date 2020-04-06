from aws_cdk import (
    core as core,
    aws_lambda as _lambda
)

class qpythonlambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines the qpython layer from the layers directory
        qpythonlayer = _lambda.LayerVersion(self, 'qpythonlayer', 
        code = _lambda.AssetCode('layers/qpython_layer.zip')
        ) 
        
        # Defines an AWS Lambda function, qpython code from code directory, memory, handler and layer
        qpython_lambda = _lambda.Function(
            self, 'qpythonFunction',
            runtime=_lambda.Runtime.PYTHON_3_6,
            code=_lambda.Code.asset('code'),
            layers= [qpythonlayer],
            memory_size = 256,
            environment={
                "HOST": self.node.try_get_context("host"),
                "PORT": self.node.try_get_context("port"),
            },
            timeout=core.Duration.seconds(10),
            handler='qpython_connect.lambda_handler'
        )

