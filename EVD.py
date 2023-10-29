import librosa
import librosa.display
import numpy as np



def features_extractor(file_name):
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=80)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)


    return mfccs_scaled_features


def lstm_prediction():
    from keras.models import load_model
    model = load_model('best_model.hdf5')

    file_name = 'output_audio.mp3'
    x = features_extractor(file_name)

    x_pred = x.reshape(1, -1, 80)


    yhat = model.predict(x_pred, verbose=0)
    print("FINAL: ", yhat)
    predicted_class = np.argmax(yhat)

    if(predicted_class==0):
        return "Ambulance"

    elif(predicted_class==1):
        return "Firetruck"

    elif(predicted_class==2):
        return "Traffic"
