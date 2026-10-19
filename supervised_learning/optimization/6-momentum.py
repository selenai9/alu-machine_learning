#!/usr/bin/env python3
"""Momentum Upgraded"""
import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """Creates the training operation for gradient descent with momentum

    Args:
        loss: the loss of the network
        alpha (float): learning rate
        beta1 (float): momentum weight
    Returns:
        the momentum optimization operation
    """
    optimizer = tf.train.MomentumOptimizer(alpha, beta1)
    return optimizer.minimize(loss)
