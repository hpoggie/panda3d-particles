# Particles

This is a particle system editor & loader for the panda3d game engine, based on the editor in Koparka by Wezu.

## Installation & Usage

```
pip install git+https://github.com/hpoggie/panda3d-particles.git
python -m particles
```

## Known issues

Setting the particle lifetime and velocity too high results in this kind of error:

```
AssertionError: !_center.is_nan() && !cnan(_radius) at line 29 of built/include/boundingSphere.I
```

This means your particle system has become too big.
