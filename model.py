import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.regularizers import l1, l2, l1_l2

import numpy as np
from os.path import join

WIDTH, HEIGHT = 64, 64
NUM_CATEGORIES = 6

def load_model():
	model = tf.keras.Sequential([
		Conv2D(
			32, (3, 3), activation="relu", input_shape=(WIDTH, HEIGHT, 3)
		),
		Conv2D(
			32, (3, 3), activation="relu", input_shape=(WIDTH, HEIGHT, 3)
		),
		# Max-pooling layer, using 2x2 pool size
		MaxPooling2D(pool_size=(2, 2)),
		Dropout(0.25),

		# Flatten units
		Flatten(),

		# Add a hidden layer with dropout
		Dense(32, activation="relu", kernel_regularizer=l2(0.01)),
		Dropout(0.5),

		# Add an output layer
		Dense(NUM_CATEGORIES, activation="softmax")
	])
	
	model.compile(
		optimizer='adam',
		loss="categorical_crossentropy",
		metrics=["accuracy"]
	)

	return model