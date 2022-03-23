from flowjax.bijections.abc import ParameterisedBijection
import jax.numpy as jnp

"""Note condition is ignored"""
class Affine(ParameterisedBijection):
    def transform(self, x, loc, log_scale, condition=jnp.array([])):
        return x * jnp.exp(log_scale) + loc

    def transform_and_log_abs_det_jacobian(self, x, loc, log_scale, condition=jnp.array([])):
        return x * jnp.exp(log_scale) + loc, jnp.sum(log_scale)

    def inverse(self, y, loc, log_scale, condition=jnp.array([])):
        return (y - loc) / jnp.exp(log_scale)

    def num_params(self, dim: int):
        return dim * 2

    def get_args(self, params):
        loc, log_scale = params.split(2)
        return loc, log_scale
