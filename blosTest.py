from datapi import blos

'''
Initialize blosture library object with your API key and set the project and batch.
'''
bObject = blos("mH7MyFt40d")
bObject.dataset("EEG","Trial_01")

# getTrainX(featureIndex, startSampleNumber, stopSampleNumber)
tx = bObject.getTrainX(20,2,50)
print tx

# getTrainY(featureIndex, startSampleNumber, stopSampleNumber)
ty = bObject.getTrainY(20,2,50)
print ty
