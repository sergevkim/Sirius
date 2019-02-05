print("hello world!")

#import cPickle as pickle
import pickle
from keras.models import Model
import numpy as np
from os.path import isfile


class model:
    
    def __init__(self,      #we are required to determine all these variables to pass them in tf.Model
                 _proportionTrainVal=0.8,
                 _batchSize=None,
                 _epochs=8,
                 _verbose=1,
                 _callbacks=None,
                 _validationSplit=0.0,
                 _shuffle=True,
                 _classWeight=None,
                 _sampleWeight=None,
                 _initialEpoch=0,
                 _stepsPerEpoch=1500,
                 _validationSteps=20):
        self.proportionTrainVal = _proportionTrainVal
        self.batchSize = _batchSize
        self.epochs = _numberOfEpochs
        self.verbose = _verbose
        self.callbacks = _callbacks
        self.validationSplit = _validationSplit
        self.shuffle = _shuffle
        self.classWeight = _classWeight
        self.sampleWeight = _sampleWeight
        self.initialEpoch = _initialEpoch
        self.stepsPerEpoch = _stepsPerEpoch
        self.validationSteps = _validationSteps
        
        self.model = Model()
        self.modelCheckpoint = 0    # we have to decide about modelCheckpoint type. and we really want to use it if we have callbacks?
        if (_callbacks != None):
            self.modelCheckpoint = self.callbacks[-1]   # i believe
    
    def fit(self, X, y):
        borderTrainVal = y.shape[0] * self.proportionTrainVal
        featuresTrain = np.array(X[:borderTrainVal])
        labelsTrain = np.array(y[:borderTrainVal])
        featuresVal = np.array(X[borderTrainVal:])
        labelsVal = np.array(y[borderTrainVal:])
        
        datasetTrain = get_dataset(featuresTrain,
                                   labelsTrain)  # features and labels are arrays or lists? and other parameters
        datasetVal = get_dataset(featuresVal,
                                 labelsVal)
        
        self.model.fit(x=datasetTrain,
                       y=None,  # because x is dataset which contains y
                       batch_size=self.batchSize,
                       epochs=self.epochs,
                       verbose=self.verbose,
                       callbacks=self.callbacks,
                       validation_split=self.validationSplit,
                       validation_data=datasetVal,
                       shuffle=self.shuffle,
                       class_weight=self.classWeight,
                       sample_weight=self.sampleWeight,
                       initial_epoch=self.initialEpoch,
                       steps_per_epoch=self.stepsPerEpoch,
                       validation_steps=self.validationSteps)

    def predict(self, X):
        pred = self.mod.predict(X)
        return pred
    
    def save(self, path="./"):
        pickle.dump(self, open(path + '_model.pickle', "w"))

    def load(self, path="./"):
        modelfile = path + '_model.pickle'
        if isfile(modelfile):
            with open(modelfile) as f:
                self = pickle.load(f)
            print("Model reloaded from: " + modelfile)
        return self



#if __name__ == "main":     dont forget to add it