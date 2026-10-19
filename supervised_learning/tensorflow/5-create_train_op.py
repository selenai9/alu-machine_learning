in"""
import tensorflow as tf


def create_train_op(loss, alpha):
    """ training operation """
    return tf.train.GradientDescentOptimizer(alpha).minimize(loss)
