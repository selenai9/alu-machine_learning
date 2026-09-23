#!/usr/bin/env python3
"""RMSProp Upgraded"""
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """Creates the training operation for a neural network in tensorflow
    using the RMSProp optimization algorithm

    Args:
        loss: the loss of the network
        alpha (float): the learning rate
        beta2 (float): the RMSProp weight
        epsilon (float): a small number to avoid division by zero
    Returns:
        the RMSProp optimization operation
    """
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha,
                                          decay=beta2,
                                          epsilon=epsilon)
    return optimizer.minimize(loss)
