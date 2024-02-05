# TaskEstimator
This machine learning model can be used to predict the number of days required to complete a given based on few features.

## Request Body
```
{
    "isNewFeature" : "1",
    "isNewStory" : "0",
    "isTechDebt" : "0",
    "isResearch" : "1",
    "isDebugging" : "0",	
    "isCoding" : "1",	
    "isTesting" : "1",
    "isDeployment" : "0",	
    "isDotnet" : "1",	
    "isNodejs" : "0",	
    "isReact" : "1",	
    "isSql" : "1",	
    "isTerraform" : "1",	
    "isAWS" : "0"
}
```

## Response Object
```
{
    "Estimated number of days to comaplete the task is ": 14.06
}
```
