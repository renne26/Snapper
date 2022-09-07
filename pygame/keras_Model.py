from cgitb import reset
from unittest import result


def ten():
    import tensorflow as tf
    import numpy as np
    TF_MODEL_FILE_PATH = 'pygame\model.tflite' # The default path to the saved TensorFlow Lite model

    interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
    classify_lite = interpreter.get_signature_runner('serving_default')
    #print(interpreter.get_signature_list())

    img1 = tf.keras.utils.load_img(
        "pygame\\g.png", target_size=(192, 144)
    )
    img1_array = tf.keras.utils.img_to_array(img1)

    img2 = tf.keras.utils.load_img(
        "e.png", target_size=(192, 144)
    )
    img2_array = tf.keras.utils.img_to_array(img2)
    # img2 = tf.keras.utils.load_img(
    #     "pygame\\t.png", target_size=(192, 144)
    # )
    # img2_array = tf.keras.utils.img_to_array(img2)

    # img3 = tf.keras.utils.load_img(
    #     "pygame\\a.png", target_size=(192, 144)
    # )
    # img3_array = tf.keras.utils.img_to_array(img3)

    img_pair = []
    img_pair += [[img1_array, img2_array]]
    img_pair = np.array(img_pair)
    predictions_lite = classify_lite(input_26=img_pair[:,0], input_27=img_pair[:,1])['dense_26']
    #score_lite = tf.nn.softmax(predictions_lite)
    #assert np.allclose(predictions, predictions_lite)
    print("save me please{}".format(predictions_lite[0][0]))
    #result = np.clip(predictions_lite[0][0],None,0.5)
    #result /= 0.5
    if (predictions_lite[0][0]) > 0:
        result = 1
    else:
        result = 0
    return(result)
#print("Label is {}".format(result))
