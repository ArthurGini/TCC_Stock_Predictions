from tensorflow.keras.utils import to_categorical

# y_binary = to_categorical(y)
# tf.random.set_seed(1)
# model = tf.keras.models.Sequential(
#     [
#         tf.keras.layers.Reshape(
#             (TIME_PERIODS, num_sensors), input_shape=(TIME_PERIODS, num_sensors)
#         ),
#         tf.keras.layers.Conv1D(
#             n_filters,
#             filter_size,
#             activation="relu",
#             padding="same",
#             input_shape=(TIME_PERIODS, num_sensors),
#         ),  # ,kernel_constraint=tf.keras.constraints.NonNeg()
#         tf.keras.layers.Conv1D(n_filters, filter_size, activation="relu"),
#         tf.keras.layers.MaxPooling1D(pool_size),
#         tf.keras.layers.Dense(100, activation="relu"),
#         tf.keras.layers.Dense(y_binary.shape[1]),
#     ]
# )

# loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=False)
# adam = tf.keras.optimizers.Adam(
#     lr=0.001,
#     learning_rate=0.001,
#     beta_1=0.9,
#     beta_2=0.999,
#     epsilon=1e-07,
#     amsgrad=False,
#     name="adam",
# )
# model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
# model.fit(x, y_binary, batch_size=64, epochs=1)




model = Sequential([
	Reshape((TIME_PERIODS, num_sensors), input_shape = (TIME_PERIODS, num_sensors)),
	Conv1D(n_filters, filter_size, activation=’relu’, padding=’same’,input_shape=(TIME_PERIODS, num_sensors)),#,kernel_constraint=tf.keras.constraints.NonNeg()
	Conv1D(n_filters, filter_size, activation=’relu’),
	MaxPooling1D(pool_size),
	Flatten(),
	Dense(100, activation = ‘relu’),
	Dense(y_binary.shape[1])
])